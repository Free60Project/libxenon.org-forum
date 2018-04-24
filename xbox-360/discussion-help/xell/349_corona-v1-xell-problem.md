# Corona V1 XeLL Problem

## 2012-08-10 04:51:35, posted by: sileandro

I have a problem with XeLL and Corona V1 Board.  
 Here is log of monitor com:  
   
 XeLL - First stage  
 * Attempting to wakeup all CPUs...  
 CPUs online: 01..  
 CPUs online: 3f..  
 * success.  
 * Decompressing stage 2...  
 * Loading ELF file...  
 0x00000000 0x0003ae28, Loading .text...done  
 0x0003ae28 0x000007c0, Loading .elfldr...done  
 0x0003b5e8 0x00006370, Loading .data...done  
 0x00041958 0x00000228, Loading .got2...done  
 0x00041b80 0x0000007c, Loading .sdata...done  
 0x00041c00 0x00009480, Loading .rodata...done  
 0x0004b080 0x000000e4, Loading .eh\_frame\_hdr...done  
 0x0004b164 0x00000584, Loading .eh\_frame...done  
 0x0004b700 0x007982ec, Clearing .bss...done  
 0x007e39ec 0x000000ac, Clearing .sbss...done  
 * GO (entrypoint: 000000000000ab00)  
 Xenos GPU ID=5841  
 unknown SMC bulk msg  
 DVD cover state: 62  
 AVPACK detected: 5c  
 . ana disable  
 . ana enable  
 .................................................. .................................................. .................................................. .................................................. .................................................. .................................................. .................................................. .................................................. .................................................. ................................................  
 after this only dots appear in console.

## 2012-08-10 15:23:21, posted by: sileandro

Can anyone help me with this problem?

## 2012-08-10 21:35:22, posted by: tuxuser

XeLL isnt updated for Corona yet. Be patient please.

## 2012-08-10 21:49:42, posted by: sileandro

It works with all boards corona, less mine. :( :( :( :( :( :( :( :'( :'( :'( :'( :'( :'( :'( :'( :'( :'( :'( :'( :'( :'(  
   
 WHAT happened to the folder corona\_testing that was in the github?  
   
 Can you make a updated ECC for me?

## 2012-08-10 21:52:24, posted by: tuxuser

It got deleted as we are rather trying a proper method to make it work on every videomode. We try to do it asap.

## 2012-08-10 21:57:37, posted by: sileandro

and when will be released to us?  
   
 seems that my corona is the first to have this problem.

## 2012-08-14 03:32:30, posted by: CoDeFl@sher

[quote="sileandro"]  
 and when will be released to us?  
   
 seems that my corona is the first to have this problem.  
 [/quote]  
   
 Calm down sileandro :),XeLL on Corona still work in progress and will be released when ready/finished.

## 2012-08-22 06:04:15, posted by: tuxuser

sendspace.com/file/xz2nqq  
   
 No video output still, boot process continues though

## 2012-08-22 15:07:02, posted by: sileandro

[quote="tuxuser"]  
 sendspace.com/file/xz2nqq  
   
 No video output still, boot process continues though  
 [/quote]  
 Work fine now! Thank You!!!

## 2012-12-15 17:49:18, posted by: taik03

hi   
   
 i have the same problem with a corona v2 4gb unit i tried the recompiled xell and it gave me a red dot? is there any version that works for the corona 4gb v2 mobo ?   
   
 thanks   
   
 this is what i got from the comport monitor   
   
 XeLL - First stage  
 * Attempting to wakeup all CPUs...  
 CPUs online: 01..  
 CPUs online: 3f..  
 * success.  
 * Decompressing stage 2...  
 * Loading ELF file...  
 0x00000000 0x0003ae28, Loading .text...done  
 0x0003ae28 0x000007c0, Loading .elfldr...done  
 0x0003b5e8 0x00006370, Loading .data...done  
 0x00041958 0x00000228, Loading .got2...done  
 0x00041b80 0x0000007c, Loading .sdata...done  
 0x00041c00 0x00009480, Loading .rodata...done  
 0x0004b080 0x000000e4, Loading .eh\_frame\_hdr...done  
 0x0004b164 0x00000584, Loading .eh\_frame...done  
 0x0004b700 0x007982ec, Clearing .bss...done  
 0x007e39ec 0x000000ac, Clearing .sbss...done  
 * GO (entrypoint: 000000000000ab00)  
 Xenos GPU ID=5841  
 ! SFCX: Unsupported Type A-0  
 ! config: sfcx not initialized  
 unknown SMC bulk msg  
 DVD cover state: 62  
 AVPACK detected: 5c  
 . ana disable  
 . ana enable  
 ...............................................................

## 2012-12-18 22:26:16, posted by: sileandro

use the xell-gggggg.bin posted by tuxuser.

## 2012-12-22 09:29:25, posted by: taik03

hey thanks for the reply sileandro, will this also work for the 4gb corona v2 ? i tried it the last time and it gave me a red dot when cr stop blinking. anyway il try it again

## 2012-12-22 11:10:11, posted by: taik03

well i tried it again still nothing cr stops blinking but router doesn't get an ip so im guessing it still stuck in a loop. :(  
   
 by the way i tried the alternate xell in a 250gb v1 corona with the same problem, and it did give me a key. so i guess there is something different with a 4gb v2

## 2012-12-29 14:38:38, posted by: xb0xguru

When you say a V2, are you meaning a BB NAND? If so, you need to write the .bin file without ECC data.

## 2013-01-03 00:24:22, posted by: taik03

[quote="xb0xguru"]  
 When you say a V2, are you meaning a BB NAND? If so, you need to write the .bin file without ECC data.  
 [/quote]  
   
 yes its a bb 4gb nand. what you mean write the .bin file with out ecc data ? how does that work ? i don't have the cpu key yet

## 2013-01-11 02:04:48, posted by: xb0xguru

Did you get this working?  
   
 How are you creating the ECC?

## 2013-01-13 08:50:54, posted by: taik03

created the .ecc using jrunner. and no wasn't able to get this working using this method. the alt xell by tuxer doesn't work with the 4gb model

## 2013-01-24 16:35:34, posted by: sileandro

Use autogg to generate the ecc. Now you can select the alternative xell-gggggggg.bin in the program.