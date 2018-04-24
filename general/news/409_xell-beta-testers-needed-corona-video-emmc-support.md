# XeLL Beta Testers needed - Corona Video / eMMC support

## 2013-08-10 07:44:04, posted by: tuxuser

Hey guys,   
   
 yeah, it has been pretty quiet here lately..   
 However, we are looking for Testers now to try out a new XeLL build with Corona video support and eMMC (reading-)support.   
   
 The following has to be tested: [quote] * Video output on Corona with various videocables  
 * All web interface functions   
 * UpdXell on non-eMMC consoles  
 * Updflash on non-eMMC consoles  
 * Launching of ELF files [/quote]   
   
 Just write me a PM if you are interested in participating. Thx :)   
   
 greetz  
 tux

## 2013-08-29 02:31:14, posted by: XeXGolden

Wish I had a corona >:( stupid falcon :-\

## 2013-08-31 13:25:29, posted by: Bizzy211

Are beta testers still needed?

## 2013-09-01 10:21:00, posted by: professor_jonny

I could not get updxell to work when booting from xell launch with the new xell-ggggg binary it would not find the update on the internal hdd (xtaf) or usb (fatx).  
   
 But I can confirm I can not get it to boot at all on my v2 mmc with the new binary (0.993) in flash only from xell launch with component hd and component ycbcr.  
   
 It boots and crashes with component hd and component ycbcr when cold booting.  
   
 on a trinity console it now fails to boot mplayer and crashes on the title screen with the new build but i guess it just need to be recompiled with the new video drivers and tool chain ?

## 2013-09-01 14:40:03, posted by: medaved

[quote="professor\_jonny"]  
 on a trinity console it now fails to boot mplayer and crashes on the title screen with the new build but i guess it just need to be recompiled with the new video drivers and tool chain ?  
 [/quote]  
 on corona v2 too...

## 2013-09-05 21:43:31, posted by: Swizzy

[quote="professor\_jonny"]  
 I could not get updxell to work when booting from xell launch with the new xell-ggggg binary it would not find the update on the internal hdd (xtaf) or usb (fatx).  
   
 But I can confirm I can not get it to boot at all on my v2 mmc with the new binary (0.993) in flash only from xell launch with component hd and component ycbcr.  
   
 It boots and crashes with component hd and component ycbcr when cold booting.  
 [/quote]  
   
 It doesn't read fatx on external, it reads FAT16/FAT32 and EXT from external... XTAF might be bugged for internal HDD, i need to look into it... v2 corona's shouldn't ever try to update XeLL or the entire thing (it doesn't have MMC write support!)  
   
 Can you explain more what you mean with "boots and crashes"? do you get a red screen? if so... could you PLEASE post a picture or just simply the stackdump from it... this is very important as it helps find the cause of the error, i've had some reports of random crashes in the Xenos init (which shouldn't even be possible where the stackdump indicates mind you!)

## 2013-09-08 01:34:50, posted by: professor_jonny

Sorry I was meaning to say fat32 on usb, but you have explaned it xell does not have mmc write support it was just skipping the update.  
   
 But I can confirm I can not get it to boot at all on my v2 mmc with the new binary (0.993) with component hd and component ycbcr cables.  
   
 it just stops glitching no red screen with a stack dump just like it did with the old xell version.   
   
   
 But I can get it to load up xell using xell launch with the same cables with the binary dropped in the xell directory no problems.  
   
 i used jrunner to create my nand and the xell binary in xebuild is correct.

## 2013-09-08 10:05:06, posted by: Swizzy

[quote="professor\_jonny"]  
 it just stops glitching no red screen with a stack dump just like it did with the old xell version.   
 [/quote]  
   
 Do you have UART connected? if so; what is the stack dump you get?

## 2013-09-08 12:41:25, posted by: professor_jonny

ill see if i can find a nokia data cable and jack up a reader but at the moment nothing. im going to try some other cables as it works with every thing else.  
   
 the cables have an auto sencing electronic circuit and sence input and switch from the different console plugs and this may be a problem ?  
 but the console works correctly from retail.

