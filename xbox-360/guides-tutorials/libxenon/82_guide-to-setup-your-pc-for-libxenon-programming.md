# Guide to Setup your PC for LibXenon Programming

## 2011-06-14 23:07:47, posted by: tuxuser

A little guide to setup your linux machine for programming with Linux and NetBeans  
   
 [attachment=1]  
   
 Please report mistakes you find.

### Attachments

[Setup your PC for LibXenon Programming_v1.1a.pdf](Setup your PC for LibXenon Programming_v1.1a.pdf)

## 2011-06-15 13:37:54, posted by: Doerek

thanks a lot!

## 2011-06-30 13:08:38, posted by: Meluxe

Building fur mupen64 now :P  
   
 Very helpful and noob-safe !  
   
 Thanks a LOT!!

## 2011-07-02 03:04:35, posted by: Hack Hunter

very helpful  
 thanks man ^^ ;)

## 2011-07-24 00:37:22, posted by: zouloum

I am stuck at this place [code]Once it’s finished with compiling & installing it tells you to add two lines to ~/.bashrc They will usually look like this: export DEVKITXENON="/usr/local/xenon" export PATH="$PATH:$DEVKITXENON/bin:$DEVKITXENON/usr/bin"[/code] and each time i try to run xenon-gcc it says command not found what am i doing wrong?

## 2011-07-24 00:45:07, posted by: tuxuser

did you re-open your terminal after doing the changes? Apply the same 2 lines to ~/.profile, logout and login again. Should fix it!

## 2011-07-30 21:07:28, posted by: Colorado880

[quote="tuxuser"]  
 did you re-open your terminal after doing the changes? Apply the same 2 lines to ~/.profile, logout and login again. Should fix it!  
 [/quote]I am stuck on the same part but how do you add the 2 lines to the bash? I just installed linux the other day and I am very new to this.  
   
 Thanks

## 2011-07-30 21:13:14, posted by: tuxuser

[code]* *nano /home/username/.bashrc nano /home/username/.profile [/code] or  
 [code]* *gedit /home/username/.bashrc gedit /home/username/.profile [/code]

## 2011-07-31 23:51:18, posted by: thegardner

Thank you. When i can get a pc for development purposes this will be very useful.  
   
 Regards

## 2011-08-31 21:13:00, posted by: chronospike

Hey guys, just stumbled across your site and am interested in starting to play with libxenon. I was walking through the tutorial and hit a speedbump while trying to compilr the toolchain. It gets as far as downloading binutils, connects to ftp.gnu.org then it says http request sent...404 not found. Any ideas?

## 2011-08-31 23:53:32, posted by: Aldanga

That package has been replaced with 2.21.1a. [url=https://aur.archlinux.org/packages.php?ID=30131]Info[/url]. You'll have to manually edit the script. Just change the BINUTILS variable to binutils-2.21.1a in the script and it should work.  
   
 EDIT: I might have spoken too soon. It's not building the toolchain. Looking into it...

## 2011-08-31 23:56:03, posted by: Doerek

[quote="dreamboy"]  
 hi to fix that issue just download my binutils version and copy paste it into the toolchain folder, that way when you retry to compile the toolchain the script will recognize the file its there and it will compile fine without problem ;) dont forget to install also libmpc-dev ;D  
   
 [url=http://www.megaupload.com/?d=2E9F34UC]http://www.megaupload.com/?d=2E9F34UC[/url]  
 [/quote]  
 Big thanks to dreamboy...

## 2011-09-01 01:26:48, posted by: chronospike

Cool thanks for the quick response

## 2011-09-06 11:07:47, posted by: Diggs

Fantastic guide Tux!  
   
 Just thought I'd post my experiences with Ubunutu 11.04...  
   
 **[b]1.[/b]** My gcc build was failing with the following error:  
   
 "Checking for correct version of mpc.h... no"  
   
 I Found this by checking the /opt/free60-git/free60/toolchain/build.log - My terminal wasn't displaying any useful output.  
   
 I fixed it by doing a:  
   
 sudo apt-get install libmpc-dev  
   
 And then re-running the toolchain build script.  
   
 **[b]2.[/b]** Secondly when it came to installing netbeans I found the easiest way to do this was:  
   
 sudo add-apt-repository ppa:ferramroberto/java  
 sudo apt-get update  
 sudo apt-get install sun-java6-jre sun-java6-bin sun-java6-jdk  
   
 And then downloading the "netbeans-7.0.1-ml-cpp-linux.sh" installer from netbeans (This is just the C/C++ IDE without Java).  
   
 Everything else worked perfectly :)  
   
 Now to get a serial cable hooked up and figure out how to run executables over the network...

