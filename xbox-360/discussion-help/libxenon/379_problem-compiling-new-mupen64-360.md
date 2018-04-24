# Problem Compiling new Mupen64-360

## 2012-11-16 16:48:59, posted by: mark291422

Hi Guys I've been banging my head trying to get this compiled since the new source was put up and an currently stuck without being able to find my current issue anywhere.  
   
 Right new I get the following error trying to build either through command line or netbeans  
   
 /usr/local/xenon/lib/gcc/xenon/4.6.1/../../../../xenon/bin/ld cannot find -lxemit  
   
 I'm running Ubuntu 12.10 *I believe I'll have to verify the revision number when I have access to my vm again.  
   
   
 I've tried several itterrations of doing things manually and/or using scripts/tools I've pieced together from multiple forums and always hit a dead-end so I'm finally asking for help. Alternatively if someone has a VM image or ISO I can load into my server it would make things 100x easier. :-[

## 2012-11-19 22:01:29, posted by: dreamboy

try installing this lib:  
 https://github.com/gligli/libxemit

## 2012-11-19 22:05:06, posted by: mark291422

Hi,   
   
 Thanks for the tip I actually did that and now moved past the compiling stage into a new issue.  
   
 I'm running into the same seg-fault  
   
 This is what I'm getting right now (http://imgur.com/uQY1P). I'm using the same USB key that works for v0.96. I used my mupen64-360.elf32 (3,599KB) and simply renamed it to replace my existing xenon.elf.  
   
 To compile Mupen64-360 I ran make CROSS\_COMPILE=-xenon- and got no errors.  
   
 I've tried formatting the usbkey with gui format and re-applying the .elf and it still fails.  
   
 Does anyone have anything else that comes to mind to solve this? Thanks in advance.

## 2012-11-23 02:10:46, posted by: dreamboy

[quote="mark291422"]  
 Hi,   
   
 Thanks for the tip I actually did that and now moved past the compiling stage into a new issue.  
   
 I'm running into the same seg-fault  
   
 This is what I'm getting right now (http://imgur.com/uQY1P). I'm using the same USB key that works for v0.96. I used my mupen64-360.elf32 (3,599KB) and simply renamed it to replace my existing xenon.elf.  
   
 To compile Mupen64-360 I ran make CROSS\_COMPILE=-xenon- and got no errors.  
   
 I've tried formatting the usbkey with gui format and re-applying the .elf and it still fails.  
   
 Does anyone have anything else that comes to mind to solve this? Thanks in advance.  
 [/quote]  
   
 try to format your usb stick with windows default formater with the default settings