## 2013-09-08 16:32:02, posted by: Swizzy

[quote="professor\_jonny"]  
 ill see if i can find a nokia data cable and jack up a reader but at the moment nothing. im going to try some other cables as it works with every thing else.  
   
 the cables have an auto sencing electronic circuit and sence input and switch from the different console plugs and this may be a problem ?  
 but the console works correctly from retail.  
 [/quote]  
   
 What happens if you grab the xell-2f.bin and put it next to XellLaunch from the 3.08 DL pack (don't rename it)? does that start? if so; you are most likely NOT using 0.993 even tho you think you do...  
   
 I don't know if it'll cause a problem, all i know is that my Squirt slaveboard(s) work perfectly fine, and so does a CK3i

## 2013-09-09 13:50:36, posted by: professor_jonny

doing that it will boot from hdmi but not the component hd cables.  
   
 im starting to think the cables are at fault in some way?

## 2013-09-09 15:44:45, posted by: Swizzy

[quote="professor\_jonny"]  
 doing that it will boot from hdmi but not the component hd cables.  
   
 im starting to think the cables are at fault in some way?  
 [/quote]  
   
 It's possible yes, could you do me a favor and test it with component in the dash, and if it works there... start it up and grab the startup log using http://*ip*/LOG then post it somewhere like www.pastebin.com (it's going to be quite alot of text) the best is if you can start it using xellLaunch as that'll dump the ana from your console aswell (which the dashboard has set) preferebly you should set the dashboard to 720p before you do so tho as that's the default mode used...

## 2013-09-09 19:52:44, posted by: peshkohacka

Is XTAF support even tested with LibXenon? I saw there was a unix port of xtaf, but Xell still doesn't understand the Internal HDD is XTAF formatted. Also is DMA error with missing DVD driver a known bug?

## 2013-09-09 23:24:44, posted by: siz

Xtaf is working for libxenon (there are some functions not implemented, write/mkdir etc., but read, opendir works). You can play videos on xmplayer from internal hdd.

## 2013-09-10 07:12:59, posted by: Swizzy

[quote="peshkohacka"]  
 Is XTAF support even tested with LibXenon? I saw there was a unix port of xtaf, but Xell still doesn't understand the Internal HDD is XTAF formatted. Also is DMA error with missing DVD driver a known bug?  
 [/quote]  
   
 DMA Error with missing DVD driver? what do you mean? if the drive is not connected you getting an error? that's like expected as it tries to communicate with hardware that isn't around... as long as it doesn't crash i don't consider it a bug...  
   
 About XTAF... it was tested before, i guess it's not been properly tested lately tho, and i think things have changed since last proper test... however, like siz said it works to read videos from it...

## 2013-09-11 01:37:06, posted by: peshkohacka

I have a disconnected DVD drive (i.e. the drive is not connected to the motherboard) and Xell spills hundreds of "DMA error" lines. I think supressing this lines is best, or at least one line status like "DVD Drive not detected".

## 2013-09-11 07:30:47, posted by: Swizzy

[quote="peshkohacka"]  
 I have a disconnected DVD drive (i.e. the drive is not connected to the motherboard) and Xell spills hundreds of "DMA error" lines. I think supressing this lines is best, or at least one line status like "DVD Drive not detected".  
 [/quote]  
   
 What motherboard do you have?

## 2013-09-12 22:46:36, posted by: peshkohacka

[quote="Swizzy"]  
 What motherboard do you have?  
 [/quote]  
   
 Trinity. Although my console was without drive for a few years and yet this is the first time i see Xell complaining about DMA errors.  
   
 btw i also bridged the tray open/closed, so it always returns "Tray closed" as a status (prevent blinking LED).

## 2013-09-12 22:54:44, posted by: Swizzy

