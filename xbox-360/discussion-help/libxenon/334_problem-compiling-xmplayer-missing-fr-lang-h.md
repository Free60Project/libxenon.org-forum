# problem compiling xmplayer missing Fr_lang.h

## 2012-07-11 00:36:06, posted by: ravendrow

so since ced2911 decided to retire i decided to try to pickup xmplayer as a pet project i have a few idea's on code improvements that i would like to try but every time i try to compile i get   
   
 xmplayer/source/gettext.cpp:7:30: fatal error: ../build/fr\_lang.h: No such file or directory  
 compilation terminated.  
 make[1]: *** [gettext.o] Error 1  
 make: *** [build] Error 2  
   
 i have tried just removing #include "../build/fr\_lang.h" but it is also required for menu.cpp so to save myself a lot of time removing the Fr option i just thought i would ask if anyone knows why fr\_lang.h is missing from the build folder and can someone please add it to the git hub?

## 2012-07-11 00:44:14, posted by: Juvenal

fr\_lang.h is built from a file called fr.lang in the source/lang folder.  
   
 it requires bin2o, so you are likely missing that and it just failed silently for some reason.  
   
 i cant remember where to find it, since we only include bin2s with the toolchain scripts. google should be able to help

## 2012-07-11 05:34:39, posted by: ravendrow

ok so i think i found it is it   
 http://www.darkfader.net/toolbox/  
   
 he has a bin2o but the only thing inside the zip is bin2o.cpp? how would i go about installing that as a lib?

## 2012-07-11 05:36:50, posted by: Juvenal

[code]* *gcc bin2o.cpp -o bin2o cp bin2o $DEVKITXENON/bin [/code]

## 2012-07-11 05:59:20, posted by: ravendrow

[quote="Juvenal"] [code]* *gcc bin2o.cpp -o bin2o cp bin2o $DEVKITXENON/bin [/code] [/quote]  
   
 dude thanks so i tried that and got   
 [code]* *bin2o.cpp: In function ‘int main(int, char**)’: bin2o.cpp:256:26: error: ‘strlwr’ was not declared in this scope [/code] not sure if i just found an old one or what, i know all my other libs are the most current available 

## 2012-07-11 06:05:05, posted by: Juvenal

