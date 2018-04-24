# Boot the Ubuntu LiveCD via USB

## 2011-03-08 23:32:38, posted by: tuxuser

It's pretty easy to accomplish that.  
   
 1. Format a USB-Flash or HDD in FAT32.  
 2. Extract the ISO of the LiveCD with any compatible program.. or mount it as a loopdrive in linux  
 3. Copy the whole content to the Root of the USB Drive  
 4. Rename vmlinux to xenon.elf  
 5. Boot it with the XeLL of your choice  
 6. Enjoy a faster boot :)

## 2011-03-09 01:30:44, posted by: Razkar

Ah cool =)  
 No more disc burned for testing :p

## 2011-03-09 07:42:02, posted by: Meluxe

Good morning everybody!  
   
 Thanks for the instruction!  
   
 I am booting xell-reloaded and Ubuntu 10.10 BETATEST via Xell-Launch and without renaming vmlinux. Works too using a USB drive. Maybe not that fast. I am going to check that out soon.  
   
 Or are you talking about an unmodified Ubuntu LiveCD?

## 2011-03-09 08:19:55, posted by: tuxuser

Nope I am talking about the Xbox specific LiveCD of course.

## 2011-03-11 03:52:09, posted by: mojobojo

Add this right after the try\_boot\_fat for xenon.elf in xell if you are too lazy to rename the file every time.  
 [code]try\_boot\_fat("vmlinux");[/code]

## 2011-03-17 19:24:31, posted by: Sonic-NKT

Wow... just wow...  
 tried it with an old slow USB Stick and this thing booted up so much faster than any live cd/DVD before :)  
 it was like... wow whats that, screensaver? Xserver allready working? what im allready running a window-manager :D  
 your work is awesome guys!   
 cant wait to see this more improving (no crashes, sound)

## 2011-03-20 13:34:35, posted by: eminwargo

Ubuntu 10.10 on the stick is fantastic its very fast so i see on the dektop an install software...  
   
 could i install it on my hdd ?  
   
 and what is the largest screen screen resolution....  
   
 thank you

## 2011-03-31 18:51:31, posted by: Doerek

[quote=""eminwargo""]Ubuntu 10.10 on the stick is fantastic its very fast so i see on the dektop an install software...  
   
 could i install it on my hdd ?[/quote]  
   
 Good point...My Question is.  
 It is possible to install it on a USB-HDD?

## 2011-04-01 07:22:28, posted by: Meluxe

As far as i know that is only possible with that by now: [url]http://libxenon.org/viewtopic.php?f=11&t=2[/url]

## 2011-04-01 14:28:42, posted by: Doerek

Thx for your reply...i will stay tuned.  
   
 Are you guys gonna write tuts for the installation Process?

## 2011-04-25 11:41:33, posted by: radddogg

I can't get this to work at all.  
   
 Formatted usb drive to fat32  
 Extracted 10.10 to usb drive so I have casper folder and linux file which I rename to xenon.bin  
 Copied xellLaunch folder to usb drive  
 Copied xell-2f.bin file to xellLaunch folder on usb drive and renamed to xell.bin  
   
 I then run the default.xex and I get a black screen for 5 seconds before being returned to freestyle dash.  
   
 I've tried a usb stick and a usb hard drive and neither work.  
   
 Any ideas?

## 2011-04-25 19:23:01, posted by: tuxuser

Two Things are wrong:  
   
 1. Rename the vmlinux to xenon.elf, not xenon.bin  
 2. You need Dash Launch installed for the XeLL-Launch to work. Dash Launch 2.21 is the latest, use the XeLL-Launch included with it.  
   
 Greetz  
 tux

## 2011-04-26 13:36:16, posted by: radddogg

[quote=""tuxuser""]Two Things are wrong:  
   
 1. Rename the vmlinux to xenon.elf, not xenon.bin  
 2. You need Dash Launch installed for the XeLL-Launch to work. Dash Launch 2.21 is the latest, use the XeLL-Launch included with it.  
   
 Greetz  
 tux[/quote]Sorry thats a typo, it is xenon.elf.  
   
 I think I have dash launch installed already. I think version 2.20 but I'll check

## 2011-04-26 14:48:24, posted by: Meluxe

