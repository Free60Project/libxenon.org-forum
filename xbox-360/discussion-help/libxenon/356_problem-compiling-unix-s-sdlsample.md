# Problem compiling UNIX's SDLSample

## 2012-09-16 16:23:38, posted by: ch.kenned

root@UBUNTU:~/IUNIXI/Xbox-360-Homebrew/SDLSample# make  
 [main.c]  
 In file included from /root/IUNIXI/Xbox-360-Homebrew/SDLSample/source/main.c:4:0:  
 /root/IUNIXI/Xbox-360-Homebrew/SDLSample/source/video\_init.h: In function 'mainInit':  
 /root/IUNIXI/Xbox-360-Homebrew/SDLSample/source/video\_init.h:9:2: warning: implicit declaration of function 'kmem\_init' [-Wimplicit-function-declaration]  
 linking ... SDLSample.elf  
 /usr/local/xenon/usr/lib/libSDL.a(SDL\_xenonaudio.o): In function `add\_to\_buffer':  
 SDL\_xenonaudio.c:(.text.add\_to\_buffer+0x50): undefined reference to `ceil'  
 collect2: ld returned 1 exit status  
 make[1]: *** [/root/IUNIXI/Xbox-360-Homebrew/SDLSample/SDLSample.elf] Error 1  
 make: *** [build] Error 2  
   
 The issue with undefined reference to 'ceil' appears with almost every SDL app I try to make. Thanks for any insight.

## 2012-09-16 17:06:38, posted by: ch.kenned

I imagine this has something to do with the includes. The ceil function should be taken care of by the -lm included in the makefile, though?

## 2012-09-16 19:08:33, posted by: ch.kenned

So, I stripped all of the SDL code of the audio related functions and edited the makefile. I also edited UNIX's code to run mainInit() so that libXenon stuff was initialized. It works!

## 2012-09-23 19:39:25, posted by: sabbath06

I am having this exact same problem as well. Just set up my dev environment per the pdf and installed SDL. Can't compile the SDL example because I get 'undefined reference to ceil'  
   
 Also, when trying to compile sdlquake I get the following:  
   
   
 linking ... sdlquake-libxenon.elf  
 sys\_sdl.o: In function `main':  
 /home/charlie/sdlquake-libxenon/src/sys\_sdl.c:409: undefined reference to `argv\_GetFilepath'  
 collect2: ld returned 1 exit status  
 make[1]: *** [/home/charlie/sdlquake-libxenon/sdlquake-libxenon.elf] Error 1  
 make: *** [build] Error 2  
   
   
 Any help would be greatly appreciated!

## 2012-09-24 01:27:24, posted by: sk1080

wrong libxenon repo maybe?  
 idk, might want to come on irc with more info

## 2012-09-24 19:37:16, posted by: sabbath06

I used the free60project repo to install the toolchain, libxenon, and the libs. I grabbed the sdl and sdlquake code from the libxenonproject repo and the above is what I get when I try to build the Sdlexample. Building and installing the sdl library didn't give me any errors.

## 2012-09-24 19:39:27, posted by: sk1080

Sorry I missed you on irc, I will check this issue when I have time

## 2012-09-26 02:38:58, posted by: sabbath06

Thanks I appreciate it. I did another test to try and eliminate as many variables as possible.   
   
   
 First I did a fresh install of ubuntu 12.04 running on vmware 9 and then followed this tutorial exactly to install the toolchain and libxenon:  
   
 [url=http://libxenon.org/http://libxenon.org//viewtopic.php?p=404#p404]http://libxenon.org/http://libxenon.org//viewtopic.php?p=404#p404[/url]  
   
 Then installed zlib, libpng and bin2s per this tutorial:  
   
 [url=http://libxenon.org/http://libxenon.org//viewtopic.php?p=465#p465]http://libxenon.org/http://libxenon.org//viewtopic.php?p=465#p465[/url]  
   
 Lastly, I installed SDL per this link:  
   
 [url=http://libxenon.org/http://libxenon.org//viewtopic.php?t=4]http://libxenon.org/http://libxenon.org//viewtopic.php?t=4[/url]  
   
   
 This time I only tried to compile the plasma demo which was included with SDL. This is the output from make:  
   
 [code]* *charlie@ubuntu:~/libSDLXenon/demos/plasma-1.0$ make linking ... plasma-1.0.elf /usr/local/xenon/usr/lib/libxenon.a(newlib.o): In function `gettimeofday': /home/charlie/free60project-github/libxenon/libxenon/ports/xenon/../../drivers/newlib/newlib.c:169: multiple definition of `gettimeofday' libxenon\_miss.o:/home/charlie/libSDLXenon/demos/plasma-1.0/src/libxenon\_miss.c:28: first defined here /usr/local/xenon/usr/lib/libxenon.a(newlib.o): In function `stat': newlib.c:(.text.stat+0x0): multiple definition of `stat' libxenon\_miss.o:/home/charlie/libSDLXenon/demos/plasma-1.0/src/libxenon\_miss.c:15: first defined here /usr/local/xenon/usr/lib/libSDL.a(SDL\_xenonaudio.o): In function `add\_to\_buffer': SDL\_xenonaudio.c:(.text.add\_to\_buffer+0x50): undefined reference to `ceil' collect2: ld returned 1 exit status make[1]: *** [/home/charlie/libSDLXenon/demos/plasma-1.0/plasma-1.0.elf] Error 1 make: *** [build] Error 2 charlie@ubuntu:~/libSDLXenon/demos/plasma-1.0$ [/code]

## 2012-10-01 03:01:10, posted by: ch.kenned

The only way I could build it using the makefile was by editing all of the audio related code from the header files included with libSDLXenon. This shouldn't have to be done. It has to be some issue with math.h. I've been trying to figure out what's wrong, but no luck so far. Does libSDLXenon depend on "/usr/local/xenon/xenon/include/math.h" for the ceil function? I wish one of the gurus would chime in, because this has been bugging me for a while! I can't figure out what to do aside from removing the audio functionality from libSDLXenon and then building it, and this is certainly not the right approach! I mean, it works....SDLSample built with no problem, but it's a bad hack to say the least!

## 2012-10-01 05:25:08, posted by: ch.kenned

Well, after some changes, this builds for me. Nice graphics, too!

### Attachments

[SDLSample.tar.gz](SDLSample.tar.gz)