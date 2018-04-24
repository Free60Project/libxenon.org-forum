# Mame-LX - compiling problems

## 2012-08-03 22:50:48, posted by: nessy74

Hallo.  
 I use Ubuntu 12.04 (precise) 32-bit i686  
   
 ================  
 I compiled Libxenon Toolchain from there:  
 http://free60.org/Compiling\_the\_Toolchain  
   
 and performed  
 ./build-xenon-toolchain libs (installed: libxenon + bin2s + zlib + libpng + bzip2 + freetype)  
   
 after installing some missing files copied manually from the repositories:  
 git://github.com/gligli/libxenon.git  
 git://github.com/sk1080/libxenon-testing.git  
 git://free60.git.sourceforge.net/gitroot/free60/free60  
 here: / usr / local / xenon / usr / include - need to copy these folders from here:  
 (initially did NOT overwrite files that are already there, we'll see)  
 libxenon\_gligli / libxenon / drivers / diskio (by the way "ata.h" - various)  
 libxenon\_gligli / libxenon / drivers / fat (it was not there at all)  
 libxenon\_gligli / libxenon / drivers / newlib (was empty)  
 libxenon\_sk1080 / libxenon / drivers / threads (it was not there at all)  
 libxenon\_free60 / libxenon / drivers / nocfe (by the way "cfe.h" - various)  
   
 now we have to install these libraries for Xenon (file systems):  
 https://github.com/LibXenonProject/xtaflib  
 https://github.com/LibXenonProject/ext2fs-xenon  
 https://github.com/LibXenonProject/ntfs-xenon  
 https://github.com/LibXenonProject/fat-xenon  
 unpack the files in any folder, then run for each folder:  
 make> and then: make install  
 will be created and filled with folders:  
 / usr / local / xenon / usr / include / libfat  
 / usr / local / xenon / usr / include / libntfs  
 / usr / local /xenon / usr / include / libext2  
 / usr / local / xenon / usr / include / libxtaf  
   
 Then you need to install the library ZLX http://libxenon.org/index.php?topic=154 - it will not install without installing "libext2" (see above)  
 make-f Makefile\_lib  
 make-f Makefile\_lib install  
 created and filled a folder: / usr / local / xenon / usr / include / zlx  
   
 . / build-xenon-toolchain cube  
 successfully compiled file cube.elf32  
   
 ==========================  
   
 then I try to compile Mame-LX:  
   
 https://github.com/LibXenonProject/mame-lx&nbsp; LibXenonProject-mame-lx-e58a80f.zip (or)  
 https://github.com/Ced2911/mame-lx&nbsp; Ced2911-mame-lx-e58a80f.zip  
   
 in the file: LibXenonProject-mame-lx-e58a80f/libxenon\_changes.txt written that we must add some lines in the files Libxenon folder:  
 (where the error is written that we should not rule ctr1.c crt1.c)  
 libxenon\_Free60Project/libxenon/startup/xenon/crt1.c - there have been exactly the line  
 libxenon\_Free60Project/libxenon/startup/xenon/startup\_from\_xell.S - there were similar strings  
 libxenon\_Free60Project/devkitxenon/app.lds - there have been exactly the line  
   
 [u]Such problems arise:[/u]  
   
 **[b]make[/b]** - begin to compile  
 Converting src/mame/layout/cps3.lay...  
 btools/file2str: btools/file2str: cannot execute binary file  
   
 precompiled binaries in a folder btools not compatible with my CPU.  
 files is as follows: file2str m68kmake makedep makedev makelist png2bdc tmsmake verinfo  
 I recompiled them from this sources: http://mamedev.org/downloader.php?file=releases/mame0144s.zip  
 in this case had to compile a complete Mame Win32 0.144 under Linux  
 then copy the new files received to folder btools in Mame-LX sources, replacing the existing incompatible versions out there.  
   
 **[b]make[/b]** - continue to compile  
 Error: src / osd / xenon / xenon\_input.c: 136:51: error: 'struct controller\_data\_s' has no member named 'select'  
 I corrected a file xenon\_input.c the word "select" on the "back"  
   
 **[b]make[/b]** - continue to compile  
 Error:  
 src / osd / xenon / gui / gui\_input.cpp: 289:9: error: 'struct controller\_data\_s' has no member named 'select'  
 src / osd / xenon / gui / gui\_input.cpp: 357:9: error: 'struct controller\_data\_s' has no member named 'select'  
 src / osd / xenon / gui / gui\_input.cpp: 423:9: error: 'struct controller\_data\_s' has no member named 'select'  
 I corrected a file gui\_input.cpp the word "select" on the "back"  
   
 **[b]make[/b]** - continue to compile  
 Error:  
 Building driver list obj / xenon / mamexenon / mame / mame.lst ...  
 btools / makelist obj / xenon / mamexenon / mame / mame.lst obj / xenon / mamexenon / mame / mameplus.lst obj / xenon / mamexenon / mame / mamehb.lst obj / xenon / mamexenon / mame / mamedecrypted.lst> obj / xenon / mamexenon / drivlist.c  
 Importing drivers from''  
 Unable to read source file''  
 obj / xenon / mamexenon / mame / mame.lst: 1 - Invalid character '"' in driver" "obj / xenon / mamexenon / mame / mame."  
   
 the problem is that the file is created drivlist.c zero length because the generated .lst files in the folder: obj / xenon / mamexenon / mame  
 have disrupted the structure, some lines are empty, some incorrect.  
   
 These .lst files appear in the compilation process and not present in the source.  
   
 From this point, I can not continue to compile more.  
   
 Help me please.

## 2012-08-04 11:21:11, posted by: Ced2911

try using linux

## 2012-08-13 01:28:18, posted by: nessy74

[quote="Ced2911"]try using linux[/quote]  
   
 Now I use Linux, I changed the topic, has moved on, but problems remain.

## 2012-08-13 08:26:54, posted by: Ced2911

btw mame is a lost of time, it's not very stable and slow

## 2012-08-13 14:26:34, posted by: nessy74

but MAME has the largest list of supported games, and many of them are not in FBANext 360 0.2.97.25 but there is a MAME-LX, which is based on MAME 0.144 or higher. Of course if you have a view of the MAME 0.72 Release 2 for the Xbox 360, it is indeed very old and inferior version of MAME 0.144 or higher, but even there there are games that are not supported in FBANext 360 0.2.97.25, because it's not all versions of arcade machine supports.

## 2012-08-13 15:14:05, posted by: Ced2911

yes i agress but mame is getting slower at each revision ...  
 i did it for fun, never released it ...  
 a lot of driver doesn't work  
 or are very slow... i don't want to lose time on it ^^

## 2012-08-13 15:50:44, posted by: Ced2911

also with the current elf size limitation (32 or 16mb) it's not possible to include all driver

## 2012-08-13 21:52:00, posted by: nessy74

[quote="Ced2911"]  
 i did it for fun, never released it ...  
 i don't want to lose time on it ^^  
 [/quote]  
   
 well, now I understand. I am not a programmer and I thought that all the sources that are uploaded to the repository must be compiled and run as a ready-made programs. but now I realize that the repositories are available for download the source code may be unfinished.

## 2012-08-13 21:55:54, posted by: Ced2911

it's why there is release version and source :)

## 2012-08-18 19:12:45, posted by: Ced2911

https://github.com/Ced2911/drunken-ironman <- based on mame 0.146 - work with "classic" libxenon  
   
 it's configured to create a tiny build ( work only with those roms http://mamedev.org/roms/ )  
   
 it's not tested tried only carpolo :)