# MAC-Address in Gentoo Live Kernel

## 2014-10-13 18:33:09, posted by: <Unknown User>

Dear all!  
 I have managed to get the LiveCD (Gentoo) working on the Xbox with NFS-Mount of the rootfs. I use the following commandline in kboot.conf:  
 gentoo="/gm/VMLINUX initrd=/gm/initramfs root=/dev/ram0 cdroot=1 real\_root=/dev/nfs nfsroot=192.168.1.1:/srv/tftp/gm video=xenonfb panic=60 maxcpus=1 loop=/image.squashfs looptype=squashfs console=tty0 nox ip=dhcp"  
   
 ...which works wonderfully, except for the IP-Adress a XBOX (we have more than one) gets from DHCP. Somehow, the MAC-Address of the eth0 Interface turns to 00:01:33:44:55:66 when the kernel comes up, however, xell displays the correct MAC before initiating the boot process.  
 Can anybody help me? I suspect the MAC address is somehow hardcoded in the kernel - can that be?  
   
 Regards,  
 Michael