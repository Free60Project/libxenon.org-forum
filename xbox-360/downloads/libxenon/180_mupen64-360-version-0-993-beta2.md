# mupen64-360 version 0.993 beta2

## 2011-09-22 21:07:05, posted by: <Unknown User>

[code] **************************** * Mupen64-360 v0.993 Beta2 * **************************** http://www.libxenon.org/ Description =========== Mupen64-360 is a Nintendo64 emulator for the Xbox 360, it’s powered by libxenon and it’s a port of Wii64 (which itself was a port of Mupen64). Usage ===== Unzip on USB sick, then run from Xell. Many ROM formats are supported, zipped ROMs also work. In the browser, the Back button changes the current drive, A selects, B goes to parent dir. Ingame, Back toggles Framerate limiting, and the Guide button quits to the browser. Other controls are described in the emulator itself. The browser background image is loaded from /mupen64-360/bg.png on the USB stick, other backgrounds are provided. Options ======= – Controls (l->r): Changes the way N64 directional controls are mapped to the 360 gamepad, from left to right. EG: Stick / D-Pad / C-buttons means N64 stick will be mapped on the 360 left stick, N64 D-pad on 360 D-pad, and N64 C-buttons on 360 right D-pad. – Textures: Changes the texture enhancement filter, depending on games, some filters will look better than others. Be aware than the highest settings can slowdown games a lot, or even crash them in some rare cases. – CPU core: Controls the speed/compatibility ratio, from fully featured dynarec to interpreter mode. ‘No linking’ and ‘No VM’ are new dynarec modes that can make some games work, while still running at playable speed. – Framerate limiting: When enabled, games won’t go faster than they would on a real N64. Can be toggled ingame with the Back button. History ======= v0.993 BETA2: – Fixes mount issues with USB devices (which caused nothing to work) My Bad! //Swizzy v0.993 BETA: Recompilation with some ZLX and Libxenon fixes – Supports Corona Video Output – Better USB Drive/HDD Compatibility v0.992 Beta: Almost a complete rewrite, notable changes: – Moved to Mupen64 Plus core. – Moved to Rice video plugin. – Dynarec overhaul. – Faster and way more compatible. – More control over the speed/compatibility ratio (see ‘CPU core’ option) – More texture enhancement filters. – Basic controls remapping. – GUI improvements. – Built with recent libxenon/ZLX (more supported filesystems, less bugs, …) – /! Use the Guide button to quit a game, Back toggles framerate limiting now. v0.96 Beta: First binary release Credits ======= Wii64 / Mupen64 teams (guess why :) GliGli (Xbox 360 port) Ced2911 (GUI library) Razkar (Backgrounds) Everyone that contributed to libxenon…[/code] [youtube]http://www.youtube.com/watch?feature=player\_embedded&v=iuP9MmW9wvY[/youtube]  
   
 Have fun =)  
   
 Edit 11/25/2012: New version: 0.992 beta !  
 Edit 12/24/2014: Version 0.993 Beta2 added!  
   
 Download link (attachment doesn't work for some reason): [url=http://www.homebrew-connection.org/files/xbox/Emulators/libXenon/mupen64-360\_v0.993\_beta2.rar]Click[/url]

## 2011-09-22 22:07:20, posted by: ravendrow

tried to compile the updated source from your git hub and got this error  
   
 /home/travis/Desktop/mupen64-360/source/main/main.cpp:222:14: error: 'loadPNGFromMemory' is not a member of 'ZLX'  
   
 downloaded the newest zlx from google reinstalled it and i am still getting this error....any idea what i am doing wrong?

## 2011-09-22 22:16:03, posted by: boflc

Ced2911 just committed a few changes from GliGli into ZLX: make sure you really -did- get the latest ZLX from svn and that you -did- correctly compile & install it.  
   
 as in, i -just- did this and compiled mupen successfully.

## 2011-09-22 22:23:49, posted by: ravendrow

yeah that was it he must have been updating as i got it first time it said 8 revisions now it says 9 all good

## 2011-09-22 22:57:04, posted by: peet8989

thanks for including the binaries :)  
   
   
 multiplayer!! how nice!

