# Some question about xell reloaded future

## 2011-03-14 17:35:51, posted by: val532

Hi,  
   
 I have some idea for xell reloaded.  
 First : a version whitout any thing like CPU key or DHCP and other stuf, just lauch vmlinux. (for speed)  
   
 And is it posible to lauch vmlinux on HDD (sata or usb) in an other files system (like ext2 or 3) ?  
   
 PS: sory for my bad english i'm a french studiant.

## 2011-03-15 00:01:05, posted by: Cancerous1

no problem, yes you can install Linux to a hdd, there are some scripts posted here to install Debian 6 Squeeze or Mint if you prefer, check out the Linux section.   
   
 As for speed, it loads the kernel very very quickly. You could build it from source and choose not to display the fuses if you are comfortable in code, but we will most likely want to retain all of Xell's features. I don't think hiding the fuse info would take any time off the boot  
   
 [align=center][youtube]http://www.youtube.com/watch?v=4B9sLgJXdgs[/youtube][/align]

## 2011-03-15 00:47:57, posted by: val532

Ok I'm going to see that I tried.  
   
 But for xell the party's longest home is DHCP (because the console is not connected to the network).  
   
 And we can start a distribution directly from the internal HDD?

## 2011-03-15 13:41:38, posted by: carlrivest1

I don't think the current build of xell reloaded can start linux from internal HDD (Sda2), i tried and it did not work. How ever, i think it can start from usb. Ill try that when i get back home from work tonight.

## 2011-03-15 15:45:01, posted by: Cancerous1

I have a kernel on my usb as xenon.elf, built to load from sda2, and xell reloaded works just fine with it. Currently Xell isn't looking for the kernel on the hdd so you have to use a kernel on your usb/a cdrom/ or tftp to boot Linux. You can look at the wiki at free60.org for more info.

## 2011-03-15 18:44:20, posted by: charlo.charli

Does anyone tried to boot a XBMC distribution installed on internal/external HDD with a xenon.elf on USB poiting to it?! Can it be possible?

## 2011-03-15 19:55:58, posted by: val532

Ok i don't understand how to make a kernel ^^. And how to config the kernel to boot the sda in place of USB/Cdrom.

## 2011-03-16 00:51:44, posted by: tuxuser

[quote=""val532""]Ok i don't understand how to make a kernel ^^. And how to config the kernel to boot the sda in place of USB/Cdrom.[/quote]  
   
 I will make a tutorial tomorrow.

## 2011-03-16 01:36:00, posted by: charlo.charli

Really nice and thanks a lot tuxuser ;)

## 2011-11-23 23:46:49, posted by: Valerie

[quote="Cancerous1"]  
 I have a kernel on my usb as xenon.elf, built to load from sda2, and xell reloaded works just fine with it. Currently Xell isn't looking for the kernel on the hdd so you have to use a kernel on your usb/a cdrom/ or tftp to boot Linux. You can look at the wiki at free60.org for more info.  
 [/quote]  
 This worked for me, thank you very much...  
 (sry bout the bump)