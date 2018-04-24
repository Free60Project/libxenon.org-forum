# VMware/Debian 6 (Squeeze) LibXenon-Ready Virtual Machine

## 2011-09-25 07:17:52, posted by: boflc

I've seen a few folks in chan looking for a little bit of help setting up a LibXenon build environment on their PC, so I spent a little time putting a VMware virtual machine together specifically for this purpose. I haven't packaged one of these up before for others' consumption, so please let me know if I missed something.  
   
 Notes: [list]- [*][u]attribution[/u]: this image was originally downloaded from http://www.thoughtpolice.co.uk/vmware/
- [*]it's base is a Debian 6 (squeeze) minimal installation (thus no window manager)
 - [*]it has since been modified to include libxenon & associated toolchain
- [*]/opt/free60 : location of the git repo checked out
- [*]/opt/src : location of bzip2-1.0.6 source (already installed), mupen64-360 source (already compiled), zlx (already installed), and pcsxr-xenon (already compiled); each one of these pkgs is straight from distribution (git/svn) as of 2011.09.25
- [*]/opt/notes : contains a proper-for-libxenon bzip Makefile (from ced via warfaren), as well as a one-line-tweaked build-xenon-toolchain for debian
- [*]root --> user: root pass: libxenon
- [*]non-root: user: xenon pass: libxenon
[/list] The virtual image itself, ~1gb compressed (3 parts), ~4.5gb uncompressed.  
 http://www.megaupload.com/?d=2J5K2PY0  
 http://www.megaupload.com/?d=7XF8C814  
 http://www.megaupload.com/?d=O7NVV6MZ  
   
 PM me on EFNET for a direct link to a single archive of the above.  
   
 and, of course, [url=http://downloads.vmware.com/d/info/desktop\_downloads/vmware\_player/3\_0?gcx=w&sourceid=chrome&ie=UTF-8&q=vmware%20player]a link to vmware.com's VMware Player's download page, here[/url].  
   
 thank you to everyone involved: i'm always reticent to name names as i'm certain i'd leave someone off without intent. so you, yes, you: thanks.

## 2011-09-25 09:11:42, posted by: SynTeX

cool idea! Thanks for sharing :)

## 2011-09-26 18:19:54, posted by: Ced2911

nice :)

## 2011-09-27 00:15:19, posted by: peet8989

thank you!

## 2012-02-16 09:03:26, posted by: Xplorer4x4

Since megaupload is now shutdown, is there a chance to get a reup on a new host? http://www.filedropper.com/ would allow you to zip/rar the folder and upload it as one single link. This host is very reliable and has been around for some time now.

## 2012-02-16 17:38:17, posted by: boflc

uploading it now.. may take a while (~1gb).

## 2012-02-16 21:37:10, posted by: boflc

filedropper failed at 1%. i'm pm'ing you a private link: if you'd like to upload what i'm providing elsewhere, please just leave a link in this thread.