## 2011-09-23 20:43:52, posted by: Sonic-NKT

Great to see a first public release :)  
   
 sure the controller emulation needs work and there are a few glitches ( ;) ) in several games but for a first release its awesome an show that 360 homebrew is still alive.   
   
 I just have one problem... is HDMI audio working?  
 Im using latest Xell 1. Stage with xelllaunch and i dont hear anything :)

## 2011-09-24 00:25:50, posted by: MagicSeb

HDMI sound is working on my Xell Reloaded September 11

## 2011-09-25 19:52:25, posted by: Sonic-NKT

Can you give me a link to the exact version?

## 2011-09-30 20:10:27, posted by: kyl3

Just played mortal kombat 4 and it was like it was in HD. You sir have blown my mind to the fullest...... and then some.

## 2011-10-01 12:53:28, posted by: MagicSeb

[quote="Sonic-NKT"]  
 Can you give me a link to the exact version?  
 [/quote]  
   
 http://www.logic-sunrise.com/telechargement-355846-xell-reloaded-23-09-2011.html  
   
 This one working too. flashed via NXE, using xellupdater by tuxuser.

## 2011-11-24 18:55:47, posted by: EdsonDario

Is there a problem running it from the dvd drive?

## 2011-12-16 07:59:51, posted by: GhaleonX

Awesome work, gligli! I'm thrilled with the performance already! I have compiled your latest build and have noticed that on my usb hdd, if I've been playing a while, upon exit I get a seg fault error (red screen of death :P) - I'm thinking that this may be an issue with some usb hdds having issues resuming from idle (hddalive.xex addressed this for FSD in the past).  
   
 Also, I'm curious - do you plan to add support for texture packs?

## 2012-05-06 03:26:20, posted by: naxil

WOW.. majora's mask on my xbox360!!! and in hiress!!! where i can found the source? for follow news?

## 2012-05-06 03:35:02, posted by: naxil

i have a question.. native n64 save is supported?

## 2012-07-03 14:01:50, posted by: skaT777

give it in the next time a update :D i want play Donkey Kong XD

## 2012-07-13 04:53:03, posted by: gangrel_1313

In the next version, it would be nice to edit the controller, I find my layout is way better than the one provided.  
   
 (for anyone interested)  
 Left Analog for N64 Analog  
 D-Pad for N64 D-Pad  
 Right Analog for C-Buttons  
 Start for N64 Start  
 Left Bumper for N64 L  
 Right Bumper for N64 R  
 Left Trigger for N64 Z  
   
 Worked great on N64 emulators on PC with my 360 controller and would be good on Mupen64-360. I don't know if having custom buttons for each rom would possible, some button combinations work better on some roms than others, it would be nice to have combinations set so you dont have to keep editing the control scheme.  
   
 Also how do you save on Mupen64-360, I cant find information anywhere

## 2012-10-28 02:29:58, posted by: MastaG

The latest mupen64 git seems to be broken.  
 I've compiled GliGli's tree of libxenon: ./build-xenon-toolchain toolchain and ./build-xenon-toolchain libs.  
 The same for libxemit and the ZLX git.  
 Mupen64-360 compiled with no errors.  
 Trasfered the mupen64-360.elf32 to the root of my fat32 formatted usb drive as xenon.elf.  
 Also places the "files" folder in the root.  
 Upon launching I'm getting a Segmentation Fault.

## 2012-10-29 00:00:17, posted by: Pa0l0ne

