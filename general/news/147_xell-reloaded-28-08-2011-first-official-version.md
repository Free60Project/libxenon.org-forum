# XeLL Reloaded 28/08/2011 : First Official Version

## 2011-08-28 21:45:08, posted by: Razkar

Besides the "Reset Glitch Hack" there's another big announcement!   
 Cancerous, [cOz], Ced2911,GliGli, RedLine99 and Tuxuser are proud to release today the first official version of XeLL-Reloaded (Codename: 2Stages)  
   
 Here's a list of the major improvements:  
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
 * Parses / decrypts keyvault (either with real or virtual CPUkey) [/quote] For now, there is still a little work to do on the nandflasher so this feature is disabled and a update will comes in the following weeks.  
 If you have a Jtag console, you can update XeLL with tuxuser's apps : XeLL Updater or LxNANDFlasher (Use at your own risks).  
   
 **[b]Download:[/b]** [url=http://libxenon.org/http://libxenon.org//viewtopic.php?p=732#p732]Thread[/url]

## 2011-08-28 21:54:51, posted by: SpkLeader

Yay!  
 Thank you Razkar and everyone involved :)

## 2011-08-29 22:53:49, posted by: chriss179

Hey, i have tried this in combination with dashlaunch's xell launcher and i have the feeling that my usb stick is somehow lagging xell-reloadeds startup. When i run xell with eject button it's much faster then with dashlaunch's xell launcher. I believe after 2 minutes i powered down because i was tired of waiting any longer for it to init usb.. maybe dashlaunch's xell launcher isn't compatible??? Or can it be the usb stick??? Sandisk cruzer 8gb???? I guess not if it works smoothly when powering on using eject to launch xell-reloaded immediatly right??   
   
 Anyways, system info:   
 Motherboard revision: Xenon  
 Video cable: Vga  
 system dashboard revision: 13599  
 dvd drive and firmware: Sammy LT 1.9  
 Using dashlaunch 2.23b to boot into freestyle dash RC 2.1

## 2011-08-29 22:56:25, posted by: Cancerous1

there have been a lot of reports of problems a new build is in the works

## 2011-08-29 23:07:46, posted by: chriss179

Thx, great!

## 2011-08-29 23:21:21, posted by: dreamboy

[quote="chriss179"]  
 Hey, i have tried this in combination with dashlaunch's xell launcher and i have the feeling that my usb stick is somehow lagging xell-reloadeds startup. When i run xell with eject button it's much faster then with dashlaunch's xell launcher. I believe after 2 minutes i powered down because i was tired of waiting any longer for it to init usb.. maybe dashlaunch's xell launcher isn't compatible??? Or can it be the usb stick??? Sandisk cruzer 8gb???? I guess not if it works smoothly when powering on using eject to launch xell-reloaded immediatly right??   
   
 Anyways, system info:   
 Motherboard revision: Xenon  
 Video cable: Vga  
 system dashboard revision: 13599  
 dvd drive and firmware: Sammy LT 1.9  
 Using dashlaunch 2.23b to boot into freestyle dash RC 2.1  
 [/quote]  
   
 Same here with Jasper 16mb jtag, also after initial lag it doesnt detect xenon.elf on my usb stick just goes to tftp.  
   
 The new feactures sound awsome :) great work everyone

## 2011-08-31 01:24:34, posted by: trash

