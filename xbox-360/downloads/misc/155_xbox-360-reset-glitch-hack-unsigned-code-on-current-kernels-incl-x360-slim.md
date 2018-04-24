# Xbox 360 Reset Glitch Hack - Unsigned Code on current Kernels incl. X360 SLIM

## 2011-09-01 01:14:05, posted by: tuxuser

The Reset Glitch Hack, developed by GliGli & Tiros, lets you run unsigned code on the following Xbox360 revisions:  
   
 [align=center]**[b][s]ZEPHYR, JASPER .......and...... TRINITY (aka SLIM!).[/s][/b]**[/align]  
 [align=center][s](Falcon support was added with v1.1, (unofficial) Opus support is also there)[/s][/align]  
 [align=center][s](no matter which Dashboard/Kernel they are running)[/s][/align]  
   
 [align=center]**[b]Team Xecuter's RGH2 / Xenon Glitch Hack supports all revisions, except Corona(Slim) ![/b]**[/align]  
   
 [align=center][youtube]http://www.youtube.com/watch?feature=player\_embedded&v=JyYdL4L6vwE[/youtube][/align]  
   
 Here is the detailed technical explaination  
 [quote] **********************************  
 * The Xbox 360 reset glitch hack *  
 **********************************  
   
 Introduction / some important facts  
 ===================================  
   
 tmbinc said it himself, software based approaches of running unsigned code on the 360 mostly don't work, it was designed to be secure from a software point of view.  
   
 The processor starts running code from ROM (1bl) , which then starts loading a RSA signed and RC4 crypted piece of code from NAND (CB).  
   
 CB then initialises the processor security engine, its task will be to do real time encryption and hash check of physical DRAM memory. From what we found, it's using AES128 for crypto and strong (Toeplitz ?) hashing. The crypto is different each boot because it is seeded at least from:  
 - A hash of the entire fuseset.  
 - The timebase counter value.  
 - A truly random value that comes from the hardware random number generator the processor embeds. on fats, that RNG could be electronically deactivated, but there's a check for "apparent randomness" (merely a count of 1 bits) in CB, it just waits for a seemingly proper random number.  
   
 CB can then run some kind of simple bytecode based software engine whose task will mainly be to initialise DRAM, CB can then load the next bootloader (CD) from NAND into it, and run it.  
   
 Basically, CD will load a base kernel from NAND, patch it and run it.  
   
 That kernel contains a small privileged piece of code (hypervisor), when the console runs, this is the only code that would have enough rights to run unsigned code.  
 In kernel versions 4532/4548, a critical flaw in it appeared, and all known 360 hacks needed to run one of those kernels and exploit that flaw to run unsigned code.  
 On current 360s, CD contains a hash of those 2 kernels and will stop the boot process if you try to load them.  
 The hypervisor is a relatively small piece of code to check for flaws and apparently no newer ones has any flaws that could allow running unsigned code.  
   
 On the other hand, tmbinc said the 360 wasn't designed to withstand certain hardware attacks such as the timing attack and "glitching".  
   
 Glitching here is basically the process of triggering processor bugs by electronical means.  
   
 This is the way we used to be able to run unsigned code.  
   
 The reset glitch in a few words  
 ===============================  
   
 We found that by sending a tiny reset pulse to the processor while it is slowed down does not reset it but instead changes the way the code runs, it seems it's very efficient at making bootloaders memcmp functions always return "no differences". memcmp is often used to check the next bootloader SHA hash against a stored one, allowing it to run if they are the same. So we can put a bootloader that would fail hash check in NAND, glitch the previous one and that bootloader will run, allowing almost any code to run.  
   
 Details for the fat hack  
 ========================  
   
 On fats, the bootloader we glitch is CB, so we can run the CD we want.  
   
 cjak found that by asserting the CPU\_PLL\_BYPASS signal, the CPU clock is slowed down a lot, there's a test point on the motherboard that's a fraction of CPU speed, it's 200Mhz when the dash runs, 66.6Mhz when the console boots, and 520Khz when that signal is asserted.  
   
 So it goes like that:  
 - We assert CPU\_PLL\_BYPASS around POST code 36 (hex).  
 - We wait for POST 39 start (POST 39 is the memcmp between stored hash and image hash), and start a counter.  
 - When that counter has reached a precise value (it's often around 62% of entire POST 39 length), we send a 100ns pulse on CPU\_RESET.  
 - We wait some time and then we deassert CPU\_PLL\_BYPASS.  
 - The cpu speed goes back to normal, and with a bit of luck, instead of getting POST error AD, the boot process continues and CB runs our custom CD.  
   
 The NAND contains a zero-paired CB, our payload in a custom CD, and a modified SMC image.  
 A glitch being unreliable by nature, we use a modified SMC image that reboots infinitely (ie stock images reboot 5 times and then go RROD) until the console has booted properly.  
 In most cases, the glitch succeeds in less than 30 seconds from power on that way.  
   
 Details for the slim hack  
 =========================  
   
 The bootloader we glitch is CB\_A, so we can run the CB\_B we want.  
   
 On slims, we weren't able to find a motherboard track for CPU\_PLL\_BYPASS.  
 Our first idea was to remove the 27Mhz master 360 crystal and generate our own clock instead but it was a difficult modification and it didn't yield good results.  
 We then looked for other ways to slow the CPU clock down and found that the HANA chip had configurable PLL registers for the 100Mhz clock that feeds CPU and GPU differential pairs.  
 Apparently those registers are written by the SMC through an I2C bus.  
 I2C bus can be freely accessed, it's even available on a header (J2C3).  
 So the HANA chip will now become our weapon of choice to slow the CPU down (sorry tmbinc, you can't always be right, it isn't boring and it does sit on an interesting bus ;)  
   
 So it goes like that:  
 - We send an i2c command to the HANA to slow down the CPU at POST code D8 .  
 - We wait for POST DA start (POST DA is the memcmp between stored hash and image hash), and start a counter.  
 - When that counter has reached a precise value, we send a 20ns pulse on CPU\_RESET.  
 - We wait some time and then we send an i2c command to the HANA to restore regular CPU clock.  
 - The cpu speed goes back to normal, and with a bit of luck, instead of getting POST error F2, the boot process continues and CB\_A runs our custom CB\_B.  
   
 When CB\_B starts, DRAM isn't initialised so we chose to only apply a few patches to it so that it can run any CD, the patches are:  
 - Always activate zero-paired mode, so that we can use a modified SMC image.  
 - Don't decrypt CD, instead expect a plaintext CD in NAND.  
 - Don't stop the boot process if CD hash isn't good.  
   
 CB\_B is RC4 crypted, the key comes from the CPU key, so how do we patch CB\_B without knowing the CPU key?  
 RC4 is basically:  
 crypted = plaintext xor pseudo-random-keystream  
 So if we know plaintext and crypted, we can get the keystream, and with the keystream, we can encrypt our own code. It goes like that:  
 guessed-pseudo-random-keystream = crypted xor plaintext  
 new-crypted = guessed-pseudo-random-keystream xor plaintext-patch  
 You could think there's a chicken and egg problem, how did we get plaintext in the first place?  
 Easy: we had plaintext CBs from fat consoles, and we thought the first few bytes of code would be the same as the new CB\_B, so we could encrypt a tiny piece of code to dump the CPU key and decrypt CB\_B!  
   
 The NAND contains CB\_A, a patched CB\_B, our payload in a custom plaintext CD, and a modified SMC image.  
 The SMC image is modified to have infinite reboot, and to prevent it from periodically sending I2C commands while we send ours.  
   
 Now, maybe you haven't realised yet, but CB\_A contains no checks on revocation fuses, so it's an unpatchable hack !  
   
 Caveats  
 =======  
   
 Nothing is ever perfect, so there are a few caveats to that hack:  
 - Even in the glitch we found is pretty reliable (25% success rate per try on average), it can take up to a few minutes to boot to unsigned code.  
 - That success rate seems to depend on something like the hash of the modified bootloader we want to run (CD for fats and CB\_B for slims).  
 - It requires precise and fast hardware to be able to send the reset pulse.  
   
 Our current implementation  
 ==========================  
   
 We used a Xilinx CoolRunner II CPLD (xc2c64a) board, because it's fast, precise, updatable, cheap and can work with 2 different voltage levels at the same time.  
 We use the 48Mhz standby clock from the 360 for the glitch counter. For the slim hack, the counter even runs at 96Mhz (incremented on rising and falling edges of clock)  
 The cpld code is written in VHDL.  
 We need it to be aware of the current POST code, our first implementations used the whole 8 bits POST port for this, but we are now able to detect the changes of only 1 POST bit, making wiring easier.  
   
 Conclusion  
 ==========  
   
 We tried not to include any MS copyrighted code in the released hack tools.  
 The purpose of this hack is to run Xell and other free software, I (GliGli) did NOT do it to promote piracy or anything related, I just want to be able to do whatever I want with the hardware I bought, including running my own native code on it.  
   
 Credits  
 =======  
   
 GliGli, Tiros: Reverse engineering and hack development.  
 cOz: Reverse engineering, beta testing.  
 Razkar, tuxuser: beta testing.  
 cjak, Redline99, SeventhSon, tmbinc, anyone I forgot... : Prior reverse engineering and/or hacking work on the 360. [/quote] [url=http://libxenon.org/index.php?topic=146.msg616#new]**[b]Tutorial[/b]**[/url]

### Attachments

[reset_glitch_hack_v1.0.rar](reset_glitch_hack_v1.0.rar)

## 2011-09-23 19:03:28, posted by: GliGli

v1.1 is out! Changelog: [list] - [*]Falcon support.
 - [*]Per hardware revision SMC patches (no more need for Jasper donor SMC on fats).
 - [*]Adding sanity check on 1BL key.
 - [*]Adding support for donor CB on fats.
 - [*]Debug pin on fats and slims.
 - [*]New Xell with some bugs fixed.
 - [*]Now using 270pf capacitor for slims, many reported it works better.
[/list] Happy hacking =)

### Attachments

[reset_glitch_hack_v1.1.rar](reset_glitch_hack_v1.1.rar)

## 2011-11-11 00:34:36, posted by: tuxuser

Reset Glitch Hack v1.1   
   
 * (Unofficial) Opus motherboard support  
   
 JED and XSVF files (for Zephyr, Falcon, Opus, Jasper, Trinity) for programming the CPLD. (JED: Xilinx iMPACT, XSVF: NANDPro)  
   
   
 Thx to Team Xecuter for converting those.

### Attachments

[coolrunner_xsvf_jed.rar](coolrunner_xsvf_jed.rar)

## 2012-04-17 02:26:03, posted by: tuxuser

Team Xecuter's Xenon Reset Glitch Hack  
   
 NOTE: These archives have M$ Code stripped  
   
 You need to obtain CB.7375.bin from the usual places  
 path: /XBOX 360/development/kernel/cd-cb\_package\_04\_16\_2012.zip  
   
 General Info [quote] --== Team Xecuter's Xenon Reset Glitch Hack ==--  
   
   
 Wiring  
 ---------  
   
 Generate your ecc image using the latest version of J-Runner and flash to your NAND   
 (+w16 just like a regular RGH).  
   
 Program your TX CoolRunner (or whatever flavor RGH mod you are using) with the   
 tx-xenon.xsvf or tx-xenon.jed file.  
   
 The Xenon has a capacitor on CPU\_RST that was removed in later models. C7R112 (located   
 near the xclamp under the CPU) must be de-soldered, and the CPU\_RST wire from the   
 TX CoolRunner(D) must be soldered to the left pad (non grounded pad).   
   
 A 47nf ( 0.047uf) capacitor needs to be added between PLL\_BYPASS(+) and GND(-). (If you   
 have a genuine TX CoolRunner REV B you can use the on-board by bridging the CAP jumper)  
   
 A 220-270pf capacitor should be added between CPU\_RST(+) and GND(-) on the cpld. (If you   
 have a genuine TX CoolRunner REV B this is already included in the design so not required)  
   
 An easy to follow picture guide can be found here:   
 http://www.team-xecuter.com/coolrunner/install/phat\_xenon.jpg  
   
   
   
 Troubleshooting  
 ----------------------  
   
 Using a TX CoolRunner Rev B, and after applying various troubleshooting measures we have  
 had glitches ranging from instant to 20 minutes.  
   
 The debug LED should flash on for less than a second and repeat every 5 seconds. If your   
 LED stays on or does not come on at all, it is usually because of something being wrong   
 with PLL\_BYPASS. Try different values of capacitors and wires. If you have enabled the   
 CAP on REV B of the TX CoolRunner, simply un-bridge it and try a 47nF cap instead as per   
 the instructions above.  
   
 If it still has not glitched after several hours, try different values of capacitors on   
 CPU\_RST of your RGH mod. A longer wire / low-loss 50 ohm double shielded cable may also   
 help with this.  
   
 To help increase boot times and stability (on all RGH installs not just Xenon) we recommend   
 that you try Low-Loss Double Shielded 50 ohm cable. It's very cheap to use and quite effective   
 - so a quick shout out to www.xconsoles.com who supplied a batch of high quality cable for   
 our development team to use. It's less than 75 cents a foot - not bad.  
   
 NOTE: Remember when programming the TX CoolRunner that the Xbox power is NOT connected and   
 that the switch is set to PRG before you connect the JTAG cable. If you connect the JTAG   
 cable and it is set to NOR with the Xbox power connected, it can damage your NAND-X and/or   
 CoolRunner. When you have finished programming, switch it back to NOR and then power on the Xbox.  
   
   
   
 The Xenon Hack  
 -----------------------  
   
 Please note that this hack is not available on consoles updated to dashboards 14717 or 14719.  
   
 If you are seeing the debug led it means that the cpu is probably not crashing and the issue   
 addressed by gligli/tiros has been fixed (This can of course be a false positive as sometimes   
 the CPU could be crashing but the SMC restarts fine - we can never be 100% sure)  
   
 So far, this is really only useful for a one time cpu\_key dump. There will undoubtedly be ways   
 of optimizing this hack in the future and who knows, it may become a reliable glitch one day.   
   
 We would appreciate that you give as much feedback to our support forums as possible to help   
 others achieve better results and to improve this method. For now we can leave this and go   
 back to RGH2.0 for Zephyr, Falcon, Jasper and also of course, the Corona.  
   
 TX CoolRunner Support Forums: http://www.team-xecuter.com/forums/forumdisplay.php?f=174  
   
 Enjoy!  
   
 Xbox 360 Xenon RGH Hack brought to you by the Xecuter RGH Development Team  
   
 www.team-xecuter.com  
   
   
 Thanks  
 ------------  
   
 Thanks are extended to Tiros & Gligli, without your work none of this would have been possible.  
   
 A special thanks goes out to cOz - your work on Dashlaunch proved to be an invaluable contribution  
 and we look froward to your next exciting project.  
   
 Greets: Team Jungle, Team FSD, ***, Libxenon & RGLoader. [/quote] build.py Info [quote] Here is the build.py for Xecuter's Xenon RGH Hack  
   
 J-Runner has no use for build.py as it doesn't use Python (or Nandpro) but figured there would be some  
 guys out there who still use this method.  
   
 Thanks to:   
   
 RF1911 for the Xenon SMC  
 GliGli & Tiros for the original build.py  
 cOz for the Universal patch  
 To the Xecuter RGH team - you know who you are.  
   
 Greets to:  
 #libxenon #FreeStyleDash #*** #rgloader #J-Runner #JungleFlasher #c4e [/quote]

### Attachments

[xecuter-xenon-rgh-python_stripped.zip](xecuter-xenon-rgh-python_stripped.zip)[reset_glitch_hack_xenon_Xecuter.zip](reset_glitch_hack_xenon_Xecuter.zip)

## 2012-04-17 02:37:53, posted by: tuxuser

Team Xecuter RGH2.0 For CoolRunner Rev A and B  
 [quote] This is Team Xecuter's RGH 2.0 release - but has M$ code stripped out!  
   
 You need to obtain the CB files from the usual places   
 path: /XBOX 360/development/kernel/cd-cb\_package\_04\_16\_2012.zip  
   
 unpack those into: XECUTER\_RGH2\_Xell/common/CB  
   
 You have to supply a proper 1BL key to build.py aswell ;) [/quote] General Info [quote]   
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

### Attachments

[Xecuter_RGH2_Official_stripped.zip](Xecuter_RGH2_Official_stripped.zip)