# CPU Register values (namely PIR)

## 2013-11-27 20:53:56, posted by: SoullessSentinel

I've recently started development on an Xbox 360 emulator using my (limited) knowledge of PowerPC and a large collection of CPU documentation from IBM's website.  
   
 I've got as far as emulating enough op codes for 1BL to start running, however, my JTAG Xenon (which I was using to perform tests) has finally broke down.  
   
 1BL is currently stopping execution with a post code of 0x93, which according to the Free60 wiki, means that the code is being executed on the wrong CPU core.   
   
 Can anybody with access to an Xbox 360 that currently works please dump the PIR register of each hardware thread so that I can program the correct initial values into my Xenon emulator core. I'd do it myself if I still had the hardware.