# Add sata loading

## 2011-03-29 18:52:30, posted by: val532

Hi,  
   
 I have one HDD (call Sda on me debian) with Sda1 fat32, Sda2 ext3 and Sda3 Swap, but this is on a usb Hdd.  
   
 Could you add suport for loading fat32 partition on sata hard-drive ?  
   
 I think this not to complicate because it's the same function like fat32 on usb drive.  
   
 Thanks.

## 2011-03-29 19:25:18, posted by: tuxuser

You are not the only one who would like that :P  
   
 We will add it for sure!

## 2011-03-29 20:26:35, posted by: val532

Yes i know but i have a probleme at this moment with the seconde stage kernel boot sda2.  
   
 When i have an HDD on sata with just sda1 ans sda2 and kenel on usb stik for the kernel my usb stik is sda and my hdd is sdb so linux can't boot ^^.

## 2011-03-30 00:13:56, posted by: tuxuser

Easy Workaround:  
   
 1. Get a hex editor  
 2. Open the precompiled kernel which is for /dev/sda2  
 3. Search for Text-String "root=/dev/sda2"  
 4. Change it according to your needs  
 5. Save File  
 6. Boot it and have fun ;)

## 2011-03-30 00:49:32, posted by: val532

Yeah thank !