[quote="MastaG"]  
 The latest mupen64 git seems to be broken.  
 I've compiled GliGli's tree of libxenon: ./build-xenon-toolchain toolchain and ./build-xenon-toolchain libs.  
 The same for libxemit and the ZLX git.  
 Mupen64-360 compiled with no errors.  
 Trasfered the mupen64-360.elf32 to the root of my fat32 formatted usb drive as xenon.elf.  
 Also places the "files" folder in the root.  
 Upon launching I'm getting a Segmentation Fault.  
 [/quote]  
   
 Wich kind of speculation leads you to think that?  
 You probably have an incompatible usb drive just like happen with XMplayer. Most people have resolved this issue reformatting the drive with Gui Format 32 or trying to use the xbox internal harddrive. Eventually changing model of external usb drive.  
   
 ...oh, and last but not least, my selfcompiled Mupen work like a charm! (Thanks GliGli!)

## 2012-10-29 07:39:18, posted by: diexsodia

[quote="MastaG"]  
 The latest mupen64 git seems to be broken.  
 I've compiled GliGli's tree of libxenon: ./build-xenon-toolchain toolchain and ./build-xenon-toolchain libs.  
 The same for libxemit and the ZLX git.  
 Mupen64-360 compiled with no errors.  
 Trasfered the mupen64-360.elf32 to the root of my fat32 formatted usb drive as xenon.elf.  
 Also places the "files" folder in the root.  
 Upon launching I'm getting a Segmentation Fault.  
 [/quote]  
   
   
 you have the 0.99 version? can you send me the emulator MP.... i don have linux for copile that..

## 2012-10-29 11:17:53, posted by: Pa0l0ne

[quote="diexsodia"]  
 [quote="MastaG"]  
 The latest mupen64 git seems to be broken.  
 I've compiled GliGli's tree of libxenon: ./build-xenon-toolchain toolchain and ./build-xenon-toolchain libs.  
 The same for libxemit and the ZLX git.  
 Mupen64-360 compiled with no errors.  
 Trasfered the mupen64-360.elf32 to the root of my fat32 formatted usb drive as xenon.elf.  
 Also places the "files" folder in the root.  
 Upon launching I'm getting a Segmentation Fault.  
 [/quote]  
   
   
 you have the 0.99 version? can you send me the emulator MP.... i don have linux for copile that..  
 [/quote]  
 Yep, all of us are here for this kind of request.  
 And maybe i'm the Queen of England.

## 2012-10-29 17:02:47, posted by: MagicSeb

The contract is clear : You can build your own version. And don't distribute it.

## 2012-10-31 07:08:42, posted by: diexsodia

[quote="MagicSeb"]  
 The contract is clear : You can build your own version. And don't distribute it.  
 [/quote]  
   
 ok.. can you give me a page of how copile?...

## 2012-10-31 13:22:45, posted by: MagicSeb

http://libxenon.org/http://libxenon.org//viewtopic.php?t=2  
   
 Follow this tutorial. You can compile under VMWARE or VBOX virtual machine.  
   
 Install linux  
 Install depedencies to build libxenon  
 Build libxenon, build libs zlib, freetype etc...  
 git clone ZLX Library, compile lib install lib  
   
 Git clone mupen64, compile it and copy it on a fresh formatted USB, renames mupen64...elf32 in xenon.elf  
 Copy necessary files from the old 0.96 version (available elsewhere...like Logic Sun....)

## 2012-11-06 01:52:04, posted by: diexsodia

[quote="MagicSeb"]  
 http://libxenon.org/http://libxenon.org//viewtopic.php?t=2  
   
 Follow this tutorial. You can compile under VMWARE or VBOX virtual machine.  
   
 Install linux  
 Install depedencies to build libxenon  
 Build libxenon, build libs zlib, freetype etc...  
 git clone ZLX Library, compile lib install lib  
   
 Git clone mupen64, compile it and copy it on a fresh formatted USB, renames mupen64...elf32 in xenon.elf  
 Copy necessary files from the old 0.96 version (available elsewhere...like Logic Sun....)  
 [/quote]  
   
   
 i am going to try it.. i am from mexico.. my english is bad.. and i dont know some thing about linux... but i am going to try....  
   
 tanks

## 2012-11-17 05:03:03, posted by: mark291422

