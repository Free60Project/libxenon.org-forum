# How to setup zlib library and libpng in order to use SDL and LZX library

## 2011-06-26 22:34:43, posted by: dreamboy

First of all download libxenon:  
 [code]* *git clone git://github.com/Free60Project/libxenon.git [/code] After that follow this steps: [code]* *cd libxenon/toolchain sudo ./build-xenon-toolchain zlib sudo ./build-xenon-toolchain libpng sudo ./build-xenon-toolchain bin2s [/code] Each step has to end with "Done", otherway check build.log in current folder.  
   
 Thats all ;)   
   
 **[b]Download ZLX:[/b]** [url=http://libxenon.org/http://libxenon.org//viewtopic.php?t=4]Thread[/url]  
 **[b]Credits for zlx file with the libraries:[/b]** [glow=red,2,300][shadow=green,bottom]Ced2911[/shadow][/glow]

## 2011-07-16 14:13:31, posted by: cocker80

If building libpng under windows you could do the following instead of regenerating configure...  
   
 "cd libpng-1.5.4  
 export CFLAGS="-mcpu=cell -mtune=cell -m32 -fno-pic -mpowerpc64 $DEVKITXENON/usr/lib/libxenon.a -L$DEVKITXENON/xenon/lib/32/ -T$DEVKITXENON/app.lds -u read -u \_start -u exc\_base"  
 export CC=xenon-gcc  
 ./configure --prefix=$DEVKITXENON/xenon --target=xenon --host=i686-pc-mingw32  
 make   
 make install"

## 2011-08-15 23:10:57, posted by: dreamboy

Lzx libray updated and added lzx samples ;)

## 2011-08-24 03:11:49, posted by: chemone

Hello, i have a problem with lzx, when i want to compile an example it takes me error "cApp was not declared in this scope" thanks for the help.  
   
 EDIT: Fixed!!

## 2011-09-01 05:37:28, posted by: Doerek

Hi Dreamboy,  
 In the First Code Sektion (About zlib) You posted at the Last Line this:  
 [attach=1] <----Screenshot  
 The brackets at the end of Line, are messing everthing up.   
 **[b]BUT it comes somehow from the Board Simple Machines itself![/b]** ...when i quote youre Post they [u]DO NOT APEAR[/u] in the Text Box.  
   
 I noticed it just after running these commands. So now my Folder Structur is a little bit Messy.  
 ...take a look, But i Think i can fix it...   
 [attach=2]  
   
 Could you Please inform some of the other Mods :)   
 Imagine some kind of bug'ed BB-Code messes up all your Info or Tutorial Threads.  
   
 Thx in advice....   
   
 Greetz  
 Doerek

### Attachments

[Code.PNG](Code.PNG)[typo_at_code..PNG](typo_at_code..PNG)

## 2011-09-01 05:41:12, posted by: tuxuser

Yes it was a typo

## 2011-09-01 06:31:02, posted by: Doerek

@ TuxUser  
 It is Enough to move and restore the Old Folder Structur?

## 2011-09-02 11:34:10, posted by: Shadow LAG

