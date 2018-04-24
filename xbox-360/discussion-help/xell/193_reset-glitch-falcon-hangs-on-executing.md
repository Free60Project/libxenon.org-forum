# Reset Glitch Falcon Hangs on Executing

## 2011-10-09 20:06:11, posted by: Matando

Not matter what .elf file I try, whether I've compiled it or prebuilt, it doesn't always launch with xell in the reset glitch hack.   
   
 I've tried gligli's port of mupen64 for the 360 and have mixed success. It's booted before, but it usually doesn't.  
   
 Also tried updating the xell-gggggg.bin as suggested by Cancerous1 here: [url=http://libxenon.org/http://libxenon.org//viewtopic.php?t=9]http://libxenon.org/http://libxenon.org//viewtopic.php?t=9[/url], but no luck.  
   
 All it usually does is get to this: [code]* *Trying uda:/xenon.elf... * uda:/xenon.elf found, loading <insert filesize here>... * Executing... [/code] And then it hangs at that spot.  
   
 I thought because this was a glitch, that xell wouldn't always boot, is that suppossed to apply to our *.elf files too?

## 2011-10-09 20:18:18, posted by: Juggahaxor

If you had UART hooked up it would be much easier to diagnose the problem. I have found that if i get problems executing and I know I have all the resource files etc... in place I unplug the power and video from the console and reset my USB drive as well. That usually takes care of it for me. That's on my Slim and Falcon.

## 2011-10-09 20:58:26, posted by: Matando

I'm working on getting uart hooked up, but was hoping that in the meantime I'd be able to find some help here, lol... I'll try what you said, thanks

## 2011-10-09 21:35:13, posted by: PDJ

I have the same on my Zephyr.  
   
 What ever I try it hangs on "Executing..."

## 2011-10-11 15:16:39, posted by: saso333

1st thanx for all the work .  
 the only .elf i got to run is N64 Emu......4now :)

## 2011-10-13 15:59:59, posted by: Matando

Problem solved. I wasn't paying attention and copied over xenon.elf instead of xenon.elf32 and then renaming it xenon.elf

## 2011-10-13 16:04:53, posted by: Juggahaxor

[quote="Matando"]  
 Problem solved. I wasn't paying attention and copied over xenon.elf instead of xenon.elf32 and then renaming it xenon.elf  
 [/quote]  
   
 Wow all this thread space for that :P I'm sure you will check that every single time from now on though. Glad it's working for you.

## 2011-12-20 16:57:03, posted by: greator

xenon.elf32? where did you get that?  
   
 I have the same exact problem, I tried rawflash v3 and v4 all failed.  
 I copy the xenon.elf file and all the other folder inside the zip file, also doesn't work.  
   
 Is this the problem with the ecc file?

## 2011-12-21 00:09:41, posted by: tuxuser

Try to use a recent XeLL build