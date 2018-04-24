# ZLX - Xenon Library

## 2011-09-01 00:16:28, posted by: tuxuser

This is ZLX, a library for libxenon, which is a nice alternative to SDL via LibXenon. It has samples included to build a filebrowser or console application.   
 Biggest benefit: You can either use it on your xbox or test stuff on windows with it.  
 Before compiling ZLX you need [url=http://libxenon.org/http://libxenon.org//viewtopic.php?t=6]libpng and zlib[/url] installed!  
   
 To compile ZLX as a library then, do: [code]make -f Makefile\_lib make -f Makefile\_lib install[/code] To compile the ZLX Browser, do: [code]make[/code] Latest version of zlx is at: [url=https://github.com/LibXenonProject/ZLX-Library]Github[/url]  
 Ced2911 codes and maintains the zlx library.  
   
 **[b]It's recommended to always use the latest version from Github![/b]**

### Attachments

[zlx-svn20110925.tar.gz](zlx-svn20110925.tar.gz)

## 2011-09-09 06:57:15, posted by: ravendrow

hey hey me again lol so i noticed gligli updated source code for mupen64 and when i went to compile it i crapped out with errors relating to my missing zlx library i was wondering if you know i might install it i already have libpng and zlib installed thanks in advance for the help  
   
 nevermind got it sorted from what i can tell not sure if this is right there are a few errors in commands at the bottom of makefile\_lib it tried to copy to lzx when it should be zlx after correcting that   
   
 make -f Makefile\_lib install  
   
 should build everything properly...tested it out on the GliGli's 0.91 build of mupen64 worked like a charm

## 2011-09-11 01:09:06, posted by: tuxuser

Updated first post with rev9 from SVN

## 2012-01-27 18:55:13, posted by: barnhilltrckn

I am not sure why but when I try to do this I get this error:  
 brian@debian:~$ cd '/home/brian/Desktop/Libxenon Stuff/zlx'   
 brian@debian:~/Desktop/Libxenon Stuff/zlx$ make -f Makefile\_lib  
 make[1]: /home/brian/Desktop/Libxenon: No such file or directory  
 make[1]: *** No rule to make target `/home/brian/Desktop/Libxenon'. Stop.  
 make: *** [build] Error 2  
 brian@debian:~/Desktop/Libxenon Stuff/zlx$   
   
 Now I know that Makefile\_lib is in that folder and I have zlib and libpng installed. Any ideas? Thanks.

## 2012-01-28 23:37:23, posted by: tuxuser

Remove the space in directory "Libxenon Stuff" and try again

## 2012-01-29 00:20:36, posted by: barnhilltrckn

Yup that took care of it. Thanks tuxuser!!

## 2012-03-25 12:40:26, posted by: joh

Nice piece of software.

## 2012-08-03 22:25:39, posted by: nessy74

Hallo.  
   
 I use Windows XP + Cygwin.  
   
 I compiled Libxenon Toolchain from there:  
 http://free60.org/Compiling\_the\_Toolchain  
   
 and performed  
 ./build-xenon-toolchain libs (installed: libxenon + bin2s + zlib + libpng + bzip2 + freetype)  
   
 then I try to compile programs  
 Some of them require the presence of ZLX - Xenon Library,  
 for example: Mupen https://github.com/LibXenonProject/mupen64-360  
   
 These programs will generate an error:  
 /home/Alex/mupen/source/main/main.cpp:75:25: fatal error: zlx/Browser.h: No such file or directory  
   
 I decided to install ZLX - Xenon Library.  
   
 Latest version of zlx is at: Github [url=https://github.com/LibXenonProject/ZLX-Library]https://github.com/LibXenonProject/ZLX-Library[/url]  
 make -f Makefile\_lib  
 error: /home/Alex/zlx/zlx/mount.h:12:24: fatal error: libfat/fat.h: No such file or directory  
 I copied folders "libfat" + "libntfs" from here: "...\Open source Wii GUI USB Loader (libfat + libntfs)"  
 here: c:\Cygwin\home\Alex\zlx\libs\include\  
 make -f Makefile\_lib  
 errors:  
 In file included from /home/Alex/zlx/zlx/mount.h:12:0,  
 from /home/Alex/zlx/zlx/Hw.cpp:29:  
 /home/Alex/zlx/libs/include/libfat/fat.h:54:25: fatal error: disc\_io.h: No such file or directory  
   
 Help me please.

## 2012-08-03 23:54:06, posted by: ravendrow

you need to have all fs libs install   
   
 ntfs-xenon  
 fat-xenon  
 xtaflib  
 extfs2  
   
 they are all on libxenon's git hub just cd into each folder and run make then make install

## 2012-08-04 01:30:10, posted by: nessy74

https://github.com/LibXenonProject/xtaflib  
 https://github.com/LibXenonProject/ext2fs-xenon  
 https://github.com/LibXenonProject/ntfs-xenon  
 https://github.com/LibXenonProject/fat-xenon  
   
 The problem is solved.  
   
 Thanks for the help.

## 2013-01-15 14:45:47, posted by: lonerr

when i make xtaflib got an error diskio/disc\_io.h: No such file or directory  
 anyone know where can i get it and where should i put it in?

## 2013-01-16 10:06:21, posted by: dreamboy

[quote="lonerr"]  
 when i make xtaflib got an error diskio/disc\_io.h: No such file or directory  
 anyone know where can i get it and where should i put it in?  
 [/quote]  
   
 did you install all libs when you installed libxenon toolchain?  
   
 open terminal with su permitions and go to the libxenon toolchain folder and type  
 [code]sudo su ./build-xenon-toolchain libs [/code] Now it will install all libs that are missing on your setup

## 2013-11-20 18:07:09, posted by: Stakhanov

Hello people I recently get a USB key for my xbox to launch Xell Homebrews and I'm quite confused, I'm using windows and I don't know how to compile those stuffs, so well if you have a tutorial for me to compile it'd be quite helpfull as I'm happy using NT I don't want to install a linux distro only to compile some Xell homebrews, is there a way I can do this easily if I'm not using linux ?  
   
 I'm especially looking for a ZLX-Browser build that'd support my corona as any of the compiled ZLX Browsers I found werent supporting corona video output...  
   
 Edit : Ok tried on a fedora vm, when I type "*[i]make zlx-svn20110925.tar.gz[/i]*" it tells me I have to specify rules but I only want the ZLX-Browser so what can I do ?  
   
 here's a screen of the error (its in french though) : ![](http://gyazo.com/0e2ef65109acf60b08d45bd156288572.png)[img]http://gyazo.com/0e2ef65109acf60b08d45bd156288572.png[/img]  
   
 Edit2: got some help on the irc channel, thank you sk1080 ;)  
   
 Edit3: well still not working properly, I'm gonna use the kboot.conf method anyway...

## 2013-11-21 15:42:57, posted by: dreamboy

[quote="Stakhanov"]  
 Hello people I recently get a USB key for my xbox to launch Xell Homebrews and I'm quite confused, I'm using windows and I don't know how to compile those stuffs, so well if you have a tutorial for me to compile it'd be quite helpfull as I'm happy using NT I don't want to install a linux distro only to compile some Xell homebrews, is there a way I can do this easily if I'm not using linux ?  
   
 I'm especially looking for a ZLX-Browser build that'd support my corona as any of the compiled ZLX Browsers I found werent supporting corona video output...  
   
 Edit : Ok tried on a fedora vm, when I type "*[i]make zlx-svn20110925.tar.gz[/i]*" it tells me I have to specify rules but I only want the ZLX-Browser so what can I do ?  
   
 here's a screen of the error (its in french though) : ![](http://gyazo.com/0e2ef65109acf60b08d45bd156288572.png)[img]http://gyazo.com/0e2ef65109acf60b08d45bd156288572.png[/img]  
   
 Edit2: got some help on the irc channel, thank you sk1080 ;)  
   
 Edit3: well still not working properly, I'm gonna use the kboot.conf method anyway...  
 [/quote]  
   
 hi, how are you? did you followed this tutorial about how to setup libxenon on your machine?  
   
 [url=http://libxenon.org/http://libxenon.org//viewtopic.php?p=404#p404]http://libxenon.org/http://libxenon.org//viewtopic.php?p=404#p404[/url]

## 2013-11-21 18:27:41, posted by: Stakhanov

Thanks, I'm gonna try this, as it seems my Xell cant properly handle my kboot.conf