hi, i have a jtagged jasper with cygnos, freeboot 13599 and dashlaunch 2.23b are installed.  
 i have updated my xellous with xell-updater 1.2 and now i have installed the new xell reloaded.  
 the question is: why do i miss che cpukey and dvdkey info? am i doing something wrong? i didn't have this problem with any xell before.  
   
 i paste my cygnos log: [code]* * \_\_ \_\_\_\_ \_\_\_ \_\_\_ \_\_\_\_\_ / \_|\_ \_\_ \_\_\_ \_\_\_| \_\_ ) / \_ \ / \_ \\_ \_| | |\_| '\_\_/ \_ \/ \_ \ \_ \| | | | | | || | | \_| | | \_\_/ \_\_/ |\_) | |\_| | |\_| || | |\_| |\_| \\_\_\_|\\_\_\_|\_\_\_\_/ \\_\_\_/ \\_\_\_/ |\_| [v0.07 - inspired by ikari] booting xell.... XeLL - First stage * Attempting to catch all CPUs... * place\_jump ... * while ... CPUs online: 3f.. * success. * Decompressing stage 2... * Loading ELF file... 0x00000000 0x00034bf8, Loading .text...done 0x00034bf8 0x000005cc, Loading .elfldr...done 0x000351c8 0x00006518, Loading .data...done 0x0003b6e0 0x00000214, Loading .got2...done 0x0003b8f8 0x0000005c, Loading .sdata...done 0x0003b958 0x000088b8, Loading .rodata...done 0x00044210 0x0000002c, Loading .eh\_frame\_hdr...done 0x0004423c 0x0000011c, Loading .eh\_frame...done 0x00044360 0x00722f14, Clearing .bss...done 0x00767274 0x00000080, Clearing .sbss...done * GO (entrypoint: 0000000000009a00) Xenos GPU ID=5831 GPU Clock at 500 MHz MEM Clock at 650 MHz EDRAM Clock at 1800 MHz FSB Clock at 2700 MHz DVD cover state: 64 AVPACK detected: 53 . ana disable . ana enable ................................................................................... . f1 . f2 * Xenos FB with 74x33 (640x576) at 0x9e000000 initialized. XeLL - Xenon linux loader second stage 0.99-git- 2011-08-28 (root@posnix i686) * nand init * network init * initializing lwip 1.4.0.r2... Reinit PHY... Waiting for link...link up! * requesting dhcp.................................failed * now assigning a static ip * starting httpd server...success * usb init * Initialising USB EHCI... Initialising EHCI bus 0 at 0xea003000 Initialising EHCI bus 1 at 0xea005000 EHCI bus 1 port 5: low speed, releasing to OHCI * Initialising USB OHCI... USB bus 0 device 1: vendor 0000 product 0000 class 09: USB Hub USB bus 1 device 1: vendor 0000 product 0000 class 09: USB Hub USB: New device connected to bus 1 hub 1 port 5 USB bus 1 device 2: vendor 045E product 0291 class FF: Xbox 360 Controller attched controller 0 [/code]   
 thank you for your hard work!!  
 and.. i do prefer the matrix style color.. or even a more stylish black background and red text :P  
 bye  
   
 EDIT: oh, and since i'm not having a dhcp ip, what's the default static one? thanks.

## 2011-09-01 00:49:06, posted by: tuxuser

[quote="trash"]  
 hi, i have a jtagged jasper with cygnos, freeboot 13599 and dashlaunch 2.23b are installed.  
 i have updated my xellous with xell-updater 1.2 and now i have installed the new xell reloaded.  
 the question is: why do i miss che cpukey and dvdkey info? am i doing something wrong? i didn't have this problem with any xell before.  
 [/quote]  
 Nope you are not doing anything wrong, problem is xell-launch in that relation. Since the latest tinyehci fixes to XeLL, Xell-Launch and Xell Reloaded arent good friends anymore :P. You got a private message concerning that issue ;)  
   
 [quote="trash"]  
 and.. i do prefer the matrix style color.. or even a more stylish black background and red text :P  
 [/quote]  
 Check the xell git repository and set [code]* *//#define DEFAULT\_THEME [/code] in config.h  
   
 [quote="trash"]  
 DIT: oh, and since i'm not having a dhcp ip, what's the default static one? thanks.  
 [/quote]  
   
 its 192.168.1.99

## 2011-09-01 03:00:25, posted by: Shadow LAG

Updated Xellous Freeboot 13599 using Xell Updater 1.2 and updxell.bin (xell-2f) and rebooter works fine but pressing the eject button leads to no video on a Xenon (opus?) motherboard (component cables) the controller acts like it is trying to sync too, the build in sneakypeanut's builder works fine but it isn't the same as the official release I take it, can't figure out what's causing this issue...  
   
 EDIT: Didn't see the new update :D will be using this with Xell-Launch then :P  
   
 EDIT2: or not... [quote]The topic or board you are looking for appears to be either missing or off limits to you.[/quote]

## 2011-09-01 03:56:07, posted by: tuxuser

Link is fixed. Thx for reporting the issue.

## 2011-09-01 03:56:47, posted by: trash

@tuxuser: thanks for your answer. i wasn't using xelllaunch anyway, i was trying with the default freeboot option of powering on with eject button.  
 i'll do some tries with xelllaunch later today, thanks!  
 and i'll try to change the theme color too! yay XD  
 bye!  
   
   
 EDIT: ok, after some testing:  
 when booting with eject button, it hangs forever after the 0 attched controller text;  
 when booting with xelllaunch got from dashlaunch2.23b package, it hangs for some seconds at the same text as before, then it proceeds normally;  
 when booting with tuxuser's xelllaunch it's everything perfect. no hangs.  
   
 oh, and i managed to put the matrix theme back :P  
 [s]is there an easy way to change colors on my own style? i'm a total noob, by the way. just asking.[/s] nevermind, i found out how to do it.  
 bye!

## 2011-09-07 07:47:15, posted by: ravendrow

k so the only problem i have had so far is that i cant get video with composite i can get it just fine with normal AV but not with composite anyone have an idea of what i need to change in the source files to get my composite working again? oh yeah and i have to ask are there any other color options you guys have hidden in there? already changed to matrix theme but i kinda agree red on black would look awesome. thanks for all your hard work cant wait to see what you guys do next kinda sad to say this but i have been jtagging boxes for years and never thought to look into libxenon that is gonna have to change ;D