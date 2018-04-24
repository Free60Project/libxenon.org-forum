# Couldnt locate xell binary in nand. Aborting!

## 2012-03-14 08:20:43, posted by: Xplorer4x4

I tried to update xell reloaded. I built xell using the git repository and everything built fine as far as I could tell. I grabbed the xell-gggggg.elf(since I have a Slim Trinity using the RGH) and renamed it to updxell.bin. I placed updxell.bin on my flash drive and booted in to Xell Reloaded but it kept giving me this error message over and over when it tried to find and elf to load:  
 [quote]!couldnt locate xell binary in nand. Aborting!  
 Trying dvd:/vmlinux...* update-xell binary found @ uda:updxell.bin ! Looking for xell binary in nand now.[/quote]

## 2012-03-14 10:22:57, posted by: tuxuser

Reading README helps sometimes...

## 2012-03-14 11:06:28, posted by: Xplorer4x4

[quote="tuxuser"] Reading README helps sometimes... [/quote] I have read it many times, guess I should have referenced it again. Thanks.  
   
 I am confused though: [quote]--Either your XeLL in NAND is too old or it's not a XeLL Reloaded binary [/quote] My build is from September 2011 and says XeLL Reloaded when I boot, is this really to old of a build?? When was the cut off? I don't suppose there is anyway to obtain a nand dump from my already RGHed console is there?

## 2012-03-14 12:21:12, posted by: tuxuser

03-09-2011 build? yeah, thats too old.. it doesnt include the new xell offsets which are used by recent nandimages.

## 2012-03-14 12:43:17, posted by: Xplorer4x4

So then the only option is to buy a Xecuter NAND-X & JTAG Connection Kit or is there a cheaper USB nand dump utility out there? I guess that even if there was a way to dump the nand as is with out a tool, a tool like that would be needed to reflash the nand? My chip is a Team-Xecuter Coolrunner.  
   
 Thanks for all the help tuxuser!

## 2012-03-14 14:29:09, posted by: tuxuser

Why make it so hard? Dump the Nand via Xell's Webinterface - build a new image - name the new image updflash.bin and flash it via XeLL.. or am I missing something?  
   
 Of course you dont have a recovery option then if something goes wrong..

## 2012-03-14 15:32:08, posted by: Xplorer4x4

[quote="tuxuser"] Why make it so hard? [/quote] That's exactly what I was asking! I googled to see if there was a way to dump the flash via xell but google didn't give any relevant results. I guess the only way to have a safe recovery option is buying a kit like the one mentioned? If the flash fails, am I still able to recover using a serial adapter?  
   
 I been trying to figure out how to build a the image. [url=http://free60.org/SMC\_Hack#Extracting\_SMC.2FCB.2FCD\_from\_a\_hacked\_image]This[/url] was all I could find. It looks a bit out dated though. Is there a better tutorial to follow?  
   
 Also I was confused by this particular sentence: [quote]If you are using XeLL-compile after 31. August 09 you could use the USB-Update feauture. [/quote] Does this not apply to XeLL Reloaded?  
   
 Thanks again Tux, I am truly grateful for your help, and I am anxious to learn!

## 2012-03-14 20:36:32, posted by: tuxuser

[quote="Xplorer4x4"] I guess the only way to have a safe recovery option is buying a kit like the one mentioned? [/quote] Yep, a USB SPI Programmer is needed for that.  
 [quote] If the flash fails, am I still able to recover using a serial adapter? [/quote] NO  
 [quote] I been trying to figure out how to build a the image. [url=http://free60.org/SMC\_Hack#Extracting\_SMC.2FCB.2FCD\_from\_a\_hacked\_image]This[/url] was all I could find. It looks a bit out dated though. Is there a better tutorial to follow? [/quote] It's still up-to-date for JTAG-consoles. http://free60.org/SMC\_Hack#From\_scratch or http://free60.org/SMC\_Hack#Updating\_a\_hacked\_image  
 [quote] [quote]If you are using XeLL-compile after 31. August 09 you could use the USB-Update feauture. [/quote] Does this not apply to XeLL Reloaded? [/quote] The date 31. August 2009 is only for original XeLL in XeLL-only images (not the *not to be discussed*-images)

## 2012-03-14 21:47:03, posted by: Xplorer4x4

[quote="tuxuser"] [quote] If the flash fails, am I still able to recover using a serial adapter? [/quote] NO [/quote] Really? So basically there is no fail safe at all? What part specifically has to screw up to cause a brick?  
 [quote]It's still up-to-date for JTAG-consoles. http://free60.org/SMC\_Hack#From\_scratch or http://free60.org/SMC\_Hack#Updating\_a\_hacked\_image[/quote] [quote] The date 31. August 2009 is only for original XeLL in XeLL-only images (not the *not to be discussed*-images) [/quote] Not to be the grammar police but the double negative kind of confused me lol. Exactly what is it that is not to be discussed just so I know how to stay with in the rules. ;) Original XeLL?   
   
 Thanks for helping a n00b learn tux, with out people like you willing to tech people like me would never learn.

## 2012-03-14 23:04:58, posted by: barnhilltrckn

Well rawflash v4 works pretty good so I doubt you will have issues unless you screw up building your image.   
   
 When it comes to recover incase of disaster flashing by lpt would be the cheapest method. If you have an old printer cable laying around cut it and take a multimeter to it to find out which wires are what on the side that hooks up to the pc. You can then use nandpro to read/write the nand from the pc. Dont let anyone tell you that you cant flash a slim by lpt because I have done it numerous times. Just do a quick google search and you can find plenty of diagrams.  
   
 Also just becuse the slim has 4gb internal memory does not mean its like the old phats with internal memory. Its a 16mb nand so treat it as such and you shouldnt have any problems.

## 2012-03-23 18:13:19, posted by: Xplorer4x4

Thanks guys, now in the wiki it says to use xell-1f.bin. Since I have a rgh shouldn't I use xell-gggggg not xell-1f.