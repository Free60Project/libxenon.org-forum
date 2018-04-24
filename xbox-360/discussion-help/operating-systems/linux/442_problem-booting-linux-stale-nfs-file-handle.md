# Problem Booting Linux, Stale NFS file handle

## 2014-08-13 08:48:31, posted by: <Unknown User>

Hello all,  
   
 as written in the subject I have got some troubles booting linux on my xbox360. I am using tftp and the beta4 of the modified linux. However, everything is going well until the point where the linux is loading. Most of the stuff is completed successfull (..... done.), but at one line it always stops with:  
 "run-init: overmounting root: Stale NFS file handle"  
   
 Here the line in the kboot.conf file, which is used to boot the iso:  
 ubuntu\_light="/ubuntu\_light/vmlinux initrd=/ubuntu\_light/initrd root=/dev/nfs boot=casper netboot=nfs nfsroot=192.168.1.1:/srv/tftp/ubuntu\_light video=xenonfb console=tty0 panic=60 nosmp maxcpus=1"  
 I have to mention, that this line was created by my professor ( I am doing this for my final exams :) )  
   
 If you need any further information just tell me! Thanks in advance ;)