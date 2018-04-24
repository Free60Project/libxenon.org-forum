# Win32 toolchain

## 2011-07-07 00:51:37, posted by: cocker80

Hi, Its just taken me about 4 hours to compile the toolchain in Windows :-\ I have uploaded it to save other people some time...  
   
 [s]http://www.multiupload.com/5GGB0BET45[/s]  
   
 http://www.multiupload.com/7A2BXJA96V - Added altivec support, added libpng-1.5.4  
   
 It consists of gcc-4.6.1, binutils-2.21.1, newlib-1.19, gliglis libxenon(d66eded) and zlib-1.2.5. Hope this will help people.  
   
 Lee.

## 2011-07-07 06:50:59, posted by: gomson

thanks a lot mate... this would really come in handy...

## 2011-07-15 05:19:29, posted by: [cOz]

Thanks a bunch cocker80 for the msys compatible (no cygwin) bins. Out of curiosity (if you even see this) what did you have to deal with to get these to build? I was thinking of using linux to do what the crosstool scripts call a "canadian build" but have never had much luck getting that sort of thing to work.

## 2011-07-16 13:34:04, posted by: cocker80

I used the Msys enviroment (http://www.multiupload.com/CZ82L3CQY0) and downloaded this version of mingw...  
 http://pcxprj.googlecode.com/files/MinGW\_gcc4.6.1release\_static\_win32.7z. (Be sure to delete sed.exe from this packages as is doesnt work aswell as the msys version.)  
   
 I didnt use a built script as such, just took the commands from the libxenon built script and typed (copyed/pasted) them in... [quote] export PATH=$PATH:/c/devkitPro/xbox360/bin  
 export DEVKITXENON=/c/devkitPro/xbox360  
 export CFLAGS="-Os -pipe"  
 export CXXFLAGS="$CFLAGS"  
   
 tar -xf binutils-2.21.1.tar.bz2  
 cd binutils-2.21.1  
 patch -Np1 -i ../binutils.patch  
 mkdir build  
 cd build  
 ../configure --prefix=/c/devkitPro/xbox360 --target=xenon --enable-multilib --disable-nls --disable-werror  
 make configure-host  
 make  
 make install  
   
   
 tar -xf gcc-core-4.6.1.tar.bz2  
 tar -xf gcc-g++-4.6.1.tar.bz2  
 cd gcc-4.6.1  
 patch -Np1 -i ../gcc.patch  
 mkdir build1  
 cd build1   
 ../configure --prefix=/c/devkitPro/xbox360 --target=xenon --enable-multilib --disable-nls --disable-werror \  
 --enable-languages="c" --without-headers --disable-shared --with-newlib --disable-libmudflap --disable-libssp \  
 --disable-shared --without-headers --disable-decimal-float --enable-altivec --with-cpu=cell -enable-interwork  
 make configure-host  
 make all-gcc  
 make install-gcc   
   
 tar -xf newlib-1.19.0.tar.gz  
 cd newlib-1.19.0  
 patch -Np1 -i ../newlib.patch  
 mkdir build  
 cd build  
 ../configure --prefix=/c/devkitPro/xbox360 --target=xenon --enable-multilib --disable-nls\  
 CFLAGS='-DHAVE\_BLKSIZE' --enable-newlib-io-long-long --enable-newlib-io-long-double  
 make configure-host  
 make  
 make install  
   
 cd gcc-4.6.1  
 mkdir build2  
 cd build2  
 ../configure --prefix=/c/devkitPro/xbox360 --target=xenon --enable-multilib --disable-nls --disable-werror --disable-shared \  
 --enable-languages="c,c++" --disable-decimal-float --disable-libquadmath --disable-libssp --disable-libmudflap \  
 --disable-linux-futex --disable-threads --disable-libgomp --enable-altivec --with-newlib --enable-cxx-flags="-G0" --with-cpu=cell   
 make configure-host  
 make  
 make install  
   
 cd libxenon  
 make -C libxenon/ports/xenon libxenon.a   
 make -C libxenon/ports/xenon install  
 cp -av devkitxenon/app.lds devkitxenon/rules $DEVKITXENON/  
 cp libxenon/startup/xenon/crt1.o $DEVKITXENON/xenon/lib/  
 cp libxenon/ports/xenon/crti.o $DEVKITXENON/xenon/lib/  
 cp libxenon/ports/xenon/crtn.o $DEVKITXENON/xenon/lib/  
   
 cd zlib-1.2.5  
 export CC=xenon-gcc  
 export CFLAGS="-mcpu=cell -mtune=cell -m32 -fno-pic -mpowerpc64 $DEVKITXENON/xenon/lib/libxenon.a -L$DEVKITXENON/xenon/lib/32/ -T$DEVKITXENON/app.lds -u read -u \_start -u exc\_base"  
 export LDFLAGS=""  
 ./configure --prefix=$DEVKITXENON/xenon  
 make  
 make install[/quote] I think if you are doing a "canadian build" in linux you would add "--host=i686-pc-mingw32 --target=xenon" to the configure line. (not to sure though)

## 2011-07-26 18:04:42, posted by: michalss

does this work ok?

## 2011-07-26 21:38:11, posted by: MagicSeb

this one works great

## 2011-07-26 21:49:06, posted by: peet8989

how can i compile something using this toolchain?  
   
 lets assume theres a given Makefile.

## 2012-08-16 07:00:08, posted by: orkid1818

I am newbie  
   
 i have error .  
   
 many file missing i think.   
   
 Panasonic@Panasonic-book ~  
 $ export PATH=$PATH:/c/devkitPro/xbox360/bin  
   
 Panasonic@Panasonic-book ~  
 $ export DEVKITXENON=/c/devkitPro/xbox360  
   
 Panasonic@Panasonic-book ~  
 $ export CFLAGS="-Os -pipe"  
   
 Panasonic@Panasonic-book ~  
 $ export CXXFLAGS="$CFLAGS"  
   
 Panasonic@Panasonic-book ~  
 $  
   
 Panasonic@Panasonic-book ~  
 $ tar -xf binutils-2.21.1.tar.bz2  
 cd binutils-2.21.1  
 patch -Np1 -i ../binutils.patch  
 mkdir build  
 cd build  
 ../configure --prefix=/c/devkitPro/xbox360 --target=xenon --enable-multilib --disable-nls --disable-werror  
 make configure-host  
 make  
 make install  
   
   
 tar -xf gcc-core-4.6.1.tar.bz2  
 tar -xf gcc-g++-4.6.1.tar.bz2  
 cd gcc-4.6.1  
 patch -Np1 -i ../gcc.patch  
 mkdir build1  
 cd build1  
 ../configure --prefix=/c/devkitPro/xbox360 --target=xenon --enable-multilib --disable-nls --disable-werror \  
 --enable-languages="c" --without-headers --disable-shared --with-newlib --disable-libmudflap --disable-libssp \  
 --disable-shared --without-headers --disable-decimal-float --enable-altivec --with-cpu=cell -enable-interwork  
 make configure-host  
 make all-gcc  
 make install-gcc  
   
 tar -xf newlib-1.19.0.tar.gz  
 cd newlib-1.19.0  
 patch -Np1 -i ../newlib.patch  
 mkdir build  
 cd build  
 ../configure --prefix=/c/devkitPro/xbox360 --target=xenon --enable-multilib --disable-nls\  
 CFLAGS='-DHAVE\_BLKSIZE' --enable-newlib-io-long-long --enable-newlib-io-long-double  
 make configure-host  
 make  
 make install  
   
 cd gcc-4.6.1  
 mkdir build2  
 cd build2  
 ../configure --prefix=/c/devkitPro/xbox360 --target=xenon --enable-multilib --disable-nls --disable-werror --disable-shared \  
 --enable-languages="c,c++" --disable-decimal-float --disable-libquadmath --disable-libssp --disable-libmudflap \  
 --disable-linux-futex --disable-threads --disable-libgomp --enable-altivec --with-newlib --enable-cxx-flags="-G0" --with-cpu=cell  
 make configure-host  
 make  
 make install  
   
 cd libxenon  
 make -C libxenon/ports/xenon libxenon.a  
 make -C libxenon/ports/xenon install  
 cp -av devkitxenon/app.lds devkitxenon/rules $DEVKITXENON/  
 cp libxenon/startup/xenon/crt1.o $DEVKITXENON/xenon/lib/  
 cp libxenon/ports/xenon/crti.o $DEVKITXENON/xenon/lib/  
 cp libxenon/ports/xenon/crtn.o $DEVKITXENON/xenon/lib/  
   
 cd zlib-1.2.5  
 export CC=xenon-gcc  
 export CFLAGS="-mcpu=cell -mtune=cell -m32 -fno-pic -mpowerpc64 $DEVKITXENON/xenon/lib/libxenon.a -L$DEVKITXENON/xenon/lib/32/ -T$DEVKITXENON/app.lds -u read -u \_start -u exc\_base"  
 export LDFLAGS=""  
 ./configure --prefix=$DEVKITXENON/xenon  
 make  
 make installtar: binutils-2.21.1.tar.bz2: Cannot open: No such file or directory  
 tar: Error is not recoverable: exiting now  
   
 Panasonic@Panasonic-book ~  
 $ cd binutils-2.21.1  
   
 Panasonic@Panasonic-book ~/binutils-2.21.1  
 $ patch -Np1 -i ../binutils.patch  
 E:\Cygwin\bin\patch.exe: **** Can't open patch file ../binutils.patch : No such file or directory  
   
 Panasonic@Panasonic-book ~/binutils-2.21.1  
 $ mkdir build  
 mkdir: cannot create directory `build': File exists  
   
 Panasonic@Panasonic-book ~/binutils-2.21.1  
 $ cd build  
   
 Panasonic@Panasonic-book ~/binutils-2.21.1/build  
 $ ../configure --prefix=/c/devkitPro/xbox360 --target=xenon --enable-multilib --disable-nls --disable-werror  
 ../configure: line 532: sed: command not found  
 ../configure: line 961: sed: command not found  
 ../configure: line 935: sed: command not found  
 ../configure: line 935: sed: command not found  
 ../configure: line 1357: sed: command not found  
 ../configure: line 1795: sed: command not found  
 ../configure: line 2166: sed: command not found  
 configure: error: cannot run /bin/sh ../config.sub  
 ../configure: line 91: sed: command not found  
 ../configure: line 37: sed: command not found  
   
 Panasonic@Panasonic-book ~/binutils-2.21.1/build  
 $ make configure-host  
 -bash: make: command not found  
   
 Panasonic@Panasonic-book ~/binutils-2.21.1/build  
 $ make  
 -bash: make: command not found  
   
 Panasonic@Panasonic-book ~/binutils-2.21.1/build  
 $ make install  
 -bash: make: command not found  
   
 Panasonic@Panasonic-book ~/binutils-2.21.1/build  
 $  
   
 Panasonic@Panasonic-book ~/binutils-2.21.1/build  
 $  
   
 Panasonic@Panasonic-book ~/binutils-2.21.1/build  
 $ tar -xf gcc-core-4.6.1.tar.bz2  
 tar: gcc-core-4.6.1.tar.bz2: Cannot open: No such file or directory  
 tar: Error is not recoverable: exiting now  
   
 Panasonic@Panasonic-book ~/binutils-2.21.1/build  
 $ tar -xf gcc-g++-4.6.1.tar.bz2  
 tar: gcc-g++-4.6.1.tar.bz2: Cannot open: No such file or directory  
 tar: Error is not recoverable: exiting now  
   
 Panasonic@Panasonic-book ~/binutils-2.21.1/build  
 $ cd gcc-4.6.1  
 -bash: cd: gcc-4.6.1: No such file or directory  
   
 Panasonic@Panasonic-book ~/binutils-2.21.1/build  
 $ patch -Np1 -i ../gcc.patch  
 E:\Cygwin\bin\patch.exe: **** Can't open patch file ../gcc.patch : No such file or directory  
   
 Panasonic@Panasonic-book ~/binutils-2.21.1/build  
 $ mkdir build1  
 mkdir: cannot create directory `build1': File exists  
   
 Panasonic@Panasonic-book ~/binutils-2.21.1/build  
 $ cd build1  
   
 Panasonic@Panasonic-book ~/binutils-2.21.1/build/build1  
 $ ../configure --prefix=/c/devkitPro/xbox360 --target=xenon --enable-multilib --disable-nls --disable-werror \  
 > --enable-languages="c" --without-headers --disable-shared --with-newlib --disable-libmudflap --disable-libssp \  
 > --disable-shared --without-headers --disable-decimal-float --enable-altivec --with-cpu=cell -enable-interwork  
 -bash: ../configure: No such file or directory  
   
 Panasonic@Panasonic-book ~/binutils-2.21.1/build/build1  
 $ make configure-host  
 -bash: make: command not found  
   
 Panasonic@Panasonic-book ~/binutils-2.21.1/build/build1  
 $ make all-gcc  
 -bash: make: command not found  
   
 Panasonic@Panasonic-book ~/binutils-2.21.1/build/build1  
 $ make install-gcc  
 -bash: make: command not found  
   
 Panasonic@Panasonic-book ~/binutils-2.21.1/build/build1  
 $  
   
 Panasonic@Panasonic-book ~/binutils-2.21.1/build/build1  
 $ tar -xf newlib-1.19.0.tar.gz  
 tar: newlib-1.19.0.tar.gz: Cannot open: No such file or directory  
 tar: Error is not recoverable: exiting now  
   
 Panasonic@Panasonic-book ~/binutils-2.21.1/build/build1  
 $ cd newlib-1.19.0  
 -bash: cd: newlib-1.19.0: No such file or directory  
   
 Panasonic@Panasonic-book ~/binutils-2.21.1/build/build1  
 $ patch -Np1 -i ../newlib.patch  
 E:\Cygwin\bin\patch.exe: **** Can't open patch file ../newlib.patch : No such file or directory  
   
 Panasonic@Panasonic-book ~/binutils-2.21.1/build/build1  
 $ mkdir build  
 mkdir: cannot create directory `build': File exists  
   
 Panasonic@Panasonic-book ~/binutils-2.21.1/build/build1  
 $ cd build  
   
 Panasonic@Panasonic-book ~/binutils-2.21.1/build/build1/build  
 $ ../configure --prefix=/c/devkitPro/xbox360 --target=xenon --enable-multilib --disable-nls\  
 > CFLAGS='-DHAVE\_BLKSIZE' --enable-newlib-io-long-long --enable-newlib-io-long-double  
 -bash: ../configure: No such file or directory  
   
 Panasonic@Panasonic-book ~/binutils-2.21.1/build/build1/build  
 $ make configure-host  
 -bash: make: command not found  
   
 Panasonic@Panasonic-book ~/binutils-2.21.1/build/build1/build  
 $ make  
 -bash: make: command not found  
   
 Panasonic@Panasonic-book ~/binutils-2.21.1/build/build1/build  
 $ make install  
 -bash: make: command not found  
   
 Panasonic@Panasonic-book ~/binutils-2.21.1/build/build1/build  
 $  
   
 Panasonic@Panasonic-book ~/binutils-2.21.1/build/build1/build  
 $ cd gcc-4.6.1  
 -bash: cd: gcc-4.6.1: No such file or directory  
   
 Panasonic@Panasonic-book ~/binutils-2.21.1/build/build1/build  
 $ mkdir build2  
 mkdir: cannot create directory `build2': File exists  
   
 Panasonic@Panasonic-book ~/binutils-2.21.1/build/build1/build  
 $ cd build2  
   
 Panasonic@Panasonic-book ~/binutils-2.21.1/build/build1/build/build2  
 $ ../configure --prefix=/c/devkitPro/xbox360 --target=xenon --enable-multilib --disable-nls --disable-werror --disable-shared \  
 > --enable-languages="c,c++" --disable-decimal-float --disable-libquadmath --disable-libssp --disable-libmudflap \  
 > --disable-linux-futex --disable-threads --disable-libgomp --enable-altivec --with-newlib --enable-cxx-flags="-G0" --with-cpu=cell  
 -bash: ../configure: No such file or directory  
   
 Panasonic@Panasonic-book ~/binutils-2.21.1/build/build1/build/build2  
 $ make configure-host  
 -bash: make: command not found  
   
 Panasonic@Panasonic-book ~/binutils-2.21.1/build/build1/build/build2  
 $ make  
 -bash: make: command not found  
   
 Panasonic@Panasonic-book ~/binutils-2.21.1/build/build1/build/build2  
 $ make install  
 -bash: make: command not found  
   
 Panasonic@Panasonic-book ~/binutils-2.21.1/build/build1/build/build2  
 $  
   
 Panasonic@Panasonic-book ~/binutils-2.21.1/build/build1/build/build2  
 $ cd libxenon  
 -bash: cd: libxenon: No such file or directory  
   
 Panasonic@Panasonic-book ~/binutils-2.21.1/build/build1/build/build2  
 $ make -C libxenon/ports/xenon libxenon.a  
 -bash: make: command not found  
   
 Panasonic@Panasonic-book ~/binutils-2.21.1/build/build1/build/build2  
 $ make -C libxenon/ports/xenon install  
 -bash: make: command not found  
   
 Panasonic@Panasonic-book ~/binutils-2.21.1/build/build1/build/build2  
 $ cp -av devkitxenon/app.lds devkitxenon/rules $DEVKITXENON/  
 cp: target `/c/devkitPro/xbox360/' is not a directory  
   
 Panasonic@Panasonic-book ~/binutils-2.21.1/build/build1/build/build2  
 $ cp libxenon/startup/xenon/crt1.o $DEVKITXENON/xenon/lib/  
 cp: cannot stat `libxenon/startup/xenon/crt1.o': No such file or directory  
   
 Panasonic@Panasonic-book ~/binutils-2.21.1/build/build1/build/build2  
 $ cp libxenon/ports/xenon/crti.o $DEVKITXENON/xenon/lib/  
 cp: cannot stat `libxenon/ports/xenon/crti.o': No such file or directory  
   
 Panasonic@Panasonic-book ~/binutils-2.21.1/build/build1/build/build2  
 $ cp libxenon/ports/xenon/crtn.o $DEVKITXENON/xenon/lib/  
 cp: cannot stat `libxenon/ports/xenon/crtn.o': No such file or directory  
   
 Panasonic@Panasonic-book ~/binutils-2.21.1/build/build1/build/build2  
 $  
   
 Panasonic@Panasonic-book ~/binutils-2.21.1/build/build1/build/build2  
 $ cd zlib-1.2.5  
 -bash: cd: zlib-1.2.5: No such file or directory  
   
 Panasonic@Panasonic-book ~/binutils-2.21.1/build/build1/build/build2  
 $ export CC=xenon-gcc  
   
 Panasonic@Panasonic-book ~/binutils-2.21.1/build/build1/build/build2  
 $ export CFLAGS="-mcpu=cell -mtune=cell -m32 -fno-pic -mpowerpc64 $DEVKITXENON/xenon/lib/libxenon.a -L$DEVKITXENON/xenon/lib/32/ -T$DEVKITXENON/app.lds -u read -u \_start -u exc\_base"  
   
 Panasonic@Panasonic-book ~/binutils-2.21.1/build/build1/build/build2  
 $ export LDFLAGS=""  
   
 Panasonic@Panasonic-book ~/binutils-2.21.1/build/build1/build/build2  
 $ ./configure --prefix=$DEVKITXENON/xenon  
 -bash: ./configure: No such file or directory  
   
 Panasonic@Panasonic-book ~/binutils-2.21.1/build/build1/build/build2  
 $ make  
 -bash: make: command not found  
   
 Panasonic@Panasonic-book ~/binutils-2.21.1/build/build1/build/build2  
 $ make install

## 2012-08-16 07:08:11, posted by: sk1080

even if you happened to have the right files win32 toolchain build is broken at the moment and won't work  
 I can post my precompiled one, but you WILL have issues compiling stuff without modification

## 2012-08-16 07:17:19, posted by: orkid1818

[quote="sk1080"]  
 even if you happened to have the right files win32 toolchain build is broken at the moment and won't work  
 I can post my precompiled one, but you WILL have issues compiling stuff without modification  
 [/quote]  
   
 I think i try install ubuntu more easy right ?

## 2012-10-02 11:30:34, posted by: OOKAMI

[quote="cocker80"]  
 Hi, Its just taken me about 4 hours to compile the toolchain in Windows :-\ I have uploaded it to save other people some time...  
   
 [s]http://www.multiupload.com/5GGB0BET45[/s]  
   
 http://www.multiupload.com/7A2BXJA96V - Added altivec support, added libpng-1.5.4  
   
 It consists of gcc-4.6.1, binutils-2.21.1, newlib-1.19, gliglis libxenon(d66eded) and zlib-1.2.5. Hope this will help people.  
   
 Lee.  
 [/quote]  
   
 very interesting but links are dead :(  
   
 can you upload it again please ?  
   
 thanks :)  
   
 .