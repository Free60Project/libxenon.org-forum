# N64 Emulator by GliGli

## 2011-02-25 11:37:25, posted by: tuxuser

By proxy I post some stuff from GliGli here about the current status of the N64 Emulator. Its copied from his blog.  
   
 Friday, 7 January 2011 [quote] I have already made quite a few improvements to my mupen64 port since the [url=http://www.youtube.com/watch?v=E8stB1EKa0o]video[/url].  
   
 About half an hour after making it, I fixed almost all the missing screens/skies and the clipped mario by adjusting the Z buffer range (previous range was 0..1, now it is -1..1).  
   
 I then improved N64 gfx combiners emulation (combiners are sort of early primitive pixel shaders). I use 360 pixel shaders to emulate them. At first it was really slow because I used many switches and loops in it and it seems doing that in a pixel shader isn't such a good idea. I got everything back to playable speeds by using mainly 3 techniques:  
   
 * a color lookup table to emulate combiner 'source' (ie vertex color/texture color/constant/...)  
 * a math formula that handles all the possible cases for the combiner operation (ie mul/add/sub/...)  
 * having different pixel shaders (one fast that can only do simple things, one intermediate, and one slow that emulates everything) and switching between then when needed.  
   
 So now gfx emulation is quite fast but the emu still runs slowly when it emulates floating point intensive scenes like the mario head demo at the begininng of SM64 so I start looking at how mupen64 emulates floating point operations, I quickly discovered that the whole floating point unit was running in interpreter mode, oops!  
 A few #define later the emu was up to 50% faster.  
   
 Next I had an idea: why not try to get the X360 GPU to render my current frame in background instead of actively waiting for it to finish rendering.  
 Usually you do this:  
   
 /* resolve (and clear) */  
 Xe\_Resolve(xe);  
 /* wait for render finish */  
 Xe\_Sync(xe);  
   
   
 Now I do this:  
   
 /* resolve (and clear) */  
 Xe\_Resolve(xe);  
 /* begin rendering in background */  
 Xe\_Execute(xe);  
   
   
 and then I call Xe\_Sync() at the last time right before beginning my next frame  
 I got a huge speed boost with this, Super Mario 64 now runs at around 100fps ingame ! [/quote] Thursday, 27 January 2011 [quote] During the last weeks, I worked a bit on improving my mupen64 port, here are the things I did.  
   
 As SM64 started to work well, I switched to the Zelda rom for my testing, it is a much more complex game to emulate graphics wise, so obviously it was completely buggy and painfully slow on the first run. The biggest problem was that unlike SM64, most of the rendering was done with my slowest pixel shader, and fixing the bugs would have made it even slower so I decided to do a complete rewrite of the shader. This time I designed it around something I just discovered: [url=http://msdn.microsoft.com/en-us/library/bb219856%28v=vs.85%29.aspx]constant boolean registers[/url], it allows flow control without a big performance hit. I took me a few tries to get it fast and accurate, but now that pixel shader is almost as fast as the old one on simple cases while being more accurate and much faster on complex cases. I also made my old shader as accurate as I could, it is now used for some rare cases the new one can't emulate. With a few more fixes to libxenon and the emulator (implementing 2D rendering for example), this makes Zelda reasonably fast and playable.  
   
 Next game was Mario Kart 64, this time it was fast and looking good on the first try, but crashed after a few races with some 'out of memory' message. It turns out something very important was missing from the libxenon 3D driver: a way to free what you allocate ! (texures/vertex buffers/...) So I replaced the very basic GFX memory allocator with some malloc-like one I found in libxenon sourcecode, and modified the emulator texture cache to actually free old textures when needed.  
   
 I think it's time for a new video so here it is :) :) :)   
   
 [align=center][youtube]http://www.youtube.com/watch?v=TvC41ku5FFA[/youtube][/align] [/quote] Tuesday, 28 June 2011 [quote] Sorry for the lack of updates, I was busy with other stuff for some months.  
   
 As you can see on my github, ( [url=https://github.com/gligli/libxenon/commits/master]https://github.com/gligli/libxenon/commits/master[/url] ), I think libXenon has improved a lot lately, with lots of stuff added from Xell (NAND access, lwip & network code,...), a new ELF loader, a unified ATA driver (that can access both HDD and DVD), the return of opendir/readdir/... functions and many bug fixes and smaller improvements in almost all drivers.  
   
 The reason for many of those changes is to be able to make most of Xell a regular libXenon app: Xell would be splitted into 2 stages, one stage which recovers from exploit and then decompresses and launches a second stage, which is a libXenon ELF. To maintain backwards compatibility, both stages would have to fit in the 256KB limit for a Xell binary.  
   
 Last but not least, I'm working on mupen64-360, my Wii64 port these days, I already added sound and done some optimisations to try to get more speed.  
 I multithreaded a good part of sound processing so it's done almost for free, and in fact anything that isn't multithreaded (RSP emulation) was already running in my version from january. I might be able to multithread RSP too, it would probably give a nice speed boost :)  
 I also redone the port of the Wii64 dynarec, I did my first port from the ps3 branch and it seems it wasn't up to date with the trunk speed-wise. Now it's using Wii64 1.1 code. I also changed the way stores were handled in the dynarec, trying to generate more code and rely less on a (slow) generic C function to do the job.  
 By the way, source code is now available on my github ( [url=https://github.com/gligli/mupen64-360]https://github.com/gligli/mupen64-360[/url] ). Anybody that can compile it can try it, but please don't distribute binaries ! It's not a good idea at all to release unofficial versions of a work in progess of someone else code so I hope You can be responsible on this.  
   
 Here's a new video showing the progress on Mario64, jerkiness is due to the video capture card, trust me that game runs smooth :)  
   
 [align=center][youtube]http://www.youtube.com/watch?v=w3o41LvZ71w[/youtube][/align] [/quote]

## 2011-02-26 20:25:45, posted by: Chrisoldinho

i cant wait to see the end product. i have been following the blog with the updates, excellent work so far :)

## 2011-06-30 19:40:38, posted by: tuxuser

Update in first post :)

## 2011-06-30 23:25:07, posted by: Doerek

Thank you, Tuxuser for keeping us up2date

## 2011-07-23 16:20:09, posted by: MagicSeb

I have built the latest modifications made by gligli  
   
 The emulation is much faster now, watch the u-tube video.great work gligli !  
   
 [youtube]http://www.youtube.com/watch?v=bIW3RxIyuwA[/youtube]  
 [youtube]http://www.youtube.com/watch?v=Vpt1RsoCIIc[/youtube]  
   
 If you want to test mupen64-360, compile it

## 2011-07-24 18:35:28, posted by: sjuut

I tried compiling the source, I get the following error message:  
   
 [ucode1.cpp]  
 cc1plus: error: invalid option argument '-Ofast'  
 cc1plus: error: unrecognized command line option "-fno-tree-slp-vectorize"  
 make[1]: *** [ucode1.o] Error 1  
 make: *** [build] Error 2  
   
 and if I remove those arguments, I get a lot of different errors.   
   
 Can someone point me in the right direction?  
 Thanks!

## 2011-07-24 23:23:00, posted by: tuxuser

In the Makefile replace '-Ofast' with '-O2' and make sure you got the latest toolchain installed by typing  
 [code]* *xenon-gcc --version [/code] It has to show Version 4.6.0

## 2011-07-25 01:07:19, posted by: sjuut

Thanks for the quick reply! I got that answer in the irc channel too, thank you all for being so supportive.  
   
 This is very frustrating! Sorry if I sound like a n00b;  
   
 Im trying to update my toolchain, with no luck.  
 first, I followed the PDF guide 'how to set up toolchain', and after following all instructions correctly, my xenon-gcc version will show 4.4.0.  
   
 Then I cloned GliGlis git, did the same commands ./build-toolchain toolchain and libxenon..   
   
 and I'm still stuck at the older version.. ! I can see that gcc-4.6.0 is downloaded, but somehow it never overwrites 4.4.0.. the build.log does not show anything strange. In desperation I even overwritten the free60-git files with gligli's files (same folder structure), but to no avail.   
   
 Someone please explain!  
   
 :EDIT:  
 Nevermind, I fixed it!  
 gcc couldn't find mpc, I downloaded and installed it manually. Now I do have xenon-gcc 4.6.0, and I could compile mupen64-360.  
 Thanks !

## 2011-08-03 06:38:27, posted by: checo

sjuut. How to install the new compiler? I followed the setup guide for your pc libxenon programming and everything went well but I have many problems installing the new compiler :(.  
   
 PD. sorry if not well understood but the Spanish translated with google.

## 2011-08-04 21:45:00, posted by: Sonic-NKT

would love to see some videos of other games emulated than mario.   
 wouldnt mind recording them myself, but i currently cant compile 360 stuff.

## 2011-08-05 23:48:42, posted by: MagicSeb

[youtube]http://www.youtube.com/watch?v=3lwpJeFCTiM[/youtube]

## 2011-08-14 00:18:45, posted by: maxaille

I have this error when compiling under mingw: [quote]make[1]: /cygdrive/c/Users/max/Desktop/minGW/mupen364/Makefile: No such file or directory  
 make[1]: *** No rule to make target `/cygdrive/c/Users/max/Desktop/minGW/mupen364/Makefile'. Stop.  
 make: *** [build] Error 2  
   
 BUILD FAILED (exit value 2, total time: 451ms)[/quote] Ubuntu (virtual), I can not compile gcc-4.6.0 / 1 with various errors ...  
 So if anyone can help me or send me binaries....  
 Thanks

## 2011-08-24 06:17:05, posted by: chemone

I can compile it, but, in wich folder i must to put my rom to load it? Thanks and sorry for my bad english.

## 2011-08-24 14:36:51, posted by: Telemaque

Salut MagicSeb,  
   
 Que j'ai hâte, trop dur d'attendre !  
   
 @+++ et Bon Courage !  
 ;)

## 2011-09-07 18:28:47, posted by: Nitrous360

This emu is looking amazing! ;D I had no idea there was an N64 emu in development, let alone looking this polished! I cant wait for a release!

## 2011-09-10 08:08:09, posted by: ravendrow

just checked out the newest 0.91 build awesome stuff i will try to upload a vid in the next day or so.....cant wait to see it emulating all the 64 roms....playing killer instinct gold with glitch rain is fun though. anyone who can should checking this out....it's well worth the time to figure out how to compile it :D

## 2011-09-10 08:47:41, posted by: SynTeX

[quote="ravendrow"]  
 it's well worth the time to figure out how to compile it :D  
 [/quote]  
   
 Thats really true :D the games that run, run like a charm! Would love to see Star Wars: RS running :(

## 2011-09-10 17:23:00, posted by: ravendrow

@synTeX you check out the latest 0.91 yet GliGli added a browser :D

## 2011-09-10 20:28:52, posted by: SynTeX

Yea, i know i just compiled it yesterday :) had a lot of trouble getting the libs for zlx running, but it worked in the end ^^

## 2011-09-10 23:40:09, posted by: ravendrow

yeah me too so i take it you found the typo in the zlx makefile\_lib ?

## 2011-09-13 20:37:24, posted by: iPSad

Any download link? :)

## 2011-09-16 04:14:55, posted by: MagicSeb

[youtube]http://www.youtube.com/watch?v=jVzLWQquo7I[/youtube]  
   
 @iPSad : You can compile the actual source from the gligli's github  
   
 Here no one gives you the compiled elf.

## 2011-09-19 18:29:21, posted by: peet8989

Mutliple Controller support for mario kart would be just awesome :)

## 2011-09-21 17:25:10, posted by: jayboy86

[quote="peet8989"]  
 Mutliple Controller support for mario kart would be just awesome :)  
 [/quote]  
   
 yea i second that, would be so sweet

## 2011-09-21 19:10:57, posted by: sk1080

EDIT: No longer needed, gligli added multiple controller support  
   
 its a very simple patch  
   
 find void getKeys  
   
 change   
 if(get\_controller\_data(&c, 0)){  
 to  
 if(get\_controller\_data(&c, Control)){  
   
 change   
 if (Control == 0) Keys->Value = b.Value;  
 to  
 Keys->Value = b.Value;  
   
 then above that find  
 void initiateControllers(CONTROL\_INFO ControlInfo)  
 and mark additional controllers as present  
   
 sorry for not making a proper patch, but I am on a winblows pc and not at home atm

## 2011-09-21 20:10:24, posted by: SynTeX

Wow! Thanks a lot for this :)   
 I will try it tomorow but i think this is going to be awesome :D

## 2011-10-02 16:32:41, posted by: 128bit

This page  
 http://www.free60.org/Emulators  
   
 Need be update whit this emulator N64 too?

## 2011-10-17 13:34:29, posted by: Lib-Jambo

is there anything else to be worked on apart from single out some games that dont work with it...Would gladly help

## 2012-01-21 22:45:53, posted by: konio38

any news on this one? it has been a while.