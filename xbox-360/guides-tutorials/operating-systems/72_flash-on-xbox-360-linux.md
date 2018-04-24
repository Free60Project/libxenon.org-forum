# Flash on Xbox 360 Linux

## 2011-05-12 13:11:23, posted by: UNIX

Hey guys, I figured I would write up a quick tutorial for people who are currently using a Linux distribution on their Xbox 360 and are bothered by not having a flash player. I thought about it for a while and came up with a somewhat decent solution!   
   
 To do this, you need will need to have SSH running on a remote PC, and have a browser with a flash plugin installed on that PC. It can be a Windows, Linux, or Mac computer you are accessing, but in this tutorial I will be describing setup on Ubuntu Linux (11.04)  
   
 In any case, it works, and it's fun to play around with :D Now let's begin:  
   
 1. You will need to install SSH on your PC. On Ubuntu, the command you will need to use is:  
 sudo apt-get install ssh  
   
 2. Now test to see if SSH is running, just to be sure, by using:  
 ssh localhost  
 You should get a message asking whether or not you want to connect to the host, type no or hit control + C  
 If not, make sure SSH installed correctly.  
   
 3. Now that SSH is running on your computer, open a terminal on your Xbox 360 Linux distro and type:  
 ssh -X username@address  
 Username is where the username of the account on your host machine will go, and address is the local IP address of the host machine  
   
 4. SSH will pause for a moment, and ask you if you want to connect, type yes and press enter.  
   
 5. Once you are logged in successfully, you are ready to test! At the terminal on your Xbox, type in your browser command. In my case, I use Firefox, so at terminal I simply type 'firefox'.  
   
 6. Once you have executed your browser command via SSH, your web browser will come up on screen! Now, you can go to youtube, or anywhere, and you will have flash player working!  
   
 NOTES:   
 *Youtube videos show up with a blue tint in my case, not sure why, but it is not really that bad.  
 *In my case, my ALSA plugin doesn't work, and the sound comes out of my PC speakers. Not sure if this will be the case for others...  
   
 I thought I would share this little tutorial with everyone. This method will also probably work on a LiveCD if SSH is installed, though I did this on my Debian HDD install. The quality isn't amazing, but it is a small work around for those who want to enjoy their Xbox's speed with Linux, but also want to use flash player. Sadly, Gnash doesn't work, so this will do :)  
   
 Enjoy, hope I helped. Ask questions below if you get stuck or something isn't working.  
 -UNIX

## 2011-05-12 18:45:47, posted by: tuxuser

Thanks for sharing :)

## 2011-05-14 00:02:03, posted by: Chrisoldinho

thanks for this. I have been struggling to get flash working.  
   
 My best hope was lightspark. I tried compiling this from source as the PPA did not work, I followed the steps here: [url=http://sourceforge.net/apps/trac/lightspark/wiki/Building]http://sourceforge.net/apps/trac/lights ... i/Building[/url]  
   
 I cannot seem to get this to work, admittedly I am new at compiling but the instructions seemed simple. I installed all necessary dependencies (and more) but I still get errors:  
 [code]-- checking for module 'libxml++-2.6>=2.33.1' -- package 'libxml++-2.6>=2.33.1' not found CMake Error at /usr/share/cmake-2.8/Modules/FindPkgConfig.cmake:266 (message): A required package was not found Call Stack (most recent call first): /usr/share/cmake-2.8/Modules/FindPkgConfig.cmake:320 (\_pkg\_check\_modules\_internal) CMakeLists.txt:155 (pkg\_check\_modules)[/code] libxml++2.6 is installed though so I am stuck now with what to try.  
   
 In the meantime I will use your tip, and hope that one day lightspark can be compiled to work as I think this would be a more long term solution.  
   
 Chris.

## 2011-05-14 02:09:02, posted by: tuxuser

did you install the dev/devel version of libxml2 ? When you are compiling from source you always have to install the development packages!

## 2011-06-04 16:27:03, posted by: danny0085

I use this stand-alone [url=http://tips-linux.net/en/linux-ubuntu/linux-windows-software/flash-player-for-linux]flash player for linux[/url] . It worked for me. It has advanced features such as full screen mode and playlists

## 2011-06-06 04:25:04, posted by: UNIX

[quote=""danny0085""]I use this stand-alone [url=http://tips-linux.net/en/linux-ubuntu/linux-windows-software/flash-player-for-linux]flash player for linux[/url] . It worked for me. It has advanced features such as full screen mode and playlists[/quote]  
   
 Hmm, I'll have to try that out sometime. Thanks for sharing that!