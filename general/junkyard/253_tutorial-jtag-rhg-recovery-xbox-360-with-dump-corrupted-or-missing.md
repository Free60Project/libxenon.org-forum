# [TUTORIAL JTAG/RHG] Recovery Xbox 360 with dump corrupted or missing

## 2011-12-28 11:38:04, posted by: AddyMc

THANKS FOR "MARCHISIO80" IN THE FORUM WWW.CONSOLEOPEN.COM  
   
 WARNING!  
 Tests and procedures performed on the forum www.consoleopen.com  
 FORBIDDEN "copying "..........  
   
 WARNING!  
 Do not do this without asking first aid, most likely you do not need this procedure, I HIGHLY recommend .................  
   
 BACKGROUND  
   
 Well that if we specify a dump has its functioning should use that to create the *** ............ and of course the JTAG and / or RGH must be installed and running.  
   
 I speak of a dump that has no operating or has corrupted dump  
   
 Example  
 But still not hackable console hack with fried nand  
 We only console kv  
 With the dump etc.  
 Console locked during an update  
 Reading the wrong nand  
 Console banned  
 False readings from nandpro  
 Nand original riflashata of red LEDs (even though all dump match)  
   
 Console to create the *** hackable, if you do not have a working nand dump, just a nand a console hardware revision of our own.  
   
 My procedure and 'applicable to all existing hackable console at the moment ...........  
   
 JTAG  
 RGH FAT  
 RGH SLIM  
   
 All TESTED  
   
 How I came to this  
 Xella cpukey .... gives a wrong!? someone enlighten me:)  
 Small discovery jtag  
   
   
 THE VIRTUAL CPUKEY Displaying XELLA-RELOADED AND 'THE CPUKEY used to create the ***  
   
   
 TO CREATE WITH THE *** MULTIBUILDER Follow this guide to the kind of hack  
   
 [JTAG TUTORIAL] Installing kernel *** 14699 and dashlaunch 2.27  
 [RGH TUTORIAL] Installing kernel *** 14699 and dashlaunch 2.27  
   
 from the point CREATION OF ***.Appena *** created back in the procedure (I recommend).  
   
   
 PROBLEM BAD BLOCK  
   
 [WARNING] In case of bad blocks to stop and ask for help.  
 Of course it would be preferable to use a dump with no bad blocks, and hope to have a NAND bad blocks without ......  
   
 I always use nandpro if ***causa when not part of the bad block, I make a new reading and writing, the more I repeat 'Sometimes, if I understand where you fit errors are bad blocks.  
 Remaps the bad blocks by hand using the following guide  
   
 [RGH / JTAG] Miniguide remappare to manually badblock  
   
   
   
 GETTING STARTED  
   
   
   
 FIRST TRY TO SEE IF AT LEAST OUR K. It 'VALID  
   
 EXAMPLE  
 Reading the wrong nand  
 Dump the original riflashato by red LEDs  
 With the dump ecc.  
 Console locked during an update  
 Console banned  
   
   
 [color=red][size=140]**[b]- Process starts by dump console *** donor (no cpukey required):[/b]**[/size][/color]  
   
   
 Procuriamoci *** nand dump of the console hardware revision of our own, rename it and save the folder NANDDONATRICE.BIN nandpro  
 Rename our backup nand and put this folder in the MIODUMP.BIN nandpro.  
   
   
 We extract from our dump the kv  
   
   
 We enter from the command prompt in the directory and give nandpro the following command to extract our kv.bin  
   
 nandpro MYDUMP.BIN: kv.bin-r16 1 1  
   
 Now we give the following command to inject the donor dump in our kv.bin  
 nandpro NANDDONOR.BIN: kv.bin-W16 1 1  
   
   
 Now our new image flashamo  
 nandpro usb: W16-NANDDONOR.BIN  
   
 Xella we start using the eject button.  
 Xella will give us' 3 values ??that we have to mark them  
   
 CPUKEY and that 'the cpukey our console  
 VIRTUAL CPUKEY which 'cpukey of the console that gave us the NAND ***  
 We mark the value of 07 fuseset  
   
   
   
 Open NANDDONOR.BIN, if the values ??of kv match our console means that our most likely kv and 'good.  
   
   
 Open 360 Flash tools, settings, key, we insert our cpukey and give it the name and click on add MYCPUKEY cpukey  
 Let's make the procedure with the virtualcpukey and give it its name and click on add to VIRTUALCPUKEY cpukey  
   
   
   
 We select patch, patches, headers, and increase the value more LDV 'to match the top 07 viewed from Xella fuseset +1.  
 We select also use cpukey rebuild image and insert our MYCPUKEY and click OK  
   
   
 Now we ask 360 flash tool 'to use the name and destination.  
 Call it MY***WORKING.BIN and choose to save it in the nandpro.  
   
   
 From nandpro give the command  
 nandpro usb: W16-MY***WORKING.BIN  
 Done.  
 From now on, we need to update the *** give "meal" and the multibuilder MY***WORKING.BIN MYCPUKEY  
   
   
 [color=red][size=140]**[b]- ORIGINAL PROCEEDINGS starting dump from the console with its donor cpukey:[/b]**[/size][/color]  
   
   
 Procuriamoci ORIGINAL nand dump of a console of the same hardware revision of our  
 NANDDONOR.BIN copy it and rename it in the folder nandpro  
 Rename the backup of our xbox in MYDUMP.BIN  
   
 We extract from our dump the kv  
   
 We enter from the command prompt in the directory and give nandpro the following command to extract our kv.bin  
 nandpro MYDUMP.BIN: kv.bin-r16 1 1  
   
 Now we give the following command to inject the donor dump in our kv.bin  
 nandpro NANDDONOR.BIN: kv.bin-W16 1 1  
   
   
 Now our new image flashamo  
 nandpro usb: W16-NANDDONOR.BIN  
   
 Create the etc as a guide here on the forum using NANDDONOR.BIN etc. and save the generated folder of nandpro.  
 Rename etc in the IMAGE\_ECCDONOR.BIN  
   
 From nandpro give the command  
 Nandpro USB + W16 IMAGE\_ECCDONOR.BIN  
   
 Xella we start using the eject button.  
 Xella will give us' 3 values ??that we have to mark them  
   
 CPUKEY and that 'the cpukey our console  
 VIRTUAL CPUKEY  
 We mark the value of 07 fuseset  
   
   
 Open 360 Flash tools, settings, key, we insert our cpukey and give it the name and click on add MYCPUKEY cpukey  
 Let's make the procedure with the virtualcpukey and give it its name and click on add to VIRTUALCPUKEY cpukey  
   
 Open NANDDONATRICE.BIN, if the values ??of kv match our console means that our kv almost certainly was good.  
   
 We create the image *** using the guide here on the forum giving in "meal" and MY***WORKING.BIN MYCPUKEY  
 Rename the image created by multibuilder in ***WORKING.BIN  
   
 We open with 360 flash tool ***WORKING.BIN  
 We select patch, patches, headers, and increase the value more LDV 'to match the top 07 viewed from Xella fuseset +1.  
 We select also use cpukey rebuild image and insert our MYCPUKEY and click OK  
   
 Now we ask 360 flash tool 'to use the name and destination.  
 Call it ***WORKING.BIN and choose to save it in the nandpro.  
   
 Flashamo nandpro by using the command  
 nandpro usb: W16-***WORKING.BIN  
   
 Done.  
 From now on, we need to update the *** give "meal" and ***WORKING.BIN MYCPUKEY  
   
   
 [color=red][size=140]**[b]- KV IF NOT 'INVALID ............ TRY TO RECOVER THE SAME The XBOX[/b]**[/size][/color]  
   
 The reader will of course not light 'most' games ....... to remedy the problem just flash the player with the present in our dvdkey nand donor ................. ........  
   
 or   
   
 try opening our *** with 360 flash tools, patches, patches keyvault, we insert our dvdkey, select rebuild image, and in our cpukey cpukey insert and click on ok.  
   
 Now 360 flash tool will ask 'name, we put MY***WITHMYDVDKEY.BIN and choose to save it in the nandpro  
   
   
 From nandpro give the command  
 nandpro usb: W16-MY***WITHMYDVDKEY.BIN  
   
 Done.  
 From now on, we give in to update the *** "meal" and MY***WITHMYDVDKEY.BIN MYCPUKEY  
   
 [color=red][size=140]**[b]- PROCESS FOR THOSE WHO DO NOT 'IN YOUR POSSESSION OF VALID KV[/b]**[/size][/color]  
   
 EXAMPLE  
 Nand fried before or during the reading nandpro  
 Reading the wrong nand  
 Other serious problems nand  
   
   
   
 Process starts by dump from console *** donor (no cpukey required):  
   
   
   
 Procuriamoci *** nand dump of a console of the same hardware revision of our  
 Rename it and put this in the folder NANDDONATRICE.BIN nandpro.  
   
 Now our image flashamo  
 nandpro usb: W16-NANDDONOR.BIN  
   
 Xella we start using the eject button.  
 Xella will give us' 3 values ??that we have to mark them  
   
 CPUKEY and that 'the cpukey our console  
 VIRTUAL CPUKEY which 'cpukey of the console that gave us the NAND ***  
 We mark the value of 07 fuseset  
   
   
 Open 360 Flash tools, settings, key, we insert our cpukey and give it the name MYCPUKEY and click on add cpukey  
 Let's make the procedure with the virtualcpukey and give it its name VIRTUALCPUKEY and click on add cpukey  
   
   
 Open NANDDONOR.BIN, if the values ??of kv match our console means that our kv was good.  
   
   
 We select patch, patches, headers, and increase the value more LDV 'to match the top 07 viewed from Xella fuseset +1.  
 We select also use cpukey rebuild image and insert our MYCPUKEY and click OK  
   
 Now we ask 360 flash tool 'to use the name and destination.  
 Call it MY***WORKING.BIN and choose to save it in the nandpro.  
   
   
 From nandpro give the command  
 nandpro usb: W16-MY***WORKING.BIN  
 Done.  
 From now on, we need to update the *** give "meal" and MY***WORKING.BIN MYCPUKEY  
   
   
 [color=red][size=140]**[b]- ORIGINAL PROCEEDINGS starting dump from the console with its donor cpukey[/b]**[/size][/color]  
   
   
 Procuriamoci ORIGINAL nand dump of a console of the same hardware revision of our and his cpukey  
 Rename the NANDDONOR.BIN  
 Create the following *** guidain the following depending on the type of hack  
   
 NANDDONOR.BIN using as our dump and its cpukey.  
 Just continue the process created the ***  
   
 Rename the image created in multibuilder NANDDONOR.BIN and save it in the folder nandpro  
 Now flashamo NANDDONOR.BIN  
 nandpro usb: W16-NANDDONOR.BIN  
   
   
 Xella we start using the eject button.  
 Xella will give us' 3 values ??that we have to mark them  
   
 CPUKEY and that 'the cpukey our console  
 VIRTUAL CPUKEY which 'cpukey of the console that gave us the original nand  
 WE mark the value of 07 fuseset  
   
   
 Open 360 Flash tools, settings, key, we insert our cpukey and give it the name MYCPUKEY and click on add cpukey  
 Let's make the procedure with the virtualcpukey and give it its name and VIRTUALCPUKEY click on add cpukey  
   
 We select patch, patches, headers, and increase the value more LDV 'to match the top 07 viewed from Xella fuseset +1.  
 We select also use cpukey rebuild image and insert our MYCPUKEY and click OK  
   
 Now we ask 360 flash tool 'to use the name and destination.  
 Call it MY***WORKING.BIN and choose to save it in the nandpro.  
   
   
 From nandpro give the command  
 nandpro usb: W16-MY***WORKING.BIN  
 Done.  
 From now on, we need to update the *** give "meal" and MY***WORKING.BIN MYCPUKEY

## 2011-12-29 00:40:40, posted by: greator

First of all,   
 does your grammar really that bad or you use google translate and copy it from somewhere else?  
   
 And what are those **** and .....?

## 2011-12-29 00:48:11, posted by: tuxuser

This is stuff which isnt allowed to be talked about in this forum so it gets censored automaticly.  
   
 And with that, even if I appreciate your effort to provide helpful tutorials.  
   
 1. These fr**b**t and other reb**ter stuff isnt allowed here!  
 2. Those methods do not even work all... and are not useful for our XeLL Image purposes  
   
 ~MOVED + CLOSED~