# ubuntu_oneiric.sh Debooting Script for Ubuntu Gives 404 errors

## 2014-04-11 22:56:28, posted by: homeboycrusoe

Hi Folks, I just want to know I am wasting my time trying to install Ubuntu 11.10 on my RGH Xbox360 (FALCON model)?  
   
 When I run install script ubuntu\_oneiric.sh it gets past point off installing files on the HDD but then stops after getting 404 errors when trying to retrieve debootstrap below:  
   
 http://ftp.nl.debian.org/debian/pool/main/d/debootstrap/debootstrap\_1.0.38\_all.deb  
   
 Sure enough, that file is no longer hosted there.  
   
 So should it be or is this thing dead in the water?  
   
 Any help much appreciated.

## 2014-04-18 23:18:59, posted by: sema

Hi. You have to edit the ubuntu\_oneiric.sh file and change the URL for debootstrap to latest debootstrap\_1.0.59\_all.deb , but it's just your first step. This script also contains link to download video driver from this site which is unavailable (seems like nobody care anymore). Whatever, if you need it, I'll upload it for you, also with instructions. I run Ubuntu 11.10 on my Slim RGH, for morer then one year, and I'm hapy. ;)  
 Good luck.

## 2014-04-20 19:48:02, posted by: homeboycrusoe

@Sema, thanks for taking time to reply.   
   
 If you can find the time to upload missing files and instructions to manually install them I would be a very happy chappy and greatly indebted to you.  
   
 Many Thanks

## 2014-04-21 23:20:14, posted by: sema

I have edited the install script to feat the latest requirements. This will install Ubuntu 11.10 on your HDD. I hope you know how to do this. If not, feel free to ask, I'll guide you through the proces.

### Attachments

[ubuntu_oneiric.sh](ubuntu_oneiric.sh)

## 2014-04-21 23:57:28, posted by: sema

After succesful install, unzip and place the content of .zip in /lib/modules directory, you must have this: /lib/modules/3.5.4-xbox0.11.1 There are drivers for some devices. Also you have to replace (or edit) the file /etc/modules (atached).

### Attachments

[3.5.4-xbox0.11.1.zip](3.5.4-xbox0.11.1.zip)[modules](modules)

## 2014-04-21 23:59:44, posted by: tuxuser

Isn't this the up-to-date version?  
 http://file.libxenon.org/free60/linux/xenosfb/ ?

## 2014-04-22 00:01:10, posted by: sema

Boot with this kernel and kboot.conf Just place it on root of the usb stick

### Attachments

[vmlinux](vmlinux)[kboot.conf](kboot.conf)

## 2014-04-22 00:09:43, posted by: sema

[quote="tuxuser"]  
 Isn't this the up-to-date version?  
 http://file.libxenon.org/free60/linux/xenosfb/ ?  
 [/quote]  
 Tux, I'm realy glad to see you here. You help me a lot with having linux on my xbox, but suddenly this forum goes down, and I try to help people who is interested in linux so am I. So, if you are here, let's work in direction of 3D video driver for xbox360 linux. I'm ready to work on it but I need some help. I have wrote to Felix Domke but no answer. Xbox 360 is realy amazing piece of hardware, let's make it better together.

## 2014-04-22 00:13:58, posted by: sema

By the way, the link in the script is right to the "up to day" you provided ;)

## 2014-04-22 00:18:22, posted by: tuxuser

[quote="sema"]  
 Tux, I'm realy glad to see you here. You help me a lot with having linux on my xbox, but suddenly this forum goes down, and I try to help people who is interested in linux so am I. So, if you are here, let's work in direction of 3D video driver for xbox360 linux. I'm ready to work on it but I need some help. I have wrote to Felix Domke but no answer. Xbox 360 is realy amazing piece of hardware, let's make it better together.  
 [/quote]  
   
 I really appreciate your motivation.. but I won't participate in that section anymore.  
 Sorry to give you such negative response..

## 2014-04-22 21:29:24, posted by: homeboycrusoe

Nice one Sema. I'll have a crack at the install tomorrow all being well.  
   
 I see a sound drivers folder...so the no sound issue has been resolved?

## 2014-04-22 22:44:00, posted by: sema

The sound issue I resolved using cheap chinesse external usb sound card, for that I have to build module. By the way, after you copy all this modules (and of course file /etc/modules) to the directory, you have to run from terminal sudo/sbin/depmod

## 2014-04-23 23:35:27, posted by: homeboycrusoe

Man, new probs. Script runs up to point of downloading debotstrap\_1.0.59\_all.deb and saving it, then seems to have a problem executing it.   
   
 Errors:  
   
 line 22: mnt/ubuntu/work/data.tar.gz : no such file or directory exists. Do I need tar app installed to unpack this file?   
   
 Line 25 : debootstrap : command not found.  
   
 Error message for lines 27, 28, 33 and 39 - no such file or directory exists.  
   
 I'm running install script from a Live Cd Beta and using a standard 60Gb seagate 2.5" Sata HDD (not a M$ signed one - is this ok?).  
   
 Any help appreciated.

## 2014-04-24 17:33:26, posted by: sema

Don't know why inside the debotstrap\_1.0.59\_all.deb is *[i]data.tar.xz[/i]* , so I have edited the install script. This one should work now. The HDD is ok, you can use any SATA 2.5 HDD since this script repartition and format it to ext.3. The Live CD Beta should be ok, but I prefer to use Ubuntu 10.10 Live from USB Stick, is much faster.

### Attachments

[ubuntu_oneiric.sh](ubuntu_oneiric.sh)

## 2014-04-24 18:58:24, posted by: homeboycrusoe

Cheers. I started off using 10.10 on an usb but the install script was wiping it so I reverted to Live CD beta. Makes me wonder whether my drives are being recognised correctly. I did a list and HDD is sda and usb was sdb so seem ok (no numbers after device). You would think the script would only be interested in sda so not a good sign it was wiping usb flash drive.  
   
 That said, I note the script has the line : "# if /dev/sda is mounted then partitions get wiped by dd but sfdisk fails!". Does this mean I should only attach HDD AFTER LiveCd boot to ensure NOT mounted or I am worrying about nothing?  
   
 Anyway, I'll use amended script and fingers crossed... 

## 2014-04-24 22:36:55, posted by: homeboycrusoe

No joy amigo!  
   
 tar: This does not look like a tar archive  
 tar: skipping to next header  
 tar: Error exit delayed from previous errors  
 cp: cannot start 'mnt.ubuntu/work/usr' : No such file or directory  
   
 Looking like I'll just sell this box and buy a pi at this rate :'(

## 2014-04-25 21:55:15, posted by: sema

That's all because they packed "data.tar.xz" instead of "data.tar.gz" as was before. Try to boot with Ubuntu 10.10 Live CD (USB) and launch the script from terminal. If you don't give up, you will finaly have Linux installed on HDD. From my experience I could tell you it took more than a year from the first try with Linux on Xbox 360 till I have had a desktop system that feat my requirements. So, go ahead and good luck.