[quote="dreamboy"]  
 First of all download the package from the link at the bottom...  
 [/quote]  
 I assume you are speaking about the zlib download, you forgot to add that in, [url=http://zlib.net/zlib-1.2.5.tar.gz]here is the link for zlib[/url]

## 2011-09-05 21:28:39, posted by: supatx

I'm having some troubles with libpng. First off, there is no makefile after I run autogen.sh. So I tried to run [code]./configure --prefix=/usr/local/xenon/usr --with-zlib-prefix=/usr/local/xenon/usr/[/code] but it can't find the zlib library (which is there in /usr/local/xenon/usr/lib). Any suggestions?  
 Oh, and I am running ubuntu 11.04

## 2011-09-05 21:37:30, posted by: Cancerous1

[quote="Shadow LAG"]  
 [quote="dreamboy"]  
 First of all download the package from the link at the bottom...  
 [/quote]  
 I assume you are speaking about the zlib download, you forgot to add that in, [url=http://zlib.net/zlib-1.2.5.tar.gz]here is the link for zlib[/url]  
 [/quote]  
   
 for clarity, he means the link at the bottom of the post that says "Download LZX: Thread"  
 even tho you already know this, just adding for future readers of this thread.

## 2011-09-09 13:25:41, posted by: SynTeX

[quote="supatx"]  
 I'm having some troubles with libpng. First off, there is no makefile after I run autogen.sh. So I tried to run [code]./configure --prefix=/usr/local/xenon/usr --with-zlib-prefix=/usr/local/xenon/usr/[/code] but it can't find the zlib library (which is there in /usr/local/xenon/usr/lib). Any suggestions?  
 Oh, and I am running ubuntu 11.04  
 [/quote]  
   
 Same problem here...   
 please help  
   
 //EDIT:  
 Fixed by using this CFLAGS:  
 export CFLAGS="-mcpu=cell -mtune=cell -m32 -fno-pic -mpowerpc64 /usr/local/xenon/usr/lib/libxenon.a -L/usr/local/xenon/xenon/lib/32/ -T/usr/local/xenon/app.lds -u read -u \_start -u exc\_base -L/usr/local/xenon/usr/lib/"  
   
 which include the path to my zlib.a ...   
   
   
 then run configure with   
 "./configure --prefix=$DEVKITXENON/xenon --target=xenon --host=i686-pc-mingw32"  
   
 make with "make CROSS\_COMPILE=-xenon- " throw this error:  
 "pngstruct.h:27:18: fatal error: zlib.h: No such file or directory"  
   
 you can fix it by changing line 27 to full path   
 f.e.: #include "/usr/local/xenon/usr/include/zlib.h"  
   
   
 Now it works :)

## 2011-09-13 07:05:59, posted by: switchback

Wow thanks so much for the tut this is a bit mot tecky then the jtag witch i never have done but i have so many boards laying around i really wonna do this one but allthough the tut really explains everything what seems to have me asking questions is the tools needed.I have done simple thing as for flashing drives and so on .I wonna tackle this but am wondering about the tools and dumping nand as i never done this.Can i make these tools is there a kit i can buy if you have the extra time to help me out as a noob i be the first noob to do this haha.any info would help.The tut really explains most everything just what all tools is needed and how to make inquire these would be awsome.Agin thanks so much that had to be allot work but is so very cool...

## 2011-09-13 20:41:30, posted by: supatx

[quote="SynTeX"]  
 [quote="supatx"]  
 I'm having some troubles with libpng. First off, there is no makefile after I run autogen.sh. So I tried to run [code]./configure --prefix=/usr/local/xenon/usr --with-zlib-prefix=/usr/local/xenon/usr/[/code] but it can't find the zlib library (which is there in /usr/local/xenon/usr/lib). Any suggestions?  
 Oh, and I am running ubuntu 11.04  
 [/quote]  
   
 Same problem here...   
 please help  
   
 //EDIT:  
 Fixed by using this CFLAGS:  
 export CFLAGS="-mcpu=cell -mtune=cell -m32 -fno-pic -mpowerpc64 /usr/local/xenon/usr/lib/libxenon.a -L/usr/local/xenon/xenon/lib/32/ -T/usr/local/xenon/app.lds -u read -u \_start -u exc\_base -L/usr/local/xenon/usr/lib/"  
   
 which include the path to my zlib.a ...   
   
   
 then run configure with   
 "./configure --prefix=$DEVKITXENON/xenon --target=xenon --host=i686-pc-mingw32"  
   
 make with "make CROSS\_COMPILE=-xenon- " throw this error:  
 "pngstruct.h:27:18: fatal error: zlib.h: No such file or directory"  
   
 you can fix it by changing line 27 to full path   
 f.e.: #include "/usr/local/xenon/usr/include/zlib.h"  
   
   
 Now it works :)  
 [/quote]  
   
 Perfect. Thanks :)

## 2011-09-20 16:41:37, posted by: Pa0l0ne

