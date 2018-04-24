# FSD run elf

## 2011-07-26 18:32:25, posted by: michalss

Hi,  
   
 Can anyone answer this question pls ? Can i run elf file on FreeStyle Dash somehow? Or can i convert elf to xex ?  
   
 Thx

## 2011-07-26 21:16:39, posted by: mojobojo

No, you must run the elf from xell. Name it "xenon.elf", put it on the root of a usb stick, and start xell. It will auto load.

## 2011-07-27 06:31:30, posted by: michalss

[quote="mojobojo"]  
 No, you must run the elf from xell. Name it "xenon.elf", put it on the root of a usb stick, and start xell. It will auto load.  
 [/quote]  
   
 OK understood, thx. So there is also not way to make convert to xex ? Actually ppl asking me to make application for them, but they dont want to use it from booting, so i'm looking for way to convert it to xex or some other way to make my apps starting from Dashes. If this is not possible then i guess i have to go forward :)

## 2011-07-27 11:30:32, posted by: mojobojo

No, you cannot covert an elf to xex. They are two different types of executables meant to be executed in two different ways.

## 2011-07-28 02:54:25, posted by: scuba156

it could be supported though. FSD could use XSetLaunchData to pass data to xell (xell would have to be set up to recieve the data too), or just have FSD do the dirty work and copy the .elf to the required location.  
   
 maybe an ELF loader would be a good idea...hmmm....

## 2011-07-29 14:29:04, posted by: Meluxe

Hi there,  
   
 like mojobojo said, xell is our elf loader. Xelllaunch.xex can be used out of FSD to load a Xell version. That Xell version runs than your .elf on the fly.  
   
 So just add Xelllaunch+Xell to your apps, and give your friends a try.