[quote="peshkohacka"]  
 [quote="Swizzy"]  
 What motherboard do you have?  
 [/quote]  
   
 Trinity. Although my console was without drive for a few years and yet this is the first time i see Xell complaining about DMA errors.  
   
 btw i also bridged the tray open/closed, so it always returns "Tray closed" as a status (prevent blinking LED).  
 [/quote]  
   
 That's likely the reason for the error, altought i don't know how to fix that since i don't have a console with that type of a mod... why not just disable the blinking in the software instead? ;)  
   
 I'll try to find what changed causing this issue tho... not that i have any way of actually testing it (i don't really want to mess with that shit as i do have my DVD drives in place...)

## 2013-09-14 01:18:09, posted by: peshkohacka

This is part of the error log:  
 [quote] * sata dvd init  
 ATAPI inquiry failed  
 no ata device connected.  
 ATA DMA read error  
 ...[/quote] The thing is that 992 never had any problems with my drive status being bridged.

## 2013-09-14 01:28:37, posted by: Swizzy

[quote="peshkohacka"] This is part of the error log:  
 [quote] * sata dvd init  
 ATAPI inquiry failed  
 no ata device connected.  
 ATA DMA read error  
 ...[/quote] The thing is that 992 never had any problems with my drive status being bridged. [/quote] 0.992 is the same code for that as 0.993... you must be talking about 0.991 or something... idk...

## 2013-09-14 09:55:30, posted by: professor_jonny

[quote="Swizzy"]  
 It's possible yes, could you do me a favor and test it with component in the dash, and if it works there... start it up and grab the startup log using http://*ip*/LOG then post it somewhere like www.pastebin.com (it's going to be quite alot of text) the best is if you can start it using xellLaunch as that'll dump the ana from your console aswell (which the dashboard has set) preferebly you should set the dashboard to 720p before you do so tho as that's the default mode used...  
 [/quote]  
   
 Im not to sure how to obtain a log do i set debugging in dash launch how does that work in xell?  
 dont i have to get xell to boot and init ETH0 on startup it does not get that far to get a log and we have no write access to the internal hdd under xtaf ?.  
   
 but with another set of cables it boots up im guessing the auto switching circuit in the cables does not like the sync signals form under xell?  
   
 on a side note I have modified an initrd and dumped it on the internal xtaf formatted hdd to boot a linux distro and I cant get it to load the kboot.conf off sda: it wont find it i just get an endless loop of searching.  
   
 I'm guessing there is problems accessing the internal hdd or ?

## 2013-09-15 01:10:13, posted by: Swizzy

[quote="professor\_jonny"]  
 [quote="Swizzy"]  
 It's possible yes, could you do me a favor and test it with component in the dash, and if it works there... start it up and grab the startup log using http://*ip*/LOG then post it somewhere like www.pastebin.com (it's going to be quite alot of text) the best is if you can start it using xellLaunch as that'll dump the ana from your console aswell (which the dashboard has set) preferebly you should set the dashboard to 720p before you do so tho as that's the default mode used...  
 [/quote]  
   
 Im not to sure how to obtain a log do i set debugging in dash launch how does that work in xell?  
 dont i have to get xell to boot and init ETH0 on startup it does not get that far to get a log and we have no write access to the internal hdd under xtaf ?.  
   
 but with another set of cables it boots up im guessing the auto switching circuit in the cables does not like the sync signals form under xell?  
   
 on a side note I have modified an initrd and dumped it on the internal xtaf formatted hdd to boot a linux distro and I cant get it to load the kboot.conf off sda: it wont find it i just get an endless loop of searching.  
   
 I'm guessing there is problems accessing the internal hdd or ?  
 [/quote]  
   
 That bug is known and i'm working on fixing it, probably an error in the xtaflib

## 2013-09-15 08:31:18, posted by: professor_jonny

I did notice that looking at the file system from xmplayer and from within the retail side is that there were directorys not listed from the mplayer browser that were in fact on the file system.  
   
 I tried to figure out why it was not booting and browsed for my initrd from within xmplayer and the folder where I stored my kernel etc did not show from xmplayer but did from under the retail side so possibly there is some other issuies?.