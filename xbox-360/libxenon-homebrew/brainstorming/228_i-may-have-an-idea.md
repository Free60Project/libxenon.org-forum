# I may have an idea 

## 2011-11-12 15:06:00, posted by: antikhrist

hi ive been reading a lot about the reset glitch, jtagging etc and have had a few ideas hopefully you'll all have a better idea than me,  
   
 ive got a number of xenon 360's so the usual reset glitch wont work due to these 'HANA' chips if im right   
 so ive been looking at the board on the front (with the lights/power button) thinking 'thats a lot of components for a power button'   
 while i know it has an ir reciever etc theres also a lot of solder points and overly complicated looking circuits that look like they could be something better in disguise  
   
 based on the idea that non xenons need a pulse on the reset pin to glitch logically this board seems to have a little potential (surely the power button has a conection to reset somewhere)  
 ive also noticed that these boards connect universally among 'phat' motherboards so by having the mod in one of those it would in theory be prety easy to switch to another console (like between a jtag box and a stock box for example)   
   
 ive also noticed that some of these boards have metal sheilding over the raised area in the top right corner (above the crystal) but others dont   
   
 if anyone has any ideas to try or further knowledge on reverse engineering please let me know as even if this is a dead end id still like to learn

## 2011-11-12 19:37:00, posted by: warfaren

[quote="antikhrist"]  
 hi ive been reading a lot about the reset glitch, jtagging etc and have had a few ideas hopefully you'll all have a better idea than me,  
   
 ive got a number of xenon 360's so the usual reset glitch wont work due to these 'HANA' chips if im right   
 so ive been looking at the board on the front (with the lights/power button) thinking 'thats a lot of components for a power button'   
 while i know it has an ir reciever etc theres also a lot of solder points and overly complicated looking circuits that look like they could be something better in disguise  
   
 based on the idea that non xenons need a pulse on the reset pin to glitch logically this board seems to have a little potential (surely the power button has a conection to reset somewhere)  
 ive also noticed that these boards connect universally among 'phat' motherboards so by having the mod in one of those it would in theory be prety easy to switch to another console (like between a jtag box and a stock box for example)   
   
 ive also noticed that some of these boards have metal sheilding over the raised area in the top right corner (above the crystal) but others dont   
   
 if anyone has any ideas to try or further knowledge on reverse engineering please let me know as even if this is a dead end id still like to learn  
 [/quote]  
   
 Well it is more than a power button and a ring of light, it also has the chip that wirelessly communicates with your controllers, so that might explain the "lot of components" for you.

## 2011-11-13 18:29:06, posted by: antikhrist

yeah i noticed that after more research probably the wrong direction to go then found out how to make the board work by usb like one of the dongles m$ sells though so not a complete waste at least

## 2011-12-20 21:39:13, posted by: GhaleonX

If it's a matter of resetting the system, I know component adapters are an easy way to reset when you switch from SDTV -> HDTV on the adapter (or unplug/replug). Same applies for connecting/disconnecting a hard drive. Both of these will only reset the console while on the main dashboard, though. So perhaps that's why they'd be useless...

## 2012-03-07 06:07:51, posted by: IceKiller

actually no.. the hd drive disconnection doesn't reboot/reset the system at those post codes or smc.. so..its kinda not gonna work.  
 Again resetting the system isn't the problem