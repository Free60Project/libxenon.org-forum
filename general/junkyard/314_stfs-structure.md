# STFS Structure

## 2012-04-28 08:10:32, posted by: walkerneo

I've looked through the x360 source and on free60 a lot over the past week, and I'm still having trouble with the STFS file structure. Currently, I have no idea why sometimes the first hash table is at 0xA000 and other times at 0xB000. Free60 doesn't mention anything about it, and I'm having trouble understanding the source of x360. It seems like he's going to 0xB6014 and reading the "status byte", but I don't really know what that is, or how it's determined. Past this, there are still other things I would like to know.  
   
   
 Where did free60 and DJ Shepherd get all their information?

## 2012-04-28 08:20:34, posted by: Cancerous1

AFAIK we don't deal with the containers used in the retail kernel, STFS isnt used or touched by libxenon. try xboxhacker.org maybe. moving this to the trash unless another admin thinks its appropriate here.

## 2012-04-28 08:49:27, posted by: Juvenal

I am willing to allow this topic since there is an extensive write up of STFS on the wiki. At some point in time it was deemed appropriate.

## 2012-04-28 08:51:11, posted by: Cancerous1

free60 wiki and libxenon.org are two different beasts, check the topic