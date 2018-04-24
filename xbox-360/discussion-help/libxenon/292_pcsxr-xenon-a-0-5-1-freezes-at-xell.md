# PCSXR-xenon_a_0.5.1 Freezes  at xell

## 2012-02-27 03:30:39, posted by: reefz3ro

Ive been trying to run PCSXR but when the xenon.elf loads in xell i just freezes and never goes past the loading .elf screen  
   
 any ideas on getting this working  
   
 Thanks in advance

## 2012-02-28 09:32:30, posted by: Haze666

[quote="reefz3ro"]  
 Ive been trying to run PCSXR but when the xenon.elf loads in xell i just freezes and never goes past the loading .elf screen  
 [/quote]  
   
 What version of Xell are you running?  
 What kind of system? RGH or JTag?  
 If you are using a RGH and you are using Xell Reloaded built with FB tool maker, or Jtag toolbox, you may need to update, or run xell via XellLaunch.

## 2012-02-29 02:15:53, posted by: reefz3ro

its an RGH Trinity its xell version 0.99 built with multibuilder v0.7 on dash 14699 and it does the same when i use XellLaunch it gets to loading the .elf the screen blinks shows the same images and freezes there.

## 2012-02-29 04:15:42, posted by: barnhilltrckn

The released binary is not running on slims atm. I have been keeping up with his progress and his current code will run on a slim(I have a slim) but only the gui, I cant get any games to load for some reason though but ced will get it there Im sure.

## 2012-02-29 04:35:07, posted by: reefz3ro

Thank you for the answer ...so i guess its a waiting game now   
   
 Can you let me know where i can follow his progress as well and get current code Thanks agian ;)

## 2012-02-29 05:19:13, posted by: dreamboy

[quote="barnhilltrckn"]  
 The released binary is not running on slims atm. I have been keeping up with his progress and his current code will run on a slim(I have a slim) but only the gui, I cant get any games to load for some reason though but ced will get it there Im sure.  
 [/quote]  
   
 yup i notice the same yesterday on my x360 slim rgh trinity 16mb with xell reloaded 0.991 it freezes on gui. my guess its maybe its because of outdated libxenon or outdated lzx lib, that was used to compile the release when it got out. I verified that the same lzx browser gui works fine on the lasted libxenon and lzx revision.

## 2012-03-01 20:44:57, posted by: barnhilltrckn

[quote="dreamboy"]  
 [quote="barnhilltrckn"]  
 The released binary is not running on slims atm. I have been keeping up with his progress and his current code will run on a slim(I have a slim) but only the gui, I cant get any games to load for some reason though but ced will get it there Im sure.  
 [/quote]  
   
 yup i notice the same yesterday on my x360 slim rgh trinity 16mb with xell reloaded 0.991 it freezes on gui. my guess its maybe its because of outdated libxenon or outdated lzx lib, that was used to compile the release when it got out. I verified that the same lzx browser gui works fine on the lasted libxenon and lzx revision.  
 [/quote]  
   
 Well I thought some of the same things but I am on the latest xell. Also I updated libxenon with ced's libxenon to see if that changed anything but the same thing happened.

## 2012-03-03 14:21:47, posted by: Pa0l0ne

Same problems here. Latest Xell 0.991 on my Falcon Jtag and latest myself compiled pcsxr-xenon with latest Ced2911 libxenon and libs (./build-xenon-toolchain libs).  
   
 Regardless where i start Xell (Pure booting or via Xell Launch) the emu won't load the GUI.  
 With older versions it's all ok.

## 2012-03-05 05:18:21, posted by: mossbreaker

Similar problems with me. Latest Xell 0.991 on Falcon RGH. Start Xell via pure boot or Xell Launch the emu won't load the GUI. It did not work on the previous version of xell I had either (0.99), always getting stuck at the loading .elf screen.