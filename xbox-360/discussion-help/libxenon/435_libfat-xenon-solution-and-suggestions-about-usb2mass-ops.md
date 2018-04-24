# [libfat-xenon] Solution and suggestions about &quot;usb2mass_ops&quot;

## 2013-12-31 00:47:40, posted by: SonicKiller

Hi all,  
   
 I recently ran into some compilation problems when building applications which rely on libfat-xenon.  
 Every time I had this error: [code]...undefined reference to `usb2mass\_ops'[/code] To all of you who with the same problem, please be aware that this variable is no more.  
   
 It has been replaced by three variables, one for each USB port, by the following commit :  
 [url=https://github.com/LibXenonProject/fat-xenon/commit/06e5454ad445a73c62de546fa7a2bdb317d9b0d9#diff-8e930348e4f25111952cd417b349b49c]https://github.com/LibXenonProject/fat-xenon/commit/06e5454ad445a73c62de546fa7a2bdb317d9b0d9#diff-8e930348e4f25111952cd417b349b49c[/url]  
 The new variables are : [code]usb2mass\_ops\_0 for uda:/ usb2mass\_ops\_1 for udb:/ usb2mass\_ops\_2 for udc:/ [/code] For information, getter functions linked to usb2mass\_ops have changed also. Check fat-xenon sources for more info.   
   
 May I suggest the contributors to keep the variable " usb2mass\_ops" and make it point on the same address as "usb2mass\_ops\_0" so that we can still support legacy code ?  
   
 If that's not in the future plans, at least let me know so that we can fork the fat-xenon repo, do the work and give it to people who still want to build old apps without modifying their code. For example, latest code of NullDC-360 isn't buildable anymore because of that modification.  
   
 If I'm wrong about anything, forgive me and tell me what's not right please.  
   
 Thanks.  
   
 PS : I know that's a 5 months old commit but I've been stucked for the last 3 days thinking that my code was wrong and couldn't find the info anywhere until I took a look at the libfat sources, so I think this topic could help some people who are in the same situation. ;)

## 2013-12-31 18:48:28, posted by: tuxuser

Hey,  
   
 How about specifying:  
 [code]* *#define usb2mass\_ops usb2mass\_ops\_0 [/code] .at the top of the sourcefile from your individiual homebrew application? Does that compile and run fine? Please report so I can commit a legacy fixup.  
   
 Greetz

## 2013-12-31 21:54:37, posted by: SonicKiller

Actually that's what I did yesterday as a workaround. ;)  
   
 I can confirm that it is working right.  
 (confirmed with my code and from a fresh checkout of NullDC-360)  
   
 Thanks really much for the quick follow up !  
   
 Edit: I forget to mention that an alias should also be created for the function "get\_io\_usbstorage\_0()" which should be called when we call "get\_io\_usbstorage()" in old code. That's all I remarked at my level, I hope to not forget something else on the libfat.

## 2014-01-01 19:38:37, posted by: tuxuser

Updated the repo.. this change already links to the new function call "get\_io\_usbstorage\_0".. so that should be fine..