Hi looks like I'm running into the same seg-fault as the other user  
   
 This is what I'm getting right now (http://imgur.com/uQY1P). I'm using the same USB key that works for v0.96. I used my mupen64-360.elf32 (3,599KB) and simply renamed it to replace my existing xenon.elf.  
   
 To compile Mupen64-360 I ran make CROSS\_COMPILE=-xenon- and got no errors.  
   
 I've tried formarting the usbkey with gui format and re-applying the .elf and it still fails.  
   
 Does anyone have anything else that comes to mind to solve this? Thanks in advance.

## 2012-11-25 22:02:42, posted by: GliGli

New version: 0.992 beta !

## 2012-11-25 23:51:15, posted by: skaT777

sry master gligli but the emulator had bugs  
 at first   
 it dont save :x (i have test it whit Donkey kong)  
 then in the video that you show had donkey kong no grafik bugs  
 but i have many the camera is ever jump back

## 2012-11-26 03:29:40, posted by: chunkz

I am having issues for some reason i cant get into the emu. it loads xenon.elf file then before loading the emu i get the seg. fault screen. I have tried this with many usb flash drives as i have a lot lol but no luck. Any advice? or is this just an all around issue?  
   
 EDIT: i got it to boot on my external 2tb hdd. out of the 7 flash sticks i have the 2tb is the only one that worked for me. only difference i can see is my 2tb is usb 3.0 and my usb flah sticks are regular usb 2.0.

## 2012-11-26 05:07:11, posted by: bigdave629

thank you gligli for releasing this emu everything works great. I wanted ask if it is possible to remap the c buttons to actual 360 buttons for the use with fighting games?

## 2012-12-03 02:37:27, posted by: iSynic

Both with the prior and latest version I get no video. The elf seems to load but I get a black screen and the TV says no input. Any clues? I'm outputting via HDMI, corona board.

## 2012-12-03 19:35:44, posted by: skaT777

Donkey Kong didnt save  
 and Zelda Majoras Mask dont work  
 please fix this

## 2012-12-04 15:50:01, posted by: dreamboy

goemon adventures works great hehe :) is there a way to enable expansion pack memory without having to recompile the source code?

## 2012-12-28 21:00:38, posted by: isaacgar12345

Just to let you guys know, the older versions of this program work for me, but this one doesn't. It could be because the flash drive I'm using sucks.

## 2013-01-11 18:25:54, posted by: chunkz

hey bud i had some issues too try this. Put the xenon.elf file on root of internal hd(hd inside xbox) Now put the mupen folder onto a fresh formated usb (use guiformat google it) make sure you make a roms folder and put what roms you want in the folder this folder must also be on root of flash drive. Now you should have the .elf file on the root of internal hd and mupen64 folder and roms folder on root of usb drive just plug usb in to xbox and start normaly. Once your dash is loaded go to your dashlaunch and run it. find the launch button and launch the elf file from internal drive. xell will load automaticly and fast Mupen should now work select rom and enjoy. this is how i get all elf files to run gives you a lot less hassle trying to get them to work hope it works for you or anyone else having issues.

## 2013-01-14 23:41:47, posted by: cieniu71

Great Stuff ! :D

## 2013-08-04 03:06:41, posted by: ploggy

Hi, has there been a fix for the saving issue?  
   
 thanks.

## 2013-09-02 12:42:33, posted by: mouarf

It seems Mupen64 needs to be recompiled with new toolchain to provide corona compatibility.  
   
 Has someone planned to provide such compiled version ?  
   
 I would be very grateful.  
   
 EDIT: It has been relseased somewhere. Thanks to everyone involved !

## 2013-09-05 21:53:44, posted by: Swizzy

[quote="mouarf"]  
 EDIT: It has been relseased somewhere. Thanks to everyone involved !  
 [/quote]  
   
 Np, it's still got a few bugs that needs to be fixed tho xD

## 2013-09-09 19:54:36, posted by: Stakhanov

