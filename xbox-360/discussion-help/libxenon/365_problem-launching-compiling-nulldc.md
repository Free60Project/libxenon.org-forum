# Problem launching/compiling NullDC

## 2012-10-02 11:00:22, posted by: parwathy

Hello everybody,  
   
 First, I want to say thank you to all the folks here helping and working on libxenon.  
   
 So, I finally managed to compile NullDC 360 (thanks Gligli!), but I got a little problem when launching the elf with XeLL. The elf is on my usb flash drive (I get 2 at the end of the process, a .elf and .elf32, both renamed to xenon, both on my flash drive).  
 XeLL finds the elf, try to launch but the screen goes like this :  
   
 ![](http://image.noelshack.com/fichiers/2012/40/1349168446-xellnulldc.jpg)[img]http://image.noelshack.com/fichiers/2012/40/1349168446-xellnulldc.jpg[/img]  
   
 And nothing launches, screen is frozen.  
   
 And here is the log of my terminal : http://pastebin.com/t0UpxSgN  
   
 So, did the compilation process went good? Any tips would be greatly appreciated :)

## 2012-10-04 05:28:15, posted by: OOKAMI

luckyyouare:)  
   
 i am currently have issue to compile it  
 maybe wrong command  
   
 i git the gligli libxenon and compiled it properly  
 everything is fine but the nulldc compiling make me many error and this at the end  
   
 collect2: error 1d returned 1 exit status  
 make(1) *** (/home/ookami/nulldc-360/nulldc-360.elf) error 1  
 make: *** (build) Error 2  
   
 many errors about undefined reference  
   
 what is the step you followed for compiling please ?  
   
 thanks :)

## 2012-10-05 08:31:30, posted by: Ced2911

renomme le elf32 en xenon.elf :)

## 2012-10-05 14:48:37, posted by: OOKAMI

[quote="Ced2911"]  
 renomme le elf32 en xenon.elf :)  
 [/quote]  
   
 mega lol ;D  
 merci :)

## 2012-10-06 11:05:41, posted by: parwathy

Hey, little update, thanks for the replies.  
   
 MagicSeb helped me a few days ago with the folder structure on the flash drive etc so that I can check if my build should work, and it wasn't.  
 Actually, it seems my Ubuntu 12.04 (gnome remix) version of linux wouldn't copy files the proper way on my flash drive. Copying the same files gave me red screen of death on a Slim. Tried it again on my jasper, and this time it did the same red screen error... Tried copying files with Windows XP, and the emu just worked. Weird, huh?  
   
 Ookami, I guess MagicSeb said everything '-' Double check the librairies :)  
   
 Ced, noob question, but what's the difference between the elf and elf32?

## 2012-10-06 22:57:28, posted by: MagicSeb

@paw : sous linux il faut "ejecter" le peripherique usb sinon ca merde ;)

## 2012-10-07 16:02:07, posted by: parwathy

Ah d'acc, merci pour le conseil :)

## 2012-10-08 08:32:53, posted by: Ced2911

the elf is the executable + debug information, xell currently can't load standard .elf but elf32

## 2012-10-09 00:47:41, posted by: OOKAMI

[quote="parwathy"]  
 Hey, little update, thanks for the replies.  
   
 MagicSeb helped me a few days ago with the folder structure on the flash drive etc so that I can check if my build should work, and it wasn't.  
 Actually, it seems my Ubuntu 12.04 (gnome remix) version of linux wouldn't copy files the proper way on my flash drive. Copying the same files gave me red screen of death on a Slim. Tried it again on my jasper, and this time it did the same red screen error... Tried copying files with Windows XP, and the emu just worked. Weird, huh?  
   
 also compiled the last libxenon updated by gligli (some bug fix and gcc 4.1.7)  
   
 Ookami, I guess MagicSeb said everything '-' Double check the librairies :)  
   
 Ced, noob question, but what's the difference between the elf and elf32?  
 [/quote]  
   
   
 yes, and i have the same result as you ;D  
   
 a sad red screen i added in one thread  
   
 http://libxenon.org/index.php?action=dlattach;topic=367.0;attach=304  
   
   
 i had also the same issue for this configuration under virtualbox  
   
 xubuntu 12.04  
   
 and fixed by make new one with disk size more big (the installation with complete libxenon take close 6gb to the vdi)  
   
 i also prefered to create on the file manager folder to avoid folder creation by root instead of machine username and applied the rest by terminal command. compiling is now good for me :)  
   
 again, thanks for the help :)

## 2012-10-09 03:20:17, posted by: OOKAMI

SOLVED ;D  
   
 tested first with HDD with 2 partitions and make the red crash  
   
 now tested with usb key 32gb and now it's running :)  
   
 i perform now new one partition on HDD external in order to see how it work :)