comment that line (//) and it should build/work fine

## 2012-07-11 07:11:45, posted by: ravendrow

[quote="Juvenal"]  
 comment that line (//) and it should build/work fine  
 [/quote]  
   
 k so that got bin2o installed but i still can't build Xmplayer , still getting the same error i was in the OP  
   
   
 wait n/m after commenting that line out i get   
 [code]* *bin2o.cpp:(.text+0x717): undefined reference to `operator new[](unsigned int)' bin2o.cpp:(.text+0x7a0): undefined reference to `operator delete(void*)' collect2: ld returned 1 exit status [/code]

## 2012-07-11 09:19:20, posted by: sk1080

I may be wrong, but try g++ instead of gcc

## 2012-07-11 19:12:52, posted by: ravendrow

@sk1080 worked perfect got the stupid bin2o installed but i am still having the same issue just to make sure i have everything i need installed here is a run down of my installed libs  
   
 toolchain  
 libxenon  
 zlib  
 libpng  
 bzip2  
 freetype  
 bin2s  
 libSDLxenon  
 libext2  
 libfat  
 libntfs  
 xtaflib  
 ZLX library   
 SDL\_ttf  
   
 if i am missing something please let me know

## 2012-07-11 22:41:51, posted by: sk1080

You are missing some stuff that isn't on the git...

## 2012-07-11 22:54:19, posted by: ravendrow

[quote="sk1080"]  
 You are missing some stuff that isn't on the git...  
 [/quote]  
   
 anyway you could help me out with that? i just need to be able to compile a working version so i can start making improvements

## 2012-07-11 23:01:42, posted by: sk1080

Hang on, we are working on it

## 2012-07-11 23:17:45, posted by: ravendrow

thanks bro ...can't wait

## 2012-07-12 04:48:31, posted by: sk1080

comment all the stuff related to fr\_lang, the image doesn't exist

## 2012-07-12 07:59:21, posted by: ravendrow

k so did that and now it is asking for a whole mess of libs i dont have i do however think i have found most of them at https://github.com/xPreatorianx/mplayer-xenon my only ? is they look already compiled so do i just copy the folders to where the rest of my libs are? or am i barking up the wrong tree?

## 2012-07-12 08:10:53, posted by: sk1080

too lazy to post these anywhere nice at the moment, so for now use these links provided by Ced:  
   
 https://docs.google.com/open?id=0B15oIdn\_3vKMZFZxWkdnVFM2MW8  
 https://docs.google.com/open?id=0B15oIdn\_3vKMY2RKY1haaV9XeVE  
   
 do make install for each of those  
   
 ignore Preatorian's repo, it is a really old version

## 2012-07-13 20:54:19, posted by: siz

[quote="sk1080"]  
 too lazy to post these anywhere nice at the moment, so for now use these links provided by Ced:  
   
 https://docs.google.com/open?id=0B15oIdn\_3vKMZFZxWkdnVFM2MW8  
 https://docs.google.com/open?id=0B15oIdn\_3vKMY2RKY1haaV9XeVE  
   
 do make install for each of those  
   
 ignore Preatorian's repo, it is a really old version  
 [/quote]  
   
 Hey, I've got both lib's from the url and patched them with patch -p1 < patchname.patch and make installed them, however when compiling xmplayer I still get "*[i]/usr/local/xenon/lib/gcc/xenon/4.6.1/../../../../xenon/bin/ld: cannot find -liconv[/i]*" and "-lfribidi" (also a missing fribidi/fribidi.h in subreader.h). Tried to "*[i]./configure --prefix=/usr/local/xenon/usr/include/fribidi[/i]*", it didn't help.   
   
 Btw the avcodec, avformat, swscale etc. are they just regular ffmpeg libs? because apt-get install ffmpeg doesn't help.

## 2012-07-13 21:58:49, posted by: sk1080

Don't run configure or patch anything  
 those are ready to go  
   
 extract the archives again and simply run  
   
 make  
 make install(supposing you have write permission, otherwise sudo it)  
   
 EDIT:  
 also you probably dropped those in /usr/local if you ran configure, so watch out

## 2012-07-13 23:02:11, posted by: siz

You have to configure fribidi and iconv or else you get "make: *** No targets specified and no makefile found. Stop.", fribidi's installation guide says use ./configure --prefix=/usr/, libiconv says ./configure --prefix=/usr/local", which I did before, with a new extracted I tried /usr/, however no luck.  
   
 The libs.7z only contains 2 patches and a url file with 2 links to fribidi and iconv, mxml-2.6 installs out of the box. Sure you have linked to the right one?

## 2012-07-13 23:03:50, posted by: sk1080

Ah, seems the zip copy is different than the 7z one I linked, hang on....

## 2012-07-13 23:09:50, posted by: sk1080

anyway, in that case you will have to configure with all the usual libxenon stuff  
   
 --build=xenon(or something), export that long CFLAGS list, --prefix=/usr/local/xenon/usr, etcetc  
   
 EDIT: I really am derping today with a double post and all

## 2012-07-13 23:27:54, posted by: tuxuser

Try:  
 [code]* *wget http://gitbrew.org/~tuxuser/libs/libiconv.sh chmod +x libiconv.sh ./libiconv.sh [/code] [code]* *wget http://gitbrew.org/~tuxuser/libs/fribidi.sh chmod +x fribidi.sh ./fribidi.sh [/code] If that doesnt work, https://docs.google.com/file/d/0B15oIdn\_3vKMVkFFR2J6bXhCY1k/edit?pli=1  
   
 cd to folder, and do "make install".. not sure if a previous make is needed..

## 2012-07-13 23:40:16, posted by: siz

thanks tuxuser, worked like a charm :)   
   
 All I need now is to get my hands on the missing libs, looks like all ffmpeg related "-lmplayer -lavformat -lavcodec -lswscale -lavutil -lpostproc", has Ced's ffmpeg port been taken down, can't seem to find it?

## 2012-07-13 23:41:03, posted by: tuxuser

nope, if you execute "make" in xmplayer's rootdir, it compiles all those ;)

## 2012-07-13 23:46:11, posted by: siz

Nice, but it can't seem to find them: [code]* */usr/local/xenon/lib/gcc/xenon/4.6.1/../../../../xenon/bin/ld: cannot find -lmplayer /usr/local/xenon/lib/gcc/xenon/4.6.1/../../../../xenon/bin/ld: cannot find -lavformat /usr/local/xenon/lib/gcc/xenon/4.6.1/../../../../xenon/bin/ld: cannot find -lavcodec /usr/local/xenon/lib/gcc/xenon/4.6.1/../../../../xenon/bin/ld: cannot find -lswscale /usr/local/xenon/lib/gcc/xenon/4.6.1/../../../../xenon/bin/ld: cannot find -lavutil /usr/local/xenon/lib/gcc/xenon/4.6.1/../../../../xenon/bin/ld: cannot find -lpostproc /usr/local/xenon/usr/lib/libext2fs.a(mmp.o): In function `sleep': mmp.c:(.text+0x0): multiple definition of `sleep' mount.o:/home/siz/xmplayer/source/mount.c:483: first defined here collect2: ld returned 1 exit status make[1]: *** [/home/siz/xmplayer/xmplayer.elf] Error 1 make: *** [build] Error 2 [/code]

## 2012-07-14 02:40:22, posted by: tuxuser

Just verified:  
   
 Worked for me with a fresh "git clone" after doin:  
 [code]* *cd xmplayer cp source/lang/fr.lang data/ nano source/winput.c # Modify references to "select" to "back" make -j 5 [/code]   
 EDIT:  
   
 Fixed the Repo, just do "git stash && git pull" and a simple "make" should work ;)

## 2012-07-14 12:48:42, posted by: siz

Thanks tux, it compiled :) I had to comment the sleep function in source/mount.c because it complained about duplicate with one in the ext2fs lib.   
 So changed xmplayer.elf to symbols.elf and xmplayer.elf32 to xenon.elf, took mplayer folder from 0.0.1a release, and it's running :D   
 However, it freezes when pressing A to play a video.

## 2012-07-14 20:40:32, posted by: sk1080

You need a spinlock fix, either the ghetto one we were using earlier(idk if thats on github anywhere), or the less-ghetto one from Nate, stand by for patch  
   
 EDIT: http://madhack.tk/xenon/lock.diff  
 we don't actually know if that is stable, so it hasn't been merged yet, however, it seems to work fine for mplayer

## 2012-07-14 22:11:41, posted by: siz

Thanks sk1080 :) everything seems to work, already messing around with the code :D

## 2012-07-15 00:18:08, posted by: sk1080

Glad I could help

## 2012-07-16 22:10:52, posted by: siz

Hey guys, maybe I'm just plain stupid ???, but I've made a file\_exists function in source\menu.cpp, and use it there to check if a file exists in mplayer\font\, but can't seem to get the path right when it's compiled. Tried mplayer\font\file, font\file, ..\mplayer\font\file, font/file etc., but can't seem to get it to work, i'm just using fopen with read mode: [code]bool file\_exists(const char * filename) { if (FILE * file = fopen(filename, "r")) { fclose(file); return true; } return false; }[/code] Any thoughts?

## 2012-07-16 23:46:15, posted by: tuxuser

[code]* *bool file\_exists(const char * filename) { FILE * fd; fd = fopen(filename, "rb"); if (fd != NULL) { fclose(fd); return true; } return false; } void main() { char *filepath = "uda:/mplayer/font/file.ext"; // It needs a ABSOULTE PATH, relative path unsupported bool ret = file\_exists(filepath); if (ret == true) printf("It exists!\n"); else printf("Doesn't exist!\n"); } [/code] greetz

## 2012-07-17 01:46:52, posted by: siz

Thx tux, trying relative paths won't get you anywhere when they aren't supported :D Now I got a simplish way to change font size (but rather complicated in the long run), oh well when my summer vacation consists of 90 % rain, why not play a little with code :)