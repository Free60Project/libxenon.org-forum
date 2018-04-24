# Slim cygnos ver E glitch hack help.

## 2011-10-16 06:43:26, posted by: Magnus_Hydra

Slim with the most updated dash.  
   
 I've got a x360glitchip flash and installed it. Made a Ecc with my nands back up (1 of many). I can't use nandpro E to flash to my nand. The cygnos will not let me use it. So I did the following:  
   
 nandpro 2.bin: +w16 image\_00000000.ecc 0 50  
   
 Then flash my cygnos chip. I plug up my xbox to AV cables and turn it on with the cygnos nand.( plan on putting in the relay later.) Anyways, without the dvd drive in and the face plate unplugged. I tap right above the header like Ive seen in videos and it xbox will turn on and the light will keep flashing. I hear a sound like power is lowering and going back to normal. I let it do that for about 5 mins and nothing happened. After I turned it off I turned it back on and it did the same thing but after like 30secs it had a red light...  
   
 So my question is   
 nandpro 2.bin: +w16 image\_00000000.ecc 0 50 and then flashing that 2.bin to my cygnos work? Any info would be nice.

## 2011-10-16 20:13:23, posted by: spandaman

Now you will need to open command prompt and navigate to the folder will all these files and type the command "nandpro nand.bin: +w16 image\_00000000.ecc", the "nand.bin" being the name of your nand file in this directory.   
   
   
   
 Sent from my iPhone using Tapatalk

## 2011-10-17 01:06:05, posted by: Magnus_Hydra

yeah   
   
 nandpro 2.bin: +w16 image\_00000000.ecc 0 50  
   
 2.bin is my nand. I was wondering if it would work writing to the nand backup would work.