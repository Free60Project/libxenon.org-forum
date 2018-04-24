# How to update XeLL

## 2012-01-24 13:06:17, posted by: tuxuser

Here's a quick HowTo for updating XeLL.  
   
 Requirements:  
   
 * XeLL Reloaded build NEWER THAN 2011-09-23  
 * FAT/FAT32 USB Stick supported by XeLL  
   
 Step 1: Download a recent XeLL Reloaded build  
 Step 2: Rename the matching XeLL-binary to "updxell.bin"   
 - xell-1f.bin for JTAG XeLL-only Image  
 - xell-2f.bin for JTAG *not allowed to talk about in here*-Images  
 - xell-gggggg.bin for Reset Glitch Hack Images  
 Step 3: Copy the updxell.bin file to the root of the FAT/FAT32 USB Stick  
 Step 4: Plug in the USB Stick and boot up XeLL. It should find the update and flash it  
 Step 5: Reboot your Xbox and enjoy the fresh XeLL build  
   
   
 Problems:  
   
 updxell.bin doesnt get found/updxell process doesn't start: You have to rebuild your whole hackimage with a recent XeLL. From there on you can use the easy update feature  
 updxell function reports that no XeLL binary was found in NAND: Either your XeLL in NAND is too old or it's not a XeLL Reloaded binary - You have to rebuild your whole hackimage with a recent XeLL.