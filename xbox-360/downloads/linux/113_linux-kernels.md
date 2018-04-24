# Linux Kernels

## 2011-06-20 01:39:05, posted by: tuxuser

This is a thread where different Linux Kernel Downloads get stored

## 2011-06-26 20:30:11, posted by: tuxuser

Linux-Kernel 2.6.39 Xenon Patch [experimental]  
   
 http://file.libxenon.org/free60/linux/kernel/patch-2.6.39-xenon0.11.diff  
 http://file.libxenon.org/free60/linux/kernel/xenon-config

## 2011-06-26 20:35:59, posted by: tuxuser

Should be 2.6.36.4 Kernel with a fix to not spinlock that often (if spinlocks appear, most likely cause of the audio driver)  
   
 http://file.libxenon.org/free60/linux/kernel/vmlinux-nospinlock-sda2.tar.gz

## 2011-06-26 20:47:45, posted by: tuxuser

Initramfs for the Ubuntu LiveCD (beta 5) to create your custom Kernel for the LiveCD

### Attachments

[casper-initramfs-ubuntu-maverick_21032011.tar.gz](casper-initramfs-ubuntu-maverick_21032011.tar.gz)

## 2011-06-26 20:58:46, posted by: tuxuser

LiveCD Kernel for Ubuntu 10.10 Beta5  
   
 * noSMP (no hyperthreading - less spinlocking)  
 * Updated from 2.6.36.2 to 2.6.36.4  
 * Included WiFi Drivers for the Marvell Chipset (Original Xbox360 Wifi Adapters)

### Attachments

[linux-2.6.36.4-liveCD-noSMP-WiFi_test2.tar.gz](linux-2.6.36.4-liveCD-noSMP-WiFi_test2.tar.gz)

## 2014-08-05 08:34:38, posted by: <Unknown User>

Compiled a 3.10.51 kernel for xbox (released 2014-07-31): [url=https://dl.dropboxusercontent.com/u/7550894/xbox/vmlinux-3.10.51-xbox0.11.1.zip]vmlinux-3.10.51-xbox0.11.1.zip[/url]

### Attachments

[config-3.10.51-xbox0.11.zip](config-3.10.51-xbox0.11.zip)[patch-3.10.51-xbox0.11.1.zip](patch-3.10.51-xbox0.11.1.zip)

## 2016-01-10 12:02:01, posted by: <Unknown User>

is there a way i could edit the xeLL bootloader-sda2-v2.6.24.3.tar.gz to the right root= parameter? because i am getting this error-   
   
 cannot open root device "sda2" or unknown-block(8,2) please append a correct "root=" boot option; here are the available partition;  
 0b00 1048575 sr0 driver: sr  
 0800 312571224 sda driver: sd  
 kernel panic - not syncing: VFS: Unable to mount root fs on unknown-block(8,2)  
   
 or another easy way someone can help me i'm not an expert in linux to put it mildly...