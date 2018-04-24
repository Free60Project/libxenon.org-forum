# Debian Packages, AKA skip the compile time.

## 2011-10-09 15:18:35, posted by: Juvenal

Hello folks,  
   
 Today I present to you the result of many weeks of trial and error.  
   
 I have created binary packages for the debian linux distribution, which means if you use debian or ubuntu as your development machine you no longer have to compile the toolchain and related libraries yourself!  
   
 To go with these packages I have setup a debian APT repo to make installation easier.  
   
 The simplest way to setup the repo and install the whole toolchain shebang is to simply execute the following command on your debian machine.  
 [code]* *wget -q http://apt.juvsoft.com/do-it-all.sh -O /tmp/do-it-all.sh && bash /tmp/do-it-all.sh [/code] This script will do three things. [list=1] - [*]Download my repo's public key and add it to APT
 - [*]Add my repo to your APT's sources.list
 - [*]Install the toolchain
[/list] If you prefer to manually do these things the commands are as follows.  
 [code]* *#Adds my public key to apt so it can read my repo wget -O - http://apt.juvsoft.com/debian/key.gpg | sudo apt-key add - #Adds my repo to your sources.list sudo echo "deb http://apt.juvsoft.com/debian/ squeeze main" >> /etc/apt/sources.list.d/libxenon.sources.list #Installs the toolchain sudo apt-get update && sudo apt-get install xenon-binutils xenon-newlib xenon-gcc libxenon [/code] The truely technical may have noticed that "squeeze" bit in there. This is because I only currently have debian squeeze installed, so no other binary packages have been built.  
   
 This is where the community comes in. Eventually I plan to have several Virtual machines setup for future builds of these packages across multiple debian releases and potentially some ubuntu releases aswell. But as of now, I have neither the time nor energy to install 5-10 copies of debian and build 5-10 toolchains! So, if you have a debian distribution installed and would like to help me/the community out Ive made it very simple :)  
   
 Anyone wishing to build my packages for whatever debian release or cpu architecture simply needs to follow this guide. (or rather series of commands)  
 [code]* *#lots of suff is going to need root, so this makes life easier sudo su root #or just login as root any way you can #install various debian packaging related tools apt-get install autoconf automake autotools-dev debhelper dh-make devscripts fakeroot git gnupg lintian patch patchutils build-essential pbuilder quilt libgmp3-dev libmpfr-dev libmpc-dev texinfo gettext autogen git clone git://github.com/Juvenal1228/xenon-debs.git cd xenon-debs make [/code] The make command will take anywhere from 30-120 minutes to finish and may, for whatever reason fail.  
   
 IF it does fail PLEASE copy as much of the output as you can and put it up on pastebin and link it in a reply here  
   
 If it completes successfully there will be a bunch of files in ./output  
 all you need to do is find me (Juvenal) on efnet, im ususally in #libxenon and send me those files somehow.  
   
 Easiest way would be to just rar them and put em on mediafire or whatever.  
   
 [s]NOTE: Currently there are only 64bit binaries up in my repo, I am building 32bit binaries as we speak, but I can assure nothing![/s]  
 32bit binaries are up. I have not tested code produced from them on a console yet, but i see no problems compile wise.  
   
 Tootles,  
 Juvenal

## 2011-10-10 20:25:09, posted by: Juvenal

Hello,  
   
 Just wanted to let everyone know the original post has been fixed in a few respects. The most important of which is making the commands work and fixing the do-it-all.sh script.  
   
 The apt repo and packages can now be installed simply by running. [code]wget -q http://apt.juvsoft.com/do-it-all.sh -O /tmp/do-it-all.sh && bash /tmp/do-it-all.sh[/code] You either need to be root, or have permission to use sudo, as it will do sudo-y things.

## 2012-01-30 06:13:24, posted by: Xplorer4x4

Seems that the URLs with in the shell script are out dated. [quote]#==================  
 #LibXenon APT Entry  
 #==================  
   
 deb http://new.apt.juvsoft.com/debian/ unstable main  
   
 Done!  
   
 Downloading GPG Public key...  
 Adding key to APT...  
 OK  
 Updating APT...  
 W: Failed to fetch http://new.apt.juvsoft.com/debian/dists/unstable/main/binary-i386/Packages.gz&nbsp; 404 Not Found  
   
 E: Some index files failed to download, they have been ignored, or old ones used instead.  
 root@debian:~# [/quote] Would some one be so kind as to post an attachment of an updated shell script? I tried to PM the author but it has been 24 hours with out a reply.

## 2012-02-02 21:41:26, posted by: Juvenal

change the line to [code]* *deb http://juvsoft.com/apt/debian/ squeeze main [/code] Ive been playing with the repo's in order to add distributions for each ubuntu/debian release and haven't finished putting libxenon in the new repo, so i suggest you use this for now

## 2012-02-07 04:41:09, posted by: Xplorer4x4

Dissregard

## 2012-02-08 17:49:56, posted by: Xplorer4x4

Ok I fixed the shell script changing [tt]codename="unstable"[/tt] to [tt]codename="squeeze"[/tt] and the repo URL is now parsed properly, but the script is not set up to deal with the packages.gz file. Would you be so kind as to tell me what(and where) I need to insert with in the script to handle the gz file?