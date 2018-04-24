# libSDLXenon / SDLQuake-libXenon

## 2011-10-20 20:45:37, posted by: lantus360

I've been working on a full fledged port of SDL for LibXenon and its at a stage where its good enough be released.  
   
 the repository is located at  
   
 https://github.com/lantus/libSDLXenon  
   
 Currently the following features are implemented in SDL  
   
 - Graphics  
 - Audio (some audio formats are probably still buggy)  
 - Joysticks (all 4 are supported)  
 - Threads (hasn't really been tested)  
   
 To compile up grab the latest source from the repository and use:  
   
 'make -f Makefile.xenon install' to build/install SDL in your environment  
   
 As a testbed, ive ported SDLQuake in parallel with libSDLXenon  
   
 SDLQuake libXenon repository is located at  
   
 https://github.com/lantus/sdlquake-libxenon  
   
 Download the source and use 'make' to build SDLQuake.  
   
 I've attached a binary with shareware quake as well.  
   
 Enjoy :)  
   
   
 SDLQuake-libXenon: [url=http://libxenon.org/http://libxenon.org//viewtopic.php?t=9]Download[/url]

## 2011-10-20 21:59:20, posted by: Juvenal

Very cool, ill package this up later today and add the binary SDL deb to my repo :)

## 2011-10-20 23:53:08, posted by: warfaren

Nice, it compiled great and runs just fine :)  
 Although, my settings don't get saved when running from USB-drive after restarting the game (I guess it can't write to FAT32?).  
   
 Also, it would be nice with networking support. Right now it just says No network interface available or something like that when I go to the multiplayer menu.

## 2011-10-21 00:04:10, posted by: Razkar

[quote="warfaren"]  
 Nice, it compiled great and runs just fine :)  
 Although, my settings don't get saved when running from USB-drive after restarting the game (I guess it can't write to FAT32?).  
   
 Also, it would be nice with networking support. Right now it just says No network interface available or something like that when I go to the multiplayer menu.  
 [/quote]  
 Save works fine for me via USB fat32 (4go usb key)

## 2011-10-21 01:01:34, posted by: warfaren

[quote="Razkar"]  
 [quote="warfaren"]  
 Nice, it compiled great and runs just fine :)  
 Although, my settings don't get saved when running from USB-drive after restarting the game (I guess it can't write to FAT32?).  
   
 Also, it would be nice with networking support. Right now it just says No network interface available or something like that when I go to the multiplayer menu.  
 [/quote]  
 Save works fine for me via USB fat32 (4go usb key)  
 [/quote]  
   
 Do you mean savegames? Because I was talking about settings: key config etc.  
   
 Btw, it doesn't seem to recognize LB/RB and clicking the thumbsticks as buttons :(

## 2011-10-21 01:25:38, posted by: lantus360

[quote="warfaren"]  
 Nice, it compiled great and runs just fine :)  
 Although, my settings don't get saved when running from USB-drive after restarting the game (I guess it can't write to FAT32?).  
   
 Also, it would be nice with networking support. Right now it just says No network interface available or something like that when I go to the multiplayer menu.  
 [/quote]  
   
 didnt you read the README where i said that networking is disabled? :p

## 2011-10-21 01:26:25, posted by: lantus360

[quote="warfaren"]  
 [quote="Razkar"]  
 [quote="warfaren"]  
 Nice, it compiled great and runs just fine :)  
 Although, my settings don't get saved when running from USB-drive after restarting the game (I guess it can't write to FAT32?).  
   
 Also, it would be nice with networking support. Right now it just says No network interface available or something like that when I go to the multiplayer menu.  
 [/quote]  
 Save works fine for me via USB fat32 (4go usb key)  
 [/quote]  
   
 Do you mean savegames? Because I was talking about settings: key config etc.  
   
 Btw, it doesn't seem to recognize LB/RB and clicking the thumbsticks as buttons :(  
 [/quote]  
   
 you have to quit Quake for your config to be stored

