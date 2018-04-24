# XeLL Updates

## 2011-02-25 11:12:12, posted by: tuxuser

All updates to XeLL will be posted here - either inofficial ones or official changes which get pushed to GIT Repository aswell.  
   
 Official XeLL Git-Repository: [url=http://free60.git.sourceforge.net/git/gitweb.cgi?p=free60/xell;a=summary]HERE[/url]  
   
   
 **[b]For bugreporting go here: [url=http://libxenon.org/http://libxenon.org//viewtopic.php?t=7]CLICK[/url][/b]**  
   
 **[b][color=#FF0000]! Keep in mind: It's a BETA / WIP, dont upload it anywhere else and please report bugs/discuss it in this board only !  
 It does NOT reflect the final build !!![/color][/b]**  
   
 If in case anyone else has problems with no video on any a/v cable please use this to get your AVPACK ID and report in the bug reports thread with info about the a/v cable you're using and the AVPACK ID given by the troubleshooter, thanks.   
   
 **[b][color=#FF0000]*this is not for flashing to the nand, launch with [url=http://libxenon.org/http://libxenon.org//viewtopic.php?t=4]Xelllaunch[/url] or HvxBootOs*[/color][/b]**  
   
 *Click on the underlined Xelllaunch to get a little How-To  
   
 [url=http://file.libxenon.org/free60/xell/xell-troubleshooting.tar.gz]Xell-novideo-troubleshooting[/url]  
   
 latest xell-reloaded public-build attached [url=http://libxenon.org/http://libxenon.org//viewtopic.php?t=7]HERE[/url]

## 2011-02-25 11:18:37, posted by: tuxuser

Yesterday I added the following to the official git:  
   
 * HDMI modesettings (yes, it works also when optical audio adapter is plugged in)  
 * Building of xell-2f

## 2011-02-25 13:34:16, posted by: tuxuser

XeLL-Testing:  
   
 * USB fix (resets the registers, enables detection of USB when using Xell-Launch.. and no replug of power supply is required to get usb detected) however, elf do not load correctly so far  
   
 * Added YUV 720p mode

## 2011-03-03 01:06:52, posted by: tuxuser

XeLL-Testing:  
   
 * Added ATA Reset (HDD & DVD) == We can boot recent Linux Kernels from XeLL-Launch now (Credit goes to GliGli & cOz - THX!)

## 2011-03-05 15:35:08, posted by: tuxuser

XeLL Testing:  
   
 * updated to lwip 1.4 r2  
 * functions to parse values of smc\_config  
 * improved flash handling  
 * Improved AVPack detection - Some IDs could be missing though  
   
 THX Redline99 and cancerous for help and testing ;)

## 2011-03-05 17:50:16, posted by: Meluxe

Thank you for the binaries, and all of your work! Seems to move on!  
   
 Just tried to boot xell (xell-2f.bin renamed to xell.bin) via Xell-Launch. Doesn`t work neither with hdmi nor scart. However, Dashlaunch is starting, visible by the rol. Going to try the others now.  
   
 edit: SOLVED with new version  
 cheers!

## 2011-03-05 22:15:02, posted by: tuxuser

Yeah I still havent figured out how to handle the avpack detection properly.. I will post updates here asap

## 2011-03-06 15:31:31, posted by: Chrisoldinho

xell-2f.bin renamed to xell.bin and placed in same folder works really well, thanks!

## 2011-03-07 00:23:25, posted by: UNIX

The newest build today works amazing, finally working with my YUV cable! Great stuff =)

## 2011-03-08 13:02:43, posted by: tuxuser

XeLL-Testing  
   
 *Major refactoring  
 *ASCII Logo  
 *Matrix Style  
 *Possible overscan fix  
 *too many changes to mention :P

## 2011-03-12 20:42:24, posted by: Chrisoldinho

just got back from holiday - progress seems really good :)

## 2011-03-13 21:48:00, posted by: tuxuser

XeLL-Testing:  
   
 * Better DVD-Drive handling  
 * Quiet Loop  
 * crypting function  
 * decrypts kv now and shows dvdkey/cpukey/virtual cpu key

## 2011-03-17 22:39:11, posted by: Sonic-NKT

would be possible to integrate a basic file selector in a future version? so if you have more than 1 elf on a usb stick to select which one to boot?

## 2011-03-18 04:43:54, posted by: Cancerous1

perhaps it could be possible, but it would add to the size of xell, and there is a different solution to that being worked on.

## 2011-03-18 08:41:46, posted by: Meluxe

[quote]...and there is a different solution to that being worked on.[/quote] Sounds really interesting! Kind of a dash for xell??  
 I am so curious... could you share some more info? Please! :roll:

## 2011-03-18 21:00:35, posted by: tuxuser

XeLL-Testing:  
   
 * Added CROSS\_COMPILE flag in Makefile  
 * Additional defines in flash.c/*.h  
 * Look for vmlinux AND xenon.elf on USB/CDROM  
 * Revert back to DEFAULT\_STYLE (green/black)

## 2011-03-20 01:12:22, posted by: kpozn360

hello!  
 i have a jasper, how should i use xell reloaded?  
   
 when i asked on an other post someone told me to try with flash360 and rename xell-2f in updslot0!  
 i did it and ... black screen at reboot! normal?  
 thanks

## 2011-03-20 02:26:49, posted by: tuxuser

[quote=""kpozn360""]hello!  
 i have a jasper, how should i use xell reloaded?  
   
 when i asked on an other post someone told me to try with flash360 and rename xell-2f in updslot0!  
 i did it and ... black screen at reboot! normal?  
 thanks[/quote]  
   
 Why didnt you read the first post in this thread? It says " DONT FLASH TO YOUR NAND, ONLY USE IT WITH XELL LAUNCH"  
   
 You need to reflash!

## 2011-03-20 02:28:50, posted by: Razkar

Yes it's normal, the version in this topic are test builds and MUST NOT flash as first bootloader. If you want to try those build, use xelllaunch (rename xell-2g.bin to xell.bin and put it next to the default.xex of xelllaunch).  
   
 Anyway for futher upadate you should never update xell in the maner you did. You HAVE TO flash a whole nand and NOT ONLY the bootloader. You can use directly fbbuild or soft like bestpig toolbox and select custom freeboot ... then change the xell-2f.bin file by the one you wanna flash  
   
 EDIT : Tux you was too fast :p

## 2011-03-20 13:42:20, posted by: kpozn360

thanks and ... sorry, really!

## 2011-04-07 14:10:12, posted by: korupt data

Great work so far, really hope you continue your progress.

## 2011-04-13 12:14:00, posted by: Doerek

[quote=""Razkar""]Yes it's normal, the version in this topic are test builds and MUST NOT flash as first bootloader. If you want to try those build, use xelllaunch (rename xell-2g.bin to xell.bin and put it next to the default.xex of xelllaunch).[/quote]  
   
 So...  
 does this mean XeLLous doesnt gets replaced and if i like to i can delete the xell.bin and every thing is like before?

## 2011-04-13 23:45:58, posted by: Sonic-NKT

Yeah,  
 if you start your console per eject xellous will start like normal,  
 xelllaunch on the other hand looks if a xell.bin is either in the Program directory or on the root of HDD or USB, if it doesnt find one it will start the xell version flashed to nand (which would be xellous)

## 2011-04-14 19:13:16, posted by: UNIX

What happened to the XeLL-testing builds? I've noticed you took it down for some time now..

## 2011-04-15 00:30:52, posted by: tuxuser

Yes, it will be up again once xell-reloaded hits final.

## 2011-04-15 00:50:25, posted by: UNIX

Awesome! Can't wait!

## 2011-04-16 03:15:56, posted by: Doerek

[quote=""Sonic-NKT""]Yeah,  
 if you start your console per eject xellous will start like normal,  
 xelllaunch on the other hand looks if a xell.bin is either in the Program directory or on the root of HDD or USB, if it doesnt find one it will start the xell version flashed to nand (which would be xellous)[/quote]  
 Thx for this very important info...

## 2011-04-19 12:54:30, posted by: val532

Any new update ?

## 2011-04-19 13:49:20, posted by: Doerek

[quote=""tuxuser""]Yes, it will be up again once xell-reloaded hits final.[/quote]  
   
 Does this mean Bugreporting is not longer needed?

## 2011-04-19 15:40:34, posted by: tuxuser

[quote=""Doerek""]  
 Does this mean Bugreporting is not longer needed?[/quote]  
   
 Correct

## 2011-05-03 20:54:35, posted by: val532

Sorry but are you alive ?

## 2011-05-04 23:50:23, posted by: Razkar

[quote=""val532""]Sorry but are you alive ?[/quote]  
 It seems he died in the navy seal assault and sadly they take all the data as proof of conspiracy against the US leadership.

## 2011-05-06 00:21:07, posted by: val532

^^

## 2011-05-21 22:03:57, posted by: chriss179

Bumping this one.... Why? I'm really looking forward to the final release because my VGA output won't work with the latest release.. I tried building from GIT but somehow it all produced erroneous xell*.bin files. I'm happy to wait it out until final. But let me express my anciety... Checking back every day in hope this one hits final!  
   
 p.s. and the world still has to end today so we'll never see the final if it doesn't hit today! :lol:

## 2011-05-30 05:22:57, posted by: Walkanator333

I'm having the same issue. Sadly I only have 2 options, either a pos tv, or a computer monitor over vga. So I'm really hoping someone figures out a way past it

## 2011-06-10 03:07:32, posted by: Walkanator333

Works great, and is absolutely awesome. Thanks for the link.

## 2011-08-10 23:05:29, posted by: Oglesan

can someone fix the link to Xelllaunch? :( goes to http 404 error

## 2011-08-10 23:10:59, posted by: tuxuser

[quote="Oglesan"]  
 can someone fix the link to Xelllaunch? :( goes to http 404 error  
 [/quote]  
   
 Thx, fixed

## 2011-08-26 21:24:31, posted by: jayboy86

sorry if this sounds dumb. i am running xell reloaded (blue screen version) via xell launch. i have seen many videos of people running a version of xell reloaded with green text and black background. can anyone please tell me where i can get this version. thx guys  
 jay

## 2011-08-27 20:27:20, posted by: silversid

Hi i'm really new to this. But does it say XeLL Reloaded when u when the text on the blue screen starts?

## 2011-08-28 19:05:25, posted by: jayboy86

yes it does say xell reloaded.  
   
 im trying to find out where i can get the xell reloaded that has the black background and green text, looks so much better  
 anyone know where i can get it?

## 2011-09-01 01:00:28, posted by: tuxuser

XeLL Reloaded 28/08/2011 : First Official Version  
 [quote] * Its divided in 2 stages:  
 - 1st Stage initalizes the Hardware, uncompresses and executes 2nd Stage  
 - 2nd Stage (based on LibXenon) loads all required drivers and does the usual "XeLL tasks"  
 * XeLL is based on LibXenon now  
 * XeLL is running with all CPU cores activated  
 * Optimized CPU Usage  
 * TinyEHCI is used, delivers full USB 2.0 speed when acccessing mass storage media  
 * lwip network stack upgraded to v1.4 rc2 - It's faster  
 * It can access the DVD-drive via DMA now: faster reading  
 * It's possible to reload into XeLL now when you are inside a LibXenon Application  
 * Refactored ELF Launching Code - shouldn't have issues when executed via XeLL-Launch  
 * New HTTP Webinterface  
 * Proper hardware init / shutdown (e.g. after XeLL Launch)  
 * Supports upgrading XeLL with a XeLL-2Stages binary from USB, named "updxell.bin"  
 * Infinite bootloop when looking for ELFs to execute  
 * Parses / decrypts keyvault (either with real or virtual CPUkey) [/quote] Source Code is available from Free60 Git Repository, branch: 2stages

## 2011-09-01 09:14:30, posted by: ddxcb

I got a great Idea for xell, have an INI file so people can set the resolution as they pleased.  
   
 so instead of me using 1024x** i can use 1280x768.

## 2011-09-10 06:43:56, posted by: ravendrow

ok guys it doesnt take much to change your 2stage build colors. this is how....assuming you have the latest toolchain and libxenon installed  
   
 open terminal  
 type sudo su (and enter your password)  
 navigate to your xell folder  
 make sure it is updated to the newest source by typing  
 git pull git://free60.git.sourceforge.net/gitroot/free60/xell  
 make sure you are on the 2stage branch by typing  
 git checkout 2stage (thanks tuxuser lol)  
 k now type  
 cd source/lv2  
 now we need to edit the config.h file so type  
 nano config.h  
 look for where is says DEFAULT\_THEME and your going to want to change that to MATRIX\_THEME make sure you use all caps if the text doesn't stay red you did it wrong then just press ctrl+o then enter, then press ctrl+x to exit nano  
   
 now all you have to do is go to the root of your xell folder and compile as normal and there you go xell-2stage with the black and green matrix theme...hope this helps those who couldn't figure out how to change themes

## 2011-09-23 01:34:31, posted by: LazyJones

The link to the latest xell-reloaded public-build is down. [quote]An Error Has Occurred!  
 The topic or board you are looking for appears to be either missing or off limits to you.[/quote]

## 2011-09-23 10:22:45, posted by: Cancerous1

Link fixed  
 [quote="LazyJones"] The link to the latest xell-reloaded public-build is down. [quote]An Error Has Occurred!  
 The topic or board you are looking for appears to be either missing or off limits to you.[/quote] [/quote]

## 2011-12-06 11:58:46, posted by: guerrierodipace

please, can someone explain the meaning of cpukey virtual?

## 2011-12-09 19:15:00, posted by: Pa0l0ne

Hello Guerrierodipace! ;)  
   
 If you mean this:  
   
 * Parses / decrypts keyvault (either with real or virtual CPUkey)  
   
 i don't think it have current use: parsing keyvault with CPUKey different of the real "cpu hardware type" cause an error, so the question is acceptable and much interesting....  
   
 Only a stylish function?

## 2011-12-09 19:24:43, posted by: Cancerous1

people still have jtag's, if you don't need that, just don't worry about it.

## 2011-12-18 12:10:44, posted by: tuxuser

New XeLL Build (TESTING) - Please report all bugs you can find  
   
 Changes: [quote] * LINUX works on RGH Consoles !  
 * additional "return\_to\_xell"-offset  
 * Support for external initramfs  
 * Search for updxell.bin on CD/DVD aswell  
 * Add status message when looking for updxell.bin  
 * Look for file named "initrd.gz" on CD/DVD and USB  
 * Added detection of kboot.conf Header  
 * Added kboot.conf parsing + Menu  
 * Supports custom CMDLINE (for linux kernel) via kboot.conf  
 * Added kboot.conf sample  
 * Looks for kboot.conf from CD/DVD and USB now [/quote] BUGREPORT-Thread: http://libxenon.org/http://libxenon.org//viewtopic.php?t=7  
 Append "Build: XeLL\_Reloaded-testing-git18122011\_fix1" when filing a bugreport.  
 If a fatal crash appears (Red Screen with alot of values :P)  
 Append the Stack Dump Values which are shown at the bottom - if there arent any, append the value of sr0 =...

### Attachments

[XeLL_Reloaded-testing-git18122011_fix1.tar.gz](XeLL_Reloaded-testing-git18122011_fix1.tar.gz)

## 2011-12-20 08:38:20, posted by: giglife

today i got a box that has E76 - seems that the nic port or ics chipset is toasted.  
 I glitched the unit and i get the unit glitched in 1 sec no problem  
 xell reloaded loads but i get the following on screen  
   
 nand init  
 network init  
 initializing lwip 1.4.0  
 Reinit PHY.........  
   
 ^ seems that part is the E76 is there anyway to get around this maybe a XELL reloaded that does not check NIC ?  
 i just need to get the CPU KEY   
 and i cant get it due to that E76 plz help

## 2011-12-21 00:21:55, posted by: tuxuser

[quote="giglife"]  
 today i got a box that has E76 - seems that the nic port or ics chipset is toasted.  
 I glitched the unit and i get the unit glitched in 1 sec no problem  
 xell reloaded loads but i get the following on screen  
   
 nand init  
 network init  
 initializing lwip 1.4.0  
 Reinit PHY.........  
   
 ^ seems that part is the E76 is there anyway to get around this maybe a XELL reloaded that does not check NIC ?  
 i just need to get the CPU KEY   
 and i cant get it due to that E76 plz help  
 [/quote]  
   
 Use this. Fuseset 03 + 05 is your cpukey

### Attachments

[xell-onlyshow_fuses_glitch.tar.gz](xell-onlyshow_fuses_glitch.tar.gz)

## 2011-12-21 07:31:08, posted by: giglife

tuxuser - u the man :)  
 it worked no problem OH MY GOD  
 i cant belive it  
 u just saved a BIG BLOCK JASPER  
 tested and CPU KEY opens NAND :)  
 thanks time to move on and make a image  
 - please add this to the list of XELL bins  
 name it xell-gggg-e76 or something [ des = will bypass e76 nic port errors ]

## 2011-12-24 00:33:00, posted by: tuxuser

New XeLL Build (TESTING) - Please report all bugs you can find  
   
 Changes: [quote] * LINUX works on RGH Consoles !  
 * additional "return\_to\_xell"-offset  
 * Support for external initramfs  
 * Search for updxell.bin on CD/DVD aswell  
 * Add status message when looking for updxell.bin  
 * Look for file named "initrd.gz" on CD/DVD and USB  
 * Added detection of kboot.conf Header  
 * Added kboot.conf parsing + Menu  
 * Supports custom CMDLINE (for linux kernel) via kboot.conf  
 * Added kboot.conf sample  
 * Looks for kboot.conf from CD/DVD and USB now  
   
 24.12.2011:  
 kboot: Fixed header-detection of some initrd (thx sk1080!)  
 elf: Relocate initrd to a static address  
 main: Directly relocate initrd-data to static address  
 kboot: Allow kernel/initrd-file to be loaded from different sources (local/tftp)  
 kboot: Beautifying fileloading [/quote] BUGREPORT-Thread: http://libxenon.org/http://libxenon.org//viewtopic.php?t=7  
 Append "Build: XeLL\_Reloaded-testing-git24122011" when filing a bugreport.  
 If a fatal crash appears (Red Screen with alot of values :P)  
 Append the Stack Dump Values which are shown at the bottom - if there arent any, append the value of sr0 =...

### Attachments

[XeLL_Reloaded-testing-git24122011.tar.gz](XeLL_Reloaded-testing-git24122011.tar.gz)

## 2011-12-24 09:03:49, posted by: guerrierodipace

[quote="Pa0l0ne"]  
 Hello Guerrierodipace! ;)  
   
 If you mean this:  
   
 * Parses / decrypts keyvault (either with real or virtual CPUkey)  
   
 i don't think it have current use: parsing keyvault with CPUKey different of the real "cpu hardware type" cause an error, so the question is acceptable and much interesting....  
   
 Only a stylish function?  
 [/quote]  
   
 nice to hear from you :D  
 I am asking because I had a xbox360 full working with virtual cpukey,in our forum you can see screenshot and discussion.

## 2011-12-29 17:21:54, posted by: greator

I tried the testing xell, but it wont boot.  
   
 write the xell-2f and it boots.  
   
 The testing xell doesn't like my 16mb jasper.

## 2011-12-29 18:44:04, posted by: tuxuser

so it doesnt work .. but when you flashed it, it worked???? Sorry, but I dont understand what you are saying, please be more precise..

## 2011-12-30 01:38:16, posted by: M007P

I flashed 15 diffrent xboxs, jasper big block, small, slim... no problem.  
   
   
   
 Sent from my iPhone using Tapatalk

## 2011-12-31 17:44:38, posted by: greator

[quote="tuxuser"]  
 so it doesnt work .. but when you flashed it, it worked???? Sorry, but I dont understand what you are saying, please be more precise..  
 [/quote]  
   
 sorry, I mean, I flashed the [XeLL\_Reloaded-testing-git18122011\_fix1] using +w command. Xell screen wont show up, the green light just keep blinking.  
   
 Then I flashed the xell-reloaded public build, Xell screen show up in just 3 sec. Obviously the testing build doesn't work on my jasper 16mb.  
 I havent try the [Build: XeLL\_Reloaded-testing-git24122011] yet.  
   
 I think the most important fix that xell reloaded need is the xenon.elf and vmlinux file that cannot be executed. Not just me, I hear alot of other ppl having the same problem. 

## 2012-01-01 02:09:10, posted by: tuxuser

@geator  
   
 Use the internal update function of XeLL!  
   
   
 @ALL  
   
 New XeLL Build (TESTING) - Please report all bugs you can find  
   
 Changes: [quote] * LINUX works on RGH Consoles !  
 * additional "return\_to\_xell"-offset  
 * Support for external initramfs  
 * Search for updxell.bin on CD/DVD aswell  
 * Add status message when looking for updxell.bin  
 * Look for file named "initrd.gz" on CD/DVD and USB  
 * Added detection of kboot.conf Header  
 * Added kboot.conf parsing + Menu  
 * Supports custom CMDLINE (for linux kernel) via kboot.conf  
 * Added kboot.conf sample  
 * Looks for kboot.conf from CD/DVD and USB now  
   
 24.12.2011:  
 kboot: Fixed header-detection of some initrd (thx sk1080!)  
 elf: Relocate initrd to a static address  
 main: Directly relocate initrd-data to static address  
 kboot: Allow kernel/initrd-file to be loaded from different sources (local/tftp)  
 kboot: Beautifying fileloading  
   
 01.01.2012  
 kboot: Reset initrd before loading a kboot-entry  
 TFTP: Send ACK after the last data packet  
 TFTP: Fix files smaller than 1 DATA packet, other minor fixes  
 kboot: enable speeding up of cpu   
 kboot: stop countdown on user input  
 kboot: Make menu controllable via UART UP/DOWN/ENTER key  
 kboot: Only reinit network if IP in configfile wasnt set previously  
 kboot: speedup code can take all speedsettings now  
 kboot: conditions for videomode checked more clearly  
 kboot: kboot\_set\_config is called even if no valid kernel-entries are found  
 kboot: simplified LOAD\_FILE function  
 kboot: better check for tftpserver-arg validity  
 main: boot\_server\_name() checks for kboot-parsed value  
 kboot: Updated kboot.conf sample  
 kboot: Don't crash due to uninitialized settings  
 kboot: initialize speedup setting  
 Try loading files from sda:/ (SATA HDD, FAT32)  
 Updated README with "How to use" information [/quote] BUGREPORT-Thread: http://libxenon.org/http://libxenon.org//viewtopic.php?t=7  
 Append "Build: XeLL\_Reloaded-testing-git01012012" when filing a bugreport.  
 If a fatal crash appears (Red Screen with alot of values :P)  
 Append the Stack Dump Values which are shown at the bottom - if there arent any, append the value of sr0 =...

### Attachments

[XeLL_Reloaded-testing-git01012012.tar.gz](XeLL_Reloaded-testing-git01012012.tar.gz)

## 2012-01-03 02:37:27, posted by: chriss179

Dunno if i should ask here or make a seperate thread on this one. Sorry if in the wrong place. But my problem's as follows. I'm trying to figure out how to run xell reloaded from dashlaunch (2.29) xell launcher without including a xell.bin with xell launcher.   
   
 the problem is i want the harddrive or usb stick containing xell launcher to work in both the RGH and JTAG consoles.  
   
 In jtags you rename xell-2f.bin to updxell.bin and let it update, then xell launcher will launch xell from flash no problem.   
   
 So is there a way for RGH to run xell from flash? All i get is a black screen when launching the xell launcher with xell-ggggggg.bin  
   
 I could ofcourse write xell-2f.bin to flash, but i would lose the ability to power on with eject and run xell.....??  
   
 Anyways, i hope there is a way. as of yet. I hate to have 2 copies of xell launcher on disk for the sake of jtags and rgh's.   
   
 [edit] i see i'm overlooking the fact that jtags need xell-2f.bin too. So i'm really making a fuss over nothing. Problem solved...

## 2012-01-03 07:53:37, posted by: sk1080

Sorry, this isn't the right forum to ask about RGH stuff...

## 2012-01-03 13:09:37, posted by: chriss179

It's a thread on the "development" of xell reloaded tho. being able to run xell from flash on this and not on that console might be a development issue? But like i said. There wasn't a problem in the first place. Only aesthetic.

## 2012-01-03 13:36:27, posted by: tuxuser

Its fine to ask stuff about the Reset Glitch Hack and XeLL development.. but its not allowed to ask stuff about the (hacked) M$ Kernel.. so questions about any xex applications dont belong in libxenon.org!

## 2012-01-04 15:28:59, posted by: covenant

I have been playing with Xell and booting via tftp for the last few days (in between sorting out MAX232 problems!). I notice that the latest binary you (tuxuser) posted has:  
 [code]* *source/lv2/tftp/tftp.c: maxtries = 1; [/code] so that one dropped packet leads to the boot device search loop restarting. This means that a single dropped packet will stop booting via tftp.  
   
 I tried recompiling from the xell-testing branch but this fails on an unrelated error (probably something you are working on) and so hand edited tftp.c from your stable xell tree to set maxtries=100. This works well and, although I seem to drop 3 or 4 packets, linux boots happily on my RGH slim.  
   
 Attached is the version of Xell I compiled if anyone else is interested in playing with it. Because the full kboot.conf support is not present in the stable branch of Xell, I have hacked main.c so that it expects the tftp server to be on 192.168.1.125 and to serve the file zImage.xenon.  
 

### Attachments

[xell-gggggg.bin](xell-gggggg.bin)

## 2012-01-05 08:07:13, posted by: sk1080

The xell-testing branch should compile just fine, so please post your error if you are getting one.

## 2012-01-05 22:13:28, posted by: covenant

Last few lines from make on a clean tree of xell-testing checked out today. I used a toolchain I compiled only a couple of days ago on a bog standard x86 PC:  
 [size=80]  
 [code]* *[device\_tree\_include.S] linking ... stage2.elf main.o: In function `launch\_elf': /home/covenant/dev/xbox360/xell-testing/source/lv2/main.c:132: undefined reference to `kernel\_set\_initrd' kbootconf.o: In function `try\_kbootconf': /home/covenant/dev/xbox360/xell-testing/source/lv2/kboot/kbootconf.c:441: undefined reference to `kernel\_build\_cmdline' /home/covenant/dev/xbox360/xell-testing/source/lv2/kboot/kbootconf.c:443: undefined reference to `kernel\_reset\_initrd' collect2: ld returned 1 exit status make[3]: *** [/home/covenant/dev/xbox360/xell-testing/stage2.elf] Error 1 make[2]: *** [build] Error 2 make[1]: *** [stage2.elf32.gz] Error 2 make: *** [xell-1f.build] Error 2 [/code] More output (from the start of compilation of kbootconf.c) here: [url=http://pastie.org/3133702]http://pastie.org/3133702[/url]  
   
 Would be nice to get it compiled but have plenty to do in the meantime with kernel debugging on slim now that I have serial logging working.

## 2012-01-06 00:43:22, posted by: sk1080

to compile xell-testing you need to install libxenon-testing

## 2012-01-07 14:13:05, posted by: covenant

Many thanks, I downloaded, compiled and tested it all last night and it works perfectly.   
   
 However, the 'maxtries = 1' is still present in the xell-testing code so the issue I encountered earlier still stands. Attached here is a xell-gggggg.bin binary compiled from the xell-testing tree with only maxtries=1 from tftp.c changed to maxtries=100.   
   
 tftpbooting my kernel that contains an initramfs (as a cpio image built in to the kernel) which performs some dirty initialisation before doing a a switch\_root on the mounted nfs fs works perfectly for me now so this xell binary may be useful for someone else too.   
   
 OT: my RGH slim is quite unstable when booted into Linux at present and **[b]some[/b]** of this seems to be related to nfs mount options which I am sorting out today. However, some is clearly kernel-related but I have not seen any specific discussion about how stable Linux on slims actually is and whether anyone else is working on this. I would love to hear from anyone who is in order to pool efforts (**[b]I am on #libxenon on EFNet a lot at the moment so catch me there instead of hijacking this thread with discussion about this[/b]**)  
   
 Update: Interesting thing about the xell-testing code. TFTP booting a kernel works fine whether my UART debug is attached or not during transfer of the kernel image from my server to the XBox. However, when serial debug is attached, every packet is dropped once. If I have serial debug detached, packets will get dropped (to an extent dependent on the level of net traffic present on my LAN at the time) but not every single one. 

### Attachments

[xell-gggggg_testing_tftp_maxtries_100.bin](xell-gggggg_testing_tftp_maxtries_100.bin)

## 2012-01-17 22:37:43, posted by: tuxuser

New XeLL Build (TESTING) - Please report all bugs you can find  
   
 Changes: [quote] * LINUX works on RGH Consoles !  
 * additional "return\_to\_xell"-offset  
 * Support for external initramfs  
 * Search for updxell.bin on CD/DVD aswell  
 * Add status message when looking for updxell.bin  
 * Look for file named "initrd.gz" on CD/DVD and USB  
 * Added detection of kboot.conf Header  
 * Added kboot.conf parsing + Menu  
 * Supports custom CMDLINE (for linux kernel) via kboot.conf  
 * Added kboot.conf sample  
 * Looks for kboot.conf from CD/DVD and USB now  
   
 24.12.2011:  
 kboot: Fixed header-detection of some initrd (thx sk1080!)  
 elf: Relocate initrd to a static address  
 main: Directly relocate initrd-data to static address  
 kboot: Allow kernel/initrd-file to be loaded from different sources (local/tftp)  
 kboot: Beautifying fileloading  
   
 01.01.2012  
 kboot: Reset initrd before loading a kboot-entry  
 TFTP: Send ACK after the last data packet  
 TFTP: Fix files smaller than 1 DATA packet, other minor fixes  
 kboot: enable speeding up of cpu   
 kboot: stop countdown on user input  
 kboot: Make menu controllable via UART UP/DOWN/ENTER key  
 kboot: Only reinit network if IP in configfile wasnt set previously  
 kboot: speedup code can take all speedsettings now  
 kboot: conditions for videomode checked more clearly  
 kboot: kboot\_set\_config is called even if no valid kernel-entries are found  
 kboot: simplified LOAD\_FILE function  
 kboot: better check for tftpserver-arg validity  
 main: boot\_server\_name() checks for kboot-parsed value  
 kboot: Updated kboot.conf sample  
 kboot: Don't crash due to uninitialized settings  
 kboot: initialize speedup setting  
 Try loading files from sda:/ (SATA HDD, FAT32)  
 Updated README with "How to use" information  
   
 17.01.2012  
 Updated README  
 kboot: some fixes to initrd relocation  
 kboot: Fix controller navigation in the menu  
 xenon\_nand: Added rawflash v4 (coded by cOz)  
 main: Look for 'updflash.bin' to process with rawflash v4  
 tftp: prevent spamming incase no tftp-server is found   
 tftp: set maxtries to 10 so it doesn't fail on the first lost TFTP packet  
 main: Print " * Executing" right before actually executing the ELF  
 main: Dont look for seperated initrd.gz on media - it only makes sense with kboot.conf  
 main: no newline for "Bad Header"-message [/quote] BUGREPORT-Thread: http://libxenon.org/http://libxenon.org//viewtopic.php?t=7  
 Append "Build: XeLL\_Reloaded-testing-git17012012" when filing a bugreport.  
 If a fatal crash appears (Red Screen with alot of values :P)  
 Append the Stack Dump Values which are shown at the bottom - if there arent any, append the value of sr0 =...

### Attachments

[XeLL_Reloaded-testing-git17012012.tar.gz](XeLL_Reloaded-testing-git17012012.tar.gz)

## 2012-01-19 20:10:53, posted by: mattia492

hi... i have a rgh jasper xbox... how i make to upgrade xell?? thanks :D

## 2012-01-24 01:31:39, posted by: tuxuser

@Mattia 492  
   
 http://libxenon.org/http://libxenon.org//viewtopic.php?t=9  
   
 ----------------------------------------------------------------------  
   
 New XeLL Build (TESTING) - Please report all bugs you can find  
   
 Changes: [quote] * LINUX works on RGH Consoles !  
 * additional "return\_to\_xell"-offset  
 * Support for external initramfs  
 * Search for updxell.bin on CD/DVD aswell  
 * Add status message when looking for updxell.bin  
 * Look for file named "initrd.gz" on CD/DVD and USB  
 * Added detection of kboot.conf Header  
 * Added kboot.conf parsing + Menu  
 * Supports custom CMDLINE (for linux kernel) via kboot.conf  
 * Added kboot.conf sample  
 * Looks for kboot.conf from CD/DVD and USB now  
   
 24.12.2011:  
 kboot: Fixed header-detection of some initrd (thx sk1080!)  
 elf: Relocate initrd to a static address  
 main: Directly relocate initrd-data to static address  
 kboot: Allow kernel/initrd-file to be loaded from different sources (local/tftp)  
 kboot: Beautifying fileloading  
   
 01.01.2012  
 kboot: Reset initrd before loading a kboot-entry  
 TFTP: Send ACK after the last data packet  
 TFTP: Fix files smaller than 1 DATA packet, other minor fixes  
 kboot: enable speeding up of cpu   
 kboot: stop countdown on user input  
 kboot: Make menu controllable via UART UP/DOWN/ENTER key  
 kboot: Only reinit network if IP in configfile wasnt set previously  
 kboot: speedup code can take all speedsettings now  
 kboot: conditions for videomode checked more clearly  
 kboot: kboot\_set\_config is called even if no valid kernel-entries are found  
 kboot: simplified LOAD\_FILE function  
 kboot: better check for tftpserver-arg validity  
 main: boot\_server\_name() checks for kboot-parsed value  
 kboot: Updated kboot.conf sample  
 kboot: Don't crash due to uninitialized settings  
 kboot: initialize speedup setting  
 Try loading files from sda:/ (SATA HDD, FAT32)  
 Updated README with "How to use" information  
   
 17.01.2012  
 Updated README  
 kboot: some fixes to initrd relocation  
 kboot: Fix controller navigation in the menu  
 xenon\_nand: Added rawflash v4 (coded by cOz)  
 main: Look for 'updflash.bin' to process with rawflash v4  
 tftp: prevent spamming incase no tftp-server is found   
 tftp: set maxtries to 10 so it doesn't fail on the first lost TFTP packet  
 main: Print " * Executing" right before actually executing the ELF  
 main: Dont look for seperated initrd.gz on media - it only makes sense with kboot.conf  
 main: no newline for "Bad Header"-message  
   
 24.01.2012  
 kboot: Menu can be aborted via 'C'-key over UART, B or BACK on X360 Controller or B on IR Remote  
 zlib: prevent buffer overflow if uncompressed file is bigger than 32MB  
 kboot: Check gzip file for cpio header without fully extracting it - allows compressed initrd up to 32MB  
 usbdevs/usbctrl: Added rf unit's DEVICE\_ID back to usbctrl\_driver init  
 oops: fixed a possible memory leak [/quote] BUGREPORT-Thread: http://libxenon.org/http://libxenon.org//viewtopic.php?t=7  
 Append "Build: XeLL\_Reloaded-testing-git24012012-RC1" when filing a bugreport.  
 If a fatal crash appears (Red Screen with alot of values :P)  
 Append the Stack Dump Values which are shown at the bottom - if there arent any, append the value of sr0 =...

### Attachments

[XeLL_Reloaded-testing-git24012012-RC1_fix1.tar.gz](XeLL_Reloaded-testing-git24012012-RC1_fix1.tar.gz)

## 2012-01-25 23:04:55, posted by: tuxuser

New XeLL Build (TESTING) - Please report all bugs you can find  
   
 Changes: [quote] * LINUX works on RGH Consoles !  
 * additional "return\_to\_xell"-offset  
 * Support for external initramfs  
 * Search for updxell.bin on CD/DVD aswell  
 * Add status message when looking for updxell.bin  
 * Look for file named "initrd.gz" on CD/DVD and USB  
 * Added detection of kboot.conf Header  
 * Added kboot.conf parsing + Menu  
 * Supports custom CMDLINE (for linux kernel) via kboot.conf  
 * Added kboot.conf sample  
 * Looks for kboot.conf from CD/DVD and USB now  
   
 24.12.2011:  
 kboot: Fixed header-detection of some initrd (thx sk1080!)  
 elf: Relocate initrd to a static address  
 main: Directly relocate initrd-data to static address  
 kboot: Allow kernel/initrd-file to be loaded from different sources (local/tftp)  
 kboot: Beautifying fileloading  
   
 01.01.2012  
 kboot: Reset initrd before loading a kboot-entry  
 TFTP: Send ACK after the last data packet  
 TFTP: Fix files smaller than 1 DATA packet, other minor fixes  
 kboot: enable speeding up of cpu   
 kboot: stop countdown on user input  
 kboot: Make menu controllable via UART UP/DOWN/ENTER key  
 kboot: Only reinit network if IP in configfile wasnt set previously  
 kboot: speedup code can take all speedsettings now  
 kboot: conditions for videomode checked more clearly  
 kboot: kboot\_set\_config is called even if no valid kernel-entries are found  
 kboot: simplified LOAD\_FILE function  
 kboot: better check for tftpserver-arg validity  
 main: boot\_server\_name() checks for kboot-parsed value  
 kboot: Updated kboot.conf sample  
 kboot: Don't crash due to uninitialized settings  
 kboot: initialize speedup setting  
 Try loading files from sda:/ (SATA HDD, FAT32)  
 Updated README with "How to use" information  
   
 17.01.2012  
 Updated README  
 kboot: some fixes to initrd relocation  
 kboot: Fix controller navigation in the menu  
 xenon\_nand: Added rawflash v4 (coded by cOz)  
 main: Look for 'updflash.bin' to process with rawflash v4  
 tftp: prevent spamming incase no tftp-server is found   
 tftp: set maxtries to 10 so it doesn't fail on the first lost TFTP packet  
 main: Print " * Executing" right before actually executing the ELF  
 main: Dont look for seperated initrd.gz on media - it only makes sense with kboot.conf  
 main: no newline for "Bad Header"-message  
   
 24.01.2012  
 kboot: Menu can be aborted via 'C'-key over UART, B or BACK on X360 Controller or B on IR Remote  
 zlib: prevent buffer overflow if uncompressed file is bigger than 32MB  
 kboot: Check gzip file for cpio header without fully extracting it - allows compressed initrd up to 32MB  
 usbdevs/usbctrl: Added rf unit's DEVICE\_ID back to usbctrl\_driver init  
 oops: fixed a possible memory leak  
   
 25.01.2012  
 xb360: additional offets for reloading & updxell  
 main: use predefined color values for console\_init  
 Updated README [/quote] BUGREPORT-Thread: http://libxenon.org/http://libxenon.org//viewtopic.php?t=7  
 Append "Build: XeLL\_Reloaded-testing-git25012012-RC2" when filing a bugreport.  
 If a fatal crash appears (Red Screen with alot of values :P)  
 Append the Stack Dump Values which are shown at the bottom - if there arent any, append the value of sr0 =...

### Attachments

[XeLL_Reloaded-testing-git25012012-RC2_fix1.tar.gz](XeLL_Reloaded-testing-git25012012-RC2_fix1.tar.gz)

## 2012-01-27 02:34:22, posted by: john.wayne

Any news about overscan problem fix? Slim\Hdmi :)  
 Please fix it! 720p )

## 2012-02-15 00:11:49, posted by: SPARK

Thank you very much for posting the new builds

## 2012-02-20 21:51:58, posted by: Xplorer4x4

[quote="tuxuser"] **[b][color=#FF0000]*this is not for flashing to the nand, launch with [url=http://libxenon.org/http://libxenon.org//viewtopic.php?t=4]Xelllaunch[/url] or HvxBootOs*[/color][/b]**  
   
 *Click on the underlined Xelllaunch to get a little How-To[/quote] URL is broken. Says [quote]The topic or board you are looking for appears to be either missing or off limits to you.[/quote]

## 2012-03-01 10:26:01, posted by: FOX 911

thanx

## 2012-06-19 23:01:42, posted by: nikos5800

Can gpu enabled on xell reloaded?

## 2013-04-21 12:13:44, posted by: frgy

can somone tell me step by step how to install updates on xbox im sooooooooo tired of searching............

## 2013-09-23 05:10:00, posted by: dreamboy

[quote="frgy"]  
 can somone tell me step by step how to install updates on xbox im sooooooooo tired of searching............  
 [/quote]  
   
 If you're talking about xell updates here you go:  
 http://libxenon.org/http://libxenon.org//viewtopic.php?t=9  
   
 If you're talking about xbox m$ kernel updates, those kind of questions are not accepted.