## 2012-02-01 11:33:07, posted by: Xplorer4x4

[quote="tuxuser"]  
 did you re-open your terminal after doing the changes? Apply the same 2 lines to ~/.profile, logout and login again. Should fix it!  
 [/quote]  
 I added the proper lines to all 4 files, and exited the shell, and even restarted the server and still get the error. Any clue what I could be doing wrong? I am following the directions from your pdf file.

## 2012-02-01 18:03:09, posted by: tuxuser

Create (as superuser) a file in /etc/profile.d/ named devkitxenon (or whatever you like to call it) so it's:  
   
 /etc/profile.d/devkitxenon  
   
 put the two exports line in there, save, logout & login the current user and try again

## 2012-02-14 01:39:03, posted by: Xplorer4x4

[quote="tuxuser"]  
 login the current user  
 [/quote]  
 I usually log in as root since most of the process needs su anyways, so do you mean log back in as root or log in as "devkitxenon?"  
   
 [quote="tuxuser"]  
 Create (as superuser) a file in /etc/profile.d/ named devkitxenon (or whatever you like to call it) so it's:  
   
 /etc/profile.d/devkitxenon  
   
 put the two exports line in there, save, logout & login the current user and try again  
 [/quote]  
 I did that, I logged out, even rebooted just to be sure, and I still get -bash: xenon-gcc: command not found  
   
 I would really like to kit my dev machine up and running. Can some one please help me here?  
   
 I been working on getting a dev VM set up for baout 2 months, amidst computer problems though. It would be great to actually get some help so I can get down to business!  
   
   
 edit by tuxuser: merged double-posting!

## 2012-02-17 05:55:09, posted by: tuxuser

Try to name it  
   
 /etc/profile.d/devkitxenon.sh  
   
 (Maybe the file-ending makes a difference)  
   
 If not: Reinstall the toolchain - It has to report: Install successfully or similar  
 If it doesnt report success - check build.log for errors!

## 2012-02-17 09:48:19, posted by: Xplorer4x4

[quote="tuxuser"]  
 If it doesnt report success - check build.log for errors!  
 [/quote]  
 This! That was exactly the tip I needed! Sure enough:  
 configure: error: Building GCC requires GMP 4.2+, MPFR 2.3.2+ and MPC 0.8.0+.  
 I think it would be very useful to mention the build.log part in the guide. Also include this info from the wiki: [code]* *cd gcc-4.6.1 wget ftp://ftp.gmplib.org/pub/gmp-5.0.2/gmp-5.0.2.tar.bz2 tar xvjf gmp-5.0.2.tar.bz2 && mv gmp-5.0.2 gmp wget http://www.multiprecision.org/mpc/download/mpc-0.9.tar.gz tar xvzf mpc-0.9.tar.gz && mv mpc-0.9 mpc wget http://www.mpfr.org/mpfr-current/mpfr-3.0.1.tar.gz tar xvzf mpfr-3.0.1.tar.gz && mv mpfr-3.0.1 mpfr cd .. ./build-xenon-toolchain toolchain [/code] However the url for mpfr-3.0.1 is dead. The current version is mpfr-3.1.0.tar.gz.

## 2012-03-19 08:33:29, posted by: Xplorer4x4