Thanks for the release GliGli.  
   
 For people using corona here's the buid you're talking about :  
   
 http://www.homebrew-connection.org/files/xbox/Emulators/libXenon/dl\_mupen64-360\_v0.993\_beta2.rar  
   
 With the first build I couldn't look into my usb device to launch my roms, but with this one I can, though as you said it seems that it doesn't save.  
   
   
   
 I've tested a few games using VGA, so here's my list of working one and issues I've met :  
   
 - GoldenEye : Working on solo, splitscreen works but shows texture artifacts on the down side screens  
 - Mario Kart 64: Working fullspeed  
 - Super Mario 64 : Working very fast and so is unplayable  
 - Lego Racers : Working near fullspeed but many artifacts are shown, some cars disappears and the game says it can't save ending up in using a temporary profile  
 - Star Wars Episode I Racer : Working fullspeed but a few shadow artifacts are present  
 - Star Wars Shadow of the Empire : Working fullspeed and properly ingame but has a glitchy and blinking menu that can only be used by blindly pressing buttons.  
 - Re-Volt: Not launching  
 - Star Wars Rogue Squadron : Not launching  
 - Star Wars Battle for Naboo : Not launching  
 - Super Smash Bros : Working, but crashes a few minutes after launch with hi-res textures

## 2013-09-10 07:09:04, posted by: Swizzy

The issue with the game running at to high speed can be manually corrected by changing the limiting with the speed... try pressing the back button :)  
   
 The not launching issue might be a problem with the game save type, if you could install a UART cable to your console it'd be awesome as it'd help me find the reason for the error :)

## 2013-09-15 08:15:13, posted by: bigdave629

Did gligli update this or is this update just for corona users?

## 2013-09-15 19:41:01, posted by: Swizzy

[quote="bigdave629"]  
 Did gligli update this or is this update just for corona users?  
 [/quote]  
   
 I Updated it fixing a few issues with some USB Drives and added corona support...

## 2013-09-16 02:38:45, posted by: bigdave629

Oh okay thanks for the response, so if I have .992 running fine on my JTAG their is no reason to update are do more games work?

## 2013-09-16 07:07:11, posted by: Swizzy

[quote="bigdave629"]  
 Oh okay thanks for the response, so if I have .992 running fine on my JTAG their is no reason to update are do more games work?  
 [/quote]  
   
 Yeah, if it works fine with the games you play now, no need to update...

## 2013-09-18 11:31:57, posted by: Stakhanov

[quote="Swizzy"]  
 The issue with the game running at to high speed can be manually corrected by changing the limiting with the speed... try pressing the back button :)  
   
 The not launching issue might be a problem with the game save type, if you could install a UART cable to your console it'd be awesome as it'd help me find the reason for the error :)  
 [/quote]  
   
 Saddly I don't have anything as an UART cable but if I can help the devellopment by using one I'll try to get one.  
   
 By not launching I meant that it displays a black screen when I launch the rom.

## 2013-09-18 11:39:41, posted by: Stakhanov

[quote="Swizzy"]  
 The issue with the game running at to high speed can be manually corrected by changing the limiting with the speed... try pressing the back button :)  
   
 The not launching issue might be a problem with the game save type, if you could install a UART cable to your console it'd be awesome as it'd help me find the reason for the error :)  
 [/quote]  
   
 Saddly I don't have anything as an UART cable but if I can help the devellopment by using one I'll try to get one...  
   
 By not launching I meant that it displays a black screen when I press A with the game selected...  
   
   
 Hmm PC crashed while posting and it seems to have caused a double post, I don't seem to have a delete post option can anyone telle me how to delete it or if I can't any admin could take care of it ?

## 2014-03-09 20:17:57, posted by: goodygumdrops

okay so i am a bit of a noob but the problem im having is that when i select a rom it restarts xell and loads up mupen64 again this happens with the zip files and the z64 file please help :(

## 2015-04-08 14:14:51, posted by: <Unknown User>

I have an XBOX 360 with Corona and I can't make the emulator work on my external USB (FAT32) HD. I've tried to play from the pendrive and It loads the game OK, but when I try to play from my external HD it gives me a black screen upon loading the game. PLZ help me.