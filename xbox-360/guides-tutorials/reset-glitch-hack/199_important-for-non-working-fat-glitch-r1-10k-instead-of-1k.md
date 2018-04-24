# IMPORTANT for non-working FAT glitch R1 10K instead of 1K !!!

## 2011-10-13 14:29:58, posted by: beremoka

For those that are going nuts trying because everything was done according to the tutorials but the damn thing won't glitch here is a solution:  
 REPLACE R1 1K with a 10K ....this lowers the voltage to 1.3 V , verified on Jasper and Falcon  
 Feel free to try it...as the 10K only lowers the voltage, you won' fry a thing...

## 2011-10-13 14:59:27, posted by: Matando

interesting. Now if only somebody could find a fix to having pulled the POST\_OUT1 pad (FT6U7) I wouldnt have a broken jasper laying around.  
   
 lol the thing flashes to bottom red lights at me (player indicator lights 3 and 4)

## 2011-10-21 15:22:39, posted by: PDJ

Even better, remove R1 the diodes and all the stuff and connect pin 5 to the internal regulator (1.8V)  
 I've made a post on another forum about that, the solution about the diodes will result that the CLPD is running out of spec.  
   
 I've attached the foto's, this much easier to build an give better results.

### Attachments

[Newglitch48nofullpost.png](Newglitch48nofullpost.png)[CMOD-1.jpg](CMOD-1.jpg)

## 2011-10-22 18:56:45, posted by: seanr28

sorry for being stupid, but where is the 1.8v regulator? and would this help my jasperBB (512mb) glitch quicker, as sometimes it takes several reboots and a fair amount of time, and sometimes it simply will not glitch at all?

## 2011-10-23 15:41:25, posted by: djblade17

Can/should this be applied to matrix  
 I am having issues with my one falcon  
 2 of them work perfect One just hangs and goes to red light or once in a while glitches  
 is this related?

## 2011-11-04 02:39:00, posted by: xb0xguru

Cool - just as an FYI, if your CPLD doesn't have a 1.8v VR output, remember that U5B2 on the motherboard does. You can use this to the same effect.

## 2011-11-05 00:18:46, posted by: avomax

How do I get 1.8v. u5b2? How can I link?  
   
 ![](http://s7.postimage.org/nl9an96q1/u5b2.jpg)[img]http://s7.postimage.org/nl9an96q1/u5b2.jpg[/img]

## 2011-11-05 18:29:09, posted by: Johnny Bravo

I tested this alternate method on a Digilent CMod. It works great with a Falcon V2 .  
 No need for Diodes, Resistor or Capacitor, and less soldering ;)  
   
 @avomax  
   
 On your Picture it is the broad left solder joint of U5B2. Easily to find if you use a Multimeter.

## 2011-11-07 14:26:45, posted by: xb0xguru

Ok - after running various tests, these are things to try if your fat console won't glitch and you've already tried the above wiring:  
   
 1. put a 680pF Capacitor between CPU\_PLL\_BYPASS and GND (CPLD->22k Resistor->Cap (other end to GND)->Console).  
 2. This is literally something I worked out about 10 mins ago with a BB Jasper which was really erratic: Put a 470pF cap [u]in line[/u] to CPU\_RST. I have it CPLD->Cap-> wire -> console).  
   
 Before I did #2, the Jasper was really erratic. Now, it's booting within 5 secs EVERY TIME.  
   
 EDIT: Updated the new pic to include the changes. See attached.  
 EDIT #2: You can swap C2 for a 680pF also. It seems to work just as well.

### Attachments

[Newglitch48nofullpostV3.png](Newglitch48nofullpostV3.png)

## 2011-11-08 19:13:16, posted by: avomax

[quote="Johnny Bravo"]  
 @avomax  
   
 On your Picture it is the broad left solder joint of U5B2. Easily to find if you use a Multimeter.  
 [/quote]  
   
 Thank you.

## 2011-11-11 17:48:37, posted by: derlucifer

Hi everyone!  
   
 I only want to pay my tribute to xb0xguru for his solution to the erratic Jasper problems!  
 I've tried over 2 weeks by now on an Jasper that Glitched only from time to time (3-15min).  
 Then i've tried the last postet wiring from xb0xguru. Now my Jasper glitches in max. 10sec!!!  
   
 THANK YOU!

## 2011-11-13 17:25:20, posted by: seanr28

Just to share, I have just sorted out my 512b jasper that would not glitch, now booting in 4 seconds max, and xell immediatley and thats every time without fail!  
   
 I ended up using a 0.068uF Cap by pure fluke on the PLL\_Bypass to Gnd  
   
 ![](http://i166.photobucket.com/albums/u85/seanr28/P1010190.jpg)[img]http://i166.photobucket.com/albums/u85/seanr28/P1010190.jpg[/img]

## 2011-11-14 19:14:58, posted by: Mojjio

i just sorted out a Jasper 16MB that would not boot,  
 by using a 22k0hm 1% Resistor instead of an 5%.   
 used awg28 (from an old ide/ata 33 cable) to wire it all up.   
 with cmod chip. + upper r2 pad to lower r1 pad (same as on the slims aka internal 1.8V regulator)

## 2011-11-19 09:17:58, posted by: EdsonDario

[quote="xb0xguru"]  
 Ok - after running various tests, these are things to try if your fat console won't glitch and you've already tried the above wiring:  
   
 1. put a 680pF Capacitor between CPU\_PLL\_BYPASS and GND (CPLD->22k Resistor->Cap (other end to GND)->Console).  
 2. This is literally something I worked out about 10 mins ago with a BB Jasper which was really erratic: Put a 470pF cap [u]in line[/u] to CPU\_RST. I have it CPLD->Cap-> wire -> console).  
   
 Before I did #2, the Jasper was really erratic. Now, it's booting within 5 secs EVERY TIME.  
   
 EDIT: Updated the new pic to include the changes. See attached.  
 EDIT #2: You can swap C2 for a 680pF also. It seems to work just as well.  
 [/quote]  
   
 Thanks!  
   
 It worked here.  
   
 Reset Line = 470PF  
 CPU\_PLL\_BYPASS = 660pf (+330 pf 330PF)  
   
 Boot is within about 1 minute. For me it is good because I just wanted to dvd key.