# GUIDE: Libxenon development on OSX

## 2011-09-17 03:51:17, posted by: Diggs

This is a work in progress as I haven't successfully done this yet but will update as I go.  
   
 This was tested on OSX Lion 10.7 running on a late 2010 Macbook Pro 13".  
   
 **[b]1.[/b]** make sure OS X is fully up to date and that you have XCode 4.1 or greater installed.  
   
 **[b]2.[/b]** Download and install the latest version of Macports from: http://www.macports.org/install.php - At the time of writing this the latest version is 2.0.3.  
   
 **[b]3.[/b]** From terminal: sudo port install mpfr gmp git-core wget libmpc gsed  
   
 **[b]4.[/b]** From terminal: sudo mv /usr/bin/sed /usr/bin/darwinsed  
   
 **[b]5.[/b]** From terminal: sudo ln -s /opt/local/bin/gsed /usr/bin/sed  
   
 **[b]6.[/b]** From terminal: sudo mkdir /usr/local/xenon; sudo chown -R USERNAME:staff /usr/local/xenon  
   
 **[b]7.[/b]** Follow tuxuser's awesome guide from http://libxenon.org/http://libxenon.org//viewtopic.php?t=2 -The only **[b]CRITICAL[/b]** change is that instead of executing "sudo ./build-xenon-toolchain toolchain" you must use "sudo CC=/usr/bin/gcc-4.2 CPP=/usr/bin/cpp-4.2 CXX=/usr/bin/g++-4.2 LD=/usr/bin/gcc-4.2 ./build-xenon-toolchain toolchain".  
   
 And more to come as I encounter it. I'm currently running step 7. :)

## 2011-09-18 21:28:07, posted by: supatx

Great idea. Two things: [list] - [*]This may come in handy: http://www.free60.org/Compiling\_the\_Toolchain#Mac\_OS\_X
 - [*]All of these packages are also available with homebrew.
[/list] Edit: I remember why I had such a hard time getting stuff installed. The dependencies for SDL (zlib/libpng) would not link correctly. I fixed this by installing the GNU version of libtool.. This probably has some sort of wide reaching effects.... BUT I haven't run in to any yet :)

## 2011-12-15 20:07:35, posted by: GhaleonX

I cannot get the toolchain working properly in osx. A few people from the irc chan (tuxuser, ced2911, juvenal) helped me to get the toolchain working at one point, but it seemed to be buggy and I have not gotten it to rebuild since.  
   
 I was using xcode 3.2, but I've just upgrade to 4.2, and macports is installed with everythying mentioned above.   
   
 Process fails during gcc 2nd pass.  
 [code]* *error: two or more data types in declaration specifiers [/code]   
 I also noticed some warnings in the log, here's one example (tho it has several occurrences with different files) [code]* * configure: WARNING: sys/sem.h: present but cannot be compiled configure: WARNING: sys/sem.h: check for missing prerequisite headers? configure: WARNING: sys/sem.h: see the Autoconf documentation configure: WARNING: sys/sem.h: section "Present But Cannot Be Compiled" configure: WARNING: sys/sem.h: proceeding with the compiler's result [/code] Can either of you lend some insight as to where I may have messed up?