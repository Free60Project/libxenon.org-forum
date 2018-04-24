# libfat

## 2012-10-21 05:56:51, posted by: ch.kenned

Can someone help with a libfat problem? I've tried, but I keep getting this error. The compilation error is:  
   
 /usr/local/xenon/usr/lib/libfat.a(disc.o): In function `get\_io\_ata':  
 /home/chkenned/free60/fat-xenon/libxenon/../source/disc.c:47: undefined reference to `xenon\_ata\_ops'  
 /home/chkenned/free60/fat-xenon/libxenon/../source/disc.c:47: undefined reference to `xenon\_ata\_ops'  
 collect2: ld returned 1 exit status  
 make[1]: *** [/home/chkenned/homebrew/sdlbmp/sdlbmp.elf] Error 1  
 make: *** [build] Error 2  
   
 I've looked at disc.c and the code in question is:  
   
 #if defined (LIBXENON)  
 extern DISC\_INTERFACE xenon\_ata\_ops;  
 extern DISC\_INTERFACE usb2mass\_ops;  
   
 static const DISC\_INTERFACE* get\_io\_ata(void) {  
 return &xenon\_ata\_ops;  
 }  
 static const DISC\_INTERFACE* get\_io\_usbstorage(void) {  
 return &usb2mass\_ops;  
 }  
   
 const INTERFACE\_ID \_FAT\_disc\_interfaces[] = {  
 {"uda", &get\_io\_usbstorage},  
 {"sda", &get\_io\_ata},  
 {NULL, NULL}  
 };   
   
 Can someone PLEASE help me out?! I'm getting that feeling of desperation that arises from not being able to access files in code! :) From what I can glean, the xenon\_ata\_ops structure is not defined. I found the definition in ata.c.

## 2012-10-21 18:06:43, posted by: ch.kenned

Nevermind, after moving some files around, I finally got everything up and running. Thank you Cancerous for your help....I can load bitmaps using sdl, finally! :) woot