# Debugging SIGSEGVs in libXenon (happens when you access an invalid pointer)

## 2011-06-23 21:12:46, posted by: GliGli

So let's say we have that code:  
 [code]* *void crashme(){ int * invalid\_ptr = (int*)42; // 42 is an invalid address :) printf("this line will print\n"); *invalid\_ptr=0xbadf00d; // any value written will crash printf("this line won't\n"); } [/code] Obviously this function will crash because we try to write an invalid address!  
 If you run it, if should print on UART output:  
 [code]* *SIGSEGVne will print PIR=0000000000000000 sr0=0000000080016b5c lr =0000000080016b48 sr1=1000000002003030 DAR=000000000000002a r00=000000000badf00d r01=000000008fffebe0 r02=800000001c00a0c8 r03=ffffffff800b6238 r04=ffffffffffffff80 r05=000000009e300080 r06=0000000000000015 r07=ffffffff800b6220 r08=00000000800c04dd r09=000000000000002a r10=00000000819527a8 r11=000000008fffeab0 r12=0000000024000088 r13=0000000002000000 r14=0000000000000000 r15=0000000000000000 r16=0000000000000000 r17=0000000000000000 r18=0000000000000000 r19=0000000000000000 r20=0000000004000270 r21=0000000000000000 r22=0000000000000000 r23=00000000019524b8 r24=00000000000c5460 r25=00000000000002d8 r26=0000000081952790 r27=000000000d000000 r28=000000000a000000 r29=0000000020000000 r30=0000000007fe0000 r31=0000000000066300 Stack 000000000fffebe0=8fffebf080016b48 000000000fffebe8=07fe000000066300 000000000fffebf0=8ffff00080016ed0 000000000fffebf8=8fffec980000002e 000000000fffec00=8fffec208002429c 000000000fffec08=8014c52080030000 000000000fffec10=0000000000000000 000000000fffec18=8fffec988014c546 000000000fffec20=8fffec908001565c 000000000fffec28=7000000000000000 000000000fffec30=5346585f42527e31 000000000fffec38=2e5a495000000000 000000000fffec40=0000000000000000 000000000fffec48=0000000000000000 000000000fffec50=0000000000000000 000000000fffec58=0000000000000000 000000000fffec60=0400027000000000 000000000fffec68=8002f9b400000004 000000000fffec70=8002f9b000000000 000000000fffec78=8fffedd900000000 000000000fffec80=8014c9508014c50c 000000000fffec88=000000008014c50c 000000000fffec90=8fffedd080016510 000000000fffec98=0046582b42726565 000000000fffeca0=646f6f73202d2033 000000000fffeca8=363066756e2e7a69 000000000fffecb0=7000000000000000 000000000fffecb8=0000000000000000 000000000fffecc0=0000000000000000 000000000fffecc8=0000000000000000 000000000fffecd0=8003e36400000000 000000000fffecd8=0000000000000000 FAIL [/code] One value that is really usefull is on the sr0 line:  
 [code]* *sr0=0000000080016b5c [/code] It's the address where the crash happened, it won't tell you much in hex but there's a little program that comes with the toolchain that can translate that into a line number in your code!  
 It's xenon-addr2line, it can be used that way:  
 [code]# xenon-addr2line -e myapp.elf crash\_address [/code] for our example:  
 [code]* *root@x360dev:/mnt/ppc/mupen64-360# xenon-addr2line -e mupen64-360.elf 0x80016b5c /mnt/ppc/mupen64-360/source/main/main.c:6 [/code] Yup it crashed at line 6 :)  
 Also the lr line tells you the return address of the last function call, you can also use xenon-addr2line on it, it doesn't always work tho.  
   
 Edit: please note that you have to use the real .elf that Makefile outputs, not the .elf32 (you might rename that one to xenon.elf for XeLL, but it won't work with xenon-addr2line).

## 2011-06-23 21:17:09, posted by: Ced2911

Thanks :D

## 2011-06-23 21:22:51, posted by: gomson

thanks a lot for this mate.. :D

## 2011-06-23 22:39:05, posted by: UNIX

Highly useful, many thanks GliGli :)

## 2011-06-23 23:05:41, posted by: tuxuser

Thx GliGli, maybe I can make a sense of some exceptions I cause now :D

## 2011-06-23 23:38:17, posted by: Juvenal

live saver man.  
   
 LIFE.  
   
   
   
   
 SAVER.