# PCSXR-Xenon (PS1 Emulator) - compiling problems

## 2012-08-04 02:43:42, posted by: nessy74

**[b]PCSXR-Xenon (PS1 Emulator) - compiling problems[/b]**  
   
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
 then I try to compile PCSXR-Xenon (PS1 Emulator):  
   
 LibXenonProject-pcsxr-xenon-26993d9.zip https://github.com/LibXenonProject/pcsxr-xenon  
 ERROR:  
 linking ... LibXenonProject-pcsxr-xenon-26993d9.elf  
 sys.o:(.data.plugins+0x42c): undefined reference to `PEOPS\_SPUinit'  
 sys.o:(.data.plugins+0x434): undefined reference to `PEOPS\_SPUshutdown'  
 sys.o:(.data.plugins+0x43c): undefined reference to `PEOPS\_SPUopen'  
 sys.o:(.data.plugins+0x444): undefined reference to `PEOPS\_SPUclose'  
 sys.o:(.data.plugins+0x44c): undefined reference to `PEOPS\_SPUsetConfigFile'  
 sys.o:(.data.plugins+0x454): undefined reference to `PEOPS\_SPUabout'  
 sys.o:(.data.plugins+0x45c): undefined reference to `PEOPS\_SPUtest'  
 sys.o:(.data.plugins+0x464): undefined reference to `PEOPS\_SPUwriteRegister'  
 sys.o:(.data.plugins+0x46c): undefined reference to `PEOPS\_SPUreadRegister'  
 sys.o:(.data.plugins+0x474): undefined reference to `PEOPS\_SPUwriteDMA'  
 sys.o:(.data.plugins+0x47c): undefined reference to `PEOPS\_SPUreadDMA'  
 sys.o:(.data.plugins+0x484): undefined reference to `PEOPS\_SPUwriteDMAMem'  
 sys.o:(.data.plugins+0x48c): undefined reference to `PEOPS\_SPUreadDMAMem'  
 sys.o:(.data.plugins+0x494): undefined reference to `PEOPS\_SPUplayADPCMchannel'  
 sys.o:(.data.plugins+0x49c): undefined reference to `PEOPS\_SPUfreeze'  
 sys.o:(.data.plugins+0x4a4): undefined reference to `PEOPS\_SPUregisterCallback'  
 sys.o:(.data.plugins+0x4ac): undefined reference to `PEOPS\_SPUregisterCDDAVolume'  
 sys.o:(.data.plugins+0x4b4): undefined reference to `PEOPS\_SPUasync'  
 collect2: ld returned 1 exit status  
 make[1]: *** [/home/alex/sources/LibXenonProject-pcsxr-xenon-26993d9/LibXenonProject-pcsxr-xenon-26993d9.elf] Error 1  
   
 **[b]Help me please.[/b]**

## 2012-08-13 03:00:02, posted by: nessy74

Topic updated.

## 2012-08-13 03:23:23, posted by: sk1080

Which repo did you start with, there shouldn't have been missing files  
   
 drivers/threads shouldn't exist at all unless you are using a threaded libxenon

## 2012-08-13 06:14:25, posted by: ravendrow

i can confirm the same issue using the libxenon repo from free60project

## 2012-08-13 11:07:25, posted by: Ced2911

oops  
 :)  
 added plugin back  
   
 gui isn't tested, compatibity is better but speed is slower (5 -> 10%) ...

## 2012-08-13 14:48:05, posted by: nessy74

[quote="sk1080"]  
 Which repo did you start with, there shouldn't have been missing files  
   
 drivers/threads shouldn't exist at all unless you are using a threaded libxenon  
 [/quote]  
   
 i use that repo:  
 https://github.com/Free60Project/libxenon  
 and manually copied the folder "threads" from that repo:   
 https://github.com/sk1080/libxenon-testing  
 because when compiling some sources of emulators require the presence of library "threads"

## 2012-08-13 15:52:26, posted by: Ced2911

the libxenon-testing - branch gdb from sk1080,  
 should work with every homebrew without major issues, it's in experimention but it's working

## 2012-08-13 20:48:32, posted by: sk1080

I thought PCSXR wasn't threaded  
   
 Also any homebrew that uses network and isn't ready for threads will fail on my repo

## 2012-08-13 21:19:07, posted by: Ced2911

yop it's not threaded but it work with :p

## 2012-08-13 21:23:36, posted by: sk1080

Then we should have said:  
   
 You can just remove the include for <threads/threads.h>

## 2012-08-16 15:22:16, posted by: nessy74

