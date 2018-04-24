# Compiling your own Linux Kernel

## 2011-03-16 08:09:56, posted by: tuxuser

Here's a short tutorial how you compile your own Linux-Kernel.  
   
 Prerequisites:  
   
 Installed Linux OS (Native or Virtual Machine)  
 Installed [url=http://free60.org/Compiling\_the\_Toolchain]Xenon-Toolchain[/url] - you wont need it if you are compiling on a PPC Machine  
   
 1. At first download the Kernel Source in a new folder and extract it: [code]* *mkdir xenon-linux-kernel cd xenon-linux-kernel/ wget http://www.kernel.org/pub/linux/kernel/v2.6/linux-2.6.36.4.tar.bz2 tar xvjf linux-2.6.36.4.tar.bz2 [/code] 2. Now download the xenon-patchset && kernel config file [code]* *wget http://file.libxenon.org/free60/linux/kernel/patch-2.6.36.4-xenon0.11.diff wget http://file.libxenon.org/free60/linux/kernel/.config [/code] 3. Apply the patchset and copy over the config-file [code]* *cd linux-2.6.36.4 patch -p1 < ../patch-2.6.36.4-xenon0.11.diff cp ../.config . [/code] 4. Edit the config to your needs [code]* *nano .config ->Editor Window opens in Terminal -> Press CTRL + W for "Search" -> Type "CONFIG\_CMDLINE" [/code] The most important part you probably want to edit is the root= parameter.**[b] Edit it to the device where your linux system is installed[/b]**. Now: [code]* *-> Press CTRL + O -> Confirm the filename with pressing ENTER -> Press CTRL + X to close nano [/code] 5. Start the compiling process  
   
 (If you are on a native PPC machine (like PS3 etc) you dont need the "CROSS\_COMPILE=xenon-" parameter !)  
 To make sure you are working with a proper config, type the following: [code]* *make CROSS\_COMPILE=xenon- ARCH=powerpc oldconfig [/code] It should only say that it saved the .config  
   
   
 Now the actual compiling begins. Type:  
 [code]* *make CROSS\_COMPILE=xenon- ARCH=powerpc all [/code] If you are using a Hyperthreading captable processor you could also append the -j parameter. It should be Number of CPU-Cores + 1, so for a quad-core (5) you would do:  
 [code]* *make -j 5 CROSS\_COMPILE=xenon- ARCH=powerpc all [/code] Once the compiling is finished you will find the ready-to-use kernel in "arch/powerpc/boot" with the name "zImage.xenon"!  
   
 Have fun :) :) :) 

## 2011-03-16 08:19:46, posted by: Razkar

Nice tuto Tux, this will be very helpful  
 Thx ;)

## 2011-03-16 13:29:11, posted by: charlo.charli

Thanks very helpfull!

## 2011-03-16 16:09:17, posted by: val532

Thanks

## 2011-03-17 01:45:04, posted by: val532

Linux kernel 2.6.38 is out can we use it ?

## 2011-03-18 03:47:36, posted by: Cancerous1

thanks for the help tux! finally my kernel builds work as expected :D

## 2011-03-18 14:26:38, posted by: Juggahaxor

