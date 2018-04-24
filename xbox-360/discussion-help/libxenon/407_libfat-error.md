# libfat error

## 2013-06-25 15:54:38, posted by: jesseed

Can some one please help me, i get an error trying to compile the file example from libxenon.  
 I get the following error:  
   
 jesse@EdubuntuTS:~/libxenon-testing/libxenon-testing/devkitxenon/examples/xenon/file/browser$ make  
 [main.c]  
 linking ... browser.elf  
 /usr/local/xenon/usr/lib/libfat.a(disc.o): In function `get\_io\_usbstorage':  
 /home/jesse/fat-xenon/libxenon/../source/disc.c:51: undefined reference to `usb2mass\_ops'  
 /home/jesse/fat-xenon/libxenon/../source/disc.c:51: undefined reference to `usb2mass\_ops'  
 collect2: error: ld returned 1 exit status  
 make[1]: *** [/home/jesse/libxenon-testing/libxenon-testing/devkitxenon/examples/xenon/file/browser/browser.elf] Error 1  
 make: *** [build] Error 2  
 jesse@EdubuntuTS:~/libxenon-testing/libxenon-testing/devkitxenon/examples/xenon/file/browser$  
   
 I can't find where "usb2mass\_ops" is defined (as it is external in disc.c).  
   
 Thanks

## 2013-06-27 23:49:09, posted by: tuxuser

Can you specifiy which git repository of libxenon you are using, which branch?  
   
 I have no problems compiling it with the current Repo: https://github.com/Free60Project/libxenon -**[b] master branch[/b]**  
   
 do a: **[b]git pull[/b]**  
 and let it build libxenon again: **[b]./build-xenon-toolchain libxenon[/b]**  
   
 Greetz

## 2013-09-01 23:55:55, posted by: Swizzy

It's probably also in the fat-xenon so run ./build-xenon-toolchain libs aswell one more time after pulling

## 2013-12-31 00:50:18, posted by: SonicKiller

Hi,  
   
 Had the same problem too, solved it by respecting the new variables names "usb2mass\_ops\_0".  
   
 Created a topic here about the modification and problems it can create :  
   
 http://libxenon.org/http://libxenon.org//viewtopic.php?t=5