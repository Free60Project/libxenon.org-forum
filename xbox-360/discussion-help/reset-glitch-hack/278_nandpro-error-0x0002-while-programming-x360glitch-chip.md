# Nandpro error 0x0002 while programming X360GLITCH chip

## 2012-02-14 19:14:11, posted by: beyond666

Hi all. I have problem while upgrading X360GLITCH firmware.  
 X360GLITCH chip have Falcon firmware but I wish there is Jasper.  
 I followed this guide: [url=http://www.x360glitch.com/upgrade.htm]http://www.x360glitch.com/upgrade.htm[/url]  
   
 Here is my video with nandpro error 0x0002.  
 [youtube]http://www.youtube.com/watch?v=aVlgG9UgSw0&feature=player\_embedded[/youtube]  
   
 ![](http://s14.postimage.org/5r6cj7qw1/DSC06962.jpg)[img]http://s14.postimage.org/5r6cj7qw1/DSC06962.jpg[/img]  
   
 I got error 0x002 in Nandpro. When type this command: nandpro xsvf: jasper.xsvf  
 Of course jasper.xsvf is in Nandpro directory.  
   
 Chip pins HAVE contact when flashing. I even try with R3 and without R3 pin soldering.  
   
 - In device manager, my "X360 Super Nand Flasher " is recognized as "Memory access" under "libUSB-Win32 Devices".  
 - USB cable is long 14 inch (35 cm)  
 - “X360GLITCH chip” have Xilinx xc2c64a chip.  
 - "X360 Super Nand Flasher " work fine because I have read NAND from my xbox.  
   
 Where is problem?

## 2012-02-15 21:04:37, posted by: tuxuser

Solder the connections to be sure....

## 2012-02-16 01:17:56, posted by: beyond666

Solved. Thank you for idea!  
 ![](http://img224.imagevenue.com/aAfkjfp01fo1i-20363/loc963/343573121_11_122_963lo.jpg)[img]http://img224.imagevenue.com/aAfkjfp01fo1i-20363/loc963/343573121\_11\_122\_963lo.jpg[/img]