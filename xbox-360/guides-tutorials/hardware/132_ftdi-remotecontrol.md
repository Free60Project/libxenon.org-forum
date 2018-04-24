# FTDI RemoteControl

## 2011-07-31 05:21:28, posted by: tuxuser

[code]* */* bitbang\_cbus.c Example to use CBUS bitbang mode of newer chipsets. You must enable CBUS bitbang mode in the EEPROM first. Thanks to Steve Brown <sbrown@ewol.com> for the the information how to do it. This program is distributed under the GPL, version 2 ############################################################################## /!\ IMPORTANT: FTDI needs to be run in 3,3V selfpowered-Mode /!\ Enable I/O Mode for CB0/CB1 in FTDI's EEPROM with FT\_PROG Connecting Xbox360: Xbox Connection FTDI J2B1.1 ----------- TXD J2B1.2 ----------- RXD J2B1.5 --100 Ohm-- CB0 J2B1.11 --100 Ohm-- CB1 GND ----------- GND /!\ USE THE HARDWARE AND THIS TOOL ON YOUR OWN RISK /!\ ############################################################################## */ #include <stdio.h> #include <unistd.h> #include <stdlib.h> #include <ftdi.h> #define CB0Hi 0xF1 #define CB1Hi 0xF2 #define CB2Hi 0xF4 #define CB3Hi 0xF8 #define CBxLo 0xF0 #define CBxHi 0xFF struct ftdi\_context ftdic; int delay = 120000; int shutdown(void) { printf("Shutting down...\n"); ftdi\_set\_bitmode(&ftdic, CBxLo, BITMODE\_CBUS); return 0; } int poweron(void) { printf("Powering on...\n"); ftdi\_set\_bitmode(&ftdic, CBxLo, BITMODE\_CBUS); usleep(delay); ftdi\_set\_bitmode(&ftdic, CB1Hi, BITMODE\_CBUS); return 0; } int eject(void) { printf("I am not workin for now...\n"); ftdi\_set\_bitmode(&ftdic, CBxLo, BITMODE\_CBUS); return 0; } int main(void) { int f; unsigned char input[10]; if (ftdi\_init(&ftdic) < 0) { fprintf(stderr, "ftdi\_init failed\n"); return EXIT\_FAILURE; } f = ftdi\_usb\_open(&ftdic, 0x0403, 0x6001); if (f < 0 && f != -5) { fprintf(stderr, "unable to open ftdi device: %d (%s)\n", f, ftdi\_get\_error\_string(&ftdic)); exit(-1); } printf("* Xbox360 FTDI RemoteControl *\n------------------------------\n\n"); printf("Connected to FTDI successfully!\n"); printf("Valid commands are: (p)oweron, (s)hutdown, (e)ject and (q)uit!\n"); while (1) { fgets(input, sizeof(input) - 1, stdin); if (input[0] == 'q') break; switch (input[0]) { case 'p': f = poweron(); sleep(1); ftdi\_disable\_bitbang(&ftdic); break; case 's': f = shutdown(); sleep(1); ftdi\_disable\_bitbang(&ftdic); break; case 'e': f = eject(); ftdi\_disable\_bitbang(&ftdic); break; } if (f < 0) { fprintf(stderr, "set\_bitmode failed, error %d (%s)\n", f, ftdi\_get\_error\_string(&ftdic)); exit(-1); } } ftdi\_usb\_close(&ftdic); ftdi\_deinit(&ftdic); } [/code]

## 2011-07-31 07:47:55, posted by: UNIX

VERY interesting. I will most definitely be trying this out soon ;)

## 2011-07-31 22:57:25, posted by: Cancerous1

;D awesome lets get eject working too ;D

## 2012-08-10 15:10:15, posted by: squirtadmin

Hi Guys,  
   
 we are team squirt, like you know our programmer is made with an FTDI FT2232HQ.  
 http://www.360squirt.com/images/slave\_jtag.jpg   
   
 The small programmer is so complete OPEN, we posted schematics and also the whole source code (GPL license) of the work done on squirter.exe programmer here:  
 http://forum.dayton360mods.com/showthread.php?260-Squirter-exe-source-code-open-gpl  
   
 Like you can see from schematics our board has only 3.3V I/O, we can provide a nice board (ex TIME ATTACK INFECTUS) that do translation from 1.8V to 3.3V (so good for Post bus reading by FTDI)   
 http://www.hardstore.com/files/RSMTRADE\_Files/Foto/9549\_22481.JPG  
   
 For who is interested 100% for free we can provide ONE FTDI SQUIRT programmer and ONE "TIME ATTACK PCB".  
   
 The ideas are:  
   
 - POST BUS analyzer: good for RGH tuning  
 - Good the idea of this thread   
   
 Contact me by email pls.  
 SQUIRT ADMIN