Hello, i'm a noob on this kind of stuff but i love to experiment and i have problem to compile mupen64-360.  
   
 ![](http://img683.imageshack.us/img683/5785/onemph.jpg)[img]http://img683.imageshack.us/img683/5785/onemph.jpg[/img]  
   
 I think it's all related about libpng install.  
   
 I have Ubuntu 10.04 and according on the Posts above this is what i have done:  
   
 i have installed succesfuly "libtool\_2.2.6b-2ubuntu3\_i386.deb" wich seems to be "libtoolize 32bits"  
 I don't think in my enviroment i have to install also libtoolize 64bits....isn't it?  
   
 Than I have done:  
 sudo su  
 apt-get install automake  
 apt-get install autoconf  
 chmod a+x ./autogen.sh (in my libpng-1.5.2)  
 ./autogen.sh  
   
   
 NOW IT'S IMPOSSIBLE FOR MY SKILL TO DO THE:  
 make CROSS\_COMPILE=-xenon-  
 make CROSS\_COMPILE=-xenon- install  
   
 because a "make" file doesnt exist!  
   
 So I have read about SynTeX solution and i have launched this:  
   
 export CFLAGS="-mcpu=cell -mtune=cell -m32 -fno-pic -mpowerpc64 /usr/local/xenon/usr/lib/libxenon.a -L/usr/local/xenon/xenon/lib/32/ -T/usr/local/xenon/app.lds -u read -u \_start -u exc\_base -L/usr/local/xenon/usr/lib/"  
   
 but he spoke about ./configure --prefix=$DEVKITXENON/xenon --target=xenon --host=i686-pc-mingw32  
 wich seems to be a "Windows Toolchain"....isn't it?  
   
 SO I DON'T HAVE IDEA HOW TO GO ON...  
   
 So is there anyone who help a very poor noob?  
   
 Thanks in advance!

## 2012-01-09 07:29:35, posted by: sk1080

Well, seeing as I still encounter people that have issues installing libpng and zlib, I will post these scripts that do it automatically:  
   
 http://madhack.tk/xenon/zlib.sh  
 http://madhack.tk/xenon/libpng.sh  
   
 EDIT: please re-download libpng.sh, it was fail  
 also, http://madhack.tk/xenon/freetype.sh, for freetype

## 2012-02-20 03:22:08, posted by: Xplorer4x4

I have tried to compile using the tut in the op, and the bash scripts above but with no luck. I tried to compile the bzip2 src and pcsxr and I get this error: http://pastebin.com/QLn2cp0h  
   
 I am using Debian 6.0.4 x64 with the ssh server and base system installed using the latest version of VMWare and the latest version of libpng and and zlib.

## 2012-03-06 03:55:32, posted by: Xplorer4x4

http://www.mediafire.com/?zbrx49sfgw7sdt5  
 I updated the scripts to reflect newer version numbers. I would host these on my server for simple wget method, but my server no longer has unmetered bandwidth.

## 2012-07-09 22:43:31, posted by: ravendrow

please update build-xenon-toolchain to reflect new zlib version 1.2.7  
   
 went WTF there for a second then i just fixed it lol

## 2012-07-10 09:05:59, posted by: sk1080

Yea I suppose that it needs to be bumped, wonder if I have push on the git....

## 2012-07-13 16:45:23, posted by: siz

Hey,  
   
 I have installed all the libs needed to make & install the zlx lib, however when I try to compile the latest ZLX Lib I get a "struct controller\_data\_s" error:  
 [code]siz@ubuntu:~/Downloads/LibXenonProject-ZLX-Library-49f93d0$ make -f Makefile\_lib [Browser.cpp] /home/siz/Downloads/LibXenonProject-ZLX-Library-49f93d0/zlx/Browser.cpp: In member function 'void ZLX::Browser::Update()': /home/siz/Downloads/LibXenonProject-ZLX-Library-49f93d0/zlx/Browser.cpp:574:22: error: 'struct controller\_data\_s' has no member named 'select' /home/siz/Downloads/LibXenonProject-ZLX-Library-49f93d0/zlx/Browser.cpp:574:42: error: 'struct controller\_data\_s' has no member named 'select' /home/siz/Downloads/LibXenonProject-ZLX-Library-49f93d0/zlx/Browser.cpp:640:13: warning: comparison between signed and unsigned integer expressions [-Wsign-compare] /home/siz/Downloads/LibXenonProject-ZLX-Library-49f93d0/zlx/Browser.cpp: At global scope: /home/siz/Downloads/LibXenonProject-ZLX-Library-49f93d0/zlx/Browser.cpp:114:18: warning: 'ZLX::FileInfoPanelPosition' defined but not used [-Wunused-variable] make[1]: *** [Browser.o] Error 1 make: *** [build] Error 2[/code] Have I missed something? Thanks in advance :)

## 2012-07-13 17:39:44, posted by: tuxuser

Change select to back

## 2012-07-13 20:57:28, posted by: siz

Thanks, it seemed to do the trick :)

## 2012-07-17 07:33:42, posted by: jesicakotez

Can you please post screenshots of set up process of libxenon?