## 2011-10-21 01:53:49, posted by: warfaren

Alright. No I didn't notice any readme, since I just followed the instructions in this thread.  
   
 Thanks for answering though :)

## 2011-10-21 17:33:48, posted by: Doerek

Razkar uploaded some Videofootage...  
 [url=http://youtu.be/6XYvFCa8LMk]http://youtu.be/6XYvFCa8LMk[/url]

## 2011-10-21 18:45:03, posted by: lantus360

yes, sound is working in SDL under libxenon :)

## 2011-10-22 00:00:54, posted by: Pa0l0ne

I'm trying to compile but i receive this error: http://pastebin.com/fx4uQdwa  
   
 Any idea how to solve?

## 2011-10-22 03:44:44, posted by: lantus360

use gliglis updated libxenon git which will resolve this issue  
   
 https://github.com/gligli/libxenon

## 2011-10-22 19:08:08, posted by: lantus360

[quote="warfaren"]  
 [quote="Razkar"]  
 [quote="warfaren"]  
 Nice, it compiled great and runs just fine :)  
 Although, my settings don't get saved when running from USB-drive after restarting the game (I guess it can't write to FAT32?).  
   
 Also, it would be nice with networking support. Right now it just says No network interface available or something like that when I go to the multiplayer menu.  
 [/quote]  
 Save works fine for me via USB fat32 (4go usb key)  
 [/quote]  
   
 Do you mean savegames? Because I was talking about settings: key config etc.  
   
 Btw, it doesn't seem to recognize LB/RB and clicking the thumbsticks as buttons :(  
 [/quote]  
   
 shoulder and thumb buttons are now supported in the last commit i made  
   
 thanks

## 2011-10-23 15:21:45, posted by: warfaren

[quote="lantus360"]  
 [quote="warfaren"]  
 [quote="Razkar"]  
 [quote="warfaren"]  
 Nice, it compiled great and runs just fine :)  
 Although, my settings don't get saved when running from USB-drive after restarting the game (I guess it can't write to FAT32?).  
   
 Also, it would be nice with networking support. Right now it just says No network interface available or something like that when I go to the multiplayer menu.  
 [/quote]  
 Save works fine for me via USB fat32 (4go usb key)  
 [/quote]  
   
 Do you mean savegames? Because I was talking about settings: key config etc.  
   
 Btw, it doesn't seem to recognize LB/RB and clicking the thumbsticks as buttons :(  
 [/quote]  
   
 shoulder and thumb buttons are now supported in the last commit i made  
   
 thanks  
 [/quote]awesome, thank you!

## 2011-10-23 19:33:11, posted by: warfaren

I found a new bug, I believe.  
 Stereo audio seem to be inverted. It's pretty obvious when you're firing a grenade, and looking to the left and (so the grenade would explode to the right of you) and yet the explosion comes in the left speaker.  
   
 I don't know if this bug is exclusive to this game or if it exists in all of Libxenon / SDL or whatever.  
   
 So unless my cable (M$ Original Component) is messed up, we have a bug.  
 edit: Ok, so I double-checked my cable and ran Mirror's Edge just to make sure. Nothing wrong with my cable.

## 2011-10-24 15:27:12, posted by: lantus360

thanks for the heads up. im not sure where the issue lies but ill check into it

## 2012-02-22 16:44:11, posted by: kryso

where compiling the code,   
   
 [SDL\_thread.c]  
 In file included from ./include/SDL\_mutex.h:32:0,  
 from src/thread/SDL\_thread.c:26:  
 ./include/SDL\_stdinc.h:63:22: fatal error: strings.h: No such file or directory  
 compilation terminated.  
 make: *** [src/thread/SDL\_thread.o]   
   
 please help

## 2012-02-23 00:05:25, posted by: tuxuser

Probably you have to look for upper/lowercase errors