edit: don`t mind

## 2011-04-26 17:08:02, posted by: tuxuser

Its a matter of THE COMBINATION of dash launch + xell-launch.  
   
 THEY HAVE TO MATCH!

## 2011-04-26 22:01:11, posted by: radddogg

Ok so if I update to 2.21 that should fix it?

## 2011-04-26 22:25:49, posted by: tuxuser

Yes, update to DL 2.21 and use the matching XeLL-Launch which came with it.

## 2011-04-26 23:44:53, posted by: radddogg

Ok, so its getting further as in it reboots but there is no video output. The RoL is green, red and amber and the flash drive indicator is flashing away as if it is active but I get no video. I'm using a vga monitor.  
   
 Looking at the bug report in [url=http://libxenon.org/http://libxenon.org//viewtopic.php?t=7.msg140#msg140]this[/url] thread, there may be a problem with vga in xell-2f. What do you think?

## 2011-04-27 09:11:24, posted by: Meluxe

[quote=""tuxuser""]Its a matter of THE COMBINATION of dash launch + xell-launch.  
   
 THEY HAVE TO MATCH![/quote]  
   
   
 Good to know, thanks for that info tux! :roll:

## 2011-04-27 19:48:19, posted by: radddogg

Any ideas on the lack of A/V?

## 2011-04-28 01:44:52, posted by: radddogg

Ok, it sort of works on my component cable but not at all on my vga. When I say sort of works, it gets stuck at a part where it is trying to read the cd rom but it is of course on a usb stick.

## 2011-04-28 02:07:13, posted by: tuxuser

And the kernel is called "xenon.elf" and is located at the Root of the USB Stick?

## 2011-04-28 11:27:47, posted by: radddogg

[quote=""tuxuser""]And the kernel is called "xenon.elf" and is located at the Root of the USB Stick?[/quote]Yes, it is in the root of the usb, the squash file is in the casper folder and the only other thing on the usb stick is the xellLaunch folder.

## 2011-05-09 18:40:44, posted by: sp1kez

I am a bit confused, does this work on any LiveCD of ubuntu or only on the Xenon Ubuntu?  
   
 Also, are there any torrents for xenon ubuntu? the download from libxenon is so slow

## 2011-05-10 07:27:00, posted by: Meluxe

It has to be a modified xenon ubuntu

## 2011-12-08 21:03:21, posted by: zwierzakdc

I have problem.  
 I copy file from ubuntu livecd beta5. then run xell reloaded (press eject) and plug usb drive (fat32). Xell find file "vmlinux" and "xenon.elf" (trying bouth), then showing "executable..." and nothing else.

## 2011-12-23 01:31:47, posted by: Hostility

yep it does the same thing for me with everyone of the linux distros, it finds vmlinux   
 then it says executing... :(

## 2011-12-23 04:35:45, posted by: Cancerous1

can you try with the latest build of xell-reloaded posted here http://libxenon.org/http://libxenon.org//viewtopic.php?p=1315#p1315

## 2012-01-21 23:37:11, posted by: frknzdmr

i think we need video tutorials...

## 2012-01-22 00:16:03, posted by: frknzdmr

tes i tried 6 times   
 everything is right   
 i have a xellLaunch folder >>xell.bin and xelllaunch.xex  
 casper folder > filesystem.squashfs file  
 xenon.elf   
 usb stick fat 32 format   
 xbox 360 slim   
 ...???

## 2012-05-09 14:48:34, posted by: haww

Me too.Executing and nothing. Please help.Xell reloaded is latest.

## 2012-05-25 22:01:52, posted by: haww

Ok i‘m started with another elf.Can someone to put driver in this distro for wired x360 pad to use like a mouse.Or tell me some compatible pc controller?

## 2012-10-15 19:10:08, posted by: FreakAlhemist

[quote="haww"]  
 Ok i‘m started with another elf.Can someone to put driver in this distro for wired x360 pad to use like a mouse.Or tell me some compatible pc controller?  
 [/quote]  
 I use a wireless keyboard & mouse.  
 I also use the gentoo live cd beta 2 on both the usb and dvd drive and everything installed nicely. 

## 2014-09-11 12:24:08, posted by: <Unknown User>

i'm gonna try to do this but i'm noob at these stuff so it might be stupid to ask but is it somehow dangerous to do this like xbox might have problems like over heating or anything like that ?