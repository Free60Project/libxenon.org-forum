# XeLL Reloaded v0.991 released!

## 2012-02-19 22:48:36, posted by: tuxuser

A new XeLL Reloaded Release is here - v0.991  
   
 Changelog [quote] v0.991 - 19/02/2012  
 ! Fixing booting of Linux Kernel on Reset Glitch Hack Consoles !  
 Write stackdump on fail to screen  
 additional offsets for reloading XeLL/updating XeLL-Reloaded  
 integrated cOz's rawflash application (look at README)  
 probably fixing freezing at "Reinit PHY..."  
 kboot.conf parsing (shows a menu inside XeLL, loads linux and homebrew elfs - look at README)  
 Fixing TFTP ACK on end of file  
 Fixing TFTP transfer for files with only 1 DATA block  
 Fixing possible buffer overflow when uncompressing gzipped file  
 dcbst the memory-range for Devtree and Initrd [/quote] Readme [quote] XeLL-Reloaded  
   
 A Xenon Linux loader based on Xell by tmbinc(Felix Domke)  
   
 Contributed to by:  
 [cOz]  
 Cancerous1  
 Ced2911  
 GliGli  
 Juvenal  
 Natelx  
 Redline99  
 sk1080  
 Tuxuser  
 ... and you?  
   
 XeLL-Reloaded catches CPU threads, sets them up, loads an ELF file from either network (tftp), USB(fat), CDROM (ISO9660) or HDD(fat), and launches it. It's made to boot Linux, so it contains a flat device tree for Linux. However, it is able to load other ELF files as well, like applications based on LibXenon.  
   
 * Now based on LibXenon  
 * Supports the new Reset Glitch Hack - RGH. (xell-gggggg)  
 * XeLL-Reloaded is now divided in 2 stages:  
 - 1st Stage initializes the Hardware, uncompresses and executes 2nd Stage  
 - 2nd Stage (based on LibXenon) loads all required drivers and does the usual "XeLL tasks"  
 * XeLL can unzip & load gzipped files  
 * Support for HDMI, and properly switches NTSC/PAL on composite.  
 * All CPU Cores are active and ready to run at full speed.  
 * TinyEHCI is used, delivers full USB 2.0 speed when accessing mass storage media  
 * lwip network stack upgraded to v1.4 Final - It's faster and DHCP is improved.  
 * It can access the DVD-drive via DMA now: faster reading  
 * It's possible to reload into XeLL now when you are inside a LibXenon Application  
 * New HTTP web interface to retrieve nand dump.  
 * Improved hardware initialization now allows chain-loading.  
 * Supports upgrading with a 2-stage XeLL-Reloaded binary, named "updxell.bin"  
 * Infinite boot loop when looking for ELFs to execute.(no more rushing to get the live-cd in)  
 * Parses / decrypts keyvault  
 * Supports kboot.conf-type file  
 * Supports external initramfs  
 * Can pass a custom CMDLINE to linux kernel via kboot.conf  
 kboot.conf/initrd support - copyright (C) 2010-2011 Hector Martin "marcan" <hector@marcansoft.com>  
 * Shows a user controllable menu for the parsed bootentries   
 xell user prompt - by Georg Lukas "Ge0rg" <georg@op-co.de>  
   
 HOW TO USE  
 ==============  
   
 XeLL Reloaded checks for *.elf(homebrew/linux elf32)/kboot.conf/updxell.bin or updflash.bin in the following order:  
   
 USB (FAT): updflash.bin  
 updxell.bin  
 kboot.conf  
 xenon.elf  
 xenon.z  
 vmlinux  
 Network: DHCP supplied bootserver and bootfile-name. You can supply a static tftpserver ip via kboot.conf. If no tftpserver is found, it falls back to a static ip.  
 ( no updxell or updflash support via tftp)  
 DVD (ISO9660): *same as USB*   
 HDD (FAT): *same as USB*  
   
   
 updflash.bin is a already remapped flashimage/nandimage. 16MB file for 16MB NAND and 64MB file for 64/256/512MB NAND.  
   
 updxell.bin is a renamed xell*.bin file. * Version depending on the used hack (JTAG XeLL: xell-1f, RGH XeLL: xell-gggggg)  
   
 kboot.conf (modified for XeLL) is a configfile  
 General XeLL config: Set TFTP-Server, CPU-Speedup, videomode, NetConfig  
 Menu: Parses bootentries, shows a user controlable menu with XboxController/UART/IR Remote  
 It can parse bootarguments for linux kernels & can load initramfs/initrd   
   
 xenon.elf/xenon.z/vmlinux can be either gzipped or bare ELF32 binaries - LINUX or Homebrew  
   
 There's also a HTTP Server running while XeLL searches for executable binaries.  
 It can serve the CPUKey/DVDKey and the console's flashdump.  
   
   
 UPDATING XELL  
 =================  
   
 1. Rename the appropriate XeLL-binary to "updxell.bin".   
 2. Copy the updxell.bin file to the root of the FAT/FAT32 USB Stick or burn a ISO9660 CD  
 3. Plug in the USB Stick/CD and boot up XeLL. It should find the update and flash it  
 4. Reboot your Xbox and enjoy the fresh XeLL build  
   
 Troubleshooting:  
   
 updxell.bin doesn't get found / updxell process doesn't start: You have to rebuild your whole hackimage with a recent XeLL. From there on you can use the inbuilt update feature  
 updxell function reports that no XeLL binary was found in NAND: Either your XeLL in NAND is too old or it's not a XeLL Reloaded binary - You have to rebuild your whole hackimage with a recent XeLL.  
   
   
 FLASHING NAND  
 =================  
   
 1. Rename the new (already remapped) flashimage to "updflash.bin"  
 2. Copy the updflash.bin file to the root of the FAT/FAT32 USB Stick or burn a ISO9660 CD  
 3. Plug in the USB Stick/CD and boot up XeLL. It should find the update and flash it  
 4. Reboot your Xbox and enjoy the new image  
   
 Troubleshooting:  
   
 XBox does not boot properly after flashing the NAND: Either your image wasn't properly remapped or you made something wrong while building the image  
   
   
 USING KBOOT.CONF  
 ===================  
   
 1. Read and understand the kboot.conf.sample which is part of every XeLL release with kboot-support  
 2. Modify the file to your needs  
 3. Copy it, named as "kboot.conf, to a CD/FAT32 USB Stick/FAT32 HDD or supply it via TFTP  
 4. Boot XeLL and wait till it loads the file and shows the menu  
 5. Navigate to the desired bootentry. You can do this in the following ways:  
 UART:   
 UP/DOWN to go up and down in the menu  
 ENTER to confirm your choice  
 C to cancel the menu  
   
 X360 Controller (1st):  
 DPAD-UP/DPAD-DOWN to go up and down in the menu  
 A to confirm your choice  
 B to cancel the menu  
   
 X360 Media Remote:  
 UP/DOWN to go up and down in the menu  
 OK to confirm your choice  
 Press the NUMBER of the desired bootentry to directly load it  
 B to cancel the menu  
   
 6. Let the bootentry load. Enjoy :)  
   
 Troubleshooting:  
   
 kboot.conf gets found but it doesn't show bootentries or autoloads a bootentry:  
 Make sure timeout is set to something higher than 0  
 Make sure you didn't forget the "" on the bootentry: label="kernelpath params" [/quote]   
 [align=center]**[b]DOWNLOAD: [url=http://www.libxenon.org/http://libxenon.org//viewtopic.php?p=1530#p1530]Thread[/url][/b]**[/align]

## 2012-02-20 00:20:14, posted by: luke69

Awesome! Thanks ;D

## 2012-02-20 16:27:27, posted by: Doerek

Now...let's do the guys from Libxenon.org a favor:  
 ~> Spread this news to every JTAG/RGH User/Community.

## 2012-02-20 17:57:49, posted by: john.wayne

will it fix overscan problem?

## 2012-02-20 21:29:31, posted by: JPizzle

thanks for the update guys, appreciate all your hard work. ;)

