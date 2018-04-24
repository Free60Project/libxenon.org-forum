# 0022 error after rgh hack

## 2011-12-07 13:18:10, posted by: lenselijer

I had 2 jasper boards that lost the dvdkey.  
   
 Installed the cpld board and recovered the dvdkeys using rgh/xell.  
 Now i flashed back the stock nand and they both give 0022 error.  
   
 Also i cannot glitch them anymore, someone knows how to fix this?  
 Did i kill the cpu by using a 680pf capacitor on ppl\_bypass?

## 2011-12-07 15:27:27, posted by: Coagulate

Have you tried removing the 3.3v and Ground from the CPLD when you reflashed the nand to stock? Sometimes it gave me 0022 when the CPLD was still hooked up.

## 2011-12-07 16:21:47, posted by: tuxuser

how did you flash the original image back? with -w or +w ? you have to do -w for images which contain valid ECC already

## 2011-12-07 19:12:27, posted by: lenselijer

the cpld is fully removed, all wires gone.  
   
 I flashed using the -w switch.  
 When i read back the image it's an exact match of the original nand before the rgh hack.

## 2011-12-07 19:55:13, posted by: Coagulate

I would check to make sure none of the small soldering points accidentally got bridged during the process. Also you can try -e16 and rewrite the original nand.

## 2011-12-09 14:23:08, posted by: lenselijer

I have cleaned all soldering points, nothing strange to see.  
   
 Also did the -e16 and then -w16, but still rrod 0022 error.  
   
 Nand image also reads fine in 360 flash tool

## 2011-12-09 19:20:20, posted by: Cancerous1

0022 is a kernel error this is the wrong place to discuss it