[quote="Ced2911"]the libxenon-testing - branch gdb from sk1080,should work with every homebrew without major issues, it's in experimention but it's working[/quote]  
   
 [quote="sk1080"]drivers/threads shouldn't exist at all unless you are using a threaded libxenon[/quote]  
   
 [quote="sk1080"]You can just remove the include for <threads/threads.h>[/quote]  
   
 OK, now I use toolchain and libs compiled from https://github.com/sk1080/libxenon-testing/tree/gdb  
 (sk1080-libxenon-testing-70cd89b.zip)  
 After compiling it appeared a folder: /usr/local/xenon/usr/include/threads - with these files inside:  
 breakpoint.h / cond.h / debug\_defines.h / debug.h / gdb.h / gdbroutines.h / mutex.h / threads.h  
   
 Before the start "make" in clear unpacked "LibXenonProject-pcsxr-xenon-26993d9.zip"   
 from https://github.com/LibXenonProject/pcsxr-xenon  
 I searched for the source files phrase **[b]threads.h[/b]** and did not find it anywhere.  
 After unsuccessful "linking ... LibXenonProject-pcsxr-xenon-26993d9.elf"   
 and got the same errors: http://libxenon.org/http://libxenon.org//viewtopic.php?p=1972#p1972  
 I found phrase "threads.h" in these files:  
   
 LibXenonProject-pcsxr-xenon-26993d9/build/httpd.d  
 line 17: /usr/local/xenon/usr/include/threads/threads.h \  
 line 59: /usr/local/xenon/usr/include/threads/threads.h:  
   
 LibXenonProject-pcsxr-xenon-26993d9/build/tftp.d  
 line 16: /usr/local/xenon/usr/include/threads/threads.h \  
 line 59: /usr/local/xenon/usr/include/threads/threads.h:  
   
 Now what I must do to successfully compile the .elf ?

## 2012-08-17 17:42:29, posted by: Ced2911

git pull

## 2012-08-17 21:22:47, posted by: ravendrow

ok so just messing around with this error i changed   
 https://github.com/Ced2911/pcsxr-xenon/blob/master/source/main/sys.c#L21  
   
 to  
   
 SPU\_XENON\_PLUGIN,  
   
 cause i figured that if the problem was in sys.o i should probably check sys.c and it got rid of that stupid peops error and the files compile but when i try to run the pcsxr-xenon.elf32 it starts to load and then Xell just resets i am gonna try commenting it cause SPU\_XENON\_PLUGIN is already listed above  
   
 oh btw i compiled it using the libxenon on free60s git hub

## 2012-08-18 13:19:01, posted by: Ced2911

there is no gui, you'll have to edit path by yourself

## 2012-08-19 00:58:50, posted by: ravendrow

so it is supposed to be using the xenon\_audio\_repair folder for SPU right? i tried to switch it to xenon\_audio\_repair110 folder (because PEOPS SPU stuff is there) and changed both SPU plugins to PEOPS but same thing compiled elf32 starts to run then just resets. also tried adding the xenon\_audio\_repair110 folder to SPU libs in the makefile but that just caused conflicts  
   
 [quote="Ced2911"]  
 there is no gui, you'll have to edit path by yourself  
 [/quote]  
   
 what happened to the GUI??? :( lmao  
   
 so i tried un-commenting GUI\_FLAGS := -DUSE\_GUI in the makefile but that didn't help, not that i thought it would just took a stab at it lol so what paths do i need to set to get this thing up and going? thanks for taking time with this Ced2911 it's good to see you still poking around :)

## 2012-08-19 07:08:48, posted by: Ced2911

dev build :p imagine the time lost for selecting rom iso :p

## 2012-08-19 21:19:11, posted by: dreamboy

[quote="Ced2911"]  
 dev build :p imagine the time lost for selecting rom iso :p  
 [/quote]  
   
 lol yeah we can always make our own iso selecting code is not that hard, ced2911 how can i enable the old spu sound plugin? great work i've tested out final fantasy 9 and it works great :D

## 2012-08-20 00:42:36, posted by: ravendrow

[quote="dreamboy"]  
 [quote="Ced2911"]  
 dev build :p imagine the time lost for selecting rom iso :p  
 [/quote]  
   
 lol yeah we can always make our own iso selecting code is not that hard, ced2911 how can i enable the old spu sound plugin? great work i've tested out final fantasy 9 and it works great :D  
 [/quote]  
   
 i could be wrong but try making a backup of the xenon\_audio\_repair folder then copy the contents of xenon\_audio\_repair110 to xenon\_audio\_repair after that is done open sys.c and change both instances of SPU\_XENON\_PLUGIN to SPU\_PEOPS\_PLUGIN... alternately you could just change the SPU lib folder in the makefile to xenon\_audio\_repair110 and make the needed changes to sys.c (this is just a guess please feel free to correct me if i am wrong)

