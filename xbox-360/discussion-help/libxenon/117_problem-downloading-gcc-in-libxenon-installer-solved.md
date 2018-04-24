# Problem downloading GCC in Libxenon Installer [SOLVED]

## 2011-06-29 07:55:33, posted by: Juggahaxor

 I was having an issue with downloading GCC using the Libxenon toolchain build script , essentially it failed trying to start the download at ftp.gnu.org , as you can see in my last post I have since found a place to download the archive for gcc-4.4.0 , and the installation is now in progess. If anyone else has this issue I am going to include a small list of how to solve the issue without editing the script manually , and simply manually downloading the archive at a command prompt.  
 First either login as root , or use sudo , I use root so I am going to skip the sudo command before my commands , if you are not running as root remember to add sudo in front of your commands. really there is only one command you need to run , then re-start the script. on the first run if it fails trying to connect to ftp.gnu.org this is what you need to do.  
 first CD into your libxenon/toolchain directory the same directory that has the install script then .....  
   
 #wget http://mirrors-us.seosue.com/gcc/releases/gcc-4.6.0/gcc-4.6.0.tar.bz2 <----- Wait for it to finish downloading.  
 #./build-xenon-toolchain toolchain  
 I updated this to include the newer 4.6.0 version of Gcc because I am still having problems with it not downloading from gnu.org.

## 2011-06-29 09:51:46, posted by: tuxuser

If you have network problems in general -> check your network settings^^ Especially the configured Nameserver!  
   
 Also try another link for the gcc archive.

## 2011-07-01 22:57:10, posted by: Juggahaxor

I was going to try another link to the GCC , I have so much school work right now I can't even think about anything else. The other parts download fine so I know it isn't my network. I am going to try again and see what happens , but even trying to browse to the gnu.org ftp site got me knowhere on my host system.

## 2011-07-03 00:04:20, posted by: mojobojo

Make sure you are connected to the internet. type "ifconfig" to check your ip address.

## 2011-07-03 06:35:55, posted by: Juggahaxor

I already checked all that , it downloaded the first part of the stuff just fine , for some reason I cannot connect to ftp.gnu.org , so I just used wget and got the archive from here [url=http://mirrors-us.seosue.com/gcc/releases/gcc-4.4.0/]http://mirrors-us.seosue.com/gcc/releases/gcc-4.4.0/[/url]  
   
 The script will skip over something if you already have the archive downloaded in the toolchain folder so manually downloading it should take care of me. While I have been constructing this post I have indeed gotten the building to continue , and it was able to also download newlib with the script.   
   
 I am not a Linux genius by far but I do know to check simple things like ifconfig , the problem is something with their servers so it may be wise to change that in the script , or try it for yourself and maybe it was just a unique problem too me.   
   
 Thanks for the responses I am going to close this thread and change the title so if anyone else has this problem they can figure out a different download location like I did.