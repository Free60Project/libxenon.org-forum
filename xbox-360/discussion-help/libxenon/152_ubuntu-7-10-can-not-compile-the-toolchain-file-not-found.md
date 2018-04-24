# Ubuntu 7.10 / Can not Compile the Toolchain -&gt; File not found

## 2011-08-31 10:30:08, posted by: Doerek

Hi there,  
   
 I just finished the Ubuntu 7.10 installation to one spare 20HDD.  
 [code]apt-get install libgmp3-dev libmpfr-dev libmpc-dev texinfo git-core gettext build-essential[/code] It seams that the Old Ubuntu 7.10 script is slowly getting out of Date because I had to install:  
 -libmpc2  
 -libmpc-dev  
 ....manually  
   
 So...the last few hours Im triing to Compile the Toolchain.  
   
 But everytime i get the same error: (Please have a look)  
 [code]root@Falcon:~# git clone git://free60.git.sourceforge.net/gitroot/free60/free60 Initialized empty Git repository in /root/free60/.git/ remote: Counting objects: 1474, done. remote: Compressing objects: 100% (1023/1023), done. Indexing 1474 objects... remote: Total 1474 (delta 653), reused 965 (delta 372) 100% (1474/1474) done Resolving 653 deltas... 100% (653/653) done root@Falcon:~# cd free60/toolchain root@Falcon:~/free60/toolchain# ./build-xenon-toolchain toolchain No LSB modules are available. Ubuntu or Debian is detected. The build-essential package was detected on your system Creating final xenon toolchain directory: /usr/local/xenon Downloading binutils-2.21.tar.bz2 --10:16:20-- http://ftp.gnu.org/gnu/binutils/binutils-2.21.tar.bz2 => `binutils-2.21.tar.bz2' Resolving ftp.gnu.org... 140.186.70.20 Connecting to ftp.gnu.org|140.186.70.20|:80... connected. HTTP request sent, awaiting response... 404 Not Found 10:16:31 ERROR 404: Not Found. root@Falcon:~/free60/toolchain# [/code] binutils-2.21.tar.bz2 ...not found.  
 But why does it not download the binutils-2.21.1a.tar.bz2 File from the FTP server?  
   
 Thx in Advice...  
 

## 2011-08-31 11:06:26, posted by: dreamboy

hi to fix that issue just download my binutils version and copy paste it into the toolchain folder, that way when you retry to compile the toolchain the script will recognize the file its there and it will compile fine without problem ;) dont forget to install also libmpc-dev ;D  
   
 [url=http://www.megaupload.com/?d=2E9F34UC]http://www.megaupload.com/?d=2E9F34UC[/url]

## 2011-08-31 11:29:24, posted by: Doerek

Normaly i dont like IRC...  
 But Thanks to my HTC HD2 & AndroIRC ~>Dreamboy was able to help me with this Problem.  
 Nicely done...Could you be so Kind and put this File onto the File.libxenon.org Server?   
 [attach=1]   
 "Building binutils, this could take a while" ~~~> **[b]time to configure / make & install some coffee[/b]** :D \o/

### Attachments

[binutils.jpg](binutils.jpg)