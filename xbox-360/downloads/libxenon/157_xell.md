# XeLL

## 2011-09-01 03:40:32, posted by: tuxuser

XeLL is the Xenon Linux Loader.   
 XeLL catches CPU threads, sets them up, loads an ELF file from either network (tftp) or CDROM (ISO9660), and launches it. It's made to boot linux. Thus it also contains a flat device tree for linux. However, it should be able to load other ELF files as well, like apps based on libXenon.  
 lwIP (http://www.sics.se/~adam/lwip/) is used for networking.  
 XeLL is available at http://free60.git.sourceforge.net/git/gitweb.cgi?p=free60/xell;a=summary  
   
 Update:Xell-reloaded, by Cancerous, [cOz], Ced2911,GliGli, RedLine99 and Tuxuser, based on original xell is available below.

## 2011-09-01 03:43:16, posted by: Cancerous1

The old build, this will work with jtags only

### Attachments

[xell-reloaded-1stage.rar](xell-reloaded-1stage.rar)

## 2011-09-01 03:45:44, posted by: tuxuser

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
   
 update: Should work fine with xellLaunch now

### Attachments

[xell-reloaded-2stage-9-4-11.rar](xell-reloaded-2stage-9-4-11.rar)

## 2011-09-23 18:57:38, posted by: GliGli

This is maily a bugfix release, quick changelog: [list] - [*]Fixed web interface download speed.
 - [*]Fixed boot loop messages not clearing properly.
 - [*]Added a 15 sec delay to have a chance to cancel updxell process.
 - [*]Fixed ata init.
 - [*]Libxenon improvements (controller leds,...).
[/list] Enjoy =)

### Attachments

[xell-reloaded-2stage-2011-09-23.rar](xell-reloaded-2stage-2011-09-23.rar)

## 2012-02-19 22:44:07, posted by: tuxuser

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
 dcbst the memory-range for Devtree and Initrd [/quote]

### Attachments

[XeLL_Reloaded-2stages-v0.991.tar.gz](XeLL_Reloaded-2stages-v0.991.tar.gz)

## 2013-08-27 16:55:07, posted by: tuxuser

[quote] v0.992 - 09/08/2013  
 ! Corona video support !  
 * NTSC gives weird black/white screen  
 eMMC Reading support for Corona consoles (no flashing!)  
 * Not working when launched via XellLaunch  
 Rawflash verify features  
 Cygnos/DemoN builds included - 38400 UART baudrate  
 Logfile writing to USB or HTTP Webinterface  
 Dumps ANA-Registers to UART / Logfile  
 "Shutdown" and "Reboot" via HTTP Webinterface  
 Option to disable Network via xell config  
 Support for all 3 USB busses  
 * Crashing when USB is plugged out or attached at runtime  
 Switched from zlib to puff (smaller) [/quote]   
   
 Download: [url=http://file.libxenon.org/xell/XeLL\_Reloaded-2stages-v0.992.tar.gz]Click[/url]

## 2013-08-28 20:57:55, posted by: tuxuser

[quote] v0.993 - 28/08/2013  
 Disabled USB writes for the logfile (not working with EXT# anyways  
 Fixed the crashing when unplugging USB memories at runtime  
   
 v0.992 - 27/08/2013 * Released by a trigger happy Tuxuser *  
 ! Corona video support !  
 * NTSC gives weird black/white screen  
 eMMC Reading support for Corona consoles (no flashing!)  
 * Not working when launched via XellLaunch  
 Rawflash verify features  
 Cygnos/DemoN builds included - 38400 UART baudrate  
 Logfile writing to USB or HTTP Webinterface  
 Dumps ANA-Registers to UART / Logfile  
 "Shutdown" and "Reboot" via HTTP Webinterface  
 Option to disable Network via xell config  
 Support for all 3 USB busses  
 * Crashing when USB is plugged out or attached at runtime  
 Switched from zlib to puff (smaller)  
 Support for mounting 1 USB memory device at runtime  
 Better support for big USB devices (or poorly formatted ones) [/quote] Download: [url=http://file.libxenon.org/xell/XeLL\_Reloaded-2stages-v0.993.tar.gz]Click[/url]