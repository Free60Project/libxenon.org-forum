# trouble installing ubuntu

## 2011-08-21 23:37:32, posted by: sabbath06

Hello,  
 I have been trying to install ubuntu from the hard drive with the script from  
   
 ep-comps.com/free60/ubuntuinstall.sh  
   
 and have been getting and error once I run the script and reboot and load the sda bootloader disc. It says 'kernel panic cannot sync: no init found.' I read somewhere that I should use fdisk to delete all the partitions on sda before running the script but that does not seem to help. Has anyone else run into a similar problem and found solution? I have included a screenshot of the error:  
   
 ![](http://charlesjanik.com/IMG_9846.JPG)[img]http://charlesjanik.com/IMG\_9846.JPG[/img]  
   
 Thank you for taking the time to read my question.

## 2011-08-22 01:22:05, posted by: Juggahaxor

I've had that problem a few times. Using fdisk to format the drives prior to running the script did fix this in my case however. Try this edition cooked up by Cancerous with a lot of testing done by myself, I can tell you this one works. You will need to build or download a newer kernel, but if you stick with lxde it is a very fast stable Linux system on the 360. I use Mint when I install it but you can still install debian 6.0. Even though it does set up the partitions with the script you are always better off manually setting them up just to make sure, especially if the drive was originally an Xbox360 internal drive. That error means it isn't able to find the files it needs to load even a terminal to complete the bootstrap install. The easiest way would be to start the install over again afeter manually formatting your drive. I would even try formatting it on your PC and marking the / partition as active just to make sure.  
 [url=http://libxenon.org/http://libxenon.org//viewtopic.php?t=2]http://libxenon.org/http://libxenon.org//viewtopic.php?t=2[/url]

## 2011-08-27 07:19:09, posted by: sabbath06

Just finished partitioning and formatting the drive on my pc, will report back if that solved the issue.