## 2012-08-20 08:35:14, posted by: Ced2911

[quote="ravendrow"]  
 [quote="dreamboy"]  
 [quote="Ced2911"]  
 dev build :p imagine the time lost for selecting rom iso :p  
 [/quote]  
   
 lol yeah we can always make our own iso selecting code is not that hard, ced2911 how can i enable the old spu sound plugin? great work i've tested out final fantasy 9 and it works great :D  
 [/quote]  
   
 i could be wrong but try making a backup of the xenon\_audio\_repair folder then copy the contents of xenon\_audio\_repair110 to xenon\_audio\_repair after that is done open sys.c and change both instances of SPU\_XENON\_PLUGIN to SPU\_PEOPS\_PLUGIN... alternately you could just change the SPU lib folder in the makefile to xenon\_audio\_repair110 and make the needed changes to sys.c (this is just a guess please feel free to correct me if i am wrong)  
 [/quote]  
   
 the makefile is what i do

## 2012-08-20 08:47:54, posted by: ravendrow

so the only thing i can't find is what to name this stupid Suikoden.bin file to make it load, i found a bunch of image paths in main.cpp but it looks like it uses that when the GUI is enabled. the reason i want to use this particular game is because it kept crashing pcsxr-xenon 0.62 so i wanted to see if the improvements help.  
   
   
 @Ced2911 yeah i thought about it after i typed the first bit and decided to add the easier way lol :P

## 2012-08-20 09:26:58, posted by: Ced2911

also keep in mind since compatibily is better, slow down are more commun ... i don't know if will be able to reach fullspeed now :s

## 2012-08-20 09:41:33, posted by: dazz

[quote="ravendrow"]  
 so the only thing i can't find is what to name this stupid Suikoden.bin file to make it load, i found a bunch of image paths in main.cpp but it looks like it uses that when the GUI is enabled. the reason i want to use this particular game is because it kept crashing pcsxr-xenon 0.62 so i wanted to see if the improvements help.  
   
   
 @Ced2911 yeah i thought about it after i typed the first bit and decided to add the easier way lol :P  
 [/quote]  
   
 Suikoden II seems to work near-on perfect for about 80-90% of the game, interesting that the first game doesn't.  
 The only issues I'm having is that saves stop working after a couple writes to the memory card, which can be solved by just restarting every time you save.

## 2012-08-20 10:04:22, posted by: Ced2911

doesn't work ?

## 2012-08-20 10:40:58, posted by: ravendrow

well i cant find where to set the suikoden.bin file path for the dev version i compiled but as for 0.62 it starts to load then about 1 1/2 minute into the opening video it halfway drops out and there is this laser light show where the video has disappeared. if you leave it running it will drop a stackdump but i can't debug it cause i never compiled my own 0.62

## 2012-08-20 10:55:33, posted by: Ced2911

in main.cpp  
 #define cdfile "path to iso"  
   
 you need to set the correct path here too   
 https://github.com/Ced2911/pcsxr-xenon/blob/master/source/main/main.cpp#L269

## 2012-08-20 11:18:07, posted by: ravendrow

[quote="Ced2911"]  
 you need to set the correct path here too   
 https://github.com/Ced2911/pcsxr-xenon/blob/master/source/main/main.cpp#L269  
 [/quote]  
   
 lol i think that right there is my problem didn't do that part assumed it was still set to the uda path , will let you know how it goes

## 2012-08-20 12:35:07, posted by: dreamboy

[quote="ravendrow"]  
 [quote="Ced2911"]  
 you need to set the correct path here too   
 https://github.com/Ced2911/pcsxr-xenon/blob/master/source/main/main.cpp#L269  
 [/quote]  
   
 lol i think that right there is my problem didn't do that part assumed it was still set to the uda path , will let you know how it goes  
 [/quote]  
   
 yup try to set those paths, i did it before and it worked without problem, saving and loading on final fantasy 9, gameplay looked fullspeed for me. i'll try to setup the sound plugin on makefile later

## 2012-08-20 13:59:21, posted by: Ced2911

ff9 will not work with other plugin

## 2012-08-21 05:30:45, posted by: ravendrow

