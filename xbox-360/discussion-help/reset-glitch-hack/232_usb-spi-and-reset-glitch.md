# USB Spi and Reset Glitch

## 2011-11-24 19:28:48, posted by: Colorado880

Do I need to update my USB SPI to a new hex in order to do the reset glitch? I see some of the new Nand flashers are on v3 and my USB Spi only works with Nand Pro 2  
   
 Thanks

## 2011-11-24 22:12:08, posted by: tuxuser

To flash your NANND there's no need to update your USB SPI Programmer... but If you want to flash your CPLD Chip with it (only possible with ARM based Programmers,not available for PIC bases ones) you need to update the HEX aswell. Make sure to use NANDPro 2.0 if you dont have the HEXv3!

## 2011-11-24 22:25:29, posted by: Colorado880

Thanks, got my falcon working now!

## 2011-12-08 17:42:58, posted by: MaysaM

hi  
 i build a nand flasher with pic 4550 .  
 its working good.  
 i can read and write nand without problem.also i did jtag in fat360 in dashboard 7371 without any problem.  
 but when i want use to glitch hack a problem founded.  
 when type in nand pro this :  
   
 nandpro usb: +w16 image\_00000000.ecc  
   
 a message appear in this pic:  
   
 ![](http://i44.tinypic.com/xggaf.png)[img]http://i44.tinypic.com/xggaf.png[/img]  
   
   
 whats problem??