[quote="val532"]Linux kernel 2.6.38 is out can we use it ?[/quote]  
   
 You can find patches and config files for 2.6.38-rc3 in the link below.   
 Here ----> [url=http://vserver.13thfloor.at/Stuff/XBOX360/]http://vserver.13thfloor.at/Stuff/XBOX360/[/url]

## 2011-03-18 15:31:15, posted by: tuxuser

[quote=""Juggahaxor""][quote=""val532""]Linux kernel 2.6.38 is out can we use it ?[/quote]  
   
 You can find patches and config files for 2.6.38-rc3 in the link below. [/quote]  
   
 But they got a delta-patch for the atomic ops in it.. so the kernel is spitting a lot of exceptions and its running more unstable than the one we are currently using..  
 Guys, I am using 2.6.36.4 for a reason :P

## 2011-03-18 16:28:32, posted by: val532

Made this patch work for 2.6.38 ^^.

## 2011-04-21 14:20:09, posted by: Doerek

Link: [url=http://libxenon.org/http://libxenon.org//viewtopic.php?p=221#p221]http://libxenon.org/http://libxenon.org//viewtopic.php?p=221#p221[/url]  
   
 [quote="tuxuser"]@Sonic-NKT  
   
 Yep, of course its possible! It's called "persistence".. however it needs modification to the Kernel CMDLINE..and as we are unable to just pass the whole CMDLINE to a "naked" kernel YET.. a new Kernel Compile has to be made to accomplish such.  
   
 Here is a little info about the persistence:  
   
 <!-- m -->[url=https://help.ubuntu.com/community/LiveCD/Persistence]https://help.ubuntu.com/community/LiveCD/Persistence[/url]<!-- m -->  
   
 Go for the initramfs attached here and compile it into the kernel.  
 To do so you extract the archive and set the following correctly in the kernel's .config   
 (CMDLINE needs to be adjusted probably)  
 [code]* *CONFIG\_CMDLINE="boot=casper video=xenonfb console=tty0 ip=dhcp panic=60 nosmp maxcpus=1 persistence" CONFIG\_INITRAMFS\_SOURCE="/path/to/casper-initramfs" CONFIG\_INITRAMFS\_COMPRESSION\_LZMA=y [/code] The Kernel's Config which is used in the "Kernel Compile Tutorial" is also updated, the changes mentioned above need to be done still.  
   
 Greetz  
 tux[/quote]  
   
 Hi tux,  
 müssen die änderungen immernoch durchgeführt werden?  
 Bin grad bei der VMware installation und wollte mich mit deinem Kernel Tut mal daran versuchen...  
 Ich weiß nur noch nicht welche distro ich benutzen soll, hab etwas platzmangel auf meinen HDDs.  
 (Kannst du mir in dem Fall eine Distro empfehlen?)  
   
 greetz  
 DCDoerek

## 2011-04-23 15:53:22, posted by: tuxuser

@Doerek  
   
 Yes the changes still need to be made if you want a persistance partition .. so you data does not get lost after you turn off your live-system.  
   
 For a small linux system in a virtual maschine: If you are not afraid of using the terminal (textconsole) all the time, just install Ubuntu without a XServer (without a GUI). Then you can still do everything.. but its fast and does not need much space.  
   
 Greetz  
 tux

## 2011-04-24 12:40:44, posted by: Doerek

Hi,  
   
 Also die installation per VMware ist fehlgeschlagen...VMware tools for inux habe ich nicht vernünftig zum laufen gebracht.   
   
 Neuer Versuch...diesmal mit "Wubi" + Ubuntu 10.10 (64bit) auf eine Externe HDD.   
 Ich melde mich später nochmal.

## 2011-04-24 14:40:03, posted by: Doerek

Hi,  
   
 Habe gerade ubuntu installiert und alle updates gezogen...soweit so gut:  
   
 Allerdings...  
 wenn ich versuche den Kernel zu kompilieren bekomme ich folgende fehlermeldung:  
 [code]doerek@ubuntu:~/xenon-linux-kernel/linux-2.6.36.4$ make -j 3 CROSS\_COMPILE=xenon- ARCH=powerpc all make: xenon-gcc: Kommando nicht gefunden scripts/kconfig/conf --silentoldconfig arch/powerpc/Kconfig /home/doerek/xenon-linux-kernel/linux-2.6.36.4/scripts/gcc-version.sh: Zeile 25: xenon-gcc: Kommando nicht gefunden. /home/doerek/xenon-linux-kernel/linux-2.6.36.4/scripts/gcc-version.sh: Zeile 26: xenon-gcc: Kommando nicht gefunden. make: xenon-gcc: Kommando nicht gefunden /home/doerek/xenon-linux-kernel/linux-2.6.36.4/scripts/gcc-version.sh: Zeile 25: xenon-gcc: Kommando nicht gefunden. /home/doerek/xenon-linux-kernel/linux-2.6.36.4/scripts/gcc-version.sh: Zeile 26: xenon-gcc: Kommando nicht gefunden. /home/doerek/xenon-linux-kernel/linux-2.6.36.4/scripts/gcc-version.sh: Zeile 25: xenon-gcc: Kommando nicht gefunden. /home/doerek/xenon-linux-kernel/linux-2.6.36.4/scripts/gcc-version.sh: Zeile 26: xenon-gcc: Kommando nicht gefunden. /home/doerek/xenon-linux-kernel/linux-2.6.36.4/scripts/gcc-version.sh: Zeile 28: xenon-gcc: Kommando nicht gefunden. *** 2.6 kernels no longer build correctly with old versions of binutils. *** Please upgrade your binutils to 2.12.1 or newer make: *** [checkbin] Fehler 1 make: *** Warte auf noch nicht beendete Prozesse... make: *** wait: Keine Kind-Prozesse. Schluss. [/code] Ich hab im softwarecenter zwar mal nach "binutils" gesucht aber wirklich fündig (im sinne eines updates) bin ich nicht geworden.

## 2011-04-24 20:54:19, posted by: Doerek

mir ist grade aufgefallen dass ich vergessen habe die Xenon toolchain zu bauen...lesen bildet ;)  
 Danach versuch ichs nochmal

## 2011-04-24 22:06:00, posted by: Doerek

also die Toolchain habe ich nach angaben auf free60.org erstellt.  
   
 Danach habe ich das verzeichnis vom Xbox Kernel gelöscht und nochmal neu angefangen.  
   
 Beim kompilieren bekomme ich trotzdem eine fehlermeldung: [code]doerek@ubuntu:~/xenon-linux-kernel/linux-2.6.36.4$ make CROSS\_COMPILE=xenon- ARCH=powerpc all /home/doerek/xenon-linux-kernel/linux-2.6.36.4/scripts/gcc-version.sh: Zeile 25: xenon-gcc: Kommando nicht gefunden. /home/doerek/xenon-linux-kernel/linux-2.6.36.4/scripts/gcc-version.sh: Zeile 26: xenon-gcc: Kommando nicht gefunden. make: xenon-gcc: Kommando nicht gefunden /home/doerek/xenon-linux-kernel/linux-2.6.36.4/scripts/gcc-version.sh: Zeile 25: xenon-gcc: Kommando nicht gefunden. /home/doerek/xenon-linux-kernel/linux-2.6.36.4/scripts/gcc-version.sh: Zeile 26: xenon-gcc: Kommando nicht gefunden. /home/doerek/xenon-linux-kernel/linux-2.6.36.4/scripts/gcc-version.sh: Zeile 25: xenon-gcc: Kommando nicht gefunden. /home/doerek/xenon-linux-kernel/linux-2.6.36.4/scripts/gcc-version.sh: Zeile 26: xenon-gcc: Kommando nicht gefunden. /home/doerek/xenon-linux-kernel/linux-2.6.36.4/scripts/gcc-version.sh: Zeile 28: xenon-gcc: Kommando nicht gefunden. *** 2.6 kernels no longer build correctly with old versions of binutils. *** Please upgrade your binutils to 2.12.1 or newer make: *** [checkbin] Fehler 1 [/code] P.s. [code]doerek@ubuntu:~/xenon-linux-kernel/linux-2.6.36.4$ ld -v GNU ld (GNU Binutils for Ubuntu) 2.20.51-system.20100908 [/code]

## 2011-04-25 01:15:22, posted by: tuxuser

hi,  
   
 Take care about the last step which get mentioned on the free60 Wiki Toolchain page:  
   
 Add following lines to ~/.bashrc  
 [code]* *export DEVKITXENON="/usr/local/xenon" export PATH="$PATH:$DEVKITXENON/bin:$DEVKITXENON/usr/bin" [/code] greetz  
 tux

## 2011-04-25 01:29:12, posted by: Doerek

die änderungen sind bereits drin...

## 2011-04-25 01:32:53, posted by: Doerek

ahh!...ich hatte die genannten zeilen einfach eingefügt...jetzt habe ich eine leer zeile mit eingefügt und anscheinend läuft das kompilieren gerade...cool!

## 2011-04-25 02:04:25, posted by: Doerek

Also nach dem kompilieren habe ich die datei "zImage.xenon" in folgendem verzeichnis: [code]/home/doerek/xenon-linux-kernel/linux-2.6.36.4/arch/powerpc/boot/[/code] was genau mache ich mit der Datei nun? Die größe der Datei beträgt "nur" 11,6MB

## 2011-04-25 02:40:15, posted by: Doerek

Ich hab die datei nun in "xenon.elf" umbenannt und mit der von der ubuntu Live Cd hier aus gem forum ausgetauscht.  
   
 Er fängt zwar an zu laden aber endet dann mit "Kernel Panic"  
   
 ![](http://farm6.static.flickr.com/5305/5651242691_44cbfc7822.jpg)[img]http://farm6.static.flickr.com/5305/5651242691\_44cbfc7822.jpg[/img]

## 2011-04-25 09:11:43, posted by: tuxuser

good mornin,  
   
 Here you got the Kernel Config and the initramfs which is needed for a LiveCD Kernel. Have fun!  
   
 PS: Please use the edit button to give new information, its kinda annoying to see 4 posts of a user in a row... thx  
   
 greetz  
 tux

## 2011-04-25 10:10:26, posted by: Doerek

[quote=""tuxuser""]good mornin,  
   
 [size=99px]**[b]Here[/b]**[/size] you got the Kernel Config and the initramfs which is needed for a LiveCD Kernel. Have fun!  
 [/quote]  
 Wo genau? :)  
   
 btw.  
 Den pfad zu den initramfs habe nach den änderungen ich an dieser stelle:  
   
 CONFIG\_INITRAMFS\_SOURCE="/path/to/casper-initramfs"  
   
 in der config angegeben.   
   
 Das hier ist das file das erstellt wurde:  
 [url=http://www.megaupload.com/?d=X7FF98U0]http://www.megaupload.com/?d=X7FF98U0[/url]

## 2011-04-26 11:12:00, posted by: tuxuser

I am sorry, [url=http://libxenon.org/http://libxenon.org//viewtopic.php?p=453#p453]HERE[/url] it is.

## 2011-04-26 12:39:41, posted by: Doerek

[quote="tuxuser"]I am sorry, [url=http://libxenon.org/http://libxenon.org//viewtopic.php?p=453#p453]HERE[/url] it is.[/quote]  
   
 Das archive habe ich ja runtergeladen und nach den anweisungen hier im forum zum kernel hinzugefügt...  
 Mein Ziel war es ja ursprünglich die noch nötigen änderungen vorzunehmen und nicht den momentanen Kernel einfach erneut zu kompilieren.

## 2011-04-26 17:20:47, posted by: tuxuser

about what changes are you talking?  
   
 PS: What about writing in english?

## 2013-11-11 20:16:45, posted by: 80JOKER80

hello tuxuser!  
   
 you wrote: "The most important part you probably want to edit is the root= parameter. Edit it to the device where your linux system is installed."  
   
 did you mean root=uda (USB Stick)  
 or did you mean boot=uda:/casper ???  
   
 hope someone will read this question :)