## 2012-03-01 18:32:43, posted by: greator

[quote="tuxuser"]  
 FLASHING NAND  
 =================  
   
 1. Rename the new (already remapped) flashimage to "updflash.bin"  
 2. Copy the updflash.bin file to the root of the FAT/FAT32 USB Stick or burn a ISO9660 CD  
 3. Plug in the USB Stick/CD and boot up XeLL. It should find the update and flash it  
 4. Reboot your Xbox and enjoy the new image  
   
 Troubleshooting:  
   
 XBox does not boot properly after flashing the NAND: Either your image wasn't properly remapped or you made something wrong while building the image  
 [/quote]  
   
 So does this mean that, Rawflash is not needed anymore?  
 I can flash image without opening rawflash xenon.elf?

## 2012-03-02 01:33:56, posted by: tuxuser

[quote="greator"]  
 So does this mean that, Rawflash is not needed anymore?  
 I can flash image without opening rawflash xenon.elf?  
 [/quote]  
   
 Correct!

## 2012-03-16 20:22:19, posted by: greator

Unfortunately, this doesn't work for me. It just cant glitch.  
 First I thought it must be my wiring. But when I flash the old [xell-reloaded-2stage-2011-09-23], it works.   
 So its not my wiring, its just that new ecc file doesn't work on me. :(