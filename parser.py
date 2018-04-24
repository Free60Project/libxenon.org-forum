import io
import sys
import os
import argparse
import sqlite3
import datetime


from slugify import slugify
from markdownify import markdownify


def get_forums(connection):
    forums = {}

    cursor = connection.cursor()
    sql = "SELECT * FROM phpbb_forums"
    cursor.execute(sql)
    for ds in cursor:
        forum_id = ds[0]
        forum = dict(parent_id=ds[1], name=ds[5])

        forums[forum_id] = forum
    return forums


def create_forums_folders(forums):
    forums_paths = {}
    for forum_id, forum in forums.items():
        path = slugify(forum['name'])
        current_parent = forum['parent_id']
        while current_parent != 0:
            parent_forum = forums.get(current_parent)
            sub_parent_id = parent_forum['parent_id']
            parent_name = slugify(parent_forum['name'])

            # Prefix path with parent foldername
            path = os.path.join(parent_name, path)
            current_parent = sub_parent_id

        # Prefix with top output dir
        # path = os.path.join('output', path)
        forums_paths[forum_id] = path
        os.makedirs(path, exist_ok=True)
    return forums_paths


def get_topics(connection):
    topics = {}

    cursor = connection.cursor()
    sql = "SELECT * FROM phpbb_topics"
    cursor.execute(sql)
    for ds in cursor:
        topic_id = ds[0]
        topic = dict(forum_id=ds[1], name=ds[5])

        topics[topic_id] = topic
    return topics


def get_attachments(connection):
    attachments = {}

    cursor = connection.cursor()
    sql = "SELECT * FROM phpbb_attachments"
    cursor.execute(sql)
    for ds in cursor:
        attach_id = ds[0]
        attachment = dict(post_id=ds[1], phys_filename=ds[6], real_filename=ds[7])

        attachments[attach_id] = attachment

    return attachments


def get_posts(connection):
    """
    RETURNS A LIST
    """
    posts = []

    cursor = connection.cursor()
    sql = "SELECT * FROM phpbb_posts ORDER BY post_id"
    cursor.execute(sql)
    for ds in cursor:
        post = dict(post_id=ds[0], topic_id=ds[1], forum_id=ds[2], post_time=ds[6], post_username=ds[12],
                    post_text=ds[14], got_attachment=ds[16])
        if not post['post_username']:
            post['post_username'] = '<Unknown User>'

        posts.append(post)
    return posts

def main():
    parser = argparse.ArgumentParser(description='Fun with phpbb database')
    parser.add_argument('dbfile', type=str,
                        help='phpBB database dump (sqlite3)')

    args = parser.parse_args()

    if not os.path.exists(args.dbfile):
        print('Failed to open file \'{}\''.format(args.dbfile))
        sys.exit(1)

    connection = sqlite3.connect(args.dbfile)

    forums = get_forums(connection)
    topics = get_topics(connection)
    attachments = get_attachments(connection)
    posts = get_posts(connection)

    forum_paths = create_forums_folders(forums)

    for post in posts:
        post_id = post['post_id']
        topic_id = post['topic_id']
        post_username = post['post_username']
        post_text = post['post_text']
        got_attachment = post['got_attachment']
        post_time = datetime.datetime.fromtimestamp(post['post_time']).strftime('%Y-%m-%d %H:%M:%S')

        topic = topics[topic_id]
        topic_name = topic['name']
        forum_id = topic['forum_id']

        base_path = forum_paths[forum_id]

        post_filepath = os.path.join(base_path, '{id}_{name}.md'.format(id=topic_id, name=slugify(topic_name)))

        with io.open(post_filepath, 'a') as f:
            if f.tell() == 0:
                # Write header
                f.write('# {}\n\n'.format(topic_name))
            else:
                f.write('\n\n')

            f.write('## {}, posted by: {}\n\n'.format(post_time, post_username))
            f.write(markdownify(post_text))

            if got_attachment:
                attachment_list = [a['real_filename'] for (i, a) in attachments.items() if a['post_id'] == post_id]
                f.write('\n\n### Attachments\n\n')
                for a in attachment_list:
                    f.write('[{attachment}]({attachment})'.format(attachment=a))

if __name__ == '__main__':
    main()
