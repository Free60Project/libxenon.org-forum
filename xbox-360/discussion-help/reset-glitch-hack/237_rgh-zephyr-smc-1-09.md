# RGH Zephyr SMC 1.09

## 2011-12-07 00:56:11, posted by: Coagulate

Hello. I have 2 Zephyrs that will not glitch because the SMC version is 1.09. Does anyone know how I can bypass this? Has anyone glitched a 1.09 SMC yet? Thanks!

## 2011-12-07 16:20:31, posted by: tuxuser

just use a higher SMC version (aka newer zephyr, falcon, jasper whatever). supply it as a donor file to build.py

## 2011-12-07 16:33:46, posted by: Coagulate

Sweet, I didn't know i could use an SMC donor file. Thanks!

## 2011-12-07 16:42:44, posted by: IceKiller

would you mind upping/sharing your smc? :)

## 2011-12-07 17:44:02, posted by: tuxuser

yes, its copyrighted MS code!

## 2011-12-07 19:53:03, posted by: Coagulate

I can't seem to inject a donor SMC since it's a retail .bin. I was reading that it's not possible....

## 2011-12-07 21:42:37, posted by: lprot

[quote="Coagulate"]  
 I can't seem to inject a donor SMC since it's a retail .bin. I was reading that it's not possible....  
 [/quote]  
 Open \common\imgbuild\build.py and change corresponding code to:  
   
 SMC\_patches = [[0xf9c96639,"Trinity, version 3.1",[[0x13b3,0x00,0x00]]],  
 [0x5b3aed00,"Jasper, version 2.3",[[0x12ba,0x00,0x00]]],  
 [0x9ad5b7ee,"Zephyr, version 1.10",[[0x1257,0x00,0x00]]],  
 [0x7e5bc217,"Zephyr, version 1.13",[[0x12a3,0x00,0x00]]],  
 [0x1d0c613e,"Falcon, version 1.6",[[0x12a3,0x00,0x00]]],  
 [0xb74ae419,"Zephyr, version 1.09",[[0x1242,0x00,0x00]]]]  
   
 PS: To find patch offset for any SMC version - search for B40510 bytes in in decrypted unpatched SMC file and decrement it by 3. For SMC 1.09 that is 0x1242. 0xb74ae419 is CRC32 of unpatched decrypted SMC file without first 4 bytes...

## 2011-12-07 22:40:59, posted by: Coagulate

Red ring went away, but still no glitch. I think my CPLD board is trashed.

## 2011-12-10 21:36:48, posted by: Coagulate

It still wont glitch with a full Xecuter Coolrunner board. It has to be the ecc file....