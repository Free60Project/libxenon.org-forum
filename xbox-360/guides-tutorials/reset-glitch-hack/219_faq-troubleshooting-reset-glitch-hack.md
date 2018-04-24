# FAQ/Troubleshooting - Reset Glitch Hack

## 2011-10-31 18:02:22, posted by: tuxuser

Some frequently asked Questions about the Reset Glitch Hack:  
   
 **[b][size=120]Programming the CPLD[/size][/b]**  
   
 **[b]Several "unknown Chips" are found by iMPACT:[/b]**  
 Check your solder work, measure through for shorts/bridges. The LPT wire length could be the problem too, try to keep it as short as possible and use thicker wire for GND/3,3V.  
   
 **[b]iMPACT only finds an "unknown chip":[/b]**  
 In this case you should use shorter wires on the LPT connector. You can directly solder the cables to the connector, no need to use a PCB.  
 A constant power supply is required (use thicker wires for GND and 3,3V).  
   
 **[b]iMPACT recognizes the chip (XC2C64A), but is showing an error while programming it:[/b]**  
 This eventually can happen if you tried to program the CPLD too often before (unsuccessfully).  
 In this case, delete the auto save file of iMPACT, which gets created on every start of the application. Notice how the file is called and where it gets saved - Delete the file and the CPLD should get programmed fine.  
 The power supply could be causing this problem aswell. Try to use thicker wires for GND and 3,3V or switch to another power supply (maybe an external one which is providing the needed 3,3V).  
   
   
 **[b][size=120]Soldering the Hardware[/size][/b]**  
   
 **[b]I don't know how to wire my CPLD:[/b]**  
 Look into this thread for a matching diagram: [url=http://libxenon.org/http://libxenon.org//viewtopic.php?t=1]Thread[/url]  
   
 **[b]After soldering in the CPLD I get a ROD 0022:[/b]**  
 This can happen if the wire from CPY\_PLL\_BYPASS is too thick or too thin. Try to use another cable.  
 Another possibly: You flashed the image with a wrong command via nandpro or you didn't flash the Hack-Image yet.  
   
   
 **[b]The point CPU\_RST got damaged while soldering (Slim):[/b]**  
 1. Get somebody, who knows what he does, to do this job  
 2. Near the CPU there's a point R4D4, use this as an alternative.  
   
 [attach=7]  
   
 **[b]The point POST\_OUT1 got damaged while soldering :[/b]**  
 1. Get somebody, who knows what he does, to do this job  
 2. There's the following alternative point:  
   
 FAT  
 [attach=5]  
   
 SLIM  
 [attach=8]  
   
 **[b]The point STBY\_CLK, near the HANA, got damaged while soldering :[/b]**  
 1. Get somebody, who knows what he does, to do this job  
 As an alternative point, you can use the left pad of the right Resistor, next to the original solder point. It's important that the cable goes through to the resistor - If the trace has no connection due to a ripped off solder point, the Xbox won't boot.  
   
 If R4B24 (Resistor) got damaged, you can replace it with a 33 Ohm/36 Ohm 1/4W Resistor.  
   
 For FATs there's another alternative (you have to scratch off the upper layer to get to the metal pad).  
 [attach=1]  
   
 There's another Pad for STBY\_CLK on FATs, it's named FT2R2 and is located on the backside of the motherboard. (The point where the white cable is connected to)  
 [attach=3]  
   
 FAT  
 [attach=9]  
   
 SLIM  
 [attach=10]  
   
 **[b]The console doesn't show any reaction after the soldering (doesn't turn on) :[/b]**  
 The trace/solder point STBY\_CLK could be damaged. Check it and solder again if needed. (It needs connection to the resistor!)  
   
 **[b][size=120]Using the Hack[/size][/b]**  
   
 **[b]Console doesn't show XeLL (only a black screen), no matter how long I wait:[/b]**  
 You should make sure that you can actually hear the Resets (Power supply giving a high pitched sound, Fans slowing down around each 5 seconds)  
   
 -> Check if the .ecc Image was created correctly  
 ---> Does the build.py script contain the valid 1BL Key ? (secret\_1BL)  
 ---> Did you choose the correct CD File? (CD/CDjasper)  
 ---> If you have a bad block in the first 50blocks, did you remap them?  
 ---> Did you flash the .ecc image with Nandpro 2.0e and the command "+w16" or "+w64" (depending on your NAND-Size) ?  
 -------------  
 Does your original dump have bad blocks in the first 0x50 Blocks? Then you have to remap them!  
 -------------  
 If you verified the above steps and it's still not working it could be cause of improper wire-positioning. You have to make sure that your cables (top and bottom) aren't too close to the "inductance coils" (see picture, labeled Ringkerndrosseln). They need at least a distance of ~3cm to them.... on both, top- and backside.   
 [attach=4]  
 -------------  
 If both steps above don't help, there are two other methods to get it to glitch (faster or at all):   
 Make the wire to CPU\_RST exactly 32cm long. (alternatively you can try 50cm aswell).  
 -------------  
 On Jasper boxes you can try to put a 68nF Capacitor across CPU\_PLL\_BYPASS and GND!  
 -------------  
 ! EXPERIMENTAL !  
 Exclusively on FATs you can do another mod to the CPLD wiring. The point on the CPLD which is faced by the black stripe of the diodes, Voltage Input, (not the GND points !) should be connected to the internal voltage regulator of the CPLD, which is outputting 1,8V. To do that, remove the 3x 1N4148 diodes, the 100nF cap and the 1K resistor and connect this pin directly to said 1,8V (Digilent CMOD Pin 5 to 1,8V of voltage regulator). Use a multimeter to find the right point!  
 For further information on this method: [url=http://libxenon.org/http://libxenon.org//viewtopic.php?t=9]Thread[/url]  
   
   
 **[b]Jasper has CB 6751 or 6752 / X360 FAT has CB\_A/CB\_B in NAND:[/b]**  
 If your Jasper has a CB of 6751 you have to provide a donor CB.6750.bin to the build.py script (don't ask for it here, you need to obtain it on your own!).  
 If you have the donor file build the image like this (notice the donor\_CB.bin): [quote]python common\imgbuild\build.py nanddumpname.bin common\cdxell\CD donor\_CB.bin common\xell\xell-gggggg.bin[/quote] If the Jasper has a CB of 6752 it's not compatible with the Glitch Hack atm.  
 If your X360 FAT has a 2-part CB (CB\_A and CB\_B) it's not compatible with the Glitch hack atm.   
   
 **[b]Xell doesn't start, 3 green LEDs are lighting up[/b]**  
 If XeLL doesn't boot but you are seeing 3 green LEDs on the Xbox's ROL you have to recheck the following solder point and eventually solder it again:  
 [attach=2]  
   
 **[b]Replacement parts[/b]**  
 R4D4 = 1,25 kOhm Resistor  
 R7R17 = 10 kOhm Resistor  
 R3B15 (Trinity) = 33 Ohm Resistor  
   
 Translated from german, from [url=http://www.360hacks.de/xbox360\_reset\_glitch\_hack\_probleml\_sungen\_faq.t17889.html]360hacks.de[/url]  
   
 Credits to: Hoax, M tha MaN, Richter77, primo1337, Screamo, Nelix, SynTeX, Marcian, CosSCasH, Icekiller  
   
 To be continued...

### Attachments

[xbox360_STBY_CLK_alt.jpg](xbox360_STBY_CLK_alt.jpg)[3greenerror.png](3greenerror.png)[alternatepoints.jpg](alternatepoints.jpg)[xbox360_MB_Drosseln.jpg](xbox360_MB_Drosseln.jpg)[regfix13.jpeg](regfix13.jpeg)[cpualt.jpg](cpualt.jpg)[postout.jpg](postout.jpg)[stby_clk_phatuwf1i.jpg](stby_clk_phatuwf1i.jpg)[stby_clk_alt_slimcjfo4.jpg](stby_clk_alt_slimcjfo4.jpg)