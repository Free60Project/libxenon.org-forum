# Debug: Endless loading screen (xmplayer)

## 2012-07-19 02:42:00, posted by: siz

Hey guys,  
   
 I previously had a issue with a endless loading screen when formatting with the windows system, which I fixed using fat32 fomat gui (http://www.ridgecrop.demon.co.uk/index.htm?guiformat.htm), but there seems to be a lot still having the issue after using the program. I noticed a blink of a red dump screen when it occurs, so to see what it says I commented some lines (Menu\_DrawImg etc.) in menu.cpp under loadingThread() and got this:  
   
 ![](http://peecee.dk/uploads/072012/debug_loading.jpg)[img]http://peecee.dk/uploads/072012/debug\_loading.jpg[/img]  
   
 I don't know if you can use it for anything, but one thing is for sure I can't interpret it, so maybe you can :)   
   
 (the red dump screen doesn't occur with those comments on drives that normally works, the menu just pops up)

## 2012-07-19 12:15:03, posted by: siz

Btw, tried it with the newest xell source today, because I saw some updates here: https://github.com/Free60Project/xell/commit/86183992aabffeb099797533635427fb8470ac2d  
   
 However, without the menu.cpp comments, it now just goes straight to red dump screen (again, a drive that worked before still works):  
 ![](http://peecee.dk/uploads/072012/debug2.jpg)[img]http://peecee.dk/uploads/072012/debug2.jpg[/img]

## 2012-07-20 02:53:36, posted by: tuxuser

On your compiled filename.elf (not elf32 !!!) do the following to debug the error:  
 [code]* *xenon-addr2line -e filename.elf 0x0000000 0x00000001 0x00000002 [/code] where 0x0 0x1 0x2 are the numbers of the stackdump (left -> right ,top -> bottom)  
   
 for example for the first stackdump picture:  
 [code]* *xenon-addr2line -e xmplayer.elf 0x80708940 0x80708848 0x8970a660 0x8070af80 0x8001df3c 0x8001e4e4 0x8000c108 0x80001ef4 0x80701bf4 [/code]

## 2012-07-20 11:52:39, posted by: siz

will do tux, stay tuned.

## 2012-07-20 12:28:07, posted by: siz

**[b]1st screendump:[/b]** [code]/home/siz/libxenon/libxenon/ports/xenon/../../drivers/usb/tinyehci/ehci.c:365 /home/siz/libxenon/libxenon/ports/xenon/../../drivers/usb/tinyehci/ehci.c:618 /home/siz/libxenon/libxenon/ports/xenon/../../drivers/usb/tinyehci/usbstorage.c:972 /home/siz/libxenon/libxenon/ports/xenon/../../drivers/usb/tinyehci/usbstorage.c:1356 /home/siz/xmplayer/source/mount.c:395 /home/siz/xmplayer/source/mount.c:494 /home/siz/xmplayer/source/menu.cpp:1716 /home/siz/libxenon/libxenon/ports/xenon/../../startup/xenon/crt1.c:27 argv.c:0[/code] Xell version: 19/02-2012  
   
 **[b]2nd screendump:[/b]** [code]/home/siz/xmplayer/source/libwiigui/gui\_element.cpp:195 /home/siz/xmplayer/source/libwiigui/gui\_element.cpp:195 /home/siz/xmplayer/source/libwiigui/gui\_image.cpp:240 /home/siz/xmplayer/source/libwiigui/gui\_image.cpp:124 /home/siz/xmplayer/source/FreeTypeGX.cpp:650 /usr/local/xenon/lib/gcc/xenon/4.6.1/../../../../xenon/include/c++/4.6.1/bits/stl\_tree.h:963 /home/siz/xmplayer/source/filebrowser.cpp:214 /home/siz/libxenon/libxenon/ports/xenon/../../startup/xenon/crt1.c:27 /home/siz/xmplayer/source/menu.cpp:539[/code] Xell version: 19/07-2012  
   
 I have some edits in menu.ccp so maybe the lines aren't the same so:  
 Line 539: browser\_files\_icon[BROWSER\_TYPE\_PICTURE] = new GuiImageData(browser\_photo\_icon\_f\_png);  
 Line 1716: findDevices();  
 ----------------------------------  
 Updated: downloaded and unmodified git version (besides comments as before):  
   
 **[b]1st dump - Xell version 19/02-2012 and 2nd dump - Xell version 19/07-2012:[/b]** [code]/home/siz/Downloads/xmplayer/source/libwiigui/gui\_element.cpp:243 /home/siz/Downloads/xmplayer/source/libwiigui/gui\_element.cpp:227 /home/siz/Downloads/xmplayer/source/libwiigui/gui\_image.cpp:33 /home/siz/Downloads/xmplayer/source/libwiigui/gui\_list.cpp:150 /home/siz/Downloads/xmplayer/source/FreeTypeGX.cpp:650 /usr/local/xenon/lib/gcc/xenon/4.6.1/../../../../xenon/include/c++/4.6.1/bits/stl\_tree.h:963 /home/siz/Downloads/xmplayer/source/filebrowser.cpp:214 /home/siz/libxenon/libxenon/ports/xenon/../../startup/xenon/crt1.c:27 /home/siz/Downloads/xmplayer/source/menu.cpp:494[/code] The 2nd dump is actually identical with the 1st one using git clone without modifications with xell from 19/07-2012.

## 2012-07-30 13:20:50, posted by: ravendrow

hey siz your issue is still spinlock that patch doesn't seem to work with mplayer but....  
   
 go to sk1080's git hub and clone libxenon-testing then go to /libxenon-testing/libxenon/drivers/ppc/  
 and copy atomic.s and atomic.h to your libxenon/drivers/ppc replacing the ones there rebuild libxenon then recompile xmplayer and all should load right  
   
 i am gonna test you changes in the morn i am tired lol  
   
 thanks to SK1080 for leaving that up :)  
   
 NOTE: ok so i just tested my sudo working build lol... that code does seem to work fine with mp4's but mkvs glitching badly

## 2012-07-30 13:41:18, posted by: siz

thanks for the tip ravendrow :) will give it go when I have the time.

## 2012-07-31 04:31:44, posted by: ravendrow

k so i manually changed atomic.S to match the lock.diff supplied by sk1080 and what do you know no more stupid stack dump flash when loading .....i must have been off slightly the first time i did it (thats what i get for doing it at 4 am lol)anyways to make it easy for anyone else looking to compile a working xmplayer l have the modified atomic.s on my git hub just copy it to libxenon/libxenon/drivers/ppc then go to your toolchain folder IE libxenon/toolchain and run [code]* *./build-xenon-toolchain libxenon [/code] as long as it says libxenon installed successfully your good to go

## 2012-07-31 15:03:48, posted by: siz

Well, tried it, and it stops endless loading screen, but the performance is really bad compared to before, videos crash without dump screen, just halts, there is slowdowns before something happens etc. So until now I'll stick to the stable one, even though some usb doesn't load.

## 2012-07-31 18:07:19, posted by: ravendrow

[quote="siz"]  
 Well, tried it, and it stops endless loading screen, but the performance is really bad compared to before, videos crash without dump screen, just halts, there is slowdowns before something happens etc. So until now I'll stick to the stable one, even though some usb doesn't load.  
 [/quote]  
   
 yeah like i said the one from SK1080 libxenon testing glitches pretty bad i switched to the stable one myself...i haven't had any issues with usb yet though (except for drives that didn't work with the initial release )  
   
 checked out that commit you made last night everything seems to run pretty smoothly  
   
 i did notice subtitle size big isn't working though