so just to make sure i am not making a stupid mistake here is what i have set [code]* *#define cdfile "uda0:/Suikoden.bin" [/code] @ like line 50 for the image path  
 [code]* *strcpy(Config.BiosDir, "uda0:/pcsxr/bios"); strcpy(Config.PatchesDir, "uda0:/pcsxr/patches\_/"); [/code] for the bios [code]* *strcpy(Config.Mcd1, "uda0:/pcsxr/memcards/card1.mcd"); strcpy(Config.Mcd2, "uda0:/pcsxr/memcards/card2.mcd"); [/code] for the memory card  
   
 and it still just resets to xell i also tried using uda instead of uda0 but eventually i just tried to use the gui to load the game  
   
 i manged to get the gui back up(just needed select changed to back in gui.cpp and re-enable in makefile) but there is a problem when i go to load a game it gives me a msg saying it cant read the drives. so is there an issue with the GUI mounting partitions?

## 2012-08-21 08:43:14, posted by: Ced2911

https://github.com/Ced2911/pcsxr-xenon/blob/master/source/main/main.cpp#L218 :p fat was disabled only ntfs was enabled

## 2012-08-21 09:29:43, posted by: dreamboy

i've manage to compile the project with SPU\_PEOPS\_PLUGIN by comenting //SPU\_XENON\_PLUGIN on sys.c , and changing the make file to PLUGINS\_SPU := source/plugins/xenon\_audio\_repair110   
   
 but i still have no sound :\ am i missing someting? i've tested it with final fantasy 7

## 2012-08-21 10:38:32, posted by: Ced2911

don't know i don't have sound on my devbox ^^

## 2012-08-22 17:54:48, posted by: Ced2911

just made a new branch very experimental (threaded\_gpu) that give a really nice boost :) need to test more game :)

## 2012-08-22 23:57:22, posted by: ravendrow

is sk1080's libxenon testing required? n/m too excited lol i'll figure it out ;D

## 2012-08-23 00:06:01, posted by: sk1080

doesn't look like it

## 2012-08-23 16:45:34, posted by: Ced2911

didn't work like is expected, in tekken i got almost 70fps ( + 15 fps)  
   
 but in other i got some slowdown ...

## 2012-12-04 17:27:49, posted by: dreamboy

[quote="Ced2911"]  
 don't know i don't have sound on my devbox ^^  
 [/quote]  
   
 :) i finally manage to set the new spu plugin with sound working, ff9 plays nice with it hehe

## 2013-04-05 06:46:35, posted by: bebo_beta2002

