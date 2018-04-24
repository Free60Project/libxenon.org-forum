# Installing toolchain and libxenon from AUR on archlinux.

## 2011-09-16 09:59:57, posted by: mfischer

As I'm using archlinux I created some PKGBUILDs to facilitate the installation for others ;-)  
   
 binutils  
 https://aur.archlinux.org/packages.php?ID=52422  
   
 gcc-base  
 https://aur.archlinux.org/packages.php?ID=52423  
   
 newlib  
 https://aur.archlinux.org/packages.php?ID=52424  
   
 gcc-elf  
 https://aur.archlinux.org/packages.php?ID=52423  
   
 libxenon  
 https://aur.archlinux.org/packages.php?ID=52426  
   
 If you intend to use them, build / install them in the order above (gcc-base is 1st pass, gcc-elf the 2nd pass of the gcc compilation).  
 Don't forget to add an export DEVKITXENON="/usr/xenon" to your .profile or .bashrc / .zshrc.  
 Let me know if you find some errors ...  
   
 Cheers

## 2011-09-20 23:15:58, posted by: peet8989

how do i then initialize a build process ?

## 2011-09-25 11:57:12, posted by: mfischer

How do you mean initiate a build process? The PKGBUILDS are to bootstrap a build environment on your PC running Archlinux. Are you running Archlinux on your dev machine?  
   
 if yes you might want to take a look at :  
   
 #$ man 8 makepkg  
   
 and   
   
 https://wiki.archlinux.org/index.php/AUR  
   
 If I missunderstood your question, feel free to ask again ;-)

## 2012-04-14 22:38:03, posted by: rz2k

latest Arch uses gcc 4.7, which has a bug compiling gcc 4.6.*. AUR packages are now broken.  
   
 here is bug on gcc bugtracker http://gcc.gnu.org/bugzilla/show\_bug.cgi?id=51969  
   
 if you have something like this: [code]gtype-desc.c:8770:18: error: subscripted value is neither array nor pointer nor vector gtype-desc.c:8889:36: error: subscripted value is neither array nor pointer nor vector gtype-desc.c:8973:31: error: subscripted value is neither array nor pointer nor vector gtype-desc.c:8994:31: error: subscripted value is neither array nor pointer nor vector gtype-desc.c:9001:31: error: subscripted value is neither array nor pointer nor vector gtype-desc.c:9008:31: error: subscripted value is neither array nor pointer nor vector[/code] apply this diff http://gcc.gnu.org/viewcvs/branches/gcc-4\_6-branch/gcc/gengtype.c?r1=184239&r2=184238&pathrev=184239 to your gcc 4.6.*