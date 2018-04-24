# Ubuntu 11.10 modprobe: FATAL: Could not load modules.dep

## 2012-09-20 21:58:23, posted by: Xenomorf

Hello!  
 I have a problem that he can not cope. I installed successfully on xbox 360 slim hdd linux Ubuntu 11.10. During boot, the system displays this information: modprobe: FATAL: Could not load /lib/modules/2.6.38.8-xbox0.11.1/modules.dep: No  
 such file or directory   
   
 Can someone explain to me step by step how to get the modules.dep and how to fix this problem.  
   
 Thank you for your help and sorry for my language ;-)   
   
 Wys?ane z mojego Optimus 2X za pomoc? Tapatalk

## 2012-09-20 22:15:49, posted by: tuxuser

dobry!  
   
 I would suggest you just use the kernel + modules that you can find here:  
   
 http://file.libxenon.org/~tuxuser/v2.6.38.8-kernel.tar.gz  
 http://file.libxenon.org/~tuxuser/v2.6.38.8-modules.tar.gz

## 2012-09-21 07:56:29, posted by: Xenomorf

Thank you very much for your help. Really great job you are doing tuxer.

## 2012-09-21 09:27:06, posted by: tuxuser

Will supply 3.5.1 kernel + modules later this day

## 2012-09-21 15:59:26, posted by: Xenomorf

Thank you so much, that would be great, your help is most appreciated.   
   
 Now, I have another problem, the picture on my tv is oversized, thus cutting the icon strip on top and bottom of the screen. Having consulted my friends, they do not experience this problem. I think the fault lays in my tv - SAMSUNG LE19C450 model. Could you help me solve this problem?   
   
 PS.   
 I do not know whether I can present this problem with the tv screen picture issue in this place. If not my apologies, please direct this problem to the suitable place.

## 2012-09-21 16:30:52, posted by: Pa0l0ne

[quote="Xenomorf"]  
 Thank you so much, that would be great, your help is most appreciated.   
   
 Now, I have another problem, the picture on my tv is oversized, thus cutting the icon strip on top and bottom of the screen. Having consulted my friends, they do not experience this problem. I think the fault lays in my tv - SAMSUNG LE19C450 model. Could you help me solve this problem?   
   
 PS.   
 I do not know whether I can present this problem with the tv screen picture issue in this place. If not my apologies, please direct this problem to the suitable place.  
 [/quote]  
   
 If you have an overscan problem you have a problem on your selfcompiled or downloaded kernel that doesn't have the correct fix for this well known problem...  
   
 Just to be clear, you have to compile a kernel with the overscan fixed"xenonfb.c"  
   
 I think [url=http://www.consoleopen.com/forum/attachments/sviluppo-homebrew-e-compilazione-linux/2823d1330339954-bug-reporting-e-commenti-linux-su-xbox-360-parte-terza-vmlinux.rar]THIS[/url] compiled version has the correct fix onboard   
   
 Maybe the new 3.5.1 kernel is another well solution....we all are on tuxuser hands... ;)

## 2012-09-21 18:50:29, posted by: tuxuser

Update:  
   
 http://file.libxenon.org/~tuxuser/v3.5.4-kernel.tar.gz  
 http://file.libxenon.org/~tuxuser/v3.5.4-modules.tar.gz  
   
 Didn't have time to test it though.  
 Thx goes to sk1080 for porting over Bertl's patches to recent kernel version

## 2012-09-21 18:56:46, posted by: Pa0l0ne

[quote="tuxuser"]  
 Update:  
   
 http://file.libxenon.org/~tuxuser/v3.5.4-kernel.tar.gz  
 http://file.libxenon.org/~tuxuser/v3.5.4-modules.tar.gz  
   
 Didn't have time to test it though.  
 Thx goes to sk1080 for porting over Bertl's patches to recent kernel version  
 [/quote]  
   
 Much appreciated!

## 2012-09-22 14:41:24, posted by: Xenomorf

