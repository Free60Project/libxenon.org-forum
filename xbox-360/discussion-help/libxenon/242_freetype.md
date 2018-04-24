# freetype

## 2011-12-09 08:32:55, posted by: kazzmir

Hello, I am new to the xbox 360 homebrew scene. I tried compiling freetype with xenon but ran into some issues.  
   
 The main issue seems to be that <sys/mman.h> does not exists in xenon. This header provides mmap/munmap which also don't look like they are part of xenon.  
   
 Is it possible to implement mmap/munmap and add sys/mman.h to xenon? If not then ftsystem.c from freetype would have to be slightly rewritten to not use mmap/munmap.  
   
 A slightly minor issue: When I ported freetype to the Wii using devkitpro I was able to use [code]* *$ ./configure --host=powerpc-eabi [/code] For xenon I tried to replace eabi with xenon but configure just complains so for now I am using 'powerpc-eabi' and manually hacking the makefiles to replace any eabi stuff with xenon. Mostly I just copy stuff from the libsdlxenon/Makefile.xenon until things compile.  
   
 I have already got SDL, zlib-1.2.5 and libpng-1.2.44 compiled with xenon. freetype is the last dependency my game has. If anyone already has a freetype library built I'll just use that, too.

## 2011-12-09 17:54:23, posted by: Ced2911

There is no mmap/munmap but you can use malloc/free

## 2011-12-09 18:40:45, posted by: kazzmir

Ok it doesn't look super critical that freetype has mmap, it will fall back to essentially malloc() if mmap returns NULL. It would still be nice to add sys/mman.h to xenon even if mmap/munmap simply return NULL. I'll add this locally.