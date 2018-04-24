# Compiling plasma-1.0 demo from libSDLXenon

## 2012-09-14 00:01:13, posted by: ch.kenned

Trying to compile the plasma-1.0 demo produced this output:  
   
 In file included from /root/free60project-github/libSDLXenon/include/SDL\_config.h:42:0,  
 from /root/free60project-github/libSDLXenon/include/SDL\_stdinc.h:30,  
 from /root/free60project-github/libSDLXenon/include/SDL\_main.h:26,  
 from /root/free60project-github/libSDLXenon/include/SDL.h:30,  
 from plasma.c:10:  
 /root/free60project-github/libSDLXenon/include/SDL\_config\_xenon.h:39:22: error: conflicting types for 'size\_t'  
 /usr/local/xenon/lib/gcc/xenon/4.6.1/include/stddef.h:212:23: note: previous declaration of 'size\_t' was here  
   
 Line 39 of SDL\_config\_xenon.h is:  
 typedef unsigned int size\_t;  
   
 Line 212 of stddef.h is:  
 typedef \_\_SIZE\_TYPE\_\_ size\_t;  
   
 It appears that \_\_SIZE\_TYPE\_\_ is a long unsigned int vs unsigned int , resulting in the conflicting types error.  
 Any suggestions on how to proceed?! My apologies for any dumb questions. :)

## 2012-09-14 11:55:56, posted by: Ced2911

there is a bug between newlib stdint.h and gcc

## 2012-09-15 18:59:08, posted by: ch.kenned

Hey Ced2911! How can I resolve this issue? Thanks for your releases, btw. I'm glad that you're contributing your knowledge to the homebrew scene.