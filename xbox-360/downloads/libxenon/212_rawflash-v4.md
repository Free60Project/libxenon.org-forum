# Rawflash v4

## 2011-10-21 20:48:33, posted by: tuxuser

A little tool that cOz made. Let's you flash full raw images (16 or 64MB) to your NAND. Started, as usual, via XeLL.  
 [quote]place "nandflash.bin" on the root of a usb device  
 start 2stage xell and shut off when prompted (replug power if you changed SMC)  
 - by default it checks blocks before writing, and will NOT overwrite or erase any block with ecc/other issues (perfect for *** images with auto remaps)  
   
 small change to libxenon was required to silence non-error messages  
   
 tested on falcon, trinity and jasper 256  
   
 v4: fix page offsets for bad block checks on big blocks (fixes problems when nandmu is present)  
 v3: re-re-refix bad block skipping so it skips it in both the dump and flash instead of just in the dump  
 v2: add big block support  
 v1: initial version[/quote]

### Attachments

[rawflash_v4.zip](rawflash_v4.zip)

## 2011-10-21 21:01:01, posted by: nitram

Thanks tux.

## 2011-10-22 09:57:50, posted by: spandaman

Sweet, thanks :)  
   
   
 Sent from my iPhone using Tapatalk

## 2011-10-22 15:17:47, posted by: mjet

hi!  
 I have a Slim Model (Trinity)  
 I used this tool, but i got following info:  
 ---------------------------------------------------  
 block 0xc1 seems bad, status 0x0000210  
 block 0x1bf seems bad, status 0x0000210  
 ---------------------------------------------------  
   
 After this, fans stayed very noises...dashboard is not loading, but xell loaded no problems.  
 Please, help me!   
 P.s. I dumped my original nand few times and all was very well - nandpro not indicated any bads or others errors.  
 Also I write this original nand in my console via NandPro - works great! No errors...

## 2011-10-24 16:44:57, posted by: chapas

Hi,  
 putted the .elf file on a Fat32 formatted USB pen, but xell didn't find it, so i tried a CD-RW and it started rawflash from CD, but then nothing happens and stay's stuck on screen like this:  
   
 [url=http://img838.imageshack.us/i/20111024080537.jpg/]![](http://img838.imageshack.us/img838/8624/20111024080537.th.jpg)[img]http://img838.imageshack.us/img838/8624/20111024080537.th.jpg[/img][/url]  
   
 I'm with on a SLIM 4GB, any suggestion?  
   
 Thanks in advance,  
 Chapas

## 2011-10-26 00:29:18, posted by: rikimaer

[quote="chapas"]  
 Hi,  
 putted the .elf file on a Fat32 formatted USB pen, but xell didn't find it, so i tried a CD-RW and it started rawflash from CD, but then nothing happens and stay's stuck on screen like this:  
   
 [url=http://img838.imageshack.us/i/20111024080537.jpg/]![](http://img838.imageshack.us/img838/8624/20111024080537.th.jpg)[img]http://img838.imageshack.us/img838/8624/20111024080537.th.jpg[/img][/url]  
   
 I'm with on a SLIM 4GB, any suggestion?  
   
 Thanks in advance,  
 Chapas  
 [/quote]  
   
 Same oribken gere aso with Slim mobo , but on Falcon mobo worked like a charm!!

## 2011-10-26 13:30:17, posted by: Razkar

V3 is out :)  
 First port updated ;)

## 2011-11-01 04:01:11, posted by: glaze83

There's an issue with samsung nands it would appear -- it fails on everyblock.  
   
 Tried with two 512 jaspers.  
   
 Was successful on a 512 jasper with a hynix nand

## 2011-11-04 04:57:41, posted by: k0mpresd

[quote="glaze83"]  
 There's an issue with samsung nands it would appear -- it fails on everyblock.  
   
 Tried with two 512 jaspers.  
   
 Was successful on a 512 jasper with a hynix nand  
 [/quote]  
   
 i had the opposite problem. i went to flash a ggbuild image on to a hynix big block and the program said error on every block. reflashing now with nandpro.  
 edit: tried again on the same console and it flashed ok. must just be a bug.

## 2011-11-17 23:49:12, posted by: Valerie

