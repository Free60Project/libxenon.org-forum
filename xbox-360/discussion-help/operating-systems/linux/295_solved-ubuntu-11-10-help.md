# [Solved] Ubuntu 11.10 Help

## 2012-03-03 05:18:14, posted by: XenonBliss

Ok, so I have installed Ubuntu 11.10 on my xbox 360. I have followed the instructions at [url=http://free60.org/Ubuntu11.10]http://free60.org/Ubuntu11.10[/url] and it has successfully installed to my xbox's hard drive at /dev/sda2. I am using the latest kernel as posted on that site and my kboot configuration is  
   
 linux\_hdd="uda:/latest\_kern root=/dev/sda2 video=xenonfb panic=60 maxcpus=3 --"  
   
 My only issue is that xorg fails to start, at least properly. Everything is extremely pixelated to a point that I do not recognize a desktop.  
   
 I have tried "Fix possible xorg fail" instructions and when I type in "sudo dpkg-reconfigure xserver-xorg" and nothing happens.  
 I have tried using the standard av cable, component cable and hdmi but no luck..  
 If you need any logs or anything, you could instruct me how to get them and I will gladly post them. I would love to get this working, any help would be appreciated!!

## 2012-03-03 09:10:33, posted by: XenonBliss

Ok, I just successfully installed Debian Squeeze onto my Xbox 360, the problem was that there was a 404 error when downloading the xenos\_dvr.so and xorg.conf and that threw off the whole install. I probably could have fixed it myself but it's taken care of :)  
   
 Now I am installing the LibXenon Toolchain.