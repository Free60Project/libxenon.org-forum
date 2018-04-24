# Xenon Homebrew Channel 

## 2013-01-06 21:39:11, posted by: shortstop

I started using the libxenon toolchain during the last few days and i am really happy with it !  
 I just would like to know if there is already a solution similar to the Wii "homebrew channel" features :  
   
 1) List the homebrew found on your USB Key   
 2) Select and launch a homebrew from a menu   
 3) On Exit function come back to the homebrew channel   
 4) Reload the USB Key Content if necessary  
   
 I am not waiting for a graphical application, i am just looking for a working solution.  
   
 After browsing the forum and google, i was able to solve issues 1 and 2 by using lzxbrowser ( launched from XellLaunch )  
   
 My main issues concern now the steps 3 and 4.   
   
 For example today, if i launch cube.elf32 from lzxbrowser, i don't know how to stop the program and come back to zlxbrowser ?  
 If i update the content or an executable on my usb key, i don't know how to reload the content of the key ?  
   
 Here follows my current stable installation :  
   
 On the Internal HDD :   
 A) HDD/Application/ : XellLaunch application Directory  
 B) HDD/Content/ : a shortcut to XellLaunch  
 C) HDD/ : launch.ini with a direct link for button\_Y => HDD/Application/XellLauncher/default.xex  
   
 On an external USB Key :  
 A) USB/ : a file xenon.elf ( = a copy of lzxbrowser.elf32 )  
 B) USB/ : for each hombrew xxx, an xxx folder with data and executables xxx.elf and xxx.elf32  
   
 Thank you for your help.

## 2013-01-07 10:03:40, posted by: Ced2911

you can make a xell remplacement with zlx

## 2013-01-08 01:55:57, posted by: shortstop

Dear Ced2911,   
   
 Thank you for your answer.   
   
 Since it is the first time i have to update this part by myself i will not replace my xell before understanding what may be the consequences and how to recover the current state. For a few days, i will try and use the function "xenon\_smc\_power\_reboot()" to quit the program if necessary even if i understand that your option is the real solution.  
   
 Is it simple to explain us why the call to exit() or return does not work when i launch Xell-Reload by using XellLaunch ?  
 Is it coded as a return to the caller ( zlx\_browser ) or a call to a specific subroutine of Xell-Reload ?  
 As a consequence, when i start directly the program with the eject button, why the function exit() does not hang but do nothing ?  
   
 Remark. I have found another discussion on a similar topic in the help part of the forum.  
 May i have to move the current topic or make a link to it ?  
   
 Best regards.

## 2013-01-12 14:54:03, posted by: shortstop

Following your answer, i have flashed my nand with a file including Xell-Reloaded so xell-reloaded is my new xell.  
 Even if i don't know exactly why, the exit button in zlx-browser allow me now to go back to Xell-Reloaded. Hourra !!   
   
 Now i am looking for the best way to debug my program game.elf32 directly from my PC without touching the usb-key and the gamepad.  
   
 Question 1 : Is there any starting guide or tutorial for "debugging a libxenon homebrew" that i could read ?   
 Question 2 : Could we put zlx browser in the nand to replace xell.bin ?