I am also getting the black screen on a program that I'm working on. I'm thinking that there must be a bug somewhere, but I have not been able to locate it. Has anyone been able to locate the issue? At first I thought that maybe it was just an issue with my xbox, and actually came really close to running down to [url=http://www.hhgregg.com]hhgregg[/url] to see if I could pick up a new one. Fortunately I didn't do that since it seems that I am not the only one having this issue. I will appreciate any help I can get with this, thank you.

## 2011-12-12 15:39:36, posted by: tuxuser

Updated first post with rawflash v4, eliminates the bug with big block consoles (Internal NAND MemoryUnit)

## 2011-12-12 16:14:29, posted by: c01eman.360

Y Thanks

## 2011-12-13 00:21:01, posted by: turnerl

Amazing tux !!! thanks my current JTAG has bad blocks remapped was a biatch injecting the bad blocks back into flash every update, now being able to flash diectly to my badblock nand and have it not touch the bad blocks is a dream come true !   
   
 Thanks Again !

## 2011-12-13 00:41:40, posted by: turnerl

sorry tux or anyone quick question I'm running an original JTAG with normal xell reloaded, can I use this or does it only run on that Xell '2Stages'?   
   
 Thanks in advance

## 2011-12-13 00:50:01, posted by: tuxuser

runs from every XeLL, no idea why xbox-scene is spreading such false info...

## 2011-12-13 01:23:15, posted by: barnhilltrckn

[quote="tuxuser"]  
 runs from every XeLL, no idea why xbox-scene is spreading such false info...  
 [/quote]  
   
 No idea either. Now i had problems with ver. 2 but since 3 came out ive had zero problems even with bb nands. Sounds to me like user error on there part. :-\

## 2011-12-13 09:42:12, posted by: cjackson

[quote="tuxuser"]  
 runs from every XeLL, no idea why xbox-scene is spreading such false info...  
 [/quote]probably b/c in readme it says stage2 xell  
   
 anyway if run on all xell after i apply RGH to myconsole can i use this to write NAND to my console without error or should i solder my SPi flasher again to write.  
 since i ve two xboxes i didn't keep flasher on MB but i could solder pins for just easy plugin. If rawflash do my job, i won't need to open box again and solder

## 2011-12-13 23:04:27, posted by: barnhilltrckn

[quote="cjackson"]  
 [quote="tuxuser"]  
 runs from every XeLL, no idea why xbox-scene is spreading such false info...  
 [/quote]probably b/c in readme it says stage2 xell  
   
 anyway if run on all xell after i apply RGH to myconsole can i use this to write NAND to my console without error or should i solder my SPi flasher again to write.  
 since i ve two xboxes i didn't keep flasher on MB but i could solder pins for just easy plugin. If rawflash do my job, i won't need to open box again and solder  
 [/quote]  
   
 Yes it should work just fine but im sure there are some unseen errors that could occur although doubtful.

## 2011-12-13 23:07:22, posted by: cjackson

at least i try and give feedback

## 2011-12-19 03:15:43, posted by: g33k

thx for this nice and usefull tool 8)  
   
 but why are ECC-errors treated like bad blocks? is there any reason i cant see?

## 2011-12-24 10:18:05, posted by: lprot

Thanks cOz. Properly works on Jasper 512Mbyte with Samsung K9F4G08U0B NAND.

## 2011-12-27 11:20:56, posted by: doolcan

How long is this supposed to take. I have been stuck on the same black screen for 15 minutes. I really don't want to turn it off and have a brick. 16mb jasper 

### Attachments

[IMG_20111227_051949.jpg](IMG_20111227_051949.jpg)

## 2011-12-27 11:24:19, posted by: sk1080

I can guess those last 4 lines are "Initializing Wireless Controller..."  
 That indicates it didn't get as far as actually flashing, so you can probably turn it off  
 lemme guess, no nand cable?  
   
 EDIT: crappy internet connection decided to download the image, yea, turn it off

## 2011-12-27 11:27:49, posted by: doolcan

nah I have a nandx but every time i even look at this jasper wrong i have to reflow my stby clock joint. hate opening it

## 2011-12-27 11:30:28, posted by: sk1080

it looks like it didn't recognize your flash drive once rawflash opened  
 you might want to try again

## 2011-12-27 11:42:42, posted by: doolcan

Thanks for the help. I reformatted the thumbstick and used the rear usb port this time. Worked like a charm.

## 2011-12-27 21:04:02, posted by: barnhilltrckn

[quote="doolcan"]  
 Thanks for the help. I reformatted the thumbstick and used the rear usb port this time. Worked like a charm.  
 [/quote]  
   
 See thats what i men right there. Alot of people claim they have problems with this program but it can ussually be solved by doing things you did. Change usb stick, format it, different usb port, ect, ect. This really is a great program to use and its so much easier to use if you dont have a setup to flash your nand without opening your 360.   
   
 I for one have had ZERO problems since v3 was released and ive used it on 16mb phats, BB phats, and slims many times. If only people would try things like you did other than trying it once without trying different methods and just assuming that its a problem with the program.

## 2012-03-23 09:55:24, posted by: bakterio

Hi  
   
 After flashing the last 360 multibuilder (.93) generated nand, i got this error code when initializing nand en xell:  
   
 !SFCX: Unknown error at address 00FC200: 00000220  
   
 And when trying to flah with rawfalsh v4 i got bad block errors from address 0x0384 and above  
   
 Is it recommended to use another rawflash version that not check this bad blocks and flash anyway?  
   
 Thanks and regards

## 2015-11-21 15:56:07, posted by: <Unknown User>

when i start xell at the end it says found:xeneon.elf file found......and after that the screen becomes blank and nothing happens but the xbox is still on...please help  
 tell me what to do to run raw flash v4...please :( :( :(