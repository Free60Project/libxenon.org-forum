# Ubuntu 13.04 xenosfb driver request

## 2013-05-19 22:25:49, posted by: fentis

Hi,  
 I've installed ubuntu 13.04 minimal with kernel 3.5.4 compiled from github.  
 Sadly, the old video drivers (debian squeeze, ubuntu precise ecc) don't work!  
 So what are the needed source code changes to compile a new working driver for ubuntu 13.04?  
 xenosfb source: https://github.com/Free60Project/xenosfb.git  
   
 Thanks in advance

## 2013-05-20 12:56:36, posted by: nikos5800

link for ubuntu 13.04 for xbox;  
 thank you

## 2013-05-20 17:44:17, posted by: fentis

[quote="nikos5800"]  
 link for ubuntu 13.04 for xbox;  
 thank you  
 [/quote] [code]http://ports.ubuntu.com/ubuntu-ports/dists/raring/main/installer-powerpc/current/images/powerpc64/netboot/[/code] download file initrd.gz  
 kboot boot entry [code]"uda:/vmlinux initrd=uda:/initrd.gz ip=dhcp console=tty0 fb=false video=xenonfb panic=60"[/code]

## 2013-05-28 21:09:45, posted by: fentis

Ok, what I've done so far  
   
 updated latest xenosfb git code to use xf86-video-fbdev-0.4.3 as base  
 compiled and tested on ubuntu 13.04  
   
 ported Bertl's xenon-patchset 0.11.1 to kernel 3.8.8  
   
 unity (default ubuntu menu) is not working  
 maybe due to hardware acceleration that xenosfb doesn't support? idk  
 audio module is loaded and installed correctly but no sound! idk  
 also tested lubuntu (lxde), fluxbox, openbox and gnome fallback and it's all ok  
   
 Now trying to enable wireless support on kernel and hope to find a working driver  
 for the slim internal (usb) wifi adapter.  
   
 Hope it's all good, I'm not such a good programmer... [code]http://www2.zshares.net/tu9rgmvanud9[/code]