# question about xenos.c

## 2012-08-06 02:53:16, posted by: ravendrow

ok so i figured out how to get video back on my composite/component cable  
   
 i just added  
 mode = VIDEO\_MODE\_PAL60;  
 break;  
 to avi pack 0x43  
   
 that brought back picture when hooked up to crappy SDTV the problem i am having now is when i switch back to the standard 3 plug RCA xell shows up in black and white going threw xenos.c i notice that on most of the video modes the first line is 0x0000004f but on the one for PAL60 it's 0x0000005f so is this the region setting? if not which one is?  
   
 thanks  
   
 EDIT   
 so the first line is not the region any Idea's ?

## 2012-08-06 06:39:10, posted by: ravendrow

0xdeadbeef really?? that's funny.... who's idea was that?

## 2012-08-06 07:11:14, posted by: sk1080

Microsoft's

## 2012-08-06 07:42:58, posted by: tydye81

Its in the ANA registers 1-2 times I think. May just be to show endianness

## 2012-08-07 02:11:09, posted by: tuxuser

What about using VIDEO\_MODE\_NTSC instead?

## 2012-08-08 08:47:59, posted by: ravendrow

tried it and video came up on standard RCA but not component/composite hookups  
   
 it's not a huge deal to me cause normally if i want to use standard RCA's i just use my slim av cable which has a different id just wondering if it can be changed so there is a NTSC composite?