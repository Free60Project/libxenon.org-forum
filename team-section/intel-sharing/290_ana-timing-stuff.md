# ana timing stuff

## 2012-02-23 20:14:43, posted by: Nathan

I will update this post with more info as I get to it.  
 This is for the resolution/display mode setup stuff btw  
   
 Timing table and other info:  
 http://dl.dropbox.com/u/12301961/tvtimings.txt  
   
 From the looks of it, portions of the above table are pointers to other sections in the kernel....  
   
 There are 44 supported video modes, apparently  
   
 UPDATE:  
 Added SMB Init values for every display mode  
   
 UPDATE:  
 Added some code that should init the smb timing stuff  
   
 UPDATE:  
 All display modes that the kernel has data for:  
 http://pastebin.com/PH8a51Wt << lol this table is weird... they apparently get the other values from somewhere else, probably upscales it  
 That or i messed up dumping the data  
   
 Blarg, there is apparently other stuff i'd have to do to get this to work, i think i am just going to make the current buffers a lot smaller instead