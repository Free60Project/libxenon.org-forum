# Process of creating a LiveCD

## 2011-04-30 04:20:21, posted by: tuxuser

Already saying sorry, some parts were written from the top of my head - so it could be incorrect sometimes ^^  
 If you know what you are doin, you will succeed though :D  
 Corrections are very welcome!  
 [quote] Process of LiveCD Creation:  
   
 **[b]1. Debootstrap a fresh system (on a PPC machine):[/b]**  
   
 mkdir -p /mnt/ubuntu  
 cd /mnt  
 debootstrap --arch=powerpc precise ubuntu http://ports.ubuntu.com/  
   
   
 **[b]2. Mount-bind /dev and /proc:[/b]**  
   
 mount -t proc none /mnt/ubuntu/proc  
 mount --rbind /dev /mnt/ubuntu/dev  
   
 cat > chroot/etc/apt/sources.list << EOF  
 # Main  
 deb http://ports.ubuntu.com/ubuntu-ports/ precise main restricted   
 deb http://ports.ubuntu.com/ubuntu-ports/ precise universe multiverse  
 # Updates  
 deb http://ports.ubuntu.com/ubuntu-ports/ precise-updates main restricted  
 deb-src http://ports.ubuntu.com/ubuntu-ports/ precise-updates restricted  
 deb http://ports.ubuntu.com/ubuntu-ports/ precise-updates universe multiverse  
 # Security  
 deb http://ports.ubuntu.com/ubuntu-ports/ precise-security main restricted  
 deb-src http://ports.ubuntu.com/ubuntu-ports/ precise-security main restricted  
 deb http://ports.ubuntu.com/ubuntu-ports/ precise-security universe multiverse  
 deb-src http://ports.ubuntu.com/ubuntu-ports/ precise-security universe multiverse  
 EOF  
   
   
 **[b]3. Now chroot:[/b]**  
   
 LANG=C chroot /mnt/ubuntu /bin/bash  
 export HOME=/root  
 export LANGUAGE=en\_US.UTF-8  
 export LANG=en\_US.UTF-8  
 export LC\_ALL=en\_US.UTF-8  
 locale-gen en\_US.UTF-8  
 dpkg-reconfigure locales  
 apt-get update  
 dpkg-reconfigure tzdata  
 echo "ubuntu-xenon" > /etc/hostname  
 apt-get install --yes dbus  
 dbus-uuidgen > /var/lib/dbus/machine-id  
 cp /sbin/initctl /sbin/initctl.bkp  
 dpkg-divert --local --rename --add /sbin/initctl  
   
 ln -s /bin/true /sbin/initctl  
 apt-get install console-data  
 dpkg-reconfigure console-data  
   
   
 **[b]4. Lets install the essential packages for the LiveCD[/b]**  
   
 apt-get install --yes casper lupin-casper  
 apt-get install --yes discover os-prober  
   
   
 **[b]5. Desktop Environment[/b]**  
   
 apt-get install --yes lxde lxdm libpciaccess0 xfonts-base xserver-common xserver-xorg xserver-xorg-core xserver-xorg-input-all xserver-xorg-input-evdev xserver-xorg-input-synaptics xserver-xorg-input-wacom xserver-xorg-input-kbd xserver-xorg-input-mouse  
   
   
   
 **[b]6. Sound System and other stuff[/b]**  
   
 apt-get install --yes xvkbd alsa-base alsa-utils openssh-server nano mc libfuse2 libfuse-dev irssi mc sshfs build-essential ncurses-dev git-core gitosis man-db ftp  
 apt-get install --yes blueman samba xrdp  
   
 **[b]7. If you want a graphical installer, also install Ubiquity:[/b]**  
   
 apt-get install ubiquity-frontend-gtk  
   
   
 **[b]8. Lets fix some nasty bugs in initramfs[/b]**  
 *******************************************************  
 #Non-Workin powerofff/reboot. Its cool for us to do cause it wont autoboot on the next Xbox-Start anyway.  
   
 in /etc/init.d/casper change  
   
 eject -p -m /cdrom >/dev/null 2>&1  
   
 [ "$prompt" ] || return 0  
   
   
 to  
   
 eject -p -m /cdrom >/dev/null 2>&1  
   
 exit 0  
   
 [ "$prompt" ] || return 0  
   
 *******************************************************  
   
 *******************************************************  
 #stdin 0: error at casper-initramfs  
   
 In /usr/share/initramfs-tools/scripts/casper-helpers - Line 44:  
   
 Change  
   
 eval $(fstype < $1)  
   
 to  
   
 eval $(fstype $1 2>/dev/null)  
   
 *******************************************************  
   
 *******************************************************  
   
 # INSTALL XBOXDRV DEB  
 # INSTALL XBOXBURNER DEB  
 # INSTALL ADDITIONAL STUFF TO /opt  
   
 *******************************************************  
   
 *******************************************************  
 #Blacklist xpad module  
 # /etc/modprobe.d/blacklist.conf - Append at the end:  
   
 #Blacklist xpad (xbox360 controller driver)  
 blacklist xpad  
   
 *******************************************************  
   
 *******************************************************  
 # Let xboxdrv + virtualkeyboard start at login-screen  
 # In /etc/lxdm/LoginReady:  
   
 # /dev/input/event14 could be another device, check it with evtest first!  
   
 /usr/local/bin/xboxdrv -c /usr/share/doc/xboxdrv/examples/virtualkeyboard.xboxdrv -s -- /usr/local/bin/virtualkeyboard -d /dev/input/event14   
 *******************************************************  
   
 *******************************************************  
 #Edit the live-password  
 nano /usr/share/initramfs-tools/scripts/casper-bottom/10adduser  
   
 Change:  
   
 # U6aMy0wojraho is just a blank password  
 db\_set passwd/root-password-crypted '*'  
 db\_set passwd/user-password-crypted U6aMy0wojraho  
   
 to  
   
 # HCJGGFOAgrFGE is password: xbox  
 db\_set passwd/root-password-crypted HCJGGFOAgrFGE  
 db\_set passwd/user-password-crypted HCJGGFOAgrFGE  
   
   
   
   
   
 #Also edit the live-username  
 nano /usr/share/initramfs-tools/scripts/casper  
   
 Change:  
   
 USERNAME=casper  
   
 to  
   
 USERNAME=xbox  
 *******************************************************  
   
 *******************************************************  
 /etc/network/interfaces  
   
 auto lo  
 iface lo inet loopback  
   
 auto eth0  
 iface eth0 inet dhcp  
 *******************************************************  
   
 *******************************************************  
 Maybe modify /etc/sudoers and add user "xbox" there ?!  
   
 *******************************************************  
   
   
 **[b]9. Create kernel deb file and initramfs.cpio in chroot-environment[/b]**  
   
 # Compile current linux-kernel sourcetree (w/ xenon patches) and install headers + modules  
 # copy zImage.xenon to /boot/  
 # mkinitramfs  
   
 **[b]10. Cleanup:[/b]**  
   
 rm /var/lib/dbus/machine-id  
   
 rm /sbin/initctl  
 dpkg-divert --rename --remove /sbin/initctl  
   
 apt-get clean  
   
 rm -rf /tmp/*  
   
 rm /etc/resolv.conf  
   
 umount -lf /proc  
 umount -lf /sys  
 umount -lf /dev/pts  
 exit  
   
 umount /mnt/ubuntu/dev  
   
 **[b]11. Squash it! (on Host System)[/b]**  
   
 apt-get install squashfs-tools  
 mksquashfs /mnt/ubuntu ~/image.squashfs  
   
 **[b]12. Assemble the CD[/b]**  
   
 Put kernel-ELF, initramfs and a kboot.conf on the disc and configure it till it boots :D  
   
 Hint:  
   
 #Structure  
 /vmlinux  
 /initrd.gz  
 /casper/filesystem.squashfs  
   
 #kboot.conf  
   
 #KBOOTCONFIG  
 livecd\_dvd="dvd:/vmlinux initrd=dvd:/initrd.gz boot=casper video=xenonfb console=tty0 console=ttyS0,115200n8 panic=60 nosplash noplymouth" [/quote]

## 2012-05-13 23:04:29, posted by: tuxuser

Updated for public consuming

## 2013-02-14 22:51:41, posted by: sema

Hi.   
 One question. What's for including graphical installer "ubiquity"? Will be possibile to install linux directly from cd, without internet connection?  
 Thanks in advance.