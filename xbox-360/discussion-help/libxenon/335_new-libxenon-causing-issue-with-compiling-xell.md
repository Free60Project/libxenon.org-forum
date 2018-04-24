# new libxenon causing issue with compiling xell?

## 2012-07-15 20:27:03, posted by: ravendrow

lol why ? why? do i get all the issues ?? ;D  
   
 so i went to make myself a custom matrix theme xell and upon compiling i get   
   
 xell/source/lv2/kboot/kbootconf.c:415:67: error: 'struct controller\_data\_s' has no member named 'select'  
 make[3]: *** [kbootconf.o] Error 1  
 make[2]: *** [build] Error 2  
 make[1]: *** [stage2.elf32.gz] Error 2  
 make: *** [xell-1f.build] Error 2  
   
 as a work around i am installing an older libxenon from someones git hub i dont remember just looked for a libxenon that was released at the same time as xell just wanted to let you guys know. oh and is there a way to change the text back to green on the matrix theme?

## 2012-07-15 20:40:38, posted by: tuxuser

[code]* *cd xell git checkout tuxuser make clean make [/code] Once the branch "tuxuser" can be considered stable it will be merged into "master" branch.  
   
 For the matrix theme comment out "#define DEFAULT\_THEME" in source/lv2/config.h and re-compile.

## 2012-07-15 21:19:30, posted by: sk1080

Lol, changing "select" to "back" broke every bit of homebrew we have :P

## 2012-07-16 19:02:36, posted by: ravendrow

lol that's ok i build xell testing w/ your libxenon testing sk1080 and it built perfect but doesn't launch elf's :P i swear i have way too much free time

## 2012-07-16 22:14:50, posted by: ravendrow

k so tux tried your fix and it was asking for xb360.h weird cause it is in source/lv2/xb360/ folder so i dunno  
   
 @sk1080 dude worked perfect changed both instances of select to back and compiled just fine if you have push on the git your should fix it when you get a chance you guys are the best!!

## 2012-07-16 22:20:40, posted by: tuxuser

xb360/ and crypt/ was moved from xell to libxenon, you have to use matching repos:  
   
 libxenon - "tuxuser"-branch  
 xell - "tuxuser"-branch

## 2012-07-17 20:20:03, posted by: ravendrow

so that seemed to work but everytime i start xell (with either of the builds i have done) with my plug and play charger connected xell crashes if i unplug it , it loads fine only when ,my charger and controller are plugged in. not sure if it is a bug or am i missing something?

## 2012-07-17 21:52:11, posted by: tuxuser

Got a stackdump?  
 Maybe compare with those: https://github.com/Free60Project/libxenon/issues/7

## 2012-07-19 06:28:39, posted by: ravendrow

k so i cant give you the full stack dump cause i dont have uart and the display is cut off on both of my tv's but here is what i can give you  
   
 STACK DUMP  
   
 0x8000cef0-->0x8000ceec-->0x8000e16c-->0x8000d174-->  
 0x8000ed1c-->0x80002720-->0x80001ef4-->0x80008a4f  
   
 i could get you a full one if you guys could tell me how to modify libxenon to display 480p instead of 720p on the 5 cable composite i know the picture fits perfect...or at least it used to (older builds like the original xell and xellous did show picture on this cable so i can only assume libxenon changed.) maybe a modification to xenos.c?

## 2012-07-25 23:12:24, posted by: ravendrow

here is the full stack dump error i get with plug and play charger connected  
 [code]* *Segmentation fault! pir=0000000000000000 dar=0000000000000002 sr0=000000008000cef0 sr1=1000000002003030 lr=000000008000ceec 00=000000008000cdf0 08=000000008009d6c8 16=0000000000000000 24=000000008070a0ec 01=000000009ddffeb0 09=0000000000000009 17=000000008009d690 25=000000008009d598 02=800000001c00a408 10=0000000000000004 18=000000008006b369 26=000000008009d690 03=000000008009d598 11=000000009ddffed0 19=000000008006b458 27=0000000080710000 04=0000000000000000 12=0000000024000084 20=000000008006b28c 28=000000008009d699 05=0000000000000001 13=0000000002000000 21=000000008000e064 29=0000000000000000 06=0000000000000000 14=0000000000000000 22=000000008006b3a7 30=000000008009d6c8 07=00000000000fb9e8 15=0000000000000000 23=0000000000000012 31=0000000000000000 STACK DUMP: 0x8000cef0 --> 0x8000ceec --> 0x8000e16c --> 0x8000d174 --> 0x8000ed1c --> 0x80002720 --> 0x80001ef4 --> 0x80008af4 [/code]

## 2012-07-26 08:51:00, posted by: tuxuser

[quote="tuxuser"]  
 On your compiled filename.elf (not elf32 !!!) do the following to debug the error:  
 [code]* *xenon-addr2line -e filename.elf 0x0000000 0x00000001 0x00000002 [/code] where 0x0 0x1 0x2 are the numbers of the stackdump (left -> right ,top -> bottom)  
   
 for example for the first stackdump picture:  
 [code]* *xenon-addr2line -e xmplayer.elf 0x80708940 0x80708848 0x8970a660 0x8070af80 0x8001df3c 0x8001e4e4 0x8000c108 0x80001ef4 0x80701bf4 [/code] [/quote]

## 2012-07-27 06:49:24, posted by: ravendrow

ok so i did this  
 [code]* *xenon-addr2line -e stage2.elf 0x8000cef0 0x8000ceec 0x8000e16c 0x8000d174 0x8000ed1c 0x80002720 0x80001ef4 0x80008af4 [/code] and it spit out this [code]* */home/ravendrow/libxenon/libxenon/ports/xenon/../../drivers/usb/usbd.c:170 /home/ravendrow/libxenon/libxenon/ports/xenon/../../drivers/usb/usbd.c:166 /home/ravendrow/libxenon/libxenon/ports/xenon/../../drivers/usb/usbhub.c:508 /home/ravendrow/libxenon/libxenon/ports/xenon/../../drivers/usb/usbd.c:424 /home/ravendrow/libxenon/libxenon/ports/xenon/../../drivers/usb/usbmain.c:125 /home/ravendrow/xell/source/lv2/main.c:124 /home/ravendrow/libxenon/libxenon/ports/xenon/../../startup/xenon/crt1.c:27 argv.c:0 [/code]