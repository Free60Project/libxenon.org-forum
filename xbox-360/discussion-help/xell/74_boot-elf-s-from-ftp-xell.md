# boot elf's from ftp xell

## 2011-05-18 04:21:53, posted by: dreamboy

hi, im new at xbox360 homebrew scene, i've got develop enviroment working with my ubuntu 11.04 and got the hello project to compile sucessfully, the only problem it that when i insert my usb stick8GB fat32 xell fails to mount it : i've read somewhere that xell can also boot elf files throw ftp, is that true? and if it is how can do that? i've read that xell reloaded has some usb fixes, but i cant load it with xell launcher :? can someone give me an hand on this?   
   
   
 Best regards,  
 Dreamboy

## 2011-05-18 22:22:12, posted by: mojobojo

Turn your console completely off, plug in your usb stick, unplug the power, hit the power button a couple times, then plug it back in. Boot into xell after you do all of that. If the stick doesn't mount then, your usb stick is not supported. I do not know how to boot with tftp, but what I said should get it working.

## 2011-05-19 10:03:11, posted by: dreamboy

[quote=""mojobojo""]Turn your console completely off, plug in your usb stick, unplug the power, hit the power button a couple times, then plug it back in. Boot into xell after you do all of that. If the stick doesn't mount then, your usb stick is not supported. I do not know how to boot with tftp, but what I said should get it working.[/quote]  
   
 Thanks a lot it worked :D

## 2011-05-20 09:18:13, posted by: dreamboy

well now i can launch xell reloaded throw fsd and xex menu, and it boots ubuntu 10.10 just fine throw my usb stick, but when i try to run by homebrew .elf its hangs on the message:  
   
 *Stop ethernet..  
 *Go (entrypoint: 0000000080001f00)  
 *Please wait a moment while the kernel loads...  
   
 i've renamed my elf file to xenon.elf as its suposed to be and its on the root of the usb stick, also tryied the xmenu 0.3 for loading homebrew at it give's me the same result : am i doing something wrong?  
 i got the lastest dash launch 2.21

## 2011-05-20 11:47:05, posted by: tuxuser

[quote=""dreamboy""]well now i can launch xell reloaded throw fsd and xex menu, and it boots ubuntu 10.10 just fine throw my usb stick, but when i try to run by homebrew .elf its hangs on the message:  
   
 *Stop ethernet..  
 *Go (entrypoint: 0000000080001f00)  
 *Please wait a moment while the kernel loads...  
   
 i've renamed my elf file to xenon.elf as its suposed to be and its on the root of the usb stick, also tryied the xmenu 0.3 for loading homebrew at it give's me the same result : am i doing something wrong?  
 i got the lastest dash launch 2.21[/quote]  
   
 You arent doing anything wrong. The problem is known and already fixed in our version which is still WIP.

## 2011-05-20 18:54:26, posted by: dreamboy

[quote=""tuxuser""][quote=""dreamboy""]well now i can launch xell reloaded throw fsd and xex menu, and it boots ubuntu 10.10 just fine throw my usb stick, but when i try to run by homebrew .elf its hangs on the message:  
   
 *Stop ethernet..  
 *Go (entrypoint: 0000000080001f00)  
 *Please wait a moment while the kernel loads...  
   
 i've renamed my elf file to xenon.elf as its suposed to be and its on the root of the usb stick, also tryied the xmenu 0.3 for loading homebrew at it give's me the same result : am i doing something wrong?  
 i got the lastest dash launch 2.21[/quote]  
   
 You arent doing anything wrong. The problem is known and already fixed in our version which is still WIP.[/quote]  
   
 cool, is there a way to bypass this problem ? the wip version that fixes this issue has been release? or it just gonna be out with the final version of xell reloaded?  
   
 thanks for the quick anwser and support :)

## 2011-05-20 20:29:22, posted by: tuxuser

We want to finish it before releasing anything new.. so you will have to wait, sorry.  
 No ETA

## 2011-05-20 20:54:23, posted by: dreamboy

[quote=""tuxuser""]We want to finish it before releasing anything new.. so you will have to wait, sorry.  
 No ETA[/quote]  
   
 Ok no problem, thanks anyway. Good luck with the project ;)