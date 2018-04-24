# Xilinx Lab Tools process not matching Tutorial

## 2011-10-20 17:52:12, posted by: radddogg

Hi,  
   
 Noob alert.  
   
 I'm working through the RGH but am stuck on Python-Crypto. The guide says to install using default settings and shows a graphic of a MSI type installer, however the download is for a .tar file which has no install files when extracted. The only thing close is a setup.py file, which when clicked flashes a dos window briefly.  
   
 Any ideas what I have missed?  
   
 Thanks!

## 2011-10-20 17:57:40, posted by: tuxuser

yes you downloaded the linux version by mistake. look at the bottom of the tutorial and catch the coreect URL there ;)

## 2011-10-20 18:16:07, posted by: radddogg

[quote="tuxuser"]  
 yes you downloaded the linux version by mistake. look at the bottom of the tutorial and catch the coreect URL there ;)  
 [/quote]Facepalm.....I spent over an hour last night trying to figure it out....  
   
 Next issue.  
   
 ![](http://img.photobucket.com/albums/v325/radddogg/DWINXPsystem32cmdexe-nandprousbw16image_00000000ecc.jpg)[img]http://img.photobucket.com/albums/v325/radddogg/DWINXPsystem32cmdexe-nandprousbw16image\_00000000ecc.jpg[/img]  
   
 Anyone seen this before? I can read fine but I get this when writing.  
   
 I'm using a USB SPI flasher I bought off xbox-experts. The same one as pictured here in my JTAG.  
   
 ![](http://img.photobucket.com/albums/v325/radddogg/IMG_20110913_221701.jpg)[img]http://img.photobucket.com/albums/v325/radddogg/IMG\_20110913\_221701.jpg[/img]

## 2011-10-20 19:11:44, posted by: tuxuser

revert to nandpro v2.0e and you are good to go

## 2011-10-20 20:14:01, posted by: radddogg

[quote="tuxuser"]  
 revert to nandpro v2.0e and you are good to go  
 [/quote]You are a legend - of course - "Requires new v3 .hex for arm". I suppose I could have flashed the PIC with the new .hex but 2.0e was much quicker.  
   
 Thanks!  
   
 I'll post back later with my next problem, lol :D  
   
 Cheers again.

## 2011-10-20 23:22:20, posted by: radddogg

As promised - I am back ::)  
   
 I plug my CPLD in via lpt with 3.3v and ground. Launch impact, the cable autodetects and asks if I want to assign config files. I say Yes, as per the guide. The guide says 'Assign New Configuration File' dialogue box should open with .jed, .isc or .bsd as the supported file types but I get a different box saying 'Do you have a BDSL or BIT file for this device?.   
   
 :-\  
   
 Help!?

## 2011-10-22 02:56:12, posted by: radddogg

Well I sorted it. I found another schematic for the programmer without all the diodes and resistors and it worked first time.  
   
 Got it all programmed and wired up and it gave me a 0022 RRoD error. I found this was a CB error caused by another omission from the tutorial. Zephyrs require an update to the SMC file.  
 [quote]- Use a donor stock Jasper 2.3 plaintext SMC and give it to build.py  
 First of all I want to thank GliGli for that beautiful genious hack. And for the second, I want to clear up the SMC difficulties for beginners.  
   
 To get right SMC file for building of zephyr, etc fat xells, do the following:  
 1. Download http://www.megaupload.com/?d=9O2ZCC9W (thanks go to oliagyok360 for that)  
 2. Load nand.bin file into 360 Flash Tool v0.97. Can be found here: http://dwl.xbox-scene.com/xbox360pc/nandtools/360\_Flash\_Tool\_v0.97.rar  
 3. Press Extract, check SMC, select folder and press OK.  
 4. You will get SMC folder with the file: SMC\_dec.bin  
   
 Use this file to build xell for fats like that:  
 c:\Python27>python common\imgbuild\build.py nand.bin SMC\_dec.bin common\cdxell\CDjasper common\xell\xell-gggggg.bin  
   
 PS: Don't forget to change build.py if you are building for fats too.  
 You need to change secret\_1BL = "" to secret\_1BL = "\xDD\x88\xAD\x0C\x9E\xD6\x69\xE7\xB5\x67\x94\xFB\x68\x56\x3E\xFA"[/quote] So now I can hear the fan speeds changing as it tries to glitch but it never actually boots into xell. It just stays on a black screen saying no input.......  
   
 ::)  
   
 I'm so close!!!!