## 2012-08-01 17:00:49, posted by: Ced2911

is it the fixe with align16 ? it's the one which should work.  
 for usb key error i think it's related to usb core (ehci)

## 2012-08-02 03:01:03, posted by: ravendrow

[quote="Ced2911"]  
 is it the fixe with align16 ? it's the one which should work.  
 for usb key error i think it's related to usb core (ehci)  
 [/quote]  
   
 the one i am using is this one http://madhack.tk/xenon/lock.diff pretty sure it is the same one siz is using

## 2012-08-02 05:58:28, posted by: sk1080

that worked for me playing a mp4  
 also give it a go by only adding  
   
 + li %r4, -1  
 + mtspr hdec, %r4 // reset the hypervisor decrementer to fix a lock issue

## 2012-08-02 15:58:20, posted by: siz

hey sk1080, it seems to do the trick, without all the side effects :) I haven't tested it to be sure there aren't any stability issues, but if it comes up, I'll give a reply. Thanks 8)  
   
 Btw the one I am using looks like this: [code]* *#include <ppc/xenonsprs.h> // Taken from: http://www.ibm.com/developerworks/library/pa-atom/ .globl atomic\_inc atomic\_inc: 1: lwarx %r4, 0, %r3 addi %r4, %r4, 1 stwcx. %r4, 0, %r3 bne- 1b blr .globl atomic\_dec atomic\_dec: 1: lwarx %r4, 0, %r3 subi %r4, %r4, 1 stwcx. %r4, 0, %r3 bne- 1b blr .globl atomic\_clearset atomic\_clearset: 1: lwarx %r6, 0, %r3 andc %r6, %r6, %r4 or %r6, %r6, %r5 stwcx. %r6, 0, %r3 bne- 1b blr .globl atomic\_compareswap atomic\_compareswap: li %r7, 0 mfmsr %r8 1: mtmsrd %r7, 1 // Turn off interrupts lwarx %r6, 0, %r3 mr %r9, %r6 // Save value in r9 cmplwi cr7, %r6, %r5 bne cr7, 2f mr %r6, %r4 2: stwcx. %r6, 0, %r3 mtmsrd %r8, 1 // Restore them to what they were before bne 1b // If unable to store, retry mr %r3, %r9 lwsync blr // thanks cOz for the following :) .globl lock lock: li %r8, 0 1: mfmsr %r7 mtmsrd %r8, 1 // Disable interrupts lwarx %r4, 0, %r3 cmplwi cr7, %r4, 0 bne cr7, 2f // If r4 is not zero, dont modify mr %r4, %r3 2: stwcx. %r4, 0, %r3 mtmsrd %r7, 1 // Restore interrupts bne cr7, 3f // r4 was not zero, lock again bne 3f // Reservation invalid, lock again lwsync blr 3: db16cyc b 1b .globl unlock unlock: li %r4, 0 lwsync stw %r4, 0(%r3) li %r4, -1 mtspr hdec, %r4 // reset the hypervisor decrementer to fix a lock issue blr[/code] Now to figure out why mplayer doesn't seek with files greater than 2 gigs..