I was trying to set up a fresh dev vm, but every time I try to compile I get an error that I can't find any info on. Configuring GCC 2nd Pass completes fine, then it tried to build libxenon and fails. I am using Debian 6 in an i686 environment. I have the dependcies listed from apt-get plus the latest versions of gmp, mpfr and mpc. I tried with older versions of gmp, mpfr and mpc but had no luck there either. I am building from the latest versions from the non-testing git repo. Here is the last few lines of my build.log: [code]../../drivers/xenon\_nand/xenon\_sfcx.c: In function 'try\_rawflash': ../../drivers/xenon\_nand/xenon\_sfcx.c:455:9: warning: implicit declaration of function 'delay' [-Wimplicit-function-declaration] [xenon\_config.c] [ucode.c] [edram.c] ../../drivers/xenos/edram.c: In function 'edram\_p2': ../../drivers/xenos/edram.c:224:12: warning: unused variable 'k' [-Wunused-variable] ../../drivers/xenos/edram.c:224:9: warning: unused variable 'j' [-Wunused-variable] [xe.c] [xenos.c] ../../drivers/xenos/xenos.c: In function 'xenos\_autoset\_mode': ../../drivers/xenos/xenos.c:1130:3: error: too few arguments to function 'xenos\_detect\_hdmi\_monitor' ../../drivers/xenos/xenos\_edid.h:210:6: note: declared here make: *** [../../drivers/xenos/xenos.o] Error 1 make: Leaving directory `/opt/free60-git/libxenon/libxenon/ports/xenon' [/code]

## 2012-03-19 09:35:11, posted by: tuxuser

[quote]../../drivers/xenos/xenos.c:1130:3: error: too few arguments to function 'xenos\_detect\_hdmi\_monitor'[/quote] Sorry, was my fault. Forgot to pass the edid function as argument - should be good now (in github.com/tuxuser)

## 2012-03-19 09:53:06, posted by: Xplorer4x4

Thanks for the quick fix, tux. Is there nay difference between your libxenon on free60/libxenon?

## 2012-08-23 19:48:10, posted by: tuxuser

Updated (and hopefully simplified) the Tutorial. See Post #1 in this thread. Enjoy - and as usual: report mistakes if you find any, thx!  
   
 UPDATE: Sorry, little flaw happened, v1.1a is up!

## 2012-10-03 21:12:25, posted by: OOKAMI

finally gone from windows to ubuntu and everything working now fine :)  
   
 thanks for your tutorial :)  
   
 can i suggest to add something about GIT ?  
   
 at the line  
 To get the required files for this step you have to make sure that you got a GIT-Client  
   
 can you add this command ?  
 sudo apt-get install git  
   
 like this, ubuntu (and maybe all other distros) will have internal git client with terminal :)  
   
 have a nice day :)  
   
 .

## 2012-10-03 21:17:34, posted by: Xplorer4x4

[quote="OOKAMI"]  
 can you add this command ?  
 sudo apt-get install git  
   
 like this, ubuntu (and maybe all other distros) will have internal git client with terminal :)  
 [/quote]  
 No this does not apply to all other distros, only those, like Ubuntu, that are derived from Debian. I would assume apt-get applies to all Debian derived linux distros but I could be wrong. For example on CentOS, it would be something like yum install git.

## 2013-01-14 13:13:55, posted by: chunkz

so im trying this out i got at as far "Go into the toolchain directory now and start the actual xenon-toolchain compile and install. The part that is suposed to take 2 hours. well when i type the command it says cd command not found any help would be great. Im a total newb to this and am learning as i go thanks again.

## 2013-08-29 03:08:35, posted by: XeXGolden

Thx dude I wanted to get into more of this :o

## 2015-02-04 09:43:30, posted by: <Unknown User>

Thank you very much

## 2015-02-20 10:33:20, posted by: <Unknown User>

PDF is deactivated. What should I do...?

## 2015-05-13 21:07:08, posted by: <Unknown User>

[quote="Jan4V"]PDF is deactivated. What should I do...?[/quote] You can check the tutorial here  
   
 [url]http://www.xboxhacks.de/index.php?page=Attachment&attachmentID=8829&h=ebb61fbf69fe5956d2399425dc5b13f37fff8ed4[/url]