# How to setup SDL Library

## 2011-06-26 22:02:12, posted by: dreamboy

Credits to: [glow=red,2,300]Lantus[/glow], [glow=red,2,300]Ced2911[/glow] and [glow=red,2,300]IUNIXI[/glow]  
   
 Setting up SDL Libray:  
 [list] -  
 - [*]Check if you have zlib and libpng first, if you don't you should install them first: [url=http://libxenon.org/http://libxenon.org//viewtopic.php?p=465#p465]Libs[/url]  
 
 - [*]Open Terminal  
 
 - [*]If you have tried to install sdl befored - delete all files and folders first  
 
 - [*]Now type:
[/list][code]* *git clone git://github.com/LibXenonProject/libSDLXenon.git cd libSDLXenon make -f Makefile.xenon make -f Makefile.xenon install [/code] Its done, yeah it got a bit shorter tutorial :)   
   
 edit by tuxuser: Uses libSDL by Lantus now

## 2012-03-06 03:18:26, posted by: Xplorer4x4

Looks like SDL was moved from the free60 git repositories to the libxenon repositories. New github link is : git://github.com/LibXenonProject/libSDLXenon.git  
 [code]git clone git://github.com/LibXenonProject/libSDLXenon.git cd libSDLXenon make -f Makefile.xenon make -f Makefile.xenon install [/code]

## 2012-07-21 06:51:05, posted by: ravendrow

please correct the following line in source  
   
 https://github.com/LibXenonProject/libSDLXenon/blob/master/src/joystick/xenon/SDL\_xenonjoystick.c#L181  
   
 line is   
 [code]* *if (joystick->hwdata->curpad.select) [/code] and it should be  
 [code]* *if (joystick->hwdata->curpad.back) [/code] changing this fixes issues with new libxenon  
   
 thank you

## 2012-07-21 14:11:28, posted by: tuxuser

will do, thx

## 2012-08-26 02:25:33, posted by: ch.kenned

After issuing "sudo make -f Makefile.xenon", I get the following output:  
 [SDL.c]  
 make: xenon-gcc: Command not found  
 make: *** [src/SDL.o] Error 127  
   
 If I issue "xenon-gcc" at the shell, the output is:  
 xenon-gcc: fatal error: no input files  
 compilation terminated.  
   
 Can someone help me resolve this issue, please?

## 2012-08-26 03:50:09, posted by: ch.kenned

After editing Makefile.xenon to point to the location of xenon-gcc...I get the following error:  
   
 sudo make -f Makefile.xenon  
 [SDL.c]  
 In file included from /usr/include/string.h:27:0,  
 from ./include/SDL\_config\_xenon.h:27,  
 from ./include/SDL\_config.h:42,  
 from src/SDL.c:22:  
 /usr/include/features.h:324:26: fatal error: bits/predefs.h: No such file or directory  
 compilation terminated.  
 make: *** [src/SDL.o] Error 1

## 2012-08-26 18:10:17, posted by: sk1080

Your OS should have a folder called /etc/profile.d or /etc/bash.d  
 Insert the export lines the toolchain script should have told you in to a file called xenon.sh in the appropriate folder  
 If the build script did not spit those lines, chances are that it failed on something like gcc stage 2

## 2012-08-26 19:43:44, posted by: ch.kenned

Thank you for the reply, but that didn't solve the problem. I added the lines from the output to xenon.sh in /etc/profile.d. I've compiled the cube example and run it on my xbox, so I know that libxenon is set up and working. It appears /bits/predefs.h is missing? Could it be an issue with cloning libSDL? Any help is greatly appreciated. Thanks.

## 2012-08-26 19:57:11, posted by: sk1080

Cube doesn't rely on environment  
 If it doesn't automatically find xenon gcc the your environment is set up wrong  
   
 Sent from my GT-I9100 using Tapatalk

## 2012-09-10 22:39:05, posted by: ch.kenned

Okay, I've given up on Netbeans and gone to strictly terminal based compilation...so far, everything appears to be working okay...I'm trying to compile the plasma-1.0 demo included in libSDLXenon...so far, no luck, though....