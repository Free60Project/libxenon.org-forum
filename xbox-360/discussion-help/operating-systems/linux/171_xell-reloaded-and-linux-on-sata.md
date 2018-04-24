# Xell-Reloaded And Linux on Sata

## 2011-09-17 01:33:35, posted by: SoulHeaven

Hello and thanks for your great work.  
   
 I would like to install your Ubuntu xenon linux on my "Glitched" Slim on the internal Hard Drive.  
   
 I know that the FATX is not working, but with a spare HD is it possible ?  
   
 AFAIK, the xell reloaded is looking for xenon.elf only on DVD and USB...  
   
 Please advise :)  
   
 Best Regards  
   
 EDIT : I also tried to boot unbuntu xenon linux from an usb key, result : xenon.elf found...executing.... and nothing :(. Is it normal ? What do I have done wrong ?

## 2011-09-21 11:32:40, posted by: SoulHeaven

No reply ?

## 2011-09-21 18:19:57, posted by: Cancerous1

Well, there are already threads here about running a live-cd from usb, or running linux from the hdd. But the Slim is new hardware not many people have experience trying Linux on yet.   
   
 So far I've only heard of success running a kernel compiled with the option NR\_CPUS=1 on slims. This is most likely the problem you ran into when trying to run the Ubuntu livecd on USB. There are tutorials for building kernels here also.

## 2011-09-21 20:11:53, posted by: covenant

[quote="Cancerous1"]  
 So far I've only heard of success running a kernel compiled with the option NR\_CPUS=1 on slims. This is most likely the problem you ran into when trying to run the Ubuntu livecd on USB. There are tutorials for building kernels here also.  
 [/quote]  
 Exactly the info I spent most of last night looking for! Many thanks for this - it seems like good enough reason to get the cross compilation environment sorted out now that my slim successfully glitches.

## 2011-09-21 21:23:48, posted by: tuxuser

Would suggest passing "nosmp maxcpus=1" with the kernel's CMDLINE... also you have to edit SATA\_XENON to say SATA\_XENON=n in the kernel-config

## 2011-09-23 01:34:58, posted by: covenant

I notice that a .config for 2.6.39 is available here:  
 [url=http://file.libxenon.org/free60/linux/kernel/xenon-config]http://file.libxenon.org/free60/linux/kernel/xenon-config[/url]  
   
 But that the latest patch against the linux source tree is 2.6.38.8 here:  
 [url=http://file.libxenon.org/free60/linux/kernel/patch-2.6.38.8-xbox0.11.1.diff]http://file.libxenon.org/free60/linux/kernel/patch-2.6.38.8-xbox0.11.1.diff[/url]  
   
 As the link to a 2.6.39 patch in the second post of this thread is broken:  
 [url=http://libxenon.org/http://libxenon.org//viewtopic.php?t=3]http://libxenon.org/http://libxenon.org//viewtopic.php?t=3[/url]  
   
 Would anyone with the patch (or who is willing to diff their source tree) post it to save me having to convert the 2.6.38.8 patch to 2.6.39?   
   
 Incidentally, compilation of pre-2.6.39 kernels fails when using gcc-4.60 (Ubuntu 11) due to a problem that has now been fixed in 2.6.39. Details here, although the patch is not compatible with earlier kernels:  
   
 [url=http://lists-archives.org/linux-kernel/27468313-ppc64-fix-build-error-when-compiling-with-gcc-4-6-0.html]http://lists-archives.org/linux-kernel/27468313-ppc64-fix-build-error-when-compiling-with-gcc-4-6-0.html[/url]

## 2011-09-23 06:59:11, posted by: tuxuser

that 2.6.39 patch was removed on purpose as it was extremly slow.

## 2011-09-27 23:04:56, posted by: covenant

Some time later..... :)  
   
 Well, I have a 2.6.38-rc3 kernel booting successfully on my Slim. Init is another matter but one thing at a time, eh?   
   
 [s]I tried using nfsroot for a while but it's like watching paint dry so I ended up patching init/do\_mounts.c to add delay/retry for rootfs mounting so that the kernel would have time to discover my USB HDD instead of just being crap and panicking.   
   
 See: [url=http://marc.info/?l=linux-kernel&m=110445705104787&w=2]http://marc.info/?l=linux-kernel&m=110445705104787&w=2[/url] for the patch (although I realise I could have used a bash script in an initramfs to achieve the same thing).   
   
 Interestingly, the patch cycled through the retries, correctly identified the USB HDD but still panicked if I specified root=/dev/sda2 (root is ext3 of 2nd partition). However, the kernel immediately identified /dev/sda2 if I specified root by the device number (in this case, 'root=0802' in CONFIG\_CMDLINE). Incidentally, my rootfs is the gentoo fs extracted from the most recent LiveCD posted on these fora.[/s]  
   
 EDIT: <facepalm> [code]rootdelay = [/code]   
 Current CONFIG\_CMDLINE: [code]"root=0802 video=xenonfb maxcpus=1 nosmp"[/code] All of this is great but I now find that init hangs on 'Starting udevd....' (sorry, no serial console connected yet so no way to post logs). Whilst I am certainly **[b]not[/b]** looking for 'show me step by step help', I was wondering if anyone else has had success booting a slim, has encountered something similiar and can shed any light as I'm damn close to a login prompt now?  
   
 **[b]UPDATE[/b]**: Got it to boot 2.6.38-rc3 to a console with kbd access with the gentoo rootfs on USB. It's a mess but it boots. Will post .config etc. if anyone wants it.

## 2011-10-03 09:08:57, posted by: tydye81

Yes can you please post a package of this? Ive spent so many hours trying to get this to work

## 2011-10-03 12:55:26, posted by: covenant

Will see what I can do when I get home tonight. It won't be a 'package' because it's all a mess at present and so not worth packaging in any way. Happy to post kernel .config and notes on other changes made to get it to boot.

## 2011-10-03 21:49:36, posted by: covenant

OK, here you go. I can't guarantee that this will work 100% of the time for you. I still get kernel panics during boot although, as long as you don't push it too hard, it's largely stable once booted.  
   
 I'm using a vanilla 2.6.38-rc3 with the 0.12 xbox patch from here applied: [url=http://vserver.13thfloor.at/Stuff/XBOX360/]http://vserver.13thfloor.at/Stuff/XBOX360/[/url]. I started with a .config from the same URL and used that as a basis for the .config posted here.  
   
 My current [font=courier].config[/font] is linked hereafter. It's got most of everything switched off, including a lot of the xenon platform-specific hardware. It's highly likely that a number of things, when enabled in kernel, will start working but, then again, they may break the boot. That pretty much encapsulates what I am working with at present (well, would be working on, if Real Life didn't keep intruding and denying time to work on this): playing about with different kernel configs to see what works, what doesn't and what breaks.  
   
 I am not entirely clear on the cause of the kernel panics but they may have something to do them tracing to [font=courier]/include/asm/atomic.h[/font]. I lack smarts and time for this problem and have only got as far as spotting that this file's seen attention in libxenon ([url=http://free60.git.sourceforge.net/git/gitweb.cgi?p=free60/libxenon;a=blob\_plain;f=libxenon/drivers/ppc/atomic.S;hb=5a9ab4c6e33e0e8609e0a953712582ea1ff90911]http://free60.git.sourceforge.net/git/gitweb.cgi?p=free60/libxenon;a=blob\_plain;f=libxenon/drivers/ppc/atomic.S;hb=5a9ab4c6e33e0e8609e0a953712582ea1ff90911[/url]).   
   
 You can't compile the kernel without having [font=courier]PPC\_DISABLE\_WERROR[/font] set. When this is not set, the compilation fails with exactly this error and can be traced back to the file [font=courier]/include/asm/pgtable-ppc64.h[/font].  
   
 You will definitely want to change [font=courier]CMDLINE\_BOOL[/font] as I am currently booting from a usb hard disk with that device ID and have not idea what setup you are using. Alter to suit your root partition preference; I have the kernel on a vfat partition (sda1) and the rootfs on ext3 (sda2). Specifying the device name to the [font=courier]root=[/font] arg in the /dev/XXX format gave me a kernel panic but using the device number worked perfectly (as long as I had a delay during boot for the USB disk containing the rootfs to be detected).  
   
 The rootfs is a modified 2011 Gentoo LiveCD. If you are using similar, you'll also want to add a value for [font=courier]rootdelay = XX[/font] into this series of options. I patched my 2.6.38-rc3 kernel source with the patch I mentioned in my previous post but, after the event, discovered the [font=courier]rootdelay[/font] switch which obviates the need for the patch. You'll also need [font=courier]maxcpus=1[/font] and [font=courier]nosmp[/font], as mentioned above.   
   
 Finally, for [font=courier]CMDLINE\_BOOL[/font], the config I am posting has single user mode set as this gives you the best chance of booting to a usable shell. Don't get me wrong, you can boot to multi-user but I found that this made panics during boot more likely. For what I want from a shell at the moment, it does what's necessary (grabbing boot time logs, examining hardware characteristics etc) as the panics need fixing first.   
   
 udev also seems very broken at the moment but, once the kernel problems are fixed, will be OK I am sure. I have had problems with virtual devices like /dev/urandom. There's lots to do!  
   
 Don't forget to edit the Live CD [font=courier]/etc/fstab[/font] and turn anything non-essential off in [font=courier]/etc/runlevels[/font]. It's worth writing a script to dump the useful boot time logs (dmesg etc.) at different times during the boot process to stand a chance of catching what's triggering errors. Quite a lot of errors end up hanging the kernel before much logging has started writing to disk, so you miss out on crash info whenever you boot kernels that force a hard reset.   
   
 Good Luck!  
   
 kernel .config: [url=http://pastebin.com/C0NDgPrU]http://pastebin.com/C0NDgPrU[/url]