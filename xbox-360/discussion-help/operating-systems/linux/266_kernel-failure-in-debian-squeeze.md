# Kernel Failure in Debian Squeeze. 

## 2012-01-11 15:02:48, posted by: Ethereal

Hi to everyone.  
   
 This is my first post, although I've been reading tuts and news for months now, after have the RGH performed on my Jasper.  
   
 Well, so I managed to install Debian Squeeze on a Xbox Drive, and it boots fine with the sda2 bootloader provided here (Kernel 2.6.34)  
   
 My 360 is connected to my TV via HDMI. When Debian starts, after login screen, it warns me of a Kernel failure. Everytime. Looking at the details, it shows me the following:   
   
 BUG: sleeping function called from invalid context at mm/slab.c:3101...module Metacity, showing a stack with rows starting with pcm\_, clearly a failure of the audio driver.  
   
 I cannot post the entire error log here, I'm doing it as soon as i can, as I'm not at home now, but this is the persistent error.  
   
 As a consequence, every module or program that uses the audio driver, as Movie Player, VLC, etc, fails and closes.  
   
 I tried to compile a new kernel, version 2.6.38.8 with .diff and .config from http://vserver.13thfloor.at/Stuff/XBOX360/. The kernel is compiled with no errors and the OS boots fine but the error persists.   
   
 I also noticed that during the boot process,several warnings are produced because of some missing modules. How can I obtain those modules? Do i need to build them in the Kernel config before compile it?  
   
 At the end of the boot process, it gives me a warning about the ALSA module, saying that it cannot modify the settings or something like this.  
   
 Any clues on how to resolve the issue or point me in the right direction?  
   
 In http://file.libxenon.org/free60/linux/src/ there is a "xenon\_snd.c" file. It seems quite recent. How can I apply it?  
   
 http://libxenon.org/http://libxenon.org//viewtopic.php?t=3 Here there's a post from tuxuser to download these files:  
   
 http://file.libxenon.org/free60/linux/kernel/patch-2.6.39-xenon0.11.diff  
 http://file.libxenon.org/free60/linux/kernel/xenon-config  
   
 But they are now offline. Can anyone upload them again, please?  
   
 Thank you in advance.  
   
 Ethereal.

## 2012-01-11 20:17:07, posted by: covenant

Boot and see if /proc/config.gz exists. If so, gunzip it and grep for XENON to seeif xenon-snd is already monolithically built into that kernel or not. If not, you are going to have to compile a new one.  
   
 All file.libxenon.org links are down as I think tuxuser was having some trouble with the server/fs.   
   
 I have a working (compiles and resulting kernels boot, all xenon-specific modules work etc) 2.6.28-rc3 kernel source tree. It's a bit of a mess and not something I would want to produce a diff from. However, as the server is down, I'll do a make clean and upload a tarball (I'll leave my current .config in place for reference though) of the source tree so that you can compile from that if you want to.   
   
 I would just upload a binary kernel+modules for you but my .config is pretty bare at present because I am debugging on slim and so have most things off/disabled.  
   
 I'll post a link to the source tree once I have cleaned, tar'd and uploaded.  
   
 Here you go. This compiles successfully using a toolchain buillt ~1 week ago. HTH: http://www.multiupload.com/4YDQTZN1N3

## 2012-01-12 22:05:15, posted by: Ethereal

First of all, Thank you...Wasn't expecting such a fast and kind answer.  
   
 Still have to check if config.gz is present but...  
   
 Downloaded the kernel, checked if all the modules I needed were present and tried to compile it.  
   
 It compiled fine (well, it returned a lot of warnings about some options defined as old but not used, but I edited Makefile to hide them).  
   
 Then I edited "CONFIG\_CMDLINE" with root=sda2 but when I tried to boot Squeeze, it returns me some errors on the HDD and cannot find root SDA2 and end to panic.  
   
 I went back to boot with my previous kernel, based on 2.6.38.8, and it booted fine (well, same situation as of my first post). Same with kernel 2.6.34.  
   
 Is there something else I need to edit to let the kernel find sda2?  
   
 Again, thank you and to anyone else who would contribute to this topic.

## 2012-01-13 08:37:41, posted by: covenant

root=/dev/sda2 perhaps?

## 2012-01-13 10:25:02, posted by: tuxuser

http://file.libxenon.org/free60/linux/kernel/patch-2.6.38.8-xbox0.11.1.diff  
   
 Gave some errors for me with ata tho, feel free to try anyways

## 2012-01-13 13:15:08, posted by: Ethereal

Thanks Covenant,  
   
 No, I double checked, just to be sure, and there wasn't any typo, i wrote only sda2 in the post.  
   
 Anyway, I'm gonna recompile it again this afternoon and let you know.  
   
 Thanks tuxuser for the .diff. Is there a diff also for 2.6.39 as shown in your post in Linux Kernel section?

## 2012-01-13 13:45:34, posted by: tuxuser

nope, there's no workin diff for 2.6.39, I ported the patches to this version some time ago... but it didnt work properly, thats why only 2.6.38.8 got posted and uploaded now, sorry.  
   
 to your problem: you should read about netconsole or get uart soldered so you can provide a detailed errorlog.

## 2012-01-13 15:57:49, posted by: covenant

[quote="tuxuser"]  
 to your problem: you should read about netconsole or get uart soldered so you can provide a detailed errorlog.  
 [/quote]  
   
 Debugging via UART makes things a LOT easier, I strongly recommend it although netconsole will give you the same but without needing hardware modification.

## 2012-01-13 18:49:09, posted by: Ethereal

This is the error stack in Squeeze. It follows warning on "couldn't load modules.dep" and an ALSA warning. Kernel loaded is 2.6.36.4 as posted on this site.  
 [code]* *Kernel failure message 1: BUG: sleeping function called from invalid context at mm/slab.c:3101 in\_atomic(): 0, irqs\_disabled(): 1, pid: 2089, name: metacity Call Trace: [c000000017093510] [c00000000000f8f8] .show\_stack+0x6c/0x16c (unreliable) [c0000000170935c0] [c00000000002e818] .\_\_might\_sleep+0x10c/0x124 [c000000017093640] [c0000000000b93b4] .kmem\_cache\_alloc+0x50/0x128 [c0000000170936e0] [c0000000000abc08] .\_\_get\_vm\_area\_node+0xc8/0x168 [c0000000170937a0] [c0000000000257cc] .\_\_ioremap\_caller+0x7c/0x118 [c000000017093840] [c00000000042000c] .snd\_xenon\_playback\_prepare+0x68/0x294 [c0000000170938f0] [c000000000412e6c] .snd\_pcm\_do\_prepare+0x34/0x70 [c000000017093970] [c0000000004129fc] .snd\_pcm\_action\_single+0x80/0xf8 [c000000017093a10] [c000000000415748] .snd\_pcm\_action\_nonatomic+0x64/0x94 [c000000017093aa0] [c000000000418a84] .snd\_pcm\_common\_ioctl1+0x4d0/0xbf0 [c000000017093b90] [c000000000419a74] .snd\_pcm\_playback\_ioctl1+0x424/0x45c [c000000017093c50] [c000000000419ccc] .snd\_pcm\_ioctl\_compat+0x220/0xc24 [c000000017093d60] [c00000000010f310] .compat\_sys\_ioctl+0x170/0x3a0 [c000000017093e30] [c00000000000752c] syscall\_exit+0x0/0x40 [/code] Any help?