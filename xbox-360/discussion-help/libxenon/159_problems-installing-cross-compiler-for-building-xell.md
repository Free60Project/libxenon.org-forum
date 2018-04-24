# problems installing cross compiler for building xell

## 2011-09-07 00:37:32, posted by: ravendrow

ok so i am pretty much a noob when it comes to compiling stuff for the jtag over the last 24 hours i managed to install the toolchain libxenon zlib ect and i was able to compile all the sample codes and i even compiled mupen 64 ( took forever to figure out what to name the ROM to make it load then i remember to look in the source code lmao) kids are currently tearing up mario kart 64.but the problem i had was i wanted to compile my own 2stage with the colors changed back to matrix style but when i went to build the cross-compiler stuff to compile your own xell it started erroring out on me first it was that i cannot run 2 of the scripts as root because they are dangerous so i went back in and tried again without su accessit said it couldnt download some gdp file (i think it couldnt download because there is a newer version) anyways downloaded that put it where it needed to be re ran the script looked like all was going well then i got   
 configure:error:  
 **** These critical programs are missing or too old: as ld  
 **** Check the INSTALL file for required versions.  
   
 kinda stuck at this point so i though someone here might be able to help me out plus i wanted to let you guys know there is a github with the right gdp package on it if you guys dont just update the script to use the newer gdp

## 2011-09-07 00:43:13, posted by: tuxuser

erm.. what are you trying to configure there? you just have to navigate into 2stages sourcedir and execute: make CROSS\_COMPILE=xenon-  
 Would be helpful if you could post the whole log, like:  
 [code]* *make CROSS\_COMPILE=xenon- > log.txt [/code]

## 2011-09-07 00:57:47, posted by: ravendrow

thanks for the fast response the problem was with me trying to build crosstool i wanted to try to compile xell with that because for some reason when i compiled using make CROSS\_COMPILE=xenon- the resulting xell-2f.bin wasn't 256kb it was only 155.4kb  
   
 sorry for being such a noob trying to compile mupen64 is what got me started on this and now i dont really wanna stop lol

## 2011-09-07 01:00:47, posted by: tuxuser

So it's working for you now?

## 2011-09-07 01:08:44, posted by: sk1080

[quote="ravendrow"]  
 the resulting xell-2f.bin wasn't 256kb it was only 155.4kb  
 [/quote]  
 [s]That should be fine[/s] I am not sure... Guess you better wait for tuxuser to get up again  
 If you need more rapid help, try the irc at efnet #libxenon

## 2011-09-07 02:26:09, posted by: ravendrow

nope my xell-2f.bin is still only 155.4kb shouldn't it be 256kb? that is the only prob i am having now...just to make sure i am compiling from the right source what is the 2stage git rep address because from what i can tell it is the main xell rep i could be wrong but that is where i get redirected to  
   
 sorry if i seem short i just found out one of my best friends died of an od this morning. trying to do this to take my mind off of it so please bear with me

## 2011-09-07 05:05:02, posted by: ravendrow

n/m got it all sorted there has to be a problem with the source listed on the free60 website i downloaded tuxuser's xell and that compiled without and issue xell-2f.bin is now 256kb now to figure out how to change the colors

## 2011-09-07 08:28:32, posted by: tuxuser

I know your mistake probably   
 [code]* *git clone git://sourceforgeurl/xell git checkout 2stages [/code] that switches to the xell 2stages branch ;)

## 2011-09-07 19:25:06, posted by: ravendrow

thanks tuxuser your the man!....oh yeah for the total noobs reading this you actually have to run 3 commands...if you dont do the cd xell command it will yell at you saying your not in a git rep...oh tuxuser is 2stages working for you on composite cables? i can only get it to work with av or hdmi cables  
 [code]* *git clone git://sourceforgeurl/xell cd xell git checkout 2stages [/code] it does boot on composite it just doesnt show any video