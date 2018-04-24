# Xbox 360 Cryptocurrency Miner

## 2017-12-14 17:29:04, posted by: <Unknown User>

For anyone that still has a hacked Xbox 360 and want to utilize it to mine low difficulty crypto coins, this is the only package available that will allow you to do so. Years ago I developed for LibXenon and was active in the IRC channels and this forum. Lately I have been missing the scene and still have my JTAG console. I decided to build a custom Linux distro based on the Ubuntu 10.10 Beta5 LiveCD. The contents of the zip archive included here can be copied to a USB drive and booted from the XeLL. You will be greeted by a black screen with a mouse cursor. Simply hit CTRL+ALT+F1 to use the live session console, where you can create an instance of minerd. The minerd included in the base system is pooler's cpuminer supporting SHA256 and Scrypt crypto algorithms. I was able to compile it on top of the Xenon CPU itself WITH altivec support. The performance of the Xenon CPU for mining is honestly pretty piss poor. But for mining low difficulty alt-coins it can generate shares at a reasonable pace.   
   
 This is just a hobby project and I don't expect to see much if any profit from using the Xbox 360 as a miner. Just wanted to contribute it for anyone else that wants to help tweak it to perform better and (maybe) add Xenos GPU support. With the 360 drawing very little power, if we can utilize the Xenos chip and get a few dozen megahash/s, viability and chance for profits could be there.  
   
 Greetz to anyone who is even still researching the long-dead Xbox 360 homebrew scene.  
   
 Xenon Miner Live OS:  
 https://ufile.io/p42s0  
   
 EDIT: You can use all 6 available logical cores of the Xenon CPU. My typical minerd command is as follows  
 minerd -a scrypt -t 6 -u USER.worker -p PASS -o stratum+tcp://MINING\_POOL\_URL:PORT\_NUMBER  
   
 Booting the Xenon Miner OS from XeLL\_Launch will grant you full speed of Xenon CPU, rather than 1/3 speed if booting from XeLL by eject button. Booting XeLL from eject starts the system in a low power state as the XeLL payload executes before the M$ kernel fully wakes the system.

## 2017-12-15 01:28:16, posted by: <Unknown User>

Thanks for sharing, this release is much appreciated! :) :)