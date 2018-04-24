# NullDC-360 (Dreamcast Emulator) for LibXenon by GliGli

## 2011-10-11 00:11:32, posted by: tuxuser

He never stops working :)  
   
 After Mupen64-360 and the Reset Glitch Hack, Gligli started a new project.  
 **[b]  
 NullDC-360[/b]**  
   
 [youtube]http://www.youtube.com/watch?v=-oh1sR1DCDI[/youtube]  
   
 This is a Dreamcast Emulator, based on NullDC, for LibXenon. Work started approximately a week ago and it's already showing nice progress.  
 Here you go with some screenshots:  
   
   
 [attach=1][attach=2][attach=3][attach=4][attach=5][attach=6][attach=7][attach=8][attach=9][attach=10][attach=11][attach=12][attach=13][attach=14][attach=15]  
   
   
 Thx GliGli for your hard work you put into all this :)  
   
 **[b]Udpate 27/11/11[/b]**  
   
 After a long dev period here's a little update about GliGli's nulldc port, on the last update, the emu was running on interpreter, and GliGli faced a big problem, there is no dynarec for the xbox 360 architecture (PowerPC), so he had to code his own :D   
   
 Currently the port runs at 168mhz ingame for Soul Calibur (DC Cpu speed is 200mhz). The speed is not constant during games, for example you can see on the video that Soul Calibur stage 1 isn't at that emulation speed, but the other stages are.  
   
 To Do : [quote]- Reach full speed  
 - Sound Emulation  
 - Add Save   
 - Add Menu[/quote] [youtube]http://www.youtube.com/watch?v=h6D27ijUu58&feature=player\_embedded[/youtube]

### Attachments

[P1030390.JPG](P1030390.JPG)[P1030392.JPG](P1030392.JPG)[P1030394.JPG](P1030394.JPG)[P1030396.JPG](P1030396.JPG)[P1030398.JPG](P1030398.JPG)[P1030400.JPG](P1030400.JPG)[sshot_1a8b7f78.jpg](sshot_1a8b7f78.jpg)[sshot_2b894868.jpg](sshot_2b894868.jpg)[sshot_4bb5f646.jpg](sshot_4bb5f646.jpg)[sshot_20fd5db4.jpg](sshot_20fd5db4.jpg)[sshot_40b18ccf.jpg](sshot_40b18ccf.jpg)[sshot_5851f42d.jpg](sshot_5851f42d.jpg)[sshot_30705b04.jpg](sshot_30705b04.jpg)[sshot_502959d8.jpg](sshot_502959d8.jpg)[sshot_47033129.jpg](sshot_47033129.jpg)

## 2011-10-11 00:15:54, posted by: Ced2911

<3 love it :)

## 2011-10-11 00:18:24, posted by: tuxuser

Ced, everybody loves GliGli! You should know that by now :P

## 2011-10-11 00:28:37, posted by: Cancerous1

:o amazing work! thanks for sharing

## 2011-10-11 02:41:33, posted by: MagicSeb

Wahooooo ;D  
   
 I hope we could boot NAOMI games with this one :)  
   
 @Cancerous1 : Did you made any progress on porting ScummVM ?

## 2011-10-11 10:25:58, posted by: avomax

great, thank you.

## 2011-10-11 11:48:34, posted by: DARKFiB3R

Awesome stuff, GliGli, and everybody else involved.  
   
 Thank you so much for all the hard work, and reviving this scene :)

## 2011-10-11 16:25:57, posted by: Gromber

THANK YOU GLIGLI!!! :)   
 I always wanted a Dreamcast emulator.  
   
 In a future it is possible to include rumble support like pc versión using libxenon?

## 2011-10-12 19:05:29, posted by: jayboy86

OMFG this is so sweet, cant wait for a release. keep up the amazing work GliGli

## 2011-10-13 00:28:46, posted by: spandaman

Yet again showing the scene lives on!!!   
   
 Great work guys:)  
   
   
 Sent from my iPhone using Tapatalk

## 2011-10-13 05:23:20, posted by: turnerl

OMG GliGli i will kiss your feet ! this is what dreams are made of !!!

## 2011-10-17 13:32:33, posted by: Lib-Jambo

Any help on beta testing for this..I'll be glad to help :).Im just a little puzzled on complining it..If any of you guys or "gligli" need a beta tester for most things im here to help :)

## 2011-10-18 19:58:22, posted by: jayboy86

lol youll have to learn how to compile as you wont be able to get this until its officially released. but check the libxenon forums i learnt how to do it and its really not that hard when you read and learn it. ill give this a go now i think. again fantastic work gligli, where would the legal homebrew scene be without you guys

## 2011-10-21 02:40:38, posted by: mjstriker5

Anyone try compiling this? Is it even to the point where it can actually be compiled? I tried and am getting an error with "xenosRend.o". I assume it has something to do with the xenosRend.cpp file but my Linux/compiling skills are pretty weak. Just learned how to do this stuff with the amazing N64 emu GliGLi put together.

## 2011-10-21 10:14:39, posted by: warfaren