## 2012-08-02 16:44:27, posted by: Ced2911

could it be a seek issue ? 32bit vs 64bit seek ?

## 2012-08-02 16:49:25, posted by: siz

Yeah, I also think so, right now I think it's because of off\_t, so I was thinking of compiling with -D\_FILE\_OFFSET\_BITS=64, but where should I place that?

## 2012-08-02 16:59:04, posted by: Ced2911

i think in newlib + libxenon

## 2012-08-02 17:38:15, posted by: siz

tried to add -D\_FILE\_OFFSET\_BITS=64 to all CFLAGS in ./build-xenon-toolchain and I installed toolchain, libs and libxenon again, no luck, also tried adding it in Makefile of xmplayer :/

## 2012-08-02 17:48:58, posted by: Ced2911

on which fs and device did you tried ?

## 2012-08-02 17:52:35, posted by: Ced2911

in toolchain ... typedef long \_off\_t; :s

## 2012-08-02 18:26:10, posted by: siz

[quote="Ced2911"]  
 on which fs and device did you tried ?  
 [/quote]  
 System is ubuntu (wubi), ntfs, Core i7.   
 On xbox, 1 external hdd with 2 partitons, fat32 for xenon.elf etc. and ntfs for files > 4 gb, xell doesn't detect xenon.elf on the ntfs partition.   
   
 [quote="Ced2911"]  
 in toolchain ... typedef long \_off\_t; :s  
 [/quote]  
 Not typedef long off\_t;? And you mean in ./build-toolchain-xenon? If yes, where? isn't it a batch file?   
   
 P.S. There is actually a "typedef long \_off\_t;" in "libxenon\include\machine\powerpc\machine\\_types.h".

## 2012-08-02 18:57:06, posted by: Ced2911

for xell did you compiled it with ntfs support ?  
 i'm tring something to see if i can get newlib working with big files

## 2012-08-02 19:22:41, posted by: siz

Nope, haven't compiled xell with ntfs support, will look into it.

## 2012-08-02 23:00:31, posted by: ravendrow

i tried to compile xell with NTFS support but it makes xell way to big there would have to be a trade off to get the size right? like sacrificing ext2fs support?

## 2012-08-02 23:16:35, posted by: tuxuser

try it, XeLL has a config.h.. where you can disable/enable the filesystems easily

## 2012-08-03 01:19:06, posted by: siz

Xell with ntfs doesn't seem to work for me, trying with xellaunch, it works fine with ntfs commented, tried even commenting iso and exf2s, no luck. It just a black screen.

## 2012-08-03 01:26:20, posted by: ravendrow

so yeah even after commenting all except NTFS xell still exceeds 256kb :(

## 2012-08-03 09:52:08, posted by: Ced2911

newlib doesn't have 64bit file io.  
 it can probably be added by adding   
 #define \_\_LARGE64\_FILES 1  
 #define \_LARGEFILE64\_SOURCE 1  
 in newlibdir/libc/include/sys/config.h  
 and implemented in libxenon

## 2012-08-03 21:05:10, posted by: siz

[quote="Ced2911"]  
 newlib doesn't have 64bit file io.  
 it can probably be added by adding   
 #define \_\_LARGE64\_FILES 1  
 #define \_LARGEFILE64\_SOURCE 1  
 in newlibdir/libc/include/sys/config.h  
 and implemented in libxenon  
 [/quote]  
   
 Actually it's already added in newlib's config.h, line 68 and 70 (newlib 1.17.0), so it's "just" a matter of implementing it in libxenon(?). + on a different note, where is the "osd toggle" defined for xmplayer, I mean removing mp\_cmd\_osd in command.c or commenting it's definition in input.c/h doesn't do anything with the osd bind in input.conf (it still shows)?

## 2012-08-04 11:23:13, posted by: Ced2911

check in getch-xenon and in mplayer input config