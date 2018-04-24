# Team Xecuter RGH2.0 - All FAT/Trinity consoles @ K: 14717/14719 can be glitched!

## 2012-04-17 02:42:11, posted by: tuxuser

Team Xecuter officially released RGH2.0 !  
   
 All FAT and SLIM(Trinity) can be glitched (when updated to 14717/14719)!  
 The timings are pretty much the same between the different motherboard revisions now and the wiring is also identical between Slim/FAT  
   
 More infos below!  
   
 General Info [quote]   
 Team Xecuter RGH2.0 For CoolRunner Rev A and B  
 ==============================================  
   
 We were not quite ready to release this due to it's unstable boot times on older glitch hardware, but as our code was leaked from a team member AGAIN we had to release this due to another team stealing the code and claiming as their own work. They were even too lazy to change any of the patches to make it look like their own - they are 1:1 same as our original sources. Super lame. It seems some teams think this is the Wii or PlayStation scene and you can act like this. They don't even give credits to cOz for his SMC patcher - because they didn't even know that code was from him of course.  
   
 We don't want to get dragged down into bullshit scene politics - most of you won't care anyway, but a lot of guys work very hard on this stuff only to have it stolen with no effort and no credits is just sad. Anyway......  
   
 The Xecuter RGH Development Team are pleased to announce the official release of the RGH2.0 hack for all CoolRunner Rev A and Rev B dev boards. All Phat consoles have now been defeated and are totally glitch-able without having a previous NAND dump or CPU KEY (the same applies to Slim Trinity that have been updated to 14717/14719).  
   
 Xecuter RGH2.0 Features introduced:  
   
 Hack now works on new CB's (14717/14719 update)  
 Hack now works with all Refurbished Split CB's (4577, 5772, 6752)  
 Zephyr CB 4578, 4575, 4577  
 Falcon/Opus CB 5771, 5772, 5773  
 Jasper CB 6750, 6752, 6753  
 Trinity (Slim) CB 9188, 9230  
   
 To confirm, we can now glitch Phats with any kernel and any bootloader. As soon as you have your CPU KEY, and you are using an Xecuter DemoN you will  
 ALWAYS be able to switch to a fully hacked NAND and it can never be stopped no matter what update you apply and no matter which efuses are blown !  
   
 Technical Info  
 -----------------------------  
   
 In the slim boot chain the 2nd bootloader (CB) is split into two pieces. The first part simply starts encryption and loads the second part, which does fuse checks and all the things that the old single CB did. By glitching the first part (CBA), we take control of the system before the fuse checks occur and can patch them out. The slim bootchain has always used this layout and some groups have even tried bringing the slim CBA to phat and using the old single phat (RGH1) CB as CBB. Glitching this way will work if you set it up right, but there are actually phat xboxes that already have their own split CB boot chain which were mostly ones that had been refurbished (CB 5772, 6752, 4577).  
   
 What we have done is simultaneously find glitch timings for these refurbs, dump their cpu\_key, decrypt the boot chain, and port it to run on every other phat! This means that on phats we can now glitch before the fuse check and thus have an unpatchable hack just like trinity!  
   
 New Xecuter CoolRunner v2 Hardware  
 ----------------------------------  
   
 There have been many obstacles to cross with this because CBA glitching does not behave quite the same as CB glitching. The Coolrunner revisions A&B  
 will glitch for RGH2.0 but results will vary and with some, boot times can be worse than trinity and with others they may be instant. These boot times  
 are unacceptable and this is why we have spent the last few weeks designing a new glitch chip that will solve all these problems and will even help with  
 trinity and corona boot times  
   
 New Xecuter CoolRunner v2 Upcoming Features:  
   
 - Corona support  
 - Much better glitch times for RGH1 and RGH2  
 - All-in-One code for all versions  
 - Demon integration  
 - Level shifted POST output  
   
 Development is almost complete - find an image of the CR v2 dev unit in this release pack.  
   
 Building an Image  
 -----------------------------  
   
 With RGH2, a cpu\_key is necessary for building the NAND image. The reason for this is because cpu\_key encryption starts at CB, and in RGH1 there was only one CB which meant that CD was encrypted with cpu\_key but CB could be "zero paired" which meant that the cpu\_key would not be applied. When split-CB was added, they started the encryption at CBA and removed the zero pairing option, which means that cpukey encryption on CBB is mandatory. Because of a vulnerability in the way they use RC4, if you have a stock NAND image that already has a CBB encrypted on it, we can derive the keystream used in that image because we know what the CBB looks like decrypted (we have already decrypted that version before). Because of this, we can embed the older vulnerable CBB into the NAND image using the keystream.  
   
 Bottom line is, after the 14717 update they turned all phats into a split CB boot chain but using unglitchable bootloaders. We can still glitch these boxes even when we don't know the cpu\_key because we can use the "XOR hack" to embed the RGH2 bootloaders. For older images (pre-14717) we need the cpu\_key to encrypt the new loaders because there is not a CBB already in the image that we can derive a keystream from.  
   
 Once the cpu\_key is retrieved, you can always build a NAND image for RGH2'ing your machine. You can flash back to stock, update, even burn all your fuses and you would still be able to run RGH2.  
   
 For building a xell image, read the readme in XECUTER\_RGH2\_Xell.  
   
   
 Instructions  
 -----------------------------  
   
 First wire up your Xecuter CoolRunner according to the diagram provided. RGH2.0 Requires that you either already have your cpu\_key or you are on dashboard 14717/14719. This means that if you do not have your cpu\_key, you must run xell first to retrieve your fuses.  
   
   
 COOLRUNNER CPLD PROGRAMMING  
 -----------------------------  
 The XSVF files are located in \xsvf folder. Start with the xsvf recommended below, however every xsvf should run on every motherboard, but one of them will work best for your setup.  
   
 Falcon/Opus: Program either TX\_RGH2\_B.xsvf, or TX\_RGH2\_C.xsvf  
   
 Jasper: Program either TX\_RGH2\_A.xsvf, or TX\_RGH2\_D.xsvf  
   
 Zephyr: Program either TX\_RGH2\_D.xsvf, or TX\_RGH2\_C.xsvf  
   
   
 Please enjoy this release and report any interesting tweaks you may find. Our forums at www.team-xecuter.com/forums offer excellent support and we would be glad to help and receive feedback from you.  
   
   
 CREDITS:  
 -----------------------------  
 If you are going to use RGH2.0 please give credits to the Team Xecuter RGH development Team. Don't be lame and try to claim the work as your own.  
   
 Thanks to Tiros & GliGli for their original RGH work.  
 Thanks to cOz for his universal SMC patcher.  
 Thanks to all the Xecuter developers and official testers. You know who you are.  
 Thanks to Ubergeek for the diagram.  
 Thanks to the asshole who leaked our code for others to steal and claim as theirs. Super lame. [/quote] XeLL image building Info [quote] Team Xecuter RGH2.0 - XELL Nand Image Builder  
   
 Prerequisites:   
 -----------------------------  
   
 You must either supply a 14717(or later) NAND image OR supply your CPU\_key in build.py  
 (you must supply CPU\_key if the image is not split\_CB)  
   
 If cpukey is found in build.py it will rebuild a new bootchain using that key instead of using the XOR hack.  
   
   
 Features:  
 -----------------------------  
   
 Zephyr 4578, 4575, 4577  
 Falcon 5771, 5772, 5773  
 Jasper 6750, 6752, 6753  
 Trinity 9188, 9230  
   
 USAGE  
 -----------------------------  
 Make sure cpukey is in build.py IF you are using an image other than 14717 (or later).  
   
 Use the following build parameters and write image.ecc to nand with +w16.  
   
 python build.py NAND.bin  
   
 CREDITS:  
 -----------------------------  
 If you are going to use RGH2.0 please give credits to the Team Xecuter RGH development Team. Don't be lame and try to claim the work as your own.   
   
 Thanks to Tiros & GliGli for their original RGH work.  
 Thanks to cOz for his universal SMC patcher.  
 Thanks to all the Xecuter developers and official testers. You know who you are.  
 Thanks to Ubergeek for the diagram.  
 Thanks to the asshole who leaked our code for others to steal and claim as theirs. Super lame. [/quote]   
 [color=blue]**[b]Download: [/b]**[/color] [url=http://libxenon.org/http://libxenon.org//viewtopic.php?p=1764#p1764]Click[/url]