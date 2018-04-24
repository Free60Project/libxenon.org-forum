# Displaying Temperatures

## 2011-03-16 09:02:10, posted by: UNIX

I am trying to add some code into XeLL (From the xell-testing repository) to read the system temperatures and print them to the screen. Here is what I have, added into XeLL's main.c:  
 [code]* *uint16\_t temps; xenon\_smc\_query\_sensors(temps); printf(temps); [/code] When I try to compile I get a build error: [code]* *main.o:(.text+0xe7c): undefined reference to `xenon\_smc\_query\_sensors' collect2: ld returned 1 exit status [/code] When I try to use it by itself, i.e as it's own .elf file to launch with XeLL, there are no build errors, but it still doesn't work. It doesn't print anything. Am I doing something wrong?   
   
 Thanks.

## 2011-03-16 10:57:12, posted by: mojobojo

Make sure you are linking the libxenon library.   
 [code]-lxenon[/code] Reference [url=http://www.libxenon.org/viewtopic.php?f=20&p=36#p36]this[/url] source code for proper linkage, code usage, and elf conversion.

## 2011-03-16 11:40:29, posted by: UNIX

Oh yeah, I am. That was actually my thread that you linked me to, already made that mistake haha. Any other ideas?

## 2011-03-16 15:45:35, posted by: mojobojo

Wow, totally missed that XD. Can you use any other things from the SMC h file, or is it just that function?  
   
 EDIT:  
 Here is some code I quickly hacked together. If I understand what you asked for, this should work for you. It worked on my jasper.  
 [code]* * #include <stdio.h> #include <stdlib.h> #include <input/input.h> #include <xenos/xenos.h> #include <console/console.h> #include <xenon\_smc/xenon\_smc.h> #include <time.h> void mainInit() { //init xenos\_init(VIDEO\_MODE\_AUTO); console\_init(); kmem\_init(); usb\_init(); usb\_do\_poll(); } int main() { uint8\_t buf[16]; float CPU\_TMP = 0, GPU\_TMP = 0, MEM\_TMP = 0, MOBO\_TMP = 0; mainInit(); printf("Testn"); while(1) { memset(buf, 0, 16); buf[0] = 0x07; xenon\_smc\_send\_message(buf); xenon\_smc\_receive\_response(buf); CPU\_TMP = (float)((buf[0 * 2 + 1] | (buf[0 * 2 + 2] << 8)) / 256.0); GPU\_TMP = (float)((buf[1 * 2 + 1] | (buf[1 * 2 + 2] << 8)) / 256.0); MEM\_TMP = (float)((buf[2 * 2 + 1] | (buf[2 * 2 + 2] << 8)) / 256.0); MOBO\_TMP = (float)((buf[3 * 2 + 1] | (buf[3 * 2 + 2] << 8)) / 256.0); printf("CPU = %4.2f°C GPU = %4.2f°C MEM = %4.2f°C Mobo = %4.2f°C", CPU\_TMP, GPU\_TMP, MEM\_TMP, MOBO\_TMP); // printf("%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X", // buf[0], buf[1], buf[2], buf[3], buf[4], buf[5], buf[6], buf[7], buf[8], // buf[9], buf[10], buf[11], buf[12], buf[13], buf[14], buf[15]); printf("r"); } return 0; } [/code]

## 2011-03-17 01:14:34, posted by: UNIX

I have no problem using other functions from the smc header file, just this one! Sorry it took me so long to get back to this, I'll test that code now and let you know if it worked :)  
   
 EDIT: Just compiled and tested, and it ran fine! Only with XeLLous from the nand though, not through XeLL Launch. When I tried to launch it through XeLL Launch is just halted after it said "Please wait a moment".

## 2011-03-18 04:46:25, posted by: Cancerous1

How did you add it into xellous?! or you chainloaded the new xell from xellous? interesting.

## 2011-03-18 05:58:47, posted by: UNIX

[quote="Cancerous1"]How did you add it into xellous?! or you chainloaded the new xell from xellous? interesting.[/quote]  
   
 I didn't add it in to XeLLous, I just loaded the .elf from XeLLous! When I tried to load the .elf via XeLL Launch (booting XeLL Reloaded) it just freezes for some reason... I want to try and add the temperature display into XeLL reloaded, but I am getting build errors.  
   
 EDIT: Spent some time looking at/modifying the XeLL reloaded sources, and I managed to add [url=http://pastebin.com/FHVUSQzR]this[/url] into main.c without build errors (finally! after modifying xenon\_smc.c/xenon\_smc.h) But I have a slight issue. The results of the temperatures still do not print to screen. Any ideas as to why?