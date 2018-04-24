# NandPro +w16 on virtual file not working

## 2012-02-18 04:05:44, posted by: LazyJones

I've done the following (NandPro v3.0a):  
   
 1) Nandpro.exe lpt: +w16 image\_00000000.ecc   
 2) Nandpro.exe lpt: -r16 verify1-lpt.bin 0 50  
 Files differ in SPARE area (that's correct..)  
   
 1) Copy image\_00000000.ecc verify2-virtual.bin  
 2) Nandpro.exe verify2-virtual.bin: +w16 image\_00000000.ecc  
   
 In this (virtual file) attempt image\_00000000.ecc and verify2-virtual.bin do match. The SPARE area hasn't been touched at all and i cannot compare it to my -r16 image (to actually verify my lpt flashing).   
   
 Does +w16 not work on virtual files?

## 2012-08-31 19:49:32, posted by: xb0xguru

Noticed you've not had a reply on this and I know it's old, but...  
   
 Yes, NANDpro WILL work with virtual files but it needs to be a valid NAND dump including a valid header.  
   
 an .ecc file is not a valid NAND image, so won't work. Had you attempted this with a valid dump it would have worked.

## 2012-08-31 19:51:04, posted by: sk1080

At this length the chance of the user coming back and looking is slim

## 2012-09-01 00:17:52, posted by: LazyJones

@sk1080:  
 No problem.. I can read minds.  
   
 @xb0xguru:  
 Thanks for clearing that up.   
 Would be helpful to have that working on partial images as well though.

## 2012-09-17 19:22:49, posted by: xb0xguru

Yes, I know - not the quickest in replying....  
   
 If you wanted to apply to a partial image, just keep a donor image at hand and +w16 the file at block 0. Then dump (-r16) the file out to a .bin file.  
   
 Open both partial and new bin in a Hex editor and paste the .bin file into the partial at address 0x0.

## 2012-09-17 20:05:34, posted by: LazyJones

Will try that next time... thanks. :)