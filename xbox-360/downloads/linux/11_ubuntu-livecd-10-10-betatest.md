# Ubuntu LiveCD 10.10 BETATEST

## 2011-02-21 20:21:51, posted by: tuxuser

UPDATE: Here is Beta 5!  
 Download: [url=http://file.libxenon.org/free60/linux/distro/ubuntu-10.10-xenon-beta5.zip]HERE[/url]  
   
 **[b][color=#FF0000]! Keep in mind: It's a BETA / WIP, dont upload it anywhere else and please report bugs/discuss it in this board only ![/color][/b]**  
   
 Known Bugs so far:  
 * [color=#FF0000]FIXED[/color] - It does not boot from XeLL-Launch cause of an IRQ bug. Fix is being worked on.  
 * It has random CPU spinlocks cause of a fail in XBOX360's CPU architecture (M$ is using a workaround to pass that). Fix is being worked on.  
 * No sound so far, being worked on aswell  
   
 Please use the following thread to report bugs: [url=http://libxenon.org/http://libxenon.org//viewtopic.php?t=0]CLICK[/url]

## 2011-02-27 02:46:34, posted by: tuxuser

Updated first post!

## 2011-03-14 17:39:19, posted by: val532

How to make our own distrib and vmlinux ?  
 And make a real instal of ubuntu on an HDD (usb or sata) ?

## 2011-03-17 19:39:05, posted by: Sonic-NKT

Just booted it from USB-Drive and its running awesome :)  
 Im typing this from the 360 right now.  
 Im amazed how fast everything is working (booted through xell-launch, old/slow USB-Drive)  
   
 btw, is someone working on an accelerated display driver for the 360?  
   
 EDIT:  
 Maybe i missed it, but could you include in a future release a VNC Viewer? that would be cool ;)  
 another nice addition in the future would be a youtube-viewer application, since we dont have a working flashplayer for that.

## 2011-03-20 22:23:13, posted by: tuxuser

If you like, you can test this new Kernel-Compile:  
   
 * noSMP (no hyperthreading - less spinlocking)  
 * Updated from 2.6.36.2 to 2.6.36.4  
 * Included WiFi Drivers for the Marvell Chipset (Original Xbox360 Wifi Adapters)  
   
 [url=http://libxenon.org/http://libxenon.org//viewtopic.php?p=454#p454]Download[/url]

## 2011-03-20 22:59:42, posted by: sbarrenechea

[quote=""tuxuser""]If you like, you can test this new Kernel-Compile:  
   
 * noSMP (no hyperthreading - less spinlocking)  
 * Updated from 2.6.36.2 to 2.6.36.4  
 * Included WiFi Drivers for the Marvell Chipset (Original Xbox360 Wifi Adapters)[/quote]  
   
 Testing!

## 2011-03-20 23:08:26, posted by: redxs

HI tuxuser   
   
 freezes have nothing to do with ethernet?  
   
 I disconnect the ethernet cable after loading the kernel  
   
 and it decreases freezes at logon and load the desktop.

## 2011-03-20 23:28:49, posted by: tuxuser

@redxs  
 Its possible that the network driver is still a little bit buggy, yeah..  
   
 But this noSMP Kernel should decrease spinlocking in general. Just try it out ;)

## 2011-03-21 16:51:08, posted by: Sonic-NKT

Tried the new kernel, booted up fine (from USB) but then i noticed that my USB Keyboard doesnt work anymore... Mouse works fine tho.   
 With the kernel included in Beta 5 the keyboard worked fine.

## 2011-03-21 17:51:58, posted by: tuxuser

[quote=""Sonic-NKT""]Tried the new kernel, booted up fine (from USB) but then i noticed that my USB Keyboard doesnt work anymore... Mouse works fine tho.   
 With the kernel included in Beta 5 the keyboard worked fine.[/quote]  
   
 Try the file again, I attached *test2, has KBD MOUSE and EVDEV modules included into the kernel.

## 2011-03-21 18:37:10, posted by: Sonic-NKT

test2 works fine...  
 but it feels a bit slower than the old kernel, but i think this is related to no hyperthreading and only 1 CPU :)

## 2011-03-21 19:19:52, posted by: tuxuser

Yep, that's what it makes slow.

## 2011-03-21 21:06:23, posted by: Sonic-NKT

Is it possible to create a virtual drive on USB or internal 360 HDD (if fatx is supported) to be able to save stuff in the live CD? Home directory would be very cool, to save stuff like Browser Favorits and like that.   
 I wonder if this works for packages too? i installed some stuff, but its limited to to ram and is gone after reboot.  
   
 Sorry, i have many ideas ;)   
 Awesome work!  
   
 PS: i know i can do a full linux install, but i currently have no spare sata 2,5 HDD, and something like this would be much better for new linux users. so the cant mess with internal or USB drives.