i hope u guys help me...i got this error at compiling  
   
 $ make -f Makefile.debug  
 [sys.c]  
 linking ... pcsxr-xenon.elf  
 main.o: In function `cmain()':  
 /home/essam/free60project-github/pcsxr/pcsxr-xenon/source/main/main.cpp:213: und efined reference to `usb2mass\_ops\_0'  
 /home/essam/free60project-github/pcsxr/pcsxr-xenon/source/main/main.cpp:213: und efined reference to `usb2mass\_ops\_0'  
 zn.o: In function `ZN\_SPUupdate()':  
 /home/essam/free60project-github/pcsxr/pcsxr-xenon/source/plugins/xenon\_audio\_re pair110/zn.cpp:46: undefined reference to `PEOPS\_SPUasync(unsigned long)'  
 zn.o: In function `ZN\_SPUreadRegister(unsigned long)':  
 /home/essam/free60project-github/pcsxr/pcsxr-xenon/source/plugins/xenon\_audio\_re pair110/zn.cpp:64: undefined reference to `PEOPS\_SPUreadRegister(unsigned long)'  
 zn.o: In function `ZN\_SPUreadDMA()':  
 /home/essam/free60project-github/pcsxr/pcsxr-xenon/source/plugins/xenon\_audio\_re pair110/zn.cpp:74: undefined reference to `PEOPS\_SPUreadDMA()'  
 zn.o: In function `ZN\_SPUwriteDMA(unsigned short)':  
 /home/essam/free60project-github/pcsxr/pcsxr-xenon/source/plugins/xenon\_audio\_re pair110/zn.cpp:84: undefined reference to `PEOPS\_SPUwriteDMA(unsigned short)'  
 zn.o: In function `ZN\_SPUwriteDMAMem(unsigned short*, int)':  
 /home/essam/free60project-github/pcsxr/pcsxr-xenon/source/plugins/xenon\_audio\_re pair110/zn.cpp:94: undefined reference to `PEOPS\_SPUwriteDMAMem(unsigned short*, int)'  
 zn.o: In function `ZN\_SPUreadDMAMem(unsigned short*, int)':  
 /home/essam/free60project-github/pcsxr/pcsxr-xenon/source/plugins/xenon\_audio\_re pair110/zn.cpp:104: undefined reference to `PEOPS\_SPUreadDMAMem(unsigned short*, int)'  
 zn.o: In function `ZN\_SPUopen()':  
 /home/essam/free60project-github/pcsxr/pcsxr-xenon/source/plugins/xenon\_audio\_re pair110/zn.cpp:140: undefined reference to `PEOPS\_SPUinit()'  
 /home/essam/free60project-github/pcsxr/pcsxr-xenon/source/plugins/xenon\_audio\_re pair110/zn.cpp:141: undefined reference to `PEOPS\_SPUopen()'  
 zn.o: In function `ZN\_SPUclose()':  
 /home/essam/free60project-github/pcsxr/pcsxr-xenon/source/plugins/xenon\_audio\_re pair110/zn.cpp:153: undefined reference to `PEOPS\_SPUclose()'  
 /home/essam/free60project-github/pcsxr/pcsxr-xenon/source/plugins/xenon\_audio\_re pair110/zn.cpp:154: undefined reference to `PEOPS\_SPUshutdown()'  
 zn.o: In function `ZN\_SPUregisterCallback(void (*)())':  
 /home/essam/free60project-github/pcsxr/pcsxr-xenon/source/plugins/xenon\_audio\_re pair110/zn.cpp:165: undefined reference to `PEOPS\_SPUregisterCallback(void (*)() )'  
 zn.o: In function `ZN\_SPUfreeze(unsigned long, void*)':  
 /home/essam/free60project-github/pcsxr/pcsxr-xenon/source/plugins/xenon\_audio\_re pair110/zn.cpp:175: undefined reference to `PEOPS\_SPUfreeze(unsigned long, SPUFr eeze\_t*)'  
 xr\_psemu.o: In function `SPUgetOne(unsigned long)':  
 /home/essam/free60project-github/pcsxr/pcsxr-xenon/source/plugins/xenon\_audio\_re pair110/xr\_psemu.cpp:43: undefined reference to `PEOPS\_SPUreadDMA()'  
 xr\_psemu.o: In function `SPUputOne(unsigned long, unsigned short)':  
 /home/essam/free60project-github/pcsxr/pcsxr-xenon/source/plugins/xenon\_audio\_re pair110/xr\_psemu.cpp:53: undefined reference to `PEOPS\_SPUwriteDMA(unsigned shor t)'  
 cmount.o: In function `mount\_interface':  
 /home/essam/free60project-github/pcsxr/pcsxr-xenon/source/newgui/cmount.c:48: un defined reference to `usb2mass\_ops\_0'  
 /home/essam/free60project-github/pcsxr/pcsxr-xenon/source/newgui/cmount.c:48: un defined reference to `usb2mass\_ops\_0'  
 /usr/local/xenon/usr/lib/libfat.a(disc.o): In function `get\_io\_usbstorage':  
 /home/Cc/xenon/fat-xenon/fat-xenon/libxenon/../source/disc.c:50: undefined refer ence to `usb2mass\_ops\_0'  
 /home/Cc/xenon/fat-xenon/fat-xenon/libxenon/../source/disc.c:50: undefined refer ence to `usb2mass\_ops\_0'  
 collect2: ld returned 1 exit status  
 /usr/local/xenon/rules:39: recipe for target `/home/essam/free60project-github/p csxr/pcsxr-xenon/pcsxr-xenon.elf' failed  
 make[1]: *** [/home/essam/free60project-github/pcsxr/pcsxr-xenon/pcsxr-xenon.elf ] Error 1  
 Makefile.debug:151: recipe for target `build\_debug' failed  
 make: *** [build\_debug] Error 2  
   
 i tried everything dreamboy stated in this topic as a solution but with no luck :(  
 i hope u guys help me

## 2015-03-15 22:04:07, posted by: <Unknown User>

Hi dreamboy.  
   
 I have the same problem, no sound in games.  
   
 How did you do to make it work ? Could you put the compiled archive here please ?  
 You would make a happy !!!

## 2015-03-18 00:22:37, posted by: <Unknown User>

[quote="dreamboy"][quote="Ced2911"] don't know i don't have sound on my devbox ^^ [/quote] :) i finally manage to set the new spu plugin with sound working, ff9 plays nice with it hehe[/quote] How did you do to have sound, I have no sound on all games I tested on my corona, but except that they run very well !  
 I don't know how to recompile xenon, but I would be so happy to make the sound work.  
   
 Any idea ?