Tuxuser I have a question for you, after unpacking the package v3.5.4-kernel.tar.gz there are three files:  
 - Config  
 - System.map  
 - Vmlinux  
 The name of the file 'vmlinux' change to 'latest\_kern'. What exactly should I do with the files: config and System.map?  
   
 I do not want to abuse your kindness, but I am forced to ask for help again. I'll start with perhaps the fact that kernel, which provided Pa0l0ne overscan solved the problem - thanks Pa0l0ne ;-).  
 Since I am new to linux and the same issues still can not solve many of the problems on their own I would very politely ask me to prepare for v3.5.4-kernel in such a way as to eliminate the problem oversan. Thank you very much for your help.  
   
 PS.  
 In my case, the new v3.5.4-kernel does not solve the problem of overscan.

## 2012-09-22 16:43:48, posted by: tuxuser

System.map and config are just giving info on how the kernel was built/configured, you dont need them really.. you only care about vmlinux.. and as you already booted it to check overscan it's all good.  
   
 Overscan is related to xenonfb/xenosfb .. as libxenon is not using proper videoinit yet, dont expect xenosfb being updated....  
 We will see what we can do, we have somebody working on it.  
   
 Greetz

## 2012-09-22 18:49:26, posted by: Xenomorf

Thank you for the explanation. I will begin testing :-)

## 2012-09-25 20:01:48, posted by: Xenomorf

I have some questions related to the topic. Well, from the very beginning of the Ubuntu 11.10 Oneiric does not detect the CD / DVD drive, also there is no sound. I thought that the reason is the lack of these modules, which are reported in the charging system. However, it soon these modules after the situation has not changed and still no sound and ubuntu does not detect the CD / DVD drive. In view of this fact, I would like to ask a few basic questions to answer, please someone well-versed in the subject.  
 1. Does Ubuntu 11.10 Oneiric installed on the HDD xbox360 slim is sound. Alternatively, if you can set it at all?,  
 2. Do you even see the ubuntu CD / DVD drive xbox 360?,  
 3. Is there any way to retrofitted WINE, because there is no suitable repository package?,  
 4. Is it possible to install Xbox Media Center?,  
 5. Image during video playback, such as xine is yellow, if you can do something that could normally watch movies?  
 6. Is it possible to connect to the internet via 3G USB modem?.  
   
 Sorry to ask so many questions, but I can not find the answers to my questions.  
   
 Thank you for your general interest and response.  
   
 PS.  
 I have a xbox 360 slim hdmi cable connected to a Samsung LE19C450 LCD TV.

## 2012-09-25 21:09:03, posted by: Pa0l0ne

My little knowledge said: We don't have a linux Xbox360 video driver capable of so much performance...actually Xine or Xbox Media Center are just a dream for "daily use"...  
   
 But regard of your question i'm so much happy to see guys interested in Xbox360 Linux instead of MS Game use. Maybe 99% of people think Xell are just a way for pirated software and DON'T remember what "Xenon Linux Loader" (initially?) mean....

## 2012-09-25 22:09:26, posted by: tuxuser

[quote="Xenomorf"]  
 1. Does Ubuntu 11.10 Oneiric installed on the HDD xbox360 slim is sound. Alternatively, if you can set it at all?,  
 2. Do you even see the ubuntu CD / DVD drive xbox 360?,  
 3. Is there any way to retrofitted WINE, because there is no suitable repository package?,  
 4. Is it possible to install Xbox Media Center?,  
 5. Image during video playback, such as xine is yellow, if you can do something that could normally watch movies?  
 6. Is it possible to connect to the internet via 3G USB modem?.  
 [/quote]  
   
 1. No sound, never got it to work.. however, sound driver is integrated into kernel.. so it should be possible to get sound out of it somehow.  
 2. Can't remember, never really took care of that.  
 3. No wine for PowerPC existing  
 4. Not with the current Video Driver which doesn't support 3D  
 5. Try this: http://file.libxenon.org/free60/linux/xenosfb/xserver-xorg-video-xenosfb\_0.0.6-0free60\_powerpc.deb  
 6. Sure, if there are linux drivers for the 3G usb modem it's no problem  
   
 Greetz

## 2012-09-25 22:24:02, posted by: Xenomorf

Thank you for your answers.   
 I would simply like to know whether after the fitting configuration, the ubuntu is suitable for normal usage, or is it only curiosity with limited possibilities.

## 2012-09-25 22:28:24, posted by: tuxuser

With enough optimization it could be a good and fast "desktop"

## 2012-09-25 22:37:47, posted by: Xenomorf

OK. I will fight on ;-)

## 2013-03-29 11:50:20, posted by: sema

\