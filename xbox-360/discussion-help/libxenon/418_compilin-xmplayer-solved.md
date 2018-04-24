# [compilin] xmplayer {solved}

## 2013-09-19 04:00:50, posted by: mesmer

guys i try compile the xmplayer and i get this error, i already search and can't find the solution, or a patch to resolve, somebody can give the light?  
   
 filebrowser.cpp: In function 'int ParseDirectory()':  
 filebrowser.cpp:362:18: error: 'struct dirent' has no member named 'd\_mtime'  
 filebrowser.cpp:363:39: error: 'struct dirent' has no member named 'd\_mtime'  
   
 obs: i use gcc 4.7.3, with all libs and the 2 libs that xmplayer ask  
   
 sorry my bad english

## 2013-09-19 07:00:35, posted by: Swizzy

Use my branch instead of the "master" branch for libxenon...

## 2013-09-19 19:35:52, posted by: medaved

i'm not compiling libiconv\_1.13.1? mint 15(ubuntu 13.04) [code]cd lib && make all make[1]: ???? ? ??????? `/home/medaved/xmplayer/libs/libiconv\_1.13.1/lib' /bin/bash ../libtool --mode=link gcc -g -O2 -fvisibility=hidden -o libiconv.la -rpath /usr/local/lib -version-info 7:0:5 -no-undefined iconv.lo localcharset.lo relocatable.lo libtool: Version mismatch error. This is libtool 2.4.2.391-ebeb8a, but the libtool: definition of this LT\_INIT comes from libtool 2.2.6. libtool: You should recreate aclocal.m4 with macros from libtool 2.4.2.391-ebeb8a libtool: and run autoconf again. make[1]: *** [libiconv.la] ?????? 63 make[1]: ????? ?? ???????? `/home/medaved/xmplayer/libs/libiconv\_1.13.1/lib' make: *** [all] ?????? 2[/code]

## 2013-09-19 22:06:51, posted by: siz

Use these: https://docs.google.com/file/d/0B15oIdn\_3vKMVkFFR2J6bXhCY1k/edit?pli=1  
   
 Just "make install" them both

## 2013-09-21 06:12:53, posted by: mesmer

[quote="Swizzy"]  
 Use my branch instead of the "master" branch for libxenon...  
 [/quote]  
   
 i don't get what branch,can u help me?   
 that's you git right? thx  
 https://github.com/Swizzy?tab=repositories  
   
 [quote="siz"]  
 Use these: https://docs.google.com/file/d/0B15oIdn\_3vKMVkFFR2J6bXhCY1k/edit?pli=1  
   
 Just "make install" them both  
 [/quote]  
   
 i download now, i'll try compile and post here thx

## 2013-09-21 06:18:44, posted by: mesmer

[quote="siz"]  
 Use these: https://docs.google.com/file/d/0B15oIdn\_3vKMVkFFR2J6bXhCY1k/edit?pli=1  
   
 Just "make install" them both  
 [/quote]  
   
 i use your libs and same error of filebrowser show up " error: 'struct dirent' has no member named 'd\_mtime'"

## 2013-09-21 06:24:14, posted by: mesmer

[quote="medaved"]  
 i'm not compiling libiconv\_1.13.1? mint 15(ubuntu 13.04) [code]cd lib && make all make[1]: ???? ? ??????? `/home/medaved/xmplayer/libs/libiconv\_1.13.1/lib' /bin/bash ../libtool --mode=link gcc -g -O2 -fvisibility=hidden -o libiconv.la -rpath /usr/local/lib -version-info 7:0:5 -no-undefined iconv.lo localcharset.lo relocatable.lo libtool: Version mismatch error. This is libtool 2.4.2.391-ebeb8a, but the libtool: definition of this LT\_INIT comes from libtool 2.2.6. libtool: You should recreate aclocal.m4 with macros from libtool 2.4.2.391-ebeb8a libtool: and run autoconf again. make[1]: *** [libiconv.la] ?????? 63 make[1]: ????? ?? ???????? `/home/medaved/xmplayer/libs/libiconv\_1.13.1/lib' make: *** [all] ?????? 2[/code] [/quote]  
   
 i think you does the normal ./configure yes? thats the erro the libs already configured, so just make and install   
 delete the folder extract again and try now with just   
   
 "make" and "make install"   
   
 or you need to do "./configure --prefix="/usr/local/xenon/" i think

## 2013-09-21 08:52:57, posted by: Swizzy

[quote="mesmer"]  
 [quote="siz"]  
 Use these: https://docs.google.com/file/d/0B15oIdn\_3vKMVkFFR2J6bXhCY1k/edit?pli=1  
   
 Just "make install" them both  
 [/quote]  
   
 i use your libs and same error of filebrowser show up " error: 'struct dirent' has no member named 'd\_mtime'"  
 [/quote]  
   
 That is because you're not using my libxenon branch, the "main" branch don't have those defined... switch to my branch of libxenon and compile libxenon again using "./build-xenon-toolchain libxenon"  
   
 to switch to my branch just go to the libxenon folder (where you downloaded the toolchain) and type in "git checkout Swizzy"

## 2013-09-21 19:28:56, posted by: mesmer

[quote="Swizzy"]  
 [quote="mesmer"]  
 [quote="siz"]  
 Use these: https://docs.google.com/file/d/0B15oIdn\_3vKMVkFFR2J6bXhCY1k/edit?pli=1  
   
 Just "make install" them both  
 [/quote]  
   
 i use your libs and same error of filebrowser show up " error: 'struct dirent' has no member named 'd\_mtime'"  
 [/quote]  
   
 That is because you're not using my libxenon branch, the "main" branch don't have those defined... switch to my branch of libxenon and compile libxenon again using "./build-xenon-toolchain libxenon"  
   
 to switch to my branch just go to the libxenon folder (where you downloaded the toolchain) and type in "git checkout Swizzy"  
 [/quote]  
   
 thx man now i get this, i 'll try compile now, thx :)

## 2013-09-21 19:42:56, posted by: mesmer

thx Swizzy now that's all ok, your branch saves my day :)