# xell problem in the corona v2

## 2012-12-27 00:43:37, posted by: marcelo

Good night got an error on my xbox 360 on my MONITOR WITH the error so  
 I've tried the alternative ECC failed .......  
   
   
 XeLL - First stage  
 * Attempting to wakeup all CPUs...  
 CPUs online: 01..  
 CPUs online: 3f..  
 * success.  
 * Decompressing stage 2...  
 * Loading ELF file...  
 0x00000000 0x00060ac0, Loading .text...done  
 0x00060ac0 0x00000814, Loading .elfldr...done  
 0x000612d8 0x00005cac, Loading .data...done  
 0x00066f84 0x00000290, Loading .got2...done  
 0x00067218 0x00000060, Loading .sdata...done  
 0x00067278 0x00009c58, Loading .rodata...done  
 0x00070ed0 0x000000e4, Loading .eh\_frame\_hdr...done  
 0x00070fb4 0x00000584, Loading .eh\_frame...done  
 0x00071600 0x00699578, Clearing .bss...done  
 0x0070ab78 0x000000b4, Clearing .sbss...done  
 * GO (entrypoint: 0000000000008900)  
 Xenos GPU ID=5841  
 ! SFCX: Unsupported Type A-0  
 ! config: sfcx not initialized  
 unknown SMC bulk msg  
 DVD cover state: 62  
 AVPACK detected: 5c  
 xenon\_smc\_i2c\_ddc\_lock failed, err=1  
 xenon\_smc\_i2c\_write failed, addr=01ec, err=1  
 xenon\_smc\_i2c\_ddc\_lock failed, err=1  
 . ana disable  
 . ana enable

## 2012-12-28 04:11:58, posted by: taik03

i have similar problem as well. been looking for a solution but seems like nobody knows corona v2 4gb

## 2012-12-28 16:20:29, posted by: marcelo

managed to solve in my case here had 3 cables connecting the ..... 1 cable network, 2cabo hdmi, 3 monitor called the 3 cables ai could climb the xell

## 2012-12-28 17:00:00, posted by: barnhilltrckn

The corona boards are still a work in progress in terms of xell. The guys here are working on it and until then we are just going to have to wait. Thats why I have a trinity. I have a slim but still have xell :p

## 2012-12-29 14:37:11, posted by: xb0xguru

[quote="marcelo"]  
 Good night got an error on my xbox 360 on my MONITOR WITH the error so  
 I've tried the alternative ECC failed .......  
   
   
 XeLL - First stage  
 * Attempting to wakeup all CPUs...  
 CPUs online: 01..  
 CPUs online: 3f..  
 * success.  
 * Decompressing stage 2...  
 * Loading ELF file...  
 0x00000000 0x00060ac0, Loading .text...done  
 0x00060ac0 0x00000814, Loading .elfldr...done  
 0x000612d8 0x00005cac, Loading .data...done  
 0x00066f84 0x00000290, Loading .got2...done  
 0x00067218 0x00000060, Loading .sdata...done  
 0x00067278 0x00009c58, Loading .rodata...done  
 0x00070ed0 0x000000e4, Loading .eh\_frame\_hdr...done  
 0x00070fb4 0x00000584, Loading .eh\_frame...done  
 0x00071600 0x00699578, Clearing .bss...done  
 0x0070ab78 0x000000b4, Clearing .sbss...done  
 * GO (entrypoint: 0000000000008900)  
 Xenos GPU ID=5841  
 ! SFCX: Unsupported Type A-0  
 ! config: sfcx not initialized  
 unknown SMC bulk msg  
 DVD cover state: 62  
 AVPACK detected: 5c  
 xenon\_smc\_i2c\_ddc\_lock failed, err=1  
 xenon\_smc\_i2c\_write failed, addr=01ec, err=1  
 xenon\_smc\_i2c\_ddc\_lock failed, err=1  
 . ana disable  
 . ana enable  
 [/quote]  
   
 Is this where the log stops, or do you get '..............................' continuously after this? If so, you need the tuxuser release of xell.