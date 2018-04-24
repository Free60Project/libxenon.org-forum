# [BUGREPORTING] XeLL

## 2011-03-07 08:47:03, posted by: tuxuser

This topic is for bugs in XeLL-Master & XeLL-Testing.  
   
   
 **[b]If you are doing bugreports please fill out the following[/b]**  
 [quote] XeLL-Rev: *XeLL-Testing fix2/fix3 - xell-2f/xell-1f/xell-readcd/...*  
 Console Type: *Retail/Devkit/...*  
 Console Revision: *Xenon/...*  
 Hack-Version: *JTAG/King Kong/...*  
 Boot-Method: *Native/XeLL-Launch/HvXBootOS/...*  
 Videocable: *Composite/YUV - in YUV MODE/...*  
 Error-Description: *Describe your error as good as possible, if you own a Serial Adapter please attach a logile*[/quote]

## 2011-03-12 04:43:52, posted by: mojobojo

XeLL-Rev: XeLL-Testing current, with some slight modifications from me only graphical is the color change  
 Console Type: Retail  
 Console Revision: Jasper 512  
 Hack-Version: JTAG  
 Boot-Method: XeLL-Launch  
 Videocable: Component with hd switch on  
 Error-Description: A message popped up right as a launched xell launch and it was stuck on the screen all the way to booting linux in where it froze while adding a live user.  
   
 ![](http://i53.tinypic.com/f2sbux.png)[img]http://i53.tinypic.com/f2sbux.png[/img]

## 2011-03-12 23:26:21, posted by: tuxuser

Yeah I am aware of that.. seems like an inproper reset / no reset of the GPU.  
 I reported it here already, not as a bug though: [url=http://libxenon.org/http://libxenon.org//viewtopic.php?t=8]Click[/url]

## 2011-03-13 21:29:07, posted by: Chrisoldinho

Will post a screenshot of this shortly, need to find mobile phone :D  
   
 XeLL-Rev: XeLL-Reloaded 2f  
 Console Type: Retail  
 Console Revision: Falcon  
 Hack-Version: JTAG  
 Boot-Method: XeLL-Launch  
 Videocable: HDMI  
 Error-Description: Repeatedly get "No answer from TFTP" message on screen over and over again, it never stops printing the message.  
   
 **[b]*RESOLVED with latest build*[/b]**

## 2011-03-14 15:41:34, posted by: charlo.charli

XeLL-Rev: xell-HDMI-troubleshooting-2f.bin  
 Console Type: Retail  
 Console Revision: Jasper  
 Hack-Version: JTAG  
 Boot-Method: Xellaunch  
 Videocable: HDMI  
 Error-Description: Getting "Fat open of xenon.elf failed!" and "REQUEST SENSE failed"  
   
 ![](http://img135.imageshack.us/img135/1787/img0232r.jpg)[img]http://img135.imageshack.us/img135/1787/img0232r.jpg[/img]  
   
 Thanks for all your effort ;)  
   
 **[b]*RESOLVED with latest build*[/b]**

## 2011-03-17 12:37:12, posted by: tohnolo

XeLL-Rev: xell-reloaded-13.03.2011.tar.gz  
 Console Type: Retail  
 Console Revision: Falcon  
 Hack-Version: JTAG  
 Boot-Method: XeLL-Launch  
 Videocable: HDMI + Component HD AV Cable for digital audio  
 Error-Description: blackscreen on boot.  
   
 When booting with xell-HDMI-troubleshooting-2f.bin i get AVPACK ID = 0f. AVPACK ID is 1f when i connect with HDMI only. Also with Component HD cables litle switch in diffrent position the AVPACK ID = 03.

## 2011-03-17 22:17:21, posted by: ddxcb

XeLL-Rev: *xell-reloaded-13.03.2011 xell-2f/*  
 Console Type: *Retail/*  
 Console Revision: *Xenon/*  
 Hack-Version: *JTAG/*  
 Boot-Method: *XeLL-Launch/*  
 Videocable: *VGA*  
 Error-Description: *No Video output for VGA only on composite/component*  
   
 error logs  
 No video output.  
 \_\_ \_\_\_\_ \_\_\_ \_\_\_ \_\_\_\_\_  
 / \_|\_ \_\_ \_\_\_ \_\_\_| \_\_ ) / \_ / \_ \_  
 \_|  
 | |\_| '\_\_/ \_ / \_ \_ | | | | | | || |  
 | \_| | | \_\_/ \_\_/ |\_) | |\_| | |\_| |  
 | |  
 |\_| |\_| \_\_\_|\_\_\_|\_\_\_\_/ \_\_\_/ \_\_\_/ |\_|  
 [v0.04 - inspired by ika  
 ri]  
 booting firmware...!  
 syscall - starting xell file  
   
 XeLL - Xenon linux loader 0.3-git- 2011-03-13 (tux@tux-XPS-L501X x86\_64)  
 * Attempting to catch all CPUs...  
 CPUs online: 01..  
 CPUs online: 11..  
 CPUs online: 3f..  
 * success.  
 * xenos init  
 AVPACK detected: 0f  
 . ana disable  
 xenon\_smc\_i2c\_write failed, addr=0108, err=3  
 . ana enable  
 ................................................................................  
 .... . f1  
 . f2  
 * Xenos FB with 152x42 (1280x720) at 800000001e000000 initialized.  
 * sfcx init  
 * config init  
 * network init  
 * initializing lwip 1.4.0.r2...  
 * requesting dhcp.......  
 //\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_//  
 xell-no\_video trouble shoot.  
 \_\_ \_\_\_\_ \_\_\_ \_\_\_ \_\_\_\_\_  
 / \_|\_ \_\_ \_\_\_ \_\_\_| \_\_ ) / \_ / \_ \_  
 \_|  
 | |\_| '\_\_/ \_ / \_ \_ | | | | | | || |  
 | \_| | | \_\_/ \_\_/ |\_) | |\_| | |\_| |  
 | |  
 |\_| |\_| \_\_\_|\_\_\_|\_\_\_\_/ \_\_\_/ \_\_\_/ |\_|  
 [v0.04 - inspired by ika  
 ri]  
 booting firmware...!  
 syscall - starting xell file  
   
 XeLL - Xenon linux loader 0.3-git- 2011-03-09 (root@posnix i686)  
 * Attempting to catch all CPUs...  
 CPUs online: 01..  
 CPUs online: 11..  
 CPUs online: 3f..  
 * success.  
 * xenos init  
 AVPACK detected: 1b  
 please report this ID: 1b, VGA1024x768 & the AV cable you're using!  
 . ana disable  
 xenon\_smc\_i2c\_write failed, addr=0108, err=3  
 . ana enable  
 ................................................................................  
 .... . f1  
 . f2  
 * Xenos FB with 128x48 (1024x768) at 800000001e000000 initialized.

## 2011-03-18 04:39:42, posted by: Cancerous1

ddxcb, did your vga work for you on the old xell? would it be possible for you to take a pic of the screen when using the Xell-VGA-troubleshooting-2f.bin?

## 2011-03-18 08:21:49, posted by: ddxcb

[quote=""Cancerous1""]ddxcb, did your vga work for you on the old xell? would it be possible for you to take a pic of the screen when using the Xell-VGA-troubleshooting-2f.bin?[/quote]  
 the regular xell I dont know, xellous it would work.  
   
 Ill upload a pic soon.

## 2011-03-20 04:03:27, posted by: sbarrenechea

XeLL-Rev: *xell-reloaded-18.03.2011 xell-2f/*  
 Console Type: *Retail/*  
 Console Revision: *Falcon/*  
 Hack-Version: *JTAG/*  
 Boot-Method: *XeLL-Launch/*  
 Videocable: *RCA*  
 Error-Description: Bad resolution, don't fit to the screen || Can't access to the Xell-Reloaded via HTTP  
   
 I'm using the stock cable that comes with the console, and the resolution dont fit to the screen, but Xellous fits perfect. When I connect to HDMI in my LCDTV it works perfect, but I have trouble when I connect to my normal TV.  
   
 I'm gonna attach two pics to show :B  
   
 Xellous  
   
 ![](http://i54.tinypic.com/30vc4sp.jpg)[img]http://i54.tinypic.com/30vc4sp.jpg[/img]  
   
 (Has a border between the text and the border of the screen)  
   
 Xell-Reloaded  
   
 ![](http://i51.tinypic.com/w2quh.jpg)[img]http://i51.tinypic.com/w2quh.jpg[/img]  
   
 That border doesn't appear and the text is a little cutted. Sometimes i don't see what say when the text is in the lower part of the screen, because is cutted and I see a half of the text xd.  
   
 I have tried in 3 different CRT TV's and always happened the same (good with Xellous, cutted with Xell-Reloaded) but, i repeat, perfect with HDMI :/  
   
 I dont know if that's a bug, but I think that's annoying view the Xenon Linux Loader cutted in the borders xd  
   
 (I'm sorry for my english, i'm from Chile and I speak spanish xd)  
   
 Uh, and when the Linux kernel loads, the text is cutted too. That happened with the desktop environment too (I can't see the border parts)  
   
   
 ---------------------------------------  
   
   
 And about the HTTP, I cant access to that like in Xellous (I've tried in Xellous right now and it works, but in Xell-Reloaded no). When I put the IP of the console in my webbrowser, it says that is not available, but in the screen appears that i'm pinging to the console or something (I don't know if says "Losing connection." or "Using connection." Something like that xd

## 2011-03-20 04:50:42, posted by: tuxuser

@sbarrenechea  
   
 Thanks for the detailed bugreport.  
   
 1. Cutted Video: I will look, together with cancerous, at this to figure out why it makes such a big difference between xell-reloaded and xellous when using the non-HDTV Modes.  
   
 2. HTTP Server: It's totally normal that you are not able to connect to its HTTP Server.. it isnt implemented yet. There is only one page you could access for now: [url=http://123.123.123.123/FUSE]http://123.123.123.123/FUSE[/url]  
 123.123.123.123 is your XeLL-IP in that case of course ;)

## 2011-03-20 05:14:12, posted by: sbarrenechea

[quote=""tuxuser""]@sbarrenechea  
   
 Thanks for the detailed bugreport.  
   
 1. Cutted Video: I will look, together with cancerous, at this to figure out why it makes such a big difference between xell-reloaded and xellous when using the non-HDTV Modes.  
   
 2. HTTP Server: It's totally normal that you are not able to connect to its HTTP Server.. it isnt implemented yet. There is only one page you could access for now: [url=http://123.123.123.123/FUSE]http://123.123.123.123/FUSE[/url]  
 123.123.123.123 is your XeLL-IP in that case of course ;)[/quote]  
   
 okay! I hope my report will be helpful to Xell-reloaded :D and please, if you can implement the HTTP server to the final version would be great :D

## 2011-04-19 10:05:41, posted by: chriss179

XeLL-Rev: xell-2f  
 Console Type: Retail  
 Console Revision: Xenon  
 Hack-Version: JTAG   
 Boot-Method: XeLL-Launch  
 Videocable: VGA  
 Error-Description: No video  
   
 I've used the troubleshooting.bin and that gave me this screen:  
 [url=http://img13.imageshack.us/i/dscn2480rd.jpg/]![](http://img13.imageshack.us/img13/2038/dscn2480rd.jpg)[img]http://img13.imageshack.us/img13/2038/dscn2480rd.jpg[/img][/url]  
   
 Uploaded with [url=http://imageshack.us]ImageShack.us[/url]

## 2011-05-08 16:43:56, posted by: bretagnerv

Xell-Rev : Xell-HDMI-troubleshooting-2f.bin  
 Console Type : Retail  
 Console Revision : Jasper 256  
 Hack-Version : JTAG  
 Boot-Method : Xell-Launch 2.21  
 Video Cable : HDMI  
 Error-description : AVPACK=0f , stop load after logo "Xell Reloaded" !

## 2011-05-08 17:47:14, posted by: tuxuser

[quote=""bretagnerv""]Xell-Rev : Xell-HDMI-troubleshooting-2f.bin  
 Error-description : AVPACK=0f , stop load after logo "Xell Reloaded" ![/quote]  
   
 Of course it stops there.. you are using the XeLL-Troubleshooting not the real XeLL binary ;) Look at the first post, the attachment is the real one.

## 2011-12-20 17:24:05, posted by: greator

XeLL-Rev: XeLL Reloaded 2f  
 Console Type: retail  
 Console Revision: Jasper 16mb  
 Hack-Version: JTAG reset glitch  
 Boot-Method: XeLL-Launch  
 Videocable: Composite and VGA  
 Error-Description: Stuck at executing xenon.elf.   
   
 I only managed to get it run one time, when running rawflash v3 to write retail image. When I go back and want to write freeboot, it doesn't work. I tried rawflash v4 and mupen emulator, also doesn't work. (Mupen does execute at first but stuck at loading the emulator, I reset the console and it doesn't execute anymore.)  
   
 Also tried booting from CD, still stuck at executing, so its not my USB stick problem.

## 2011-12-20 17:42:08, posted by: tuxuser

Use latest xell build, you can find it in LibXenon -> XeLL -> XeLL Updates .. pretty much at the end of the thread

## 2011-12-20 18:40:36, posted by: DHeir

I have kboot.conf on root of USB stick. Apparently I made a type and it decided it wanted to continue to look for other avenues to boot from after timing out.  
 I pulled out the USB stick and made the correction to kboot.conf. Xell froze at Trying uda:/initrd.gz. When I placed the usb stick back in I get red crash screen.  
   
 Ouput from that:  
 [code]Exception Vector! (0x600) pir=0000000000000000 dar=00000000ec68fff3 sr0=0000000080029c18 sr1=0000000002003030 Ir=0000000080029c18 STACK DUMP: 0x80029c18 --> 0x80029c18 --> 0x8000fe20 --> 0x8001018c --> 0x80010b0c --> 0x80011440 --> 0x800117e8 --> 0x80011888 --> 0x80011948[/code]   
 I realize that maybe isn't a serious bug, however it's something worth reporting I thought.

## 2011-12-20 18:43:53, posted by: greator

[quote="tuxuser"]  
 Use latest xell build, you can find it in LibXenon -> XeLL -> XeLL Updates .. pretty much at the end of the thread  
 [/quote]  
   
 I already use the latest xell-reloaded-2stage-2011-09-23.  
   
 tried using debian liveCD. Fail, stuck at executing.

## 2011-12-21 00:12:05, posted by: tuxuser

[quote="greator"] I already use the latest xell-reloaded-2stage-2011-09-23. [/quote] Try this one: [url=http://libxenon.org/http://libxenon.org//viewtopic.php?p=1315#p1315]Click me[/url]  
 [quote] I have kboot.conf on root of USB stick. Apparently I made a type and it decided it wanted to continue to look for other avenues to boot from after timing out.  
 I pulled out the USB stick and made the correction to kboot.conf. Xell froze at Trying uda:/initrd.gz. When I placed the usb stick back in I get red crash screen. [/quote] Let me give you an example: You are installing Linux or Windows from a CD onto your computer. in the middle of the install-process you remove the installation-media! What will the setup program do? Right, it will report: Cant read file xyz. Please check your media.  
 As XeLL isnt really Plug'n'Play captable.. and also pretty low-level... it will error of course if you remove a media where its trying to load from atm. Dont expect us to fix it but thx for reporting it nontheless.

## 2011-12-21 17:53:28, posted by: greator

[quote="tuxuser"]  
 [quote="greator"]  
 I already use the latest xell-reloaded-2stage-2011-09-23.  
 [/quote]  
   
 Try this one: [url=http://libxenon.org/http://libxenon.org//viewtopic.php?p=1315#p1315]Click me[/url][/quote]  
   
 Oh yeah, I forgot to write on that one. I tried that but the xell didn't boot.  
   
 Maybe I didnt build it right.   
 Question: If I erase the nand, and then just write the xell file, will it work?

## 2011-12-21 18:15:02, posted by: tuxuser

nope, it wont work if you just write the xell binary. you need to build a new image with it.

## 2011-12-22 10:18:33, posted by: greator

I wonder if the original nand is the cause of the xenon.elf not executing...

## 2011-12-22 11:23:47, posted by: tuxuser

@greator: nope, that cant be the reason for not-launchin ELFs

## 2012-01-15 01:14:22, posted by: Ethereal

XeLL-Rev: *XeLL\_Reloaded-testing-git01012012*  
 Console Type: *Retail*  
 Console Revision: *Jasper 16MB*  
 Hack-Version: *RGH*  
 Boot-Method: *XeLL-Launch*  
 Videocable: *HDMI.*  
 Error-Description:   
 *Exception vector! (0x700)  
 pir=0000000000000000 dar=0000000080800000  
 sr0=00000000800164f8 sr1=1000000002883030 lr=00000000800160c0  
 (other rows follow from 00 to 07)  
 STACK DUMP: *0x800164f8 --> 0x800160c0 --> 0x800023b8 --> 0x8000a7f4*  
   
 Hope this helps.

## 2012-01-15 02:02:19, posted by: Ethereal

Well, seems I found out why it was keeping to end up on Red Screen with Exception Vector.  
   
 The error was (and is) caused by the Kinect sensor connected to the Xbox 360  
   
 Once disconnected, Xell-testing boots with no issues.  
   
 Tried Mupen64 with no problem.  
   
 Ced2911's Pcsxr-xenon 0.5.1 for some reason does not start. Xell executes the .elf, I got black screen for a second and then Xell hangs. Last line of Xell is "Device tree prepared".  
   
 Hope this helps.

## 2012-01-20 20:55:47, posted by: mojobojo

XeLL-Rev: XeLL\_Reloaded-testing-git17012012  
 Console Type: Retail  
 Console Revision: Jasper 512  
 Hack-Version: JTAG  
 Boot-Method: XeLL-Launch  
 Videocable: HMDI  
 Error-Description: No video output when set to mode 6 (VIDEO\_MODE\_VGA\_1360x768) in kboot.conf when boot menu loads. When in boot menu unable to get controller (wireless) or keyboard input to switch through boot menu entries.

## 2012-01-21 17:23:07, posted by: tuxuser

[quote="mojobojo"] Videocable: HMDI  
 Error-Description: No video output when set to mode 6 (VIDEO\_MODE\_VGA\_1360x768) in kboot.conf when boot menu loads. [/quote] So you have the xbox connected via HDMI, you are changing the resolution via kboot.conf to VGA and get no video? wait, what.....  
 [quote] When in boot menu unable to get controller (wireless) or keyboard input to switch through boot menu entries. [/quote] Maybe try the attached build for controller input, should work then. If it still doesnt, try to resync your controller while in xell.  
   
 btw, allowed buttons via controller: DPAD-UP, DPAD-DOWN, A to confirm, B to cancel  
   
 Also, you can try navigate with usb keyboard as long as you want - its not implemented...  
   
 You can navigate via: IR Remote, Xbox360 Controller and UART (Serial Console).

### Attachments

[m0j0_210112.tar.gz](m0j0_210112.tar.gz)

## 2012-01-22 00:27:42, posted by: mojobojo

[quote="tuxuser"]  
 [quote="mojobojo"]  
 Videocable: HMDI  
 Error-Description: No video output when set to mode 6 (VIDEO\_MODE\_VGA\_1360x768) in kboot.conf when boot menu loads.  
 [/quote]  
   
 So you have the xbox connected via HDMI, you are changing the resolution via kboot.conf to VGA and get no video? wait, what.....  
 [/quote]  
   
 Haha woops, I didn't look that over very well. I was thinking about my native screen resolution instead of what cable I had connected. Dumb mistake on my part.   
   
 I was not sure after I started the boot menu if I may have needed the keyboard so I tried it as well. I did not see anything about the keyboard in the information, but I figured it would not hurt to try just in case it was in there.  
   
 Thanks for the build, I will test it in a moment.

## 2012-02-14 21:08:21, posted by: Haze666

XeLL-Rev: XeLL\_Reloaded-testing-git25012012-RC2\_fix1  
 Console Type: retail  
 Console Revision: Jasper 16mb  
 Hack-Version: Reset Glitch Hack  
 Boot-Method: Native  
 Videocable: HDMI  
 Error-Description: Xell loads fine, but whenever i try to load an elf file, or a linux distro i get a green tint over the screen, i have tried VGA and it resolves the issue, but i would prefer to use HDMI so i can have sound through the monitor. Also the HDMI cable works fine playing games and homebrew from dash.  
 Additional Information: I have tried multiple versions of Xell Reloaded, but since this was the most up to date version at the time of posting, i loaded it using XellLaunch then used the updxell.bin feature to update the native version of xell, because it wouldn't load linux in spite of it being outdated, I didn't see anything else about my issue on Google this bug thread, also not sure if it might be my setup.  
 I'm using a gold plated monster hdmi cable "lifetime warranty ftw" hooking directly between my Xbox360 and my Asus 23.6in LED Monitor.  
   
 I'll be sure to update if i run into any more issues, I'm going to try out the other new features.

## 2012-02-15 21:08:40, posted by: tuxuser

[quote="Haze666"]  
 XeLL-Rev: XeLL\_Reloaded-testing-git25012012-RC2\_fix1  
 Console Type: retail  
 Console Revision: Jasper 16mb  
 Hack-Version: Reset Glitch Hack  
 Boot-Method: Native  
 Videocable: HDMI  
 Error-Description: Xell loads fine, but whenever i try to load an elf file, or a linux distro i get a green tint over the screen, i have tried VGA and it resolves the issue, but i would prefer to use HDMI so i can have sound through the monitor.  
 [/quote]  
   
 Thx for the report.  
 Just got another report today from a guy who has a pink tinted screen with XeLL & Linux. Can't imagine what's causing that currently :( Sorry

## 2012-02-16 06:52:35, posted by: Haze666

[quote="tuxuser"]  
 Thx for the report.  
 Just got another report today from a guy who has a pink tinted screen with XeLL & Linux. Can't imagine what's causing that currently :( Sorry  
 [/quote]  
   
 Is there any way that I can give you more information? Maybe a debug mode in Xell?  
 I thought I read something about a serial adapter, to output some codes pertaining to Xell in the original post.

## 2012-03-18 22:51:21, posted by: kruzer

[color=black]Hello:  
   
 Using XeLL\_Reloaded-2stages-v0.991 to use the   
 mupen64-360 v0.96 beta and pcsxr-xenon 0.62 emus  
   
 Looking at the quick scrolling xell data, I gathered the following codes using the below controllers:  
 1) Official Microsoft Wired Controller [White] by Microsoft Vendor: 045E Prod:028E   
 2) Xbox 360 Pad EX 2 with Turbo - Black by Hori Vendor: 1BAD Prod:F501   
   
 However, when I do get to the emus, the controller light around the guide goes off and it is like nothing is connected because you're unable to do anything.   
 Appreciate the hard work and excellent results of all the devs. Hopefully this can be fixed. Thanks for your time.[/color]

## 2013-02-04 10:47:31, posted by: professor_jonny

XeLL-Rev: XeLL-Reloaded 2f  
 Console Type: Retail  
 Console Revision: trinity  
 Hack-Version: glitch  
 Boot-Method: eject button and xell loader  
 Videocable: HDMI  
 Error-Description: get sata no ata init with specific hdd (seagate momentus 5200.2 ST96812As firmware 3.14)  
   
 drive works perfectly within metro dash and from my pc other drives i have tried with this console work/pick up in this console from with in xell so i expect there to be a compatibility issue with this specific drive and xell.  
   
 the drive originally came from a ylod faulty ps3 console.  
   
 is there a way to dump the log file to ftp or http as i dont have a ttl serial cable?  
   
 i also get several seconds of dark screeen on boot of xell after it flashes up xell logo then comes back after blank period (im guessing this is normal)for the time being.