## 2011-03-21 22:40:34, posted by: tuxuser

@Sonic-NKT  
   
 Yep, of course its possible! It's called "persistence".. however it needs modification to the Kernel CMDLINE..and as we are unable to just pass the whole CMDLINE to a "naked" kernel YET.. a new Kernel Compile has to be made to accomplish such.  
   
 Here is a little info about the persistence:  
   
 [url=https://help.ubuntu.com/community/LiveCD/Persistence]https://help.ubuntu.com/community/LiveCD/Persistence[/url]  
   
 Go for the initramfs attached [url=http://libxenon.org/http://libxenon.org//viewtopic.php?p=453#p453]here[/url] and compile it into the kernel.  
 To do so you extract the archive and set the following correctly in the kernel's .config   
 (CMDLINE needs to be adjusted probably)  
 [code]* *CONFIG\_CMDLINE="boot=casper video=xenonfb console=tty0 ip=dhcp panic=60 nosmp maxcpus=1 persistence" CONFIG\_INITRAMFS\_SOURCE="/path/to/casper-initramfs" CONFIG\_INITRAMFS\_COMPRESSION\_LZMA=y [/code] The Kernel's Config which is used in the "Kernel Compile Tutorial" is also updated, the changes mentioned above need to be done still.  
   
 Greetz  
 tux

## 2011-03-22 10:21:37, posted by: Chrisoldinho

i've not tested the livecd yet, so excuse the obvious question...  
   
 can this be installed to the hdd and if so does it install to the internal hdd (sda2) or external usb.  
   
 thanks

## 2011-03-22 15:29:18, posted by: doughnut360

so like how to install on sda2 device or hdd is my question. haven't been into linux for quite sometime now, and I've just started on the 360 a year with 7.10. would it be possible using the 10.10 livecd on my usb?

## 2011-03-22 16:16:25, posted by: tuxuser

@doughnut360  
 [url=http://libxenon.org/viewtopic.php?p=76#p76]http://libxenon.org/viewtopic.php?p=76#p76[/url]

## 2011-03-23 06:49:41, posted by: doughnut360

@ tuxuser   
   
 thanks for the quick response sir, what I was trying to ask was if it's possible to do a full install of it on a spare hdd or possibly on the usb stick. I read of the possibility of persistence, from the post above, but how about on the hdd? so I can tweak more settings, probably change GUI environments (prefer xfce) and the likes. Thanks!

## 2011-03-23 11:30:35, posted by: Sonic-NKT

The LiveCD has an install Option on the Desktop, but i dont know if it works.

## 2011-03-23 17:26:01, posted by: doughnut360

somehow it doesnt. it just stops after the username.pc name selection.

## 2011-03-23 23:18:06, posted by: Sonic-NKT

Oh ok, i didnt try it myself, only started it once but quit cause i have no spare USB-HDD/SATA-HDD at the moment and didnt want to wipe my 360 formated disk

## 2011-03-24 08:19:48, posted by: Meluxe

Hi there,  
   
 i read somewere here that it is working on the install feature, but since it is still a beta there is no real reason to install it. Instead persistance was mentioned.  
   
 c ya

## 2011-05-10 19:06:38, posted by: sp1kez

does flash work with this on the xbox??  
   
 I want ubuntu on my xbox mainly so I can watch flash

## 2011-05-12 09:51:03, posted by: xxcrashxx

great job so far. seen some good vidz online. i seem to be having a problem though, dashlaunch 2.21, falcon retail jtag, component cables(hd on). using dashlaunch xell launch. followed the tuts on here. im getting it to go through the boot process, gets past xell, finishes up with the penguins up top then switches to the next "page" where it starts with the error 0 like 10 times or so. gets past that, but it hangs for 30 sec. after the CD-ROM mount point /cdrom/. next line looks like it says identifying.. [numbers], then a couple lines later it says "please provide a name for this Disc, suck as 'Debian 5.0.3 Disk 1': and just sits there. am i doing something wrong here??

## 2011-05-12 15:38:16, posted by: siontx

For everyone that want to Download and share the LiveCD   
   
 [url=http://linuxtracker.org/download.php?id=f502c840e26cbbad23350585b0efe58c5560c69d&f=Free60%20Ubuntu%2010.10%20LXDE%20LiveCD%20BETA%205.torrent]Ubuntu LiveCD Torrent[/url]

## 2011-05-12 18:47:37, posted by: tuxuser

[quote=""xxcrashxx""] im getting it to go through the boot process, gets past xell, finishes up with the penguins up top then switches to the next "page" where it starts with the error 0 like 10 times or so. gets past that, but it hangs for 30 sec. after the CD-ROM mount point /cdrom/. next line looks like it says identifying.. [numbers], then a couple lines later it says "please provide a name for this Disc, suck as 'Debian 5.0.3 Disk 1': and just sits there. am i doing something wrong here??[/quote]  
   
 the "error: stdin 0" lines are normal, the disc-name thing aswell. It seems like the crash is caused by the CPU spinlocking.  
 Did you try some more boots to see if it happens at the same place always?

## 2011-05-13 02:00:21, posted by: xxcrashxx

all i have tried so far is the one on the first page on this thread. I was trying this really late last night, kinda screwed up my day today at work trying this... but oh well.... LOL. i think i just might wanna wait till this is out of the beta stages, or even wait till its working more. any word if flash stuff will work on the 360 though?? I would love to be able to run streams and stuff on the 360. the ps3 kinda does it, but some streams for like WWE ppv's have a ad type thing that sometimes screws up on the ps3 and ends up blocking the whole screen.  
   
 also, does the linux version of XBMC or VLC work on this?? would be great if it was integrated in a future release, allowing you to play any video clip.

## 2011-09-01 18:14:23, posted by: lazarusjx

Thanks for providing us this Ubuntu liveCD for xbox 360, it works for me so far, I'm typing this from my xbox 360, connected to a 32" LCD tv through HDMI . I'm using a USB mouse and a PS/2 keyboard attached to a PS/2-USB converter. Internet is OK but no Flash so I can't watch youtube but it's OK, this is a beta anyway. I hope this liveCD can be refined more and be a LiveDVD :)  
   
 BTW, is it really normal that my XBOX360 has 2 orange lights lit while running the LiveCD? ???

## 2011-09-01 23:42:39, posted by: utar

@lazarusjx - Yes the various different color lights are normal.  
   
 @tux - Thanks for putting together this LiveCD. I still have a really old version of Debian running off the HDD of one of my 360s using the KK hack. This distribution is a vast improvement!

## 2011-09-27 02:04:22, posted by: djblade17

working on reset glitch? are any of the releases for linux?  
 cant find it in forums

## 2011-10-13 13:21:08, posted by: avomax

[quote="tuxuser"]  
 If you like, you can test this new Kernel-Compile:  
   
 * noSMP (no hyperthreading - less spinlocking)  
 * Updated from 2.6.36.2 to 2.6.36.4  
 * Included WiFi Drivers for the Marvell Chipset (Original Xbox360 Wifi Adapters)  
   
 [url=http://libxenon.org/http://libxenon.org//viewtopic.php?p=454#p454]Download[/url]  
 [/quote]  
   
 Thank you.

## 2011-10-13 20:31:28, posted by: iPSad

is it working on RGH?

## 2011-11-03 13:56:20, posted by: nikos5800

how many xbox 360 cpu core use this version of linux?

## 2011-12-22 09:03:43, posted by: redman21

hello I'm new but impossible to launch either linux or gentoo on my xbox360 console it always blocks for gentoo linux black screen and thank you for any information to operate

## 2012-01-21 19:34:23, posted by: roost

[quote="redman21"]  
 hello I'm new but impossible to launch either linux or gentoo on my xbox360 console it always blocks for gentoo linux black screen and thank you for any information to operate  
 [/quote]  
   
 try xelllaunch. that worked for me

## 2012-02-16 02:25:15, posted by: Haze666

seems to spinlockal on my Jasper16mb if i have the hard drive in, it's a 7200rpm wd 320gb.  
 also, the last time i tried to boot, it froze at something like "burning read-write image to fs" during the boot sequence.  
 not sure what that meant.  
 kind of wish that i could find some network manager, i have tried net config, but it says invalid santyx or something along those lines, so i have no way to set an ip because i don't have dhcp running on my current network.

## 2012-02-18 00:19:17, posted by: sema

My dear friends, I boot Ubuntu 10.10 from USB Stick on my JTAG-ed Xbox every time I need using Xell (Insert USB Stick with Ubuntu 10.10, Unplug power cable, press Power on buton for 5 to 10 secconds, plug power cable, press Eject for booting in Xell, and after a few minutes of wait I'm in Ubuntu......

## 2012-05-05 14:21:57, posted by: speed3r

[quote="tuxuser"]  
 If you like, you can test this new Kernel-Compile:  
   
 * noSMP (no hyperthreading - less spinlocking)  
 * Updated from 2.6.36.2 to 2.6.36.4  
 * Included WiFi Drivers for the Marvell Chipset (Original Xbox360 Wifi Adapters)  
   
 [url=http://libxenon.org/http://libxenon.org//viewtopic.php?p=454#p454]Download[/url]  
 [/quote]  
   
 Cant download the file?

## 2012-05-27 05:54:28, posted by: droptables

[quote="tuxuser"]  
 If you like, you can test this new Kernel-Compile:  
   
 * noSMP (no hyperthreading - less spinlocking)  
 * Updated from 2.6.36.2 to 2.6.36.4  
 * Included WiFi Drivers for the Marvell Chipset (Original Xbox360 Wifi Adapters)  
   
 [url=http://libxenon.org/http://libxenon.org//viewtopic.php?p=454#p454]Download[/url]  
 [/quote]  
 Link is dead

## 2012-08-05 14:04:30, posted by: nikos5800

This project its still alive?

## 2012-12-01 17:02:28, posted by: wolfarvak

I too am interested in this project or others like it :) Love homebrew on all consoles and what you can do

## 2013-04-03 15:24:55, posted by: jefinhorc3d

:)  
 hello guys! I am a Brazilian player who became interested in the distribution of linux you guys, I'm running it smoothly on my xbox 360 with with plate falcon. I have a personal question, I replaced the file folder filesystem.squashfs casper linux ububtu that you have posted here a squashfs distribution of linux ubuntu 12.4 for PowerPC. apparently she usually climbed by xell, only to show the graphics all she was checkered. vcs discontinued free60 linux? right now the scenario has increased rgh? someone from the forum (including tuxuser) could help me? :D

## 2014-01-11 12:18:35, posted by: u2020bulet

Anyone still working on this? Maybe a version with sound?

## 2015-01-04 15:27:55, posted by: <Unknown User>

Im also interested in that!

## 2016-01-09 16:43:21, posted by: <Unknown User>

since this livecd is working for me even from a usb like you showed here- http://libxenon.org/viewtopic.php?f=48&t=32 is there a way to just copy this ubuntu into the xbox hard drive instead of all the scripts that don't work? maybe it wil work and it's much easier...

## 2016-01-17 13:06:54, posted by: <Unknown User>

Is it possible to install this version into the hdd, booting from this livecd (without all the need for links that don't work etc.) with just a minimalistic script that just installs this version of ubuntu into the hdd, either by copying from the livecd as the source or using the link from which the livecd was downloaded from? thanks in advance.