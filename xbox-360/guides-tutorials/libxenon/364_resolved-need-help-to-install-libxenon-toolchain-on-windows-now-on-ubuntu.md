# [RESOLVED] Need help to install Libxenon toolchain on WINDOWS - now on UBUNTU

## 2012-10-02 10:51:18, posted by: OOKAMI

update  
   
 with the help of MSYSGIT soft, i performed new installation of GYGWIN and added WGET in order to download what is needed  
 indeed, sh script include the possibility to download what is needed to compile  
   
 after this, i have this result  
   
 $ ./build-xenon-toolchain help  
 ./build-xenon-toolchain: line 29: lsb\_release : commande introuvable  
 Usage:  
 "./build-xenon-toolchain toolchain" (install toolchain + libxenon)  
 "./build-xenon-toolchain libs" (install libxenon + bin2s + libraries seen below)  
 "./build-xenon-toolchain libxenon" (install or update libxenon)  
 "./build-xenon-toolchain zlib" (install or update zlib)  
 "./build-xenon-toolchain libpng" (install or update libpng)  
 "./build-xenon-toolchain bzip2" (install or update bzip2)  
 "./build-xenon-toolchain freetype" (install or update freetype)  
 "./build-xenon-toolchain filesystems" (install libxenon filesystems)  
 "./build-xenon-toolchain cube" (compile the cube sample)  
   
   
 $ ./build-xenon-toolchain toolchain  
 ./build-xenon-toolchain: line 29: lsb\_release : commande introuvable  
 Creating final xenon toolchain directory: /usr/local/xenon  
 Extracting binutils...  
 Configuring binutils...  
   
 xenon folder is created  
 but compilation still not working  
   
 i really don't understand what is missing :(  
   
   
 ---------------------------------------------- FIRST POST  
 Hello  
   
 First, i find this forum by some research for installing libxenon toolchain on windows  
   
 currently, except free60 git, i don't find any tutorial who explain how to set up correctly CYGWIN and what to add for   
   
 GCC   
 Make   
 Git   
 build-essential   
 texinfo   
 Etc.  
   
 i mean, wich version i must install  
   
 i have CYGWIN insatlled but impossible to compile libxenon toolchain properly :p  
   
 someone can help me about ?  
   
 thanks and have a nice day :)  
   
 .

## 2012-10-02 21:45:31, posted by: OOKAMI

hello  
   
 just begin to advance but weirds things about MINGW32  
   
 i can't use properly the standard from CYGWIN but not problem if i launch from MSYSGIT  
   
 i can compile cube and have all others stuff but when i want to compile libxenon toolchain, I have this error  
   
 ./build-xenon-toolchain: line 30: lsb\_release: command not found  
   
   
 this is all the mingw32 purpose for libxenon with this error before compiling  
   
 $ build-xenon-toolchain  
 ./build-xenon-toolchain: line 30: lsb\_release: command not found  
 Usage:  
 "./build-xenon-toolchain toolchain" (install toolchain + libxenon)  
 "./build-xenon-toolchain libs" (install libxenon + bin2s + libraries seen below)  
   
 "./build-xenon-toolchain libxenon" (install or update libxenon)  
 "./build-xenon-toolchain zlib" (install or update zlib)  
 "./build-xenon-toolchain libpng" (install or update libpng)  
 "./build-xenon-toolchain bzip2" (install or update bzip2)  
 "./build-xenon-toolchain freetype" (install or update freetype)  
 "./build-xenon-toolchain cube" (compile the cube sample)  
   
   
 someone can help me about ?  
 thanks :)  
   
 .

## 2012-10-02 22:02:06, posted by: OOKAMI

ok, found it  
   
 removed in the SH file these line  
   
 # variables to check if we are running a debian distribution  
 LSBRELEASE="`lsb\_release -a`"  
 SEARCH\_UBUNTU="Ubuntu"  
 SEARCH\_DEBIAN="Debian"  
 DEB=false  
   
 because i'm not in debian  
   
 now, all seem working  
   
 $ build-xenon-toolchain  
 Usage:  
 "./build-xenon-toolchain toolchain" (install toolchain + libxenon)  
 "./build-xenon-toolchain libs" (install libxenon + bin2s + libraries seen below)  
   
 "./build-xenon-toolchain libxenon" (install or update libxenon)  
 "./build-xenon-toolchain zlib" (install or update zlib)  
 "./build-xenon-toolchain libpng" (install or update libpng)  
 "./build-xenon-toolchain bzip2" (install or update bzip2)  
 "./build-xenon-toolchain freetype" (install or update freetype)  
 "./build-xenon-toolchain cube" (compile the cube sample)  
   
   
 $ build-xenon-toolchain toolchain  
 Ubuntu or Debian is detected.  
 The build-essential package was detected on your system  
 Creating final xenon toolchain directory: /usr/local/xenon  
 mkdir: cannot create directory `/usr/local/xenon': No such file or directory  
 c:\Program Files\Gow\bin\chown.exe: `ookami-net\\ookami:ookami-net\\ookami': inv  
 alid group  
 Downloading binutils-2.22.tar.bz2  
 SYSTEM\_WGETRC = c:/progra~1/wget/etc/wgetrc  
 syswgetrc = c:\Program Files\Gow/etc/wgetrc  
 --2012-10-02 22:08:09-- http://ftp.gnu.org/gnu/binutils/binutils-2.22.tar.bz2  
 Resolving ftp.gnu.org... 208.118.235.20  
 Connecting to ftp.gnu.org|208.118.235.20|:80... connected.  
 HTTP request sent, awaiting response... 200 OK  
 Length: 19973532 (19M) [application/x-bzip2]  
 Saving to: `binutils-2.22.tar.bz2'  
   
 24% [========> ] 4 830 932 66,1K/s eta 7m 30s  
   
   
 even if i have this error, it seem the compilation will working after downloading  
   
 i'll update you when all is done :)  
   
 .

## 2012-10-15 03:22:57, posted by: FreakAlhemist

I don't know any form of code.  
 I was wondering if i could start by learning c++ because i would really love to make some apps on the the 360.  
 Is there an easy way to learn or do i have to go through a 2 year course of classes?   
   
 Also this is my first post on libxenon.  
 I hope i can help and be help around here.