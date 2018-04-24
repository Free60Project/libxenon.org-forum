# [RGH]Collection of CPLD Diagrams

## 2011-10-21 12:15:36, posted by: tuxuser

Hey,  
 It would be cool if we could collect all diagrams for compatible CPLD boards which can be used for the Reset Glitch Hack.   
 Please post the diagram and write underneath whats the Target Revision (Slim/Fat).  
   
 [size=180]**[b]GENERAL NOTES[/b]**[/size]  
   
 [size=160]**[b]SLIM[/b]**[/size]  
 If the diagram mentions 220pF for the Capacitor value and your X360 Slim doesnt glitch good / at all - Try to use **[b]270pF[/b]**!  
   
 [size=160]**[b]FAT[/b]**[/size]  
 To *possibly* glitch a FAT Console better, stuff out the 1K Resistor, the 100nF Cap and the 3x 1N1418 Diodes and just connect the Voltage-Input Pin (the pin which is faced by the direction-stripe of the diodes) directly to 1,8V of an internal voltage regulator.  
 Thanks for the hint PDJ - [url=http://libxenon.org/http://libxenon.org//viewtopic.php?p=1060#p1060]Original Post[/url]  
   
 [size=160]**[b]BOTH[/b]**[/size]  
 Make the CPU\_RST Wire exactly **[b]32 cm[/b]** to get the best results!

## 2011-10-21 12:46:33, posted by: tuxuser

**[b]Dangerous Prototypes / Seeedstudio Coolrunner II[/b]**  
   
 FAT  
 [attach=1]  
   
 SLIM  
 [attach=2]  
   
 Verified: No  
   
 **[b]THAOYU XC2C64A Coolrunner-II Clone[/b]**  
   
 FAT  
 [attach=3]  
   
 SLIM  
 [attach=4]  
   
 Verified: Yes  
   
 **[b]Xilinx Coolrunner II XC9500[/b]**  
   
 FAT/SLIM  
 [attach=5]  
   
 Verified: No

### Attachments

[seeedstudiocoolrunner2FAT.jpg](seeedstudiocoolrunner2FAT.jpg)[seeedstudiocoolrunner2SLIM.jpg](seeedstudiocoolrunner2SLIM.jpg)[thaoyou_FAT.jpg](thaoyou_FAT.jpg)[thaoyou_SLIM.jpg](thaoyou_SLIM.jpg)[xc9500_cpld.jpg](xc9500_cpld.jpg)

## 2011-11-08 02:55:31, posted by: xb0xguru

I can confirm the THAOYU wiring posted works for both slim and fat consoles.

## 2011-11-24 19:02:02, posted by: EdsonDario

I also confirm that **[b]THAOYU XC2C64A Coolrunner-II Clone[/b]** **[b]works properly[/b]**. I used 270pf.

## 2011-12-11 23:00:24, posted by: c0sth4

Hello, can I ask you for some help?  
 I have  
 Xilinx Coolrunner II XC9500 but there is not installed C1 C5 Leds, P2 etc... can you provide me some diagram or write me, which parts are installed on that one which is on image? Or if its nescesary for using it in xbox? I can install it, but I cannot find complete datasheet or something what could help me, Thank you very much...

## 2012-05-14 11:55:17, posted by: smx

Seeedstudio coolrunner works fine with my Falcon with the provided diagram. Sometimes the console doesn't boot and it freezes, but it's 1 fail on 10 boots. Normally it boots immediatly.

## 2012-07-06 16:00:22, posted by: ddsdavey

Sorry if its an outdated thread but has anyone had any luck using these boards on RGH 2.0? I cannot for the life of me find any info,everyone has the Matrix etc.No info out there on the original boards like the ones featured on this page.

## 2012-07-07 00:34:24, posted by: saso333

i can confirm that Xilinx Coolrunner II XC9500 works with RGH2 by adding 3.3k resistor & 680pf cap on CPU\_RST line Jasper with slim setup

## 2012-07-07 13:34:59, posted by: ddsdavey

And thats the board im struggling with so great,thanks! do you use the same coolrunner points on phats that 12c\_SDA & 12c\_SDL use on slims ie pins 9 & 10? And that on Phat mobo 12C\_SDA goes to J2B1-9 and 12C\_SCL goes to J2B1-10?  
 One more thing (sorry!),i have to modify my board like this for slims...[url=http://imageshack.us/photo/my-images/94/fullview.jpg/]![](http://img94.imageshack.us/img94/5834/fullview.jpg)[img]http://img94.imageshack.us/img94/5834/fullview.jpg[/img][/url]  
 I have to modify it differently for phats,but im thinking for RGH 2.0 the above is necessary even on Phats?  
 To be clear,i am wanting to do RGH 2.0 on a falcon.  
 And your advice,3.3k resistor to gnd on CPU\_RST pin & 680pf cap in series on CPU\_RST or again to gnd.  
 Sorry again for all these questions,just ignore me if you cannot be bothered lol but your the first person to give me a glimmer of hope!  
 Have you any sources for further info on cpld use with RGh 2.0 to save hassling you lol!  
 Thanks again.