[quote="mjstriker5"]  
 Anyone try compiling this? Is it even to the point where it can actually be compiled? I tried and am getting an error with "xenosRend.o". I assume it has something to do with the xenosRend.cpp file but my Linux/compiling skills are pretty weak. Just learned how to do this stuff with the amazing N64 emu GliGLi put together.  
 [/quote]  
   
 Yeah, I've compiled it on Linux. Had to fix quite a few case-sensitivity related errors in the source and changing a few backslashes to slashes. I've also given the updated source to GliGli, which he merged, so next time he commits I'm sure you'll have a source that compiles just fine.  
   
 If you can't wait, at least I've given you a hint on what to do to make the current source compile :)

## 2011-10-22 15:01:48, posted by: Pa0l0ne

[quote="mjstriker5"]  
 Anyone try compiling this? Is it even to the point where it can actually be compiled? I tried and am getting an error with "xenosRend.o". I assume it has something to do with the xenosRend.cpp file but my Linux/compiling skills are pretty weak. Just learned how to do this stuff with the amazing N64 emu GliGLi put together.  
 [/quote]  
   
 I have this Error too. More specific here it is the Error:  
 [code]/home/pa0l0ne/nulldc-360/plugins/drkPvr/xenosRend.cpp:1220:31: error: 'Xe\_SetClipPlaneEnables' was not declared in this scope /home/pa0l0ne/nulldc-360/plugins/drkPvr/xenosRend.cpp:1228:33: error: 'Xe\_SetClipPlaneEnables' was not declared in this scope /home/pa0l0ne/nulldc-360/plugins/drkPvr/xenosRend.cpp:1257:26: error: 'Xe\_SetClipPlane' was not declared in this scope[/code] Fixing typo as warfaren said (Thank you dude!), and rebuilding your libxenon dev with gligli fixed libxenon git, solve the problem! ([url=https://github.com/gligli/libxenon]https://github.com/gligli/libxenon[/url])  
   
 Good Luck!

## 2011-10-22 18:28:26, posted by: mjstriker5

Thanks for the hints. To be honest I have no coding ability just really good at following instructions :P . I have no idea how to tell what is a typo and what is not. I have downloaded the update libxenon and from what I know I think it is installing the updated version. Just did the same process I did for initially installing the toolchains.   
   
 Any suggestions on what I could read to learn how to compile and understand code? Seems like there are soo many sources I even know where to start. Thanks

## 2011-10-23 15:27:36, posted by: warfaren

i dont really know how to code either. So what you need to do is fix upper/lower case errors in the code. You gotta attempt to compile, when you hit an error it will say in which source file the error is located, and *filename* file not found. Go look for that file and check how upper/lowercase really is on that filename and edit in the source.also like i said before there are some backslashes that needs to be changed to regular slashes.

## 2011-10-26 21:03:39, posted by: p4r0l3

Thanks for the tip on using GliGli's updated libxenon repo, Pa0l0ne. I was able to get the current revision (with minor edits) to compile after installing zlib, libpng and after updating the libxenon toolchain. Haven't tested the elf file that was produced yet though.

## 2011-10-26 23:00:14, posted by: Pa0l0ne

[quote="p4r0l3"]  
 Thanks for the tip on using GliGli's updated libxenon repo, Pa0l0ne. I was able to get the current revision (with minor edits) to compile after installing zlib, libpng and after updating the libxenon toolchain. Haven't tested the elf file that was produced yet though.  
 [/quote]  
   
 Good Job p4r0l3! I have tested the elf, and bios load correctly, but i have to compile this source:  
 [url=https://github.com/gligli/nulldc-360/zipball/master]https://github.com/gligli/nulldc-360/zipball/master[/url] instead of the source you can download with the command "git clone https://github.com/gligli/nulldc-360"  
   
 You have to manually add some files from PC versione like this:  
   
 [color=red]ROOT DIRECTORY:[/color]  
 ![](http://img89.imageshack.us/img89/912/rootw.jpg)[img]http://img89.imageshack.us/img89/912/rootw.jpg[/img]  
   
 [color=red]NULLDC-360 DIRECTORY:[/color]  
 ![](http://img248.imageshack.us/img248/8159/nulldc360.jpg)[img]http://img248.imageshack.us/img248/8159/nulldc360.jpg[/img]  
   
 [color=red]DATA DIRECTORY:[/color]  
 ![](http://img507.imageshack.us/img507/6599/datat.jpg)[img]http://img507.imageshack.us/img507/6599/datat.jpg[/img]  
   
 [color=red]PLUGINS DIRECTORY:[/color]  
 ![](http://img18.imageshack.us/img18/5411/pluginso.jpg)[img]http://img18.imageshack.us/img18/5411/pluginso.jpg[/img]  
   
 [color=red]THE nullDC.cfg file:[/color] [code];; nullDC config file;; [nullDC] Dynarec.Enabled=0 Dynarec.DoConstantPropagation=1 Dynarec.UnderclockFpu=0 Dreamcast.Cable=3 Dreamcast.RTC=1543276800 Dreamcast.Region=1 Dreamcast.Broadcast=0 Emulator.AutoStart=1 Emulator.NoConsole=0 Dynarec.SafeMode=1 [nullDC\_plugins] GUI=nullDC\_GUI\_Win32.dll Current\_PVR=drkPvr\_Win32.dll Current\_GDR=ImgReader\_Win32.dll Current\_AICA=nullAica\_Win32.dll Current\_ARM=vbaARM\_Win32.dll Current\_ExtDevice=nullExtDev\_Win32.dll Current\_maple0\_5=drkMapleDevices\_Win32.dll:0 Current\_maple0\_0=NUL Current\_maple0\_1=NUL Current\_maple1\_5=NUL Current\_maple2\_5=NUL Current\_maple3\_5=NUL [nullExtDev] mode=0 adapter=0 [Xmaple] Controller.DeadZone=25 PuruPuru.UseRealFrequency=1 PuruPuru.Length=175 PuruPuru.Intensity=100 [drkpvr] Emulation.AlphaSortMode=2 Emulation.PaletteMode=1 Emulation.ModVolMode=2 Emulation.ZBufferMode=2 Emulation.TexCacheMode=0 OSD.ShowFPS=0 OSD.ShowStats=0 Video.ResolutionMode=0 Video.VSync=0 Enhancements.MultiSampleCount=0 Enhancements.MultiSampleQuality=0 Enhancements.AspectRatioMode=0 [ImageReader] PatchRegion=0 LoadDefaultImage=0 DefaultImage=defualt.gdi LastImage=c:\game.gdi [/code]   
   
 IF YOU WANT TO TEST SOULCALIBUR GAME YOU HAVE TO PLAY WITH THE FILE [color=red]"ImgReader.cpp"[/color] located on plugins/ImgReader and edit the line 52 and 54  
   
 Line 52 seems to autoload the game if set to "true" [code]irsettings.LoadDefaultImage=true;[/code] Line 54 seems to set the path of your iso game (soulcalibur) [code]strcpy(irsettings.DefaultImage,"sda:/dcisos/soulcalibur/Soul Calibur v1.000 (1999)(Namco)(NTSC)(US)[!][4S T-1401N].gdi");[/code] Remember that "SDA" unit is the internal HD, and "UDA" unit is the external USB PENDRIVE OR USB HARDDISK  
   
 ...but on my tests the iso won't load....  
   
 GliGli Work is very promising but probably the actual committed source is still immature (The Dynamic recompilation (Dynarec) won't work so the emulation is still slow)  
   
 Anyway, can you test if the .gdi image work on your compiled source?

## 2011-11-06 08:03:41, posted by: silva

Hi Everyone,  
   
 Have the same issue here of can not get images to load. Emulator does run OK to DC menu (Play, Music, File, etc) if loadDefaultImage=false. Have tried soulcalibur.gdi and some scene demos of .cdi format. USB hdd light indicates activity but in the end, nothing..  
   
 Used MinGW on Win7 to build the elf. Had to edit plugins/ImgReader/common.h (wstring path; to std::wstring path;). Don't know if thats ok or not?  
   
 Anybody get further than this have any tips?  
   
 Kindest Regards

## 2011-11-06 15:37:36, posted by: warfaren

[quote="silva"]  
 Hi Everyone,  
   
 Have the same issue here of can not get images to load. Emulator does run OK to DC menu (Play, Music, File, etc) if loadDefaultImage=false. Have tried soulcalibur.gdi and some scene demos of .cdi format. USB hdd light indicates activity but in the end, nothing..  
   
 Used MinGW on Win7 to build the elf. Had to edit plugins/ImgReader/common.h (wstring path; to std::wstring path;). Don't know if thats ok or not?  
   
 Anybody get further than this have any tips?  
   
 Kindest Regards  
 [/quote]  
   
 GliGli told me BIOS is all it can play for now.

## 2011-11-06 17:35:25, posted by: silva

Ok Cool, good fun following the progress in code updates on github for these projects.  
   
 Thanks !

## 2011-11-27 02:47:43, posted by: warfaren

Ok, so I just tried out Soul Calibur. All I can say is.... wow!  
 Thank you GliGli!!!

## 2011-11-27 23:48:04, posted by: Razkar

First post updated   
 Thx to Gli²

## 2011-11-28 09:19:11, posted by: Sonic-NKT

Looks awesome :)   
 cant wait for a first release...

## 2011-12-02 00:47:33, posted by: Pa0l0ne

[quote="Sonic-NKT"]  
 Looks awesome :)   
 cant wait for a first release...  
 [/quote]  
   
 ...so just compile yourself...and enjoy actual state of art! ;)

## 2011-12-22 13:08:16, posted by: HiGhLaNdR

Hello, I'm getting this problem:  
   
 /home/rui/xbox/nulldc-360/plugins/ImgReader/deps/chdr.cpp:44:18: fatal error: zlib.h: No such file or directory  
 compilation terminated.  
 make[1]: *** [chdr.o] Error 1  
 make: *** [build] Error 2  
   
 Any ideia why?  
 If I copy the zlib.h and the zconf.h to the libxenon lib dir it will pass this error and then I'll get other errors like the png library missing which I can copy too ... in the end when linking to finalize I get the lpng and lz missing ...  
   
 Thanks!

## 2011-12-22 13:21:46, posted by: tuxuser

http://www.libxenon.org/index.php?topic=116

## 2011-12-22 13:51:51, posted by: HiGhLaNdR

Thanks.  
   
 linking ... nulldc-360.elf  
 converting and stripping ... nulldc-360.elf32  
   
 Done :)  
   
 Cheers!

## 2011-12-27 12:00:26, posted by: moco

Can I please have a cOmpiled copy? I have every dc title and can upload

## 2011-12-27 12:08:31, posted by: warfaren

You've gotta compile it yourself. It's not that hard, just look around these forums. All the help you'll ever need is here. If you still can't figure it out, come visit the IRC channel, #libxenon @ EFNet, and ask for help there. As for uploading games, that would be piracy and that does certainly not belong here!

## 2011-12-27 18:40:50, posted by: GhaleonX

[quote="moco"]  
 Can I please have a cOmpiled copy? I have every dc title and can upload  
 [/quote]  
   
 At present, in addition to compiling, you need to edit gligli's code yourself (slightly) in order to run any games, too. So essentially, you'd have a NullDC.elf for every potential DC title you wish to test. Many of them will not load at all yet, even ones mentioned in his source code. If you compile his source as-is, it will be expecting to find the dc bios, plugins, and soul calibur on a linux hard drive, and there is no 'rom browser' feature, either.   
   
 Once you do compile his source successfully, you'll still have to deal with the fact that it's about 75% speed and no sound. Let's also not forget that you have to have a raw GDI rip of your games, and not .bin/.iso/.cdi/etc  
   
 Very promising emu, but if you're wanting to check it out "just to play" then just wait a little longer for a playable version.

## 2011-12-30 02:04:00, posted by: Cancerous1

[quote="moco"]  
 Can I please have a cOmpiled copy? I have every dc title and can upload  
 [/quote]  
   
 If the author wants to post a binary they will, and we will respect their wishes.  
   
 Never offer to upload roms/iso's here again or you'll be banned thank you. It's not a debate about if sega cares or what is right or wrong. It is against our rules for this board.

## 2012-02-27 16:23:51, posted by: val532

Hello, there is news about the development ?   
 I see news comit on the GiT.

## 2012-02-29 00:27:52, posted by: Pa0l0ne

The only playable game remain "Soulcalibur" without sound but excellent game speed with dynamic recompilation fully "stable" and functional.  
 The recent commits are about optimization and aren't specifically interesting for people that not understand the code.  
 All credits goes to GliGli for his wonderful piece of code.

## 2012-06-01 04:16:15, posted by: Mimoc

hi, any news of this great emu?

## 2012-06-13 22:29:42, posted by: Pa0l0ne

Nothing...i think libxenon is in a complete rewrote state..be patience..and i'm sure the master Gligli wil soon make something magic

## 2012-08-30 17:01:32, posted by: GliGli

Got back to it :)  
   
 http://gligli360.blogspot.fr/2012/08/still-alive.html

## 2012-09-13 23:43:23, posted by: MagicSeb

http://www.youtube.com/watch?v=Bcw8s98OoGY&feature=plcp  
   
 And working great !

## 2012-09-14 13:45:21, posted by: chicco30

Where can i find this emu?

## 2012-09-14 15:00:06, posted by: Pa0l0ne

[quote="chicco30"]  
 Where can i find this emu?  
 [/quote]  
   
 You can try compile yourself. The progress on the emu are amazing but ATM is not an officiale release (maybe soon).  
   
 Take a look on the new Menu Interface:  
 [youtube]GLzLtO4U12Q[/youtube]

## 2012-09-14 18:20:33, posted by: ploggy

Have you tried Sonic Adventure 1/2? How well do they run, maybe a vid of it in action? :p

## 2012-09-14 22:10:40, posted by: Pa0l0ne

[quote="ploggy"]  
 Have you tried Sonic Adventure 1/2? How well do they run, maybe a vid of it in action? :p  
 [/quote]  
   
 I have tried Sonic Adventure 1, the emulation speed is very good and the graphics seems not have any problem except for the Intro Video (the colors are wrong and the frames are tearing garbage) and random crashes that often appear.  
   
 BUT SLOW DOWN A BIT...ATM we have only a beta/preview compiled binary...

## 2012-09-15 00:05:11, posted by: ploggy

It's ok, I was just a bit curious. ;D What about SA2, Same?

## 2012-09-15 20:23:50, posted by: Pa0l0ne

Here you are.  
   
 [youtube]-w45LdzpskA[/youtube]

## 2012-09-16 02:07:12, posted by: ploggy

Thank you Pa0l0ne, very much appreciated. things seem to be progressing nicely. (apart from the random crashes) but I'm sure they will get sorted soon :)  
   
 I'm very excited for this, plus seeing GliGli back working on Mupen-360 again too. Can't wait. :)  
   
 Thanks.

## 2012-09-16 19:06:37, posted by: Pa0l0ne

Tested without luck "Shenmue I"  
   
 The Intro Video is almost perfect, only some little audio/video glitches. Unfortunately hangs on ingame as Sonic Adventure does.

## 2012-09-17 21:49:05, posted by: MagicSeb

We have the same problem on same games ^^  
   
 So i think our builds is equal.  
   
 Crazy taxi is working great :p

## 2012-09-18 12:59:26, posted by: COOLRUNNER007

WHEN IS THERE GONNA BE A LINK FOR THE GENERAL PUBLIC TO TRY THIS EMULATOR?????I BEEN LITERALLY WAITING FOR ALMOST 12 MONTHES FOR THIS,EVEN IF ITS STILL IN BETA STAGES I WANNA GET THIS EMULATION RUNNING ON MY CONSOLE,IM A CONSOLE HACKER AND WORK FOR A LIVING IN A REPAIR/MODDING BUSINESS SO I DONT GET TO MUCH TIME TO SIT DOWN AND UNDERSTAND THE GAME/EMULATOR HACKING SIDE OF THINGS,LOL,WOULD BE GREAT IF SOMETHING WAS RELEASED ASAP,IM GETTING OLD AND FEELING IT EVERYDAY!!!! >:( >:( >:( >:( >:(

## 2012-09-18 19:06:57, posted by: Pa0l0ne

[quote="COOLRUNNER007"]  
 WHEN IS THERE GONNA BE A LINK FOR THE GENERAL PUBLIC TO TRY THIS EMULATOR?????I BEEN LITERALLY WAITING FOR ALMOST 12 MONTHES FOR THIS,EVEN IF ITS STILL IN BETA STAGES I WANNA GET THIS EMULATION RUNNING ON MY CONSOLE,IM A CONSOLE HACKER AND WORK FOR A LIVING IN A REPAIR/MODDING BUSINESS SO I DONT GET TO MUCH TIME TO SIT DOWN AND UNDERSTAND THE GAME/EMULATOR HACKING SIDE OF THINGS,LOL,WOULD BE GREAT IF SOMETHING WAS RELEASED ASAP,IM GETTING OLD AND FEELING IT EVERYDAY!!!! >:( >:( >:( >:( >:(  
 [/quote]  
   
 Im a totally moron lamer and i have compiled myself the public Gligli source, and you, a real console hacker, don't have skill for this kind of things?  
 c'mon...maybe you are like the best asshole modder Spagotcy?  
   
 Be patience sweet child o'mine!

## 2012-09-18 22:56:33, posted by: MagicSeb

And Caps Lock can be unlock  
   
 Some tests today : (latest build by me, 2012.09.20)  
   
 [color=green]WORKING GREAT :[/color]  
 - AeroWings 2 : good speed  
 - Bomberman Online : good speed, jerky video but it's ok  
 - Charge n blast : full speed  
 - Daytona USA : full speed  
 - Gigawings 2 : no slow down  
 - Capcom Vs Snk 2 JP : great sound and graphics, intro is fast as it should be. fight is ok 100 full speed  
 - Ecco The Dolphin  
 - Project Justice (Rival Schools 2 ?) USA : little glitch on sound  
 - Ready 2 Rumble 2 : minor sound glitches  
 - Sonic Adventure 2 PAL : some jerky sound  
 - Rayman 2 The Great Escape USA : full speed, little sratches on sound some display bugs  
   
 [color=green]WORKING :[/color]  
 - AeroWings : not very playable slow down  
 - Gigawings : missings graphics ?  
 - Crazy Taxi 1 & 2 : some slow down but it's fully playable  
 - Dead or Alive 2 : slow  
 - Virtua Tennis : little jerky sound  
 - Virtua Tennis 2 - Tennis 2K2 : lot of jerky sound, slow down  
   
 [color=red]NOT WORKING :[/color]  
 - Caesar Palace : red screen  
 - Carrier : very slow, and red screen  
 - Centipede : lock on mpeg sofdec logo  
 - Championship Surfer : just crash at loading  
 - Coaster Works : crash after Xicat logo  
 - D2, console locked after sega logo  
 - Ikaruga : crash or let you to dreamcast menu  
 - Fatal Fury : Mark of the Wolves. : white screen and nothing  
 - Fighting Force 2 : Red screen after a long waiting  
 - GTA 2 : white screen and nothing.  
 - Midway Greatest Hits Vol 2 : red screen after patching VGA cable...  
 - POD 2 PAL : Locked on loading first track  
 - Rez : Crash red screen etc...  
 - Shenmue I : Intro is ok, but red screen when the game should start  
 - Shenmue II : go to black screen and lock console -no red screen-  
 - Under Deafeat : red screen, Unknown ARM instruction  
 - Zero Gunner 2 : crashing or dreamcast menu  
   
 NOTE : Some games doesn't support VGA Cable, like Midway Greatest Arcade Hits Vol 2. I need to modify IP.BIN in track03.bin  
   
 I will update this post when i test other games

## 2012-09-22 20:27:05, posted by: MagicSeb

[youtube]http://www.youtube.com/watch?v=yZaXOVGQtLM[/youtube]  
   
 Youtube doesn't like reencoded mp3 ^^

## 2012-09-23 02:07:28, posted by: COOLRUNNER007

@Pa0l0ne,yes your right mate and I totally agree with you,but when you work for 6 days a week 10 hours a day and have a wife and 2 kids no older than 10 to come home to believe me you don't get much time to sit down and try this side of hacking,once you have kids mate your free time is G.O.N.E. until they become adults themselves,sweet child o mine it should be SAD BUT TRUE!!!

## 2012-09-23 07:35:37, posted by: sk1080

If you have a wife and 2 kids then you shouldn't rage in all caps...  
   
 oh: and I like your XeLL build

## 2012-09-23 20:23:27, posted by: GliGli

[quote="COOLRUNNER007"]  
 WHEN IS THERE GONNA BE A LINK FOR THE GENERAL PUBLIC TO TRY THIS EMULATOR?????I BEEN LITERALLY WAITING FOR ALMOST 12 MONTHES FOR THIS,EVEN IF ITS STILL IN BETA STAGES I WANNA GET THIS EMULATION RUNNING ON MY CONSOLE,IM A CONSOLE HACKER AND WORK FOR A LIVING IN A REPAIR/MODDING BUSINESS SO I DONT GET TO MUCH TIME TO SIT DOWN AND UNDERSTAND THE GAME/EMULATOR HACKING SIDE OF THINGS,LOL,WOULD BE GREAT IF SOMETHING WAS RELEASED ASAP,IM GETTING OLD AND FEELING IT EVERYDAY!!!! >:( >:( >:( >:( >:(  
 [/quote]  
   
 Hmmmm.... seriously wtf man, you think I owe you something?  
 I do that stuff on my free time, I also have a job and all, and if I don't feel like working on it, this kind of messages won't help at all...  
 Also, if you want to try it that much, your hacker skills should help you compiling it in no time !

## 2012-09-24 13:25:47, posted by: COOLRUNNER007

Owe you?????????what did I say bout owing you or something???all I said was when was this emulator gonna roughly be released to the general public,I didn't demand anything from you at all or was trying to express myself in that way,I been following this nulldc360 project now since it was announced and hangin to try it and if my caps lock comes across the wrong way to people I apologise for that,I've just always typed in capitals,sorry GliGli if you misunderstood my punctuation.

## 2012-10-09 01:30:17, posted by: parwathy

Virtua striker 2 is working quite good! Game is playable, little problems with sound and few graphics bugs, but speed is very good! I can't stop playing this again :)  
   
 Thanks Gligli!!!! ;D ;D  
   
 By the way, is it possible to use another cable setting? Like RGB? To play games not supporting VGA?  
 Maybe modifying nullDC.cpp line before compiling? (didnt try yet, maybe this is a stupid idea ... :o) [code]settings.dreamcast.cable=min(max(settings.dreamcast.cable,0),3); settings.dreamcast.region=min(max(settings.dreamcast.region,0),3); settings.dreamcast.broadcast=min(max(settings.dreamcast.broadcast,0),4);[/code]   
   
 Can't wait for the future updates ^^ ;D

## 2012-10-09 12:19:19, posted by: OOKAMI

[quote="parwathy"]  
 Virtua striker 2 is working quite good! Game is playable, little problems with sound and few graphics bugs, but speed is very good! I can't stop playing this again :)  
   
 Thanks Gligli!!!! ;D ;D  
   
 By the way, is it possible to use another cable setting? Like RGB? To play games not supporting VGA?  
 Maybe modifying nullDC.cpp line before compiling? (didnt try yet, maybe this is a stupid idea ... :o) [code]settings.dreamcast.cable=min(max(settings.dreamcast.cable,0),3); settings.dreamcast.region=min(max(settings.dreamcast.region,0),3); settings.dreamcast.broadcast=min(max(settings.dreamcast.broadcast,0),4);[/code]   
   
 Can't wait for the future updates ^^ ;D  
 [/quote]  
   
 this is exactly what i think about :p  
   
 regarding cfg file from pc version to see how change video cable setting in the emu cfg file seem not working  
   
 the king of fighters 99 not working because of video cable setting and even modification to have the same configuration as pc not working  
   
 maybe in the source code like you think :)  
   
 .

## 2012-11-12 02:17:43, posted by: MDashK

Hello all. =)  
   
 First off, a big special thanks to gligli for creating this project and work on it to bring us the best he can.  
   
 I recently installed ubuntu and all the libxenon libraries, etc etc, to be able to compile the emu to be able to test it myself.  
 After a struggle of hours to do it, i was finally able to compile the latest git available of the emu.  
 But now, I have a few questions, if anyone can answer them. =)  
   
 1) The make created a ELF and a ELF32. Which one is to use? Differences?  
 2) In the compiling process, there where a lot of warnings, specially reffering to variables defined but not in use. Is this normal? Should I worry?  
   
 Best regards to all! (thumbs up)

## 2012-11-13 00:53:20, posted by: MagicSeb

use the elf32  
   
 elf is used for debugging purpose.  
   
 also don't forget nulldc-360 folder (a description of the content is [url=http://libxenon.org/http://libxenon.org//viewtopic.php?p=1098#p1098]here[/url]

## 2012-11-14 01:22:13, posted by: MDashK

Thanks for the help MagicSeb. =)  
   
 I managed to discover myself that only the ELF32 is to be used. The other one didn't even run. XD  
 Then, it ran, but it would give me the red screen error. Then I noticed someone around here with the same error, and saw that it was those missing files.  
   
 I tried again to run the emu, loaded a GDI, no errors, but the screen just remained black... Still trying to figure out what's wrong.  
 The game I tried was: Sonic Adventure 2 The Trial.  
   
 Still have to try a few more.  
   
 Update: I was missing the "dc\_nvmem.bin" file in the data directory. Already added it. Still haven't tested it. I'm @ work.  
 BTW: my 360 is using HDMI. Can it affect if the emu runs or not? I can't find anything related to this "black screen".... Maybe it's the same behaviour has this one: "- Shenmue II : go to black screen and lock console -no red screen-" although the full game works OK for the looks of it...  
   
 Also: the files I'm using is from PC version "nullDC\_104\_r136"  
   
 **[b]New Update[/b]**: Ok, I dunno what, but I must have done something wrong...  
 Just tried with the game "Capcom vs snk 2" and it still gives me the "black screen" error. even the console freezes for the looks of it. But no error is given... Both games to the same thing. Can anyone confirm with me if the newest git update of the emulator is working with any other game?  
 Also, the CRC32 or MD5 of the ELF32 file would also be usefull, so I can check if my elf executable is compiled OK or not...  
   
 Oh, other thing: doubts.  
 1) The newest git update, to compile it correctly, do I have to update my libxenon with the libxenon from gligli, or does the standard one compiles ok?  
 2) can anyone who has the emulator in working state inform me of it's folder structure. Just to triple check I'm not missing anything...  
   
 Thanks!  
   
 **[b]NEW UPDATE[/b]**  
 OK, so I've waited for someone to help me out here, but in the meantime, I decided to try to grab the "libxenon" from the gligli repository. I didn't really knew how to "update" using the git command (i'm not very good with linux) so I just renamed the libxenon directory to "libxenon\_" and made the git clone command.  
 So after that, just grabbed the nulldc-360 git again, and recompiled using (i hope) the libxenon from gligli.  
 It compiled OK, lots of warning due to unused variables (again) but no critical errors for the looks of it.  
 Once again, I'm not really shure if it's compiled OK. Only thing I know is that this new ELF has a different CRC32 than the other one. So I'm gessing that something is different, and hoping that this new ELF was compiled using the libxenon from gligli.  
   
 Here are the CRC32's from my files. If anyone can confirm which is the good one, that would be very helpfull. =)  
   
 CRC32 from **[b]old ELF[/b]**: 8443ED42  
 CRC32 from **[b]new ELF[/b]**: 7F2A11FE  
   
 **[b]UPDATE[/b]**: Well, I just tried the new ELF; tried loading the same 2 games again. No progress... Seems to be loading, but goes to black screen and stays there...  
 Can the region of the bios affect in anything? I tried both NTSC USA and PAL EUR bios with the emu, and no luck so far.... =(  
   
 Thanks.  
   
 Regards to all.

## 2012-11-25 14:06:16, posted by: MDashK

Can anyone around here help me with the previous post?  
 Been wanting to play Capcom vs SNK 2 for some time now. =)  
   
 Also, just posting to see if someone sees the updates, since updating the post doesn't send e-mail to the subscribers nor bumps the thread up... Sorry for double-posting...  
   
 Regards!  
   
   
 **[b]UPDATE: [/b]**MagicSeb helped me out by sending me information via PM regarding the contents of the folder nulldc-360.  
 After a couple of testes, turns out, that not only my ELF must be not good, but also, the CFG file was influentiating the result.  
   
 I made tests with both my ELF files (still don't know which one is OK) and tried various CFG files.  
 In the end, I always get one of these 2 results, regardless of the ELF I use:  
   
 1) Either the GDI loads and the screen remains black without sound nor anything.  
 Or  
 2) I try to load a GDI but the loading screen doesn't disappear, and the USB pen keeps flashing forever... Like it's loading something VERY BIG. I waited for 5 minutes, didn't stop. Just kept flashing...  
   
 So these are my results so far... Really trying to understand what is wrong and WHERE is wrong.  
 I still think something's wrong with my ELF files. One of them, at least, is compiled incorrectly, if not both.  
 I followed the PDF tutorial of the site OK, double checked that, so... I really don't know what's wrong here.....

## 2012-11-30 10:57:19, posted by: MDashK

Sorry for the double post here... Just giving a "heads-up" for those with the thread subscribed.  
   
 Still not being able to run any game. I don't know if anyone around here is having or HAD the same problem as I'm having.  
 Either something's missing me, or i'm very VERY stupid in Linux and I compiled this thing VERY wrongly. I don't think it's the second case, but who knows...  
   
 Anyways, once again, I request: please if anyone can, provide me with the CRC32 value that WinRAR gives you when compressing the ELF. The CRC32 value is the perfect way for me to know if both my ELF files are compiled OK or not. I'm gessing that are BOTH wrong for some reason.  
   
 Another thing: if I want to use the LibXenon version of gligli, what do I have to do? Can I simply replace the standard libxenon files with the ones from gligli? WHen I compile the ELF; will those be used? Or do I have to do something else?  
   
 Best regards to all and sorry for all the trouble and doule-post thing... =S

## 2012-12-21 17:43:37, posted by: SonicKiller

Hi all,  
   
 MDashK, I've got exactly the same problem.  
 Latest nulldc-360 commit from GliGli repo and latest libxenon toolchain + libs from free60 repo.  
   
 No matter which Bios files I try, I always got a black screen.  
   
 Tried with Crazy Taxi US and Capcom vs SNK 2 (which is also the only game I want to play ;-) )  
   
 Thanks for keeping us updated anyway, i will try to do the same if there's anything new.

## 2012-12-26 02:06:25, posted by: MDashK

Hey SonicKiller,  
   
 Sorry to hear that you got the same problem has I have... =(  
 So far, I don't have any new updates on the matter, but if I ever do, I will post them here for you too (and for anyone else that has the same issue).  
   
 Thanks for posting your share.

## 2013-01-05 20:00:39, posted by: iSynic

I'm guessing you guys are on Corona boards? We're kinda screwed out of a bunch of these new emulators because of their dependency on Xell, which has no video out on Corona boards and the devs haven't answered my PMs for weeks now about how progress is coming.  
   
 No Mupen64, no NullDC. Some sort of response from somebody would be appreciated.

## 2013-01-05 21:12:29, posted by: MDashK

No, my board is a Trinity board.  
 Xell works OK. All other apps on Xell work 100% for me.

## 2013-01-05 23:37:18, posted by: barnhilltrckn

[quote="iSynic"]  
 I'm guessing you guys are on Corona boards? We're kinda screwed out of a bunch of these new emulators because of their dependency on Xell, which has no video out on Corona boards and the devs haven't answered my PMs for weeks now about how progress is coming.  
   
 No Mupen64, no NullDC. Some sort of response from somebody would be appreciated.  
 [/quote]  
   
 Well I have an answer and I am sorry if its not the answer you want but......it will be done when its done. Im sure the reason you havent got an answer is that they are busy. Also it may not be possible?? Im not sure but rest assured the guys here always pull through. Respect the devs ;)

## 2013-01-06 05:14:38, posted by: iSynic

I absolutely respect the Devs. But I've asked politely on multiple forums with active devs and still haven't gotten a reply. So I apologize if I got a bit snarky, but the last update regarding the Xell/Corona video problems was four months ago.   
   
 With all of these exciting homebrew releases that are dependent on Xell, it's becoming higher priority.

## 2013-02-14 11:11:17, posted by: MagicSeb

[quote="MDashK"]  
 Sorry for the double post here... Just giving a "heads-up" for those with the thread subscribed.  
   
 Still not being able to run any game. I don't know if anyone around here is having or HAD the same problem as I'm having.  
 Either something's missing me, or i'm very VERY stupid in Linux and I compiled this thing VERY wrongly. I don't think it's the second case, but who knows...  
   
 Anyways, once again, I request: please if anyone can, provide me with the CRC32 value that WinRAR gives you when compressing the ELF. The CRC32 value is the perfect way for me to know if both my ELF files are compiled OK or not. I'm gessing that are BOTH wrong for some reason.  
   
 Another thing: if I want to use the LibXenon version of gligli, what do I have to do? Can I simply replace the standard libxenon files with the ones from gligli? WHen I compile the ELF; will those be used? Or do I have to do something else?  
   
 Best regards to all and sorry for all the trouble and doule-post thing... =S  
 [/quote]  
   
 Hi,  
   
 You have to make a separate folder and glitclone the libxenon by gligli. Note : You don't have to recompile the toolchain, just do :  
   
 ./build-xenon-toolchain libxenon  
   
 of course do that for all libs and filesystems (important)  
   
 build nulldc-360 with that and it should work.

## 2013-02-14 20:25:32, posted by: MDashK

Did that right from the beggining. Didn't work... =(  
   
 Thanks for the help though.

## 2013-02-15 21:14:00, posted by: MagicSeb

Do you have dc\_bios.bin, dc\_boot.bin dc\_flash.bin in nulldc-360\data\ ????

## 2013-02-18 19:40:43, posted by: SonicKiller

(Excuse me all for the delay, I had a lot to do.)  
   
 About the motherboard, I've got a Falcon one, so I don't think there's something linked with the S models.  
   
 I still have the same problem and I have all the files in nulldc-360/data (from my working demul on pc) but I did not work on it a lot since the last time I've posted...  
   
   
 Anyway, I can maybe help about with your failures : Try with another USB key !  
   
 I don't know exactly why but I have one which absolutely doesn't work with with NullDC-360 and it works with any other elf file I've tried with. It gives me the famous red screen. FYI, it has a 360 FatX partition on it and it is a "ID 0781:5408 SanDisk Corp. Cruzer Titanium U3" with the U3 partition removed. When I try with my other noname key I can still launch the emulator, use the main menu then get the black screen when I try to launch a game.  
   
 Here's the report guys, thanks for the hard work devs ;-)

## 2013-02-18 19:56:25, posted by: MDashK

Well, I already resolved my problems with the compiling and the emulator, etc.  
   
 Right now, it's working OK, tried Sonic Adventure and Capcom vs SNK 2, aside from the slight sound problems, and sporadic red screen, it works OK.  
   
 The problem? Bad compile of the ELF.  
 For some reason was not compiling ok. Managed to get OK with fresh install of everything from the start, including ubuntu.

## 2013-02-18 20:57:24, posted by: SonicKiller

Ok, thanks MDashK.  
   
 I will retry from scratch as you did, when I'll have some spare time and come back hopefully with some good news.

## 2015-07-21 09:20:20, posted by: <Unknown User>

Hallo guys ! I've come to ask about AV Cable error in some snk games, like kofs, garou, last blade 2 etc... Is there a way to fiz this or no luck ? >:D   
 Keep going gligli the great work !!!

## 2015-07-21 09:33:14, posted by: <Unknown User>

The project still continue Gligli ?