# why debian squeze in hdd freeze and livecd not?

## 2011-03-19 19:56:25, posted by: redxs

what is the differential in this ?  
 livecd all ok buy in HDD is a gamble.  
   
 I read that was some of the cpu and that is working but the error would also occur at 10.10 ubuntu livecd or not?

## 2011-03-19 21:04:12, posted by: UNIX

I also have an issue with squeeze running from the HDD.   
   
 Nothing to do with the drive itself though, the cpu is locking up. Pretty sure there is a fix being worked on. Next time you load squeeze from the hard drive leave a terminal open, just before the system locks it will most likely say something like "CPU spinlock on CPU #X"

## 2011-03-19 22:37:26, posted by: Juggahaxor

This is a known problem and a fix is being worked on. Any or most of the time when the Kernel tries to do a spinlock on a CPU it deadlocks that CPU and subsequently the system. This problem is present on ALL HDD installs and any LiveCD that uses a newer kernel. The old Gentoo Live CD doesn't have this issue , and also if you do an HDD install of Ubuntu 7.10 , or older Debian distros ,then use the old SDA bootloader you won't have that issue. Aside from working on Xell itself , I know this has been given a top priority and will be fixed.

## 2011-03-19 23:55:11, posted by: redxs

ok thanks to you, I understand the problem and I've seen that warning on the terminal.  
   
   
 good day  
   
 edit:  
   
 i use icewease browser and delete ip=dhcp of .config "CONFIG\_CMDLINE" (this is more speed for start with ethernet cable desconect) and the rate of freeze is little or null..