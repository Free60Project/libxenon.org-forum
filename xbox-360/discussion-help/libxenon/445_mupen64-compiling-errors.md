# Mupen64 compiling errors

## 2014-12-23 21:22:18, posted by: <Unknown User>

I got the toolchain installed thanks to help from Swizzy and his script, and now I'm having a little trouble compiling mupen64. At first I was getting make errors about no rule to make target /usr/local/xenon/rules, but I copied over the rules and app.lds files from the devkitxenon folder to /usr/local/xenon/rules to fix that. Is that ok?  
   
 Now, when I try to run make I get this:  
 $ make  
 [main.cpp]  
 make[1]: xenon-g++: Command not found  
 make[1]: *** [main.o] Error 127  
 make: *** [build] Error 2  
   
 Where am I supposed to get the xenon-g++ command from?

## 2014-12-28 06:31:14, posted by: <Unknown User>

Switched to debian 7 and things went much smoother... All working now :)