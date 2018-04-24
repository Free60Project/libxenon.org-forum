# [Tutorial and Application] AutoXenon 0.3_b beta install / upgrade libxenon  

## 2012-04-29 19:57:55, posted by: chemone

Credits for all the people from Free60Project and libxenon.org for all their selfless contributions  
   
 Auto Xenon is an application programmed in Java designed for easy installation and updating of the free development environment for Xbox 360 libxenon, even despite being made in java, for now only supports Ubuntu / Debian, later try to add support with windows.  
   
 I take the upgrade to release the source application, so that what there you can compile, modify or get the latest version:  
   
 https://github.com/chemone/autoXenon  
   
 -Changes in version 0.3\_b:  
   
 -Fixed installation of SDL in recent versions of Ubuntu.  
   
 -Download:  
   
 http://www.mediafire.com/?au434s1xft1apsy  
   
 [u]Previous versions:[/u]  
   
 -Changes in version 0.3:  
   
 -New GUI  
   
 -Added the installation of the following libraries: freetype, zlib, bin2s, libpng, bzip2 and libSDLXenon  
   
 -Now you can select the toolchain to be installed between Free60Project and gligli repositories.  
   
 -Download:  
   
 http://www.mediafire.com/?gkru43s2a27417g  
   
 -Changes in version 0.2\_b:  
   
 -Fixed small bug in Ubuntu 11.04.  
   
 -Download:  
   
 http://www.mediafire.com/?2ptvsgjv97tzzxv  
   
   
 -How to use:  
   
 We must have java installed on our computer, I recommend installing jdk open.  
   
 To use the application you must first give execute permissions by clicking properties right click and click in the box allow you to run.  
   
 To run we right click and select run, if we double click will open with the manager gives filers.  
   
 Select the toolchain to be installed, the default is selected from free60Project, then press the install button.  
   
 The application will ask our password in a terminal to install the previous packages, then you ask your user name to give permissions to the folder opt.  
   
 If you are updating will ask permission to delete files from the previous repositories.  
   
 In order to compile our projects we need to edit the file. Bashrc, both the root user as our normal user, adding:  
   
 export DEVKITXENON = "/ usr / local / xenon"  
 export PATH = "$ PATH: $ DEVKITXENON / bin: $ DEVKITXENON / usr / bin"  
   
 Once done, install the libraries you must go to the tab and press the button, if we have not entered before a user, we would ask at this time, must be the same user you're logged.  
   
 Note that it is still a beta and may have bugs, it is also my first real contribution, so do not be too bad with me hehehehe. A greeting.  
   
 EDIT: Sorry for my english, i am from Spain and the tutorial is Google translated, my original tutorial is here:  
   
 http://www.elotrolado.net/hilo\_aplicacion-autoxenon-0-3-b-beta-instalar-actualizar-libxenon-automaticamente-en-linux-con-gnome\_1723024#p1727728421

## 2012-06-12 12:03:05, posted by: c01eman.360

have you got an english version?