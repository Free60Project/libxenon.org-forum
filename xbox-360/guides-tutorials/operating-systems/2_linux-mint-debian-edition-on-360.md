# Linux Mint Debian Edition on 360

## 2011-02-19 18:27:26, posted by: Cancerous1

**[b]Updated and should be working as of May 6th 2011[/b]**  
   
 Hello, I've modified the Debian 6 install script to install Mint on the 360  
   
 First you'll want to boot one of the Live CD's for the 360 through xell.  
 I used this one [url=http://downloads.sourceforge.net/free60/gentoo-livecd-xenon-beta-v2.iso]Gentoo-livecd[/url]  
   
 open a terminal  
 then type: [code]* *sudo su [enter] passwd [enter] (here you'll enter a password) wget http://file.libxenon.org/free60/linux/script/squeeze-mint-install.sh [enter] sh squeeze-mint-install.sh [enter] [/code] and that's all it takes to get started, the script should instruct you if it needs any input, which i tried to make as minimal as possible. It will install Debian Squeeze, then optionally you can install MintPPC from [url=http://mintppc.org/]MintPPC.org[/url] on top of it enjoy!  
   
 [attach=2] here is a kernel targeting the hdd once it is installed *9/5/2011  
   
 *If you choose, you can optionally skip the Mint part of the install and just use Squeeze, I built this script off of Tuxuser's squeeze-install script with some changes.  
 **You may also have to choose mint-lxde from the sessions at the login screen, your first login.  
   
 *** I'm also attaching these scripts to this post in case the ones Tux is nice enough to be hosting get out of date, you can edit them and still use them to install from your own hosting, or for those curious to see what i did in them.  
   
 ****modified scripts on server, and attached versions to always get current debootstrap image, please test :)

### Attachments

[mint-scripts-8-21-11.7z](mint-scripts-8-21-11.7z)[xenon.elf](xenon.elf)

## 2011-02-23 01:37:49, posted by: Cancerous1

[align=center][attach=1]  
 Mint LXDE ^  
   
 [youtube]http://www.youtube.com/watch?v=2oa3TR7R42s[/youtube]  
 Mint with GDM and LXDE ^[/align]

### Attachments

[k19bsw.jpg](k19bsw.jpg)

## 2011-02-23 23:54:37, posted by: Chrisoldinho

i love mint, but then i also love kde, choices choices :)

## 2011-02-24 19:12:00, posted by: Chrisoldinho

for some unknown reason debootstrap\_1.0.27\_all.deb has been removed, debootstrap\_1.0.28\_all.deb works. Scripts need updating or it will fail.  
   
 Chris.

## 2011-02-26 03:31:16, posted by: Cancerous1

thanks, the script is updated

## 2011-03-16 17:46:36, posted by: Cancerous1

Ok, got XBMC installed but I will warn that **[b]*it's not yet working for me*[/b]**  
   
 but anyone following along all the Squeeze/Mint testing perhaps someone can have better luck and share some experience.  
   
 edit /etc/apt/sources.list  
 add these two lines  
 [code]* *deb http://www.debian-multimedia.org squeeze main non-free deb-src http://www.debian-multimedia.org sid main [/code] then run these commands from a terminal [code]* *sudo apt-get install debian-multimedia-keyring sudo apt-get update sudo apt-get install xbmc [/code] you'll then find XBMC under audio/video in the menu, good luck and please share back if you find a method to make it usable.

## 2011-03-17 01:43:57, posted by: val532

Hi,  
   
 If we créate two partition on an USB HDD (one swap and one ext3) can we install debian on USB HDD ?  
   
 I know we have to modify the install script but is it possible ?

## 2011-03-19 16:27:06, posted by: Cancerous1

sure sounds plausible, let people know how that goes.

## 2011-03-20 20:12:55, posted by: val532

I think if I have some time this week i mad some test.

## 2011-03-30 07:00:56, posted by: val532

Hi,  
   
 I have now debien mint on me Hdd but when x-server start my mouse and keybord do not respond.  
 Any idea of what it's th probleme ?

## 2011-04-09 11:47:36, posted by: mojobojo

I have been having some issues. For some reason I could no longer load it off of my HDD. So I decided to reinstall it and for some reason this is happening.  
 [quote]root@ubuntu:/home/xbox# sh squeeze-mint-install.sh  
 Thu Feb 24 00:00:00 UTC 2011  
 1+0 records in  
 1+0 records out  
 512 bytes (512 B) copied, 0.000222918 s, 2.3 MB/s  
 Checking that no-one is using this disk right now ...  
 BLKRRPART: Device or resource busy  
   
 This disk is currently in use - repartitioning is probably a bad idea.  
 Umount all file systems, and swapoff all swap partitions on this disk.  
 Use the --no-reread flag to suppress this check.  
 Use the --force flag to overrule all checks.  
 mke2fs 1.41.12 (17-May-2010)  
 /dev/sda2 is mounted; will not make a filesystem here!  
 /dev/sda1: Device or resource busy  
 swapon: /dev/sda1: read swap header failed: Invalid argument  
 mkdir: cannot create directory `/mnt/debian': File exists  
 mount: /dev/sda2 already mounted or /mnt/debian busy  
 mount: according to mtab, /dev/sda2 is already mounted on /mnt/debian  
 mkdir: cannot create directory `/mnt/debian/work': File exists  
 --2011-02-24 00:00:00-- [url=http://ftp.us.debian.org/debian/pool/main/d/debootstrap/debootstrap\_1.0.28\_all.deb]http://ftp.us.debian.org/debian/pool/ma ... 28\_all.deb[/url]  
 Resolving ftp.us.debian.org... 199.6.12.70, 128.30.2.36, 35.9.37.225, ...  
 Connecting to ftp.us.debian.org|199.6.12.70|:80... connected.  
 HTTP request sent, awaiting response... 404 Not Found  
 2011-02-24 00:00:00 ERROR 404: Not Found.  
   
 ar: debootstrap\_1.0.28\_all.deb: No such file or directory  
 squeeze-mint-install.sh: 22: cannot open /mnt/debian/work/data.tar.gz: No such file  
 tar: This does not look like a tar archive  
 tar: Exiting with failure status due to previous errors  
 cp: cannot stat `/mnt/debian/usr/sbin/debootstrap': No such file or directory  
 squeeze-mint-install.sh: 26: debootstrap: not found  
 squeeze-mint-install.sh: 27: cannot create /mnt/debian/etc/hostname: Directory nonexistent  
 sed: can't read /mnt/debian/etc/hosts: No such file or directory  
 This will be a temporary root password.  
 chroot: failed to run command `passwd': No such file or directory  
 This will be the user password and info.  
 chroot: failed to run command `adduser': No such file or directory  
 squeeze-mint-install.sh: 34: cannot create /mnt/debian/etc/fstab: Directory nonexistent  
 squeeze-mint-install.sh: 39: cannot create /mnt/debian/etc/network/interfaces: Directory nonexistent  
 squeeze-mint-install.sh: 45: cannot create /mnt/debian/etc/apt/sources.list: Directory nonexistent  
 mv: cannot stat `/mnt/debian/root/.bashrc': No such file or directory  
 /mnt/debian/root/.bashrc: No such file or directory  
 Base System Install Complete!  
 You may now shutdown the xbox360.  
 Then continue the install by booting the Xell-Bootloader-sda2.  
 And log in as user: root  
 root@ubuntu:/home/xbox# [/quote] And it keeps reformatting my USB stick. I am restoring my HDD image from before linux was installed all together.

## 2011-04-12 18:42:11, posted by: Cancerous1

sounds like that debootstrap image link is not good anymore, maybe there is a new version or that mirror is down. Might have to google that filename and see if there's news of a newer one.  
   
 some people had problems installing also from the mirrors i chose in the script that were good for my location, but when they changed it to a local mirror it cleared things up

## 2011-05-06 07:39:02, posted by: Cancerous1

The scripts have been updated, and should be working (again), it's nothing magical or secret I'm attaching them to the first post in this thread in case anything changes (again) and the one's Tux is hosting for us get out of date. That way anyone interested in installing Mint/Squeeze this way can edit them without needing to wait for me to do it.

## 2011-05-13 18:08:08, posted by: sema

Dear friends. I need help. I want to install Debian on my Xbox 360, but I don't have a PC. I have two USB modems, Huawei E1750, Huawei E160e. Maybe somebody know how to mount one of them in Gentoo Live CD, so I could install Debian from the internet?

## 2011-06-16 23:53:51, posted by: Walkanator333

Can someone post a working link for the Xell-Bootloader-sda2. I've been googling for about an hour now and no luck. Thanks

## 2011-06-17 00:59:59, posted by: tuxuser

[quote="Walkanator333"]Can someone post a working link for the Xell-Bootloader-sda2. I've been googling for about an hour now and no luck. Thanks[/quote]  
   
 You could have looked on Linux Kernels Download section for it:  
 [url=http://libxenon.org/http://libxenon.org//viewtopic.php?t=9]Linux Kernels[/url]

## 2011-06-26 17:19:11, posted by: Doerek

[quote="Cancerous1"]  
 [align=center][attach=1]  
 Mint LXDE ^  
   
 [youtube]http://www.youtube.com/watch?v=2oa3TR7R42s[/youtube]  
 Mint with GDM and LXDE ^[/align]  
 [/quote]  
   
 @ **[b]Cancerous1[/b]**  
 Could you please reupload your "Xell-Reloaded booting Debian Mint360" video?  
 I got removed because of the Audio track you used (I think)  
 that would be really great...  
   
 Thx in advice...  
   
 Greetz  
 DCDoerek  
   
 Edit by Cancerous1: Fixed :)

## 2011-07-09 20:05:20, posted by: Doerek

[quote="tuxuser"]  
 [quote="Walkanator333"]Can someone post a working link for the Xell-Bootloader-sda2. I've been googling for about an hour now and no luck. Thanks[/quote]  
   
 You could have looked on Linux Kernels Download section for it:  
 [url=http://libxenon.org/http://libxenon.org//viewtopic.php?t=9]Linux Kernels[/url]  
 [/quote]  
   
   
 Dead Link...   
   
   
 :-/

## 2011-07-09 20:16:47, posted by: Cancerous1

[url=http://libxenon.org/http://libxenon.org//viewtopic.php?t=3]linux kernels[/url]

## 2011-07-09 21:40:09, posted by: Cancerous1

[quote="Doerek"]  
 @ **[b]Cancerous1[/b]**  
 Could you please reupload your "Xell-Reloaded booting Debian Mint360" video?  
 I got removed because of the Audio track you used (I think)  
 that would be really great...  
   
 Thx in advice...  
   
 Greetz  
 DCDoerek  
 [/quote]  
   
 I believe the video was from juggahaxor, but it doesn't take much to install it n try it out yourself if he doesn't have the video anymore

## 2011-07-09 22:06:53, posted by: Doerek

I just updated my Xell to xell-Reloaded...and installed "mint debian" througt the "Ubuntu LiveCd Beta5"  
 but everytime when i try to load "vmlinux-nospinlock-sda2.tar.gz" from USB i get Kernel panic.... 

## 2011-07-10 00:29:31, posted by: tuxuser

Did you follow the output while install-script execution? Any errors? What's the kernel panic saying exactly?   
   
 check via LiveCD whats the output of   
 [code]* *fdisk -l [/code] ?  
   
 Greetz  
 tux

## 2011-07-10 22:12:54, posted by: Doerek

[quote="tuxuser"]  
 Did you follow the output while install-script execution? Any errors? What's the kernel panic saying exactly?   
 [/quote]

### Attachments

[10072011109.jpg](10072011109.jpg)

## 2011-07-10 22:42:23, posted by: tuxuser

You didnt follow the install-script execution: Your system wasnt installed properly, thats why you get the kernel panic.

## 2011-07-11 13:14:21, posted by: Doerek

after this..  
 [code]* *sudo su [enter] passwd [enter] (here you'll enter a password) wget http://file.libxenon.org/free60/linux/script/squeeze-mint-install.sh [enter] sh squeeze-mint-install.sh [enter] [/code] it says that i must continue using the Xell-Bootloader.

## 2011-07-11 13:35:40, posted by: Doerek

This is what happens when i run the "squeeze-mint-install.sh"  
 It seams that there are some files not found, like "deboostrap\_1.0.30\_all.deb"  
 And on Line 20 the command "ar" is not found (probably "tar"?)  
 here is a screenshot:

### Attachments

[11072011110.jpg](11072011110.jpg)

## 2011-07-11 13:52:39, posted by: Doerek

Also..  
 when i try to run the Mint PPC installer from"[url=http://file.libxenon.org/free60/linux/script/mintscript.sh]http://file.libxenon.org/free60/linux/script/mintscript.sh[/url]"   
 after the squeeze-mint-install.sh   
 it gives me some errors, see below

### Attachments

[11072011111.jpg](11072011111.jpg)

## 2011-07-11 18:16:46, posted by: Cancerous1

Doerek, i attached the scripts to the first post so you can download them and edit it as these debootstrap images go out of date, tbh I don't know how to make it always get the current one or I'd edit the script to do that. If you follow the thread this exact problem has happened before. It should go smooth for you after you fix the link for that file, lets hope.

## 2011-07-11 18:31:19, posted by: tuxuser

@Cancerous  
 [code]* *DEB\_MIRROR="http://cdn.debian.net/debian" DEBOOTSTRAP\_VERSION=$(wget -q "$DEB\_MIRROR/pool/main/d/debootstrap/?C=M;O=D" -O- | grep -o 'debootstrap[^"]*all.deb' | head$ URL\_DEBOOTSTRAP="$DEB\_MIRROR/pool/main/d/debootstrap/$DEBOOTSTRAP\_VERSION" [/code] there you go

## 2011-07-11 18:42:27, posted by: Doerek

[quote="Cancerous1"]  
 Doerek, i attached the scripts to the first post so you can download them and edit it as these debootstrap images go out of date, tbh I don't know how to make it always get the current one or I'd edit the script to do that. If you follow the thread this exact problem has happened before. It should go smooth for you after you fix the link for that file, lets hope.  
 [/quote]  
 This was the first thing i tried, yesterday...(using Winvi32)   
 ...but no luck, still not working.

## 2011-07-12 15:46:42, posted by: Doerek

[quote="tuxuser"]  
 @Cancerous  
 [code]* *DEB\_MIRROR="http://cdn.debian.net/debian" DEBOOTSTRAP\_VERSION=$(wget -q "$DEB\_MIRROR/pool/main/d/debootstrap/?C=M;O=D" -O- | grep -o 'debootstrap[^"]*all.deb' | head$ URL\_DEBOOTSTRAP="$DEB\_MIRROR/pool/main/d/debootstrap/$DEBOOTSTRAP\_VERSION" [/code] there you go  
 [/quote]  
 where do we have to insert the code?  
 this is my (some how) updated Installscript for mint debian:  
 ~Updated deboostrap link  
 ~Updated xorg.conf link  
 ~Updated xenosfb link   
   
 [code]* *#!/bin/bash # set the date to anything except 1/1/1970 since this causes issues # time is now also set after first boot by .bashrc script below date -s 1/1/2012 mkdir /mnt/ubuntu # USB Partition einhängen mount /dev/sda2 /mnt/ubuntu cd /mnt/ubuntu mkdir /mnt/ubuntu/work cd /mnt/ubuntu/work # download extract and run debootstrap wget http://ftp.de.debian.org/debian/pool/main/d/debootstrap/debootstrap\_1.0.32\_all.deb ar -xf debootstrap\_1.0.32\_all.deb cd /mnt/ubuntu zcat < /mnt/ubuntu/work/data.tar.gz | tar xv export DEBOOTSTRAP\_DIR=/mnt/ubuntu/usr/share/debootstrap export PATH=$PATH:/mnt/ubuntu/usr/sbin debootstrap --arch powerpc natty /mnt/ubuntu http://ports.ubuntu.com/ # create needed files on hdd echo Falcon > /mnt/ubuntu/etc/hostname cat > /mnt/ubuntu/etc/fstab << EOF /dev/sda2 / ext2 defaults 0 0 /dev/sda1 none swap sw 0 0 proc /proc proc defaults 0 0 EOF cat > /mnt/ubuntu/etc/network/interfaces << EOF iface lo inet loopback auto lo auto eth0 iface eth0 inet dhcp EOF cat > /mnt/ubuntu/etc/apt/sources.list << EOF deb http://ports.ubuntu.com/ natty main restricted universe multiverse EOF #Change root-pwd inside chroot chroot /mnt/ubuntu echo -e "xbox\nxbox" | (passwd --stdin $USER) apt-get update apt-get --reinstall install grub-common grub-pc os-prober grub-setup /dev/sda exit cp /mnt/ubuntu/root/.bashrc /mnt/ubuntu/root/.bashrc.orginal # create .bashrc script on hdd cat >> /mnt/ubuntu/root/.bashrc << EOF date -s 1/1/2012 passwd #mkdir /lib/modules/2.6.24.3 #touch /lib/modules/2.6.24.3/modules.dep apt-get update apt-get install ntp wget -y --force-yes aptitude install ubuntu-desktop -y echo "AVAHI\_DAEMON\_START=0" > /etc/default/avahi-daemon #/etc/init.d/networking restart service networking cd /usr/lib/xorg/modules/drivers/ wget http://file.libxenon.org/free60/linux/driver/xenosfb/xenosfb\_drv.so\_natty mv xenosfb\_drv.so\_natty xenosfb\_drv.so cd /etc/X11/ wget http://file.libxenon.org/free60/linux/driver/xenosfb/xorg.conf #mv ubuntu.conf xorg.conf #cd /usr/lib/xorg/modules/linux/ #mv libfbdevhw.so libfbdevhw.so.bk #wget http://home.comcast.net/~ssmurf/libfbdevhw.so rm -r -f /work/ echo "" > /etc/gdm/gdm.conf-custom sed -i 's/AllowRoot=false/AllowRoot=true/' /etc/gdm/gdm.conf rm /root/.bashrc mv /root/.bashrc.orginal /root/.bashrc /etc/init.d/gdm start EOF # done echo "Base installation completed." echo "To finish the installation. Reboot then load the sda2 bootloader CD." echo "This may take up to two hours" [/code]

## 2011-08-22 05:09:30, posted by: Cancerous1

Okay, update the scripts on the server to always grab the latest debootstrap image if anyone is keen on testing please post results.

## 2011-08-23 02:45:27, posted by: Cancerous1

new video up in first post, sorry about the low screen resolution, no hdmi capture card :s

## 2011-08-24 01:46:47, posted by: Doerek

Hi,  
 After booting sda-bootloader i get this error:  
 ![](http://farm7.static.flickr.com/6086/6074983924_1e0d88d844_b.jpg)[img]http://farm7.static.flickr.com/6086/6074983924\_1e0d88d844\_b.jpg[/img]  
 So...  
 How should i prepare the Xbox 20GB HDD before installing?   
 filesystem, ect.  
   
 Thx in advice...

## 2011-08-24 01:55:46, posted by: tuxuser

Chroot into debian from a liveCD (either Gentoo or Ubuntu, use what you like)  
   
 then do:  
 [code]* *cd /dev mknod -m 622 console c 5 1 mknod -m 622 tty0 c 4 0 [/code]

## 2011-08-24 02:51:43, posted by: Doerek

![](http://farm7.static.flickr.com/6076/6075127744_fa8c7a96ff.jpg)[img]http://farm7.static.flickr.com/6076/6075127744\_fa8c7a96ff.jpg[/img]  
 when booting with sda-bootloader i still get the same error, like above...

## 2011-08-24 03:13:45, posted by: Cancerous1

try this to chroot into debian first like tux said  
   
 mkdir /mnt/debian  
 mount /dev/sda2 /mnt/debian  
 chroot /mnt/debian

## 2011-08-24 04:28:44, posted by: Doerek

[quote="Cancerous1"]  
 try this to chroot into debian first like tux said  
   
 mkdir /mnt/debian  
 mount /dev/sda2 /mnt/debian  
 chroot /mnt/debian  
 [/quote]  
   
   
 After Chroot into debian i selected (2)  
 "Stop here and use Squeeze"  
 but after fetching some files it promt me to restart.  
 should it select option (1) and try to install "mint" ?

## 2011-08-24 04:30:35, posted by: Cancerous1

whichever you wanted should work

## 2011-08-24 04:36:40, posted by: Doerek

I tried booting to sda2, but still Same error

## 2011-08-24 06:00:00, posted by: Cancerous1

perhaps there was an error earlier in the install you may not have noticed. Mount debian from a livecd chroot into it again and check the home folder for an error log.

## 2011-09-24 22:06:46, posted by: Plastic

So after the first step i boot the XeLL Sda iso? and then do i run the mint script and how would i run the mint script ? Sorry I am bad at this type of stuff.

## 2011-12-22 00:48:21, posted by: Grim187

a lot of the dependencies are missing from ftp://mirrors.kernel.org/debian/  
 everything from Mawk on fails to download.

## 2011-12-22 00:59:10, posted by: Cancerous1

I didn't have that problem when I test 1 month ago, although I guess I could install again to be sure the problem wasn't on your end. Unless you can suggest a fix?

## 2011-12-22 01:15:07, posted by: Grim187

im pretty sure the mawk files should be here; ftp://mirrors.kernel.org/debian/pool/main/m/mawk/  
   
 i think the files its failing to download are just missing from the server.

## 2012-02-01 04:11:15, posted by: checo

Hello. Excuse me.  
 Has anyone been able to install Squeeze?  
   
 The installation script no longer works. :'(

## 2012-02-15 08:02:21, posted by: windowsx

Modified the script- if you couldnt get the last one to work this should (2/15/12) [code]#!/bin/bash # set the date to anything except 1/1/1970 since this causes issues # time is now also set after first boot by .bashrc script below date -s 2/24/2011 dd if=/dev/zero of=/dev/sda bs=512 count=1 sfdisk /dev/sda << EOF ,124,S ,,L EOF mkfs.ext3 /dev/sda2 mkswap /dev/sda1 sync; sync; sync swapon /dev/sda1 mkdir /mnt/debian mount /dev/sda2 /mnt/debian cd /mnt/debian mkdir /mnt/debian/work cd /mnt/debian/work wget http://ftp.us.debian.org/debian/pool/main/d/debootstrap/debootstrap\_1.0.38\_all.deb ar -xf debootstrap\_1.0.38\_all.deb cd /mnt/debian zcat < /mnt/debian/work/data.tar.gz | tar xv cp /mnt/debian/usr/sbin/debootstrap /mnt/debian/usr/share/debootstrap export DEBOOTSTRAP\_DIR=/mnt/debian/usr/share/debootstrap export PATH=$PATH:/mnt/debian/usr/share/debootstrap debootstrap --arch powerpc squeeze /mnt/debian ftp://mirrors.kernel.org/debian/ echo Xenon > /mnt/debian/etc/hostname sed 's/localhost/localhost Xenon/g' /mnt/debian/etc/hosts echo "This will be a temporary root password." chroot /mnt/debian passwd echo "This will be the user password and info." chroot /mnt/debian adduser xbox cat > /mnt/debian/etc/fstab << EOF /dev/sda2 / ext3 defaults 0 0 /dev/sda1 none swap sw 0 0 proc /proc proc defaults 0 0 EOF cat > /mnt/debian/etc/network/interfaces << EOF iface lo inet loopback auto lo auto eth0 iface eth0 inet dhcp EOF cat > /mnt/debian/etc/apt/sources.list << EOF deb ftp://mirrors.kernel.org/debian/ squeeze main contrib non-free EOF mv /mnt/debian/root/.bashrc /mnt/debian/root/.bashrc.orginal wget -O /mnt/debian/root/.bashrc http://christiansphotography.net/vid/.bashrc echo "Base System Install Complete!" echo "You may now shutdown the xbox360." echo "Then continue the install by booting the Xell-Bootloader-sda2." echo "And log in as user: root" [/code]

## 2012-06-25 18:44:07, posted by: kikofras

This script is no longer valid, i've changed the debootstrap to 1.0.41 but.... no way.  
   
 Can anyone fix this?  
   
 Thanks alot.

## 2012-06-25 19:15:36, posted by: Cancerous1

same instructions, but use this script, should work  
   
 wget http://home.comcast.net/~cancerous1/squeeze-mint-install.sh

## 2016-01-05 07:49:38, posted by: <Unknown User>

tuxuser dUde you roCk and also great work cancerous for this great and helpfull tutorial  
   
 now hElp me out here guys i've tried this debian mint, ubuntu 11.10, debian etch, etc. etc. and whatnot... i can't get them to work, it seems the debians are short on debootstrap links it doesn't work in any debian script(?) while the ubuntu 11.10 posted here did work for me (or seem to, all the downloads were working including the debootsrap links, but i have no idea how to boot it? is it with the xeLL bootloader-sda2-v2.6.24.3.tar.gz CD? when i boot with it it says 'cannot open root device "sda2" or unknown-block(8,2) please append a correct "root=" boot option; here are the available partition; 0b00 1048575 sr0 driver: sr. 0000 312571224 sda driver: sd'.. and when i 'fdisk -l' this ubuntu 11.10 from the livecd it says the partitions r not good (i can't remember the exact words) while the debians when i do the 'fdisk -l' the partitions seem fine, but as i said the debootstrap links don't work and from there on the script doesn't work and when i try to boot the debians with the xeLL bootloader-sda2-v2.6.24.3.tar.gz CD the Kernel panics :P so how do i get this Linux into my xbox 360 rgh 320gb hd? what am i doing wrong? please help. thanks. and btw excellent work and your signature is hilarious as hell! ;D and great work cancerous as well so if you guys can help please would b greatly appreciated thanks in advance!