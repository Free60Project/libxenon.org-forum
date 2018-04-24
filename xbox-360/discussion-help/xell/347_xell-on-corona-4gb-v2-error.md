# Xell on corona 4gb v2 error 

## 2012-08-09 05:39:56, posted by: orkid1818

XeLL - First stage  
 * Attempting to wakeup all CPUs...  
 CPUs online: 03..  
 CPUs online: 3f..  
 * success.  
 * Decompressing stage 2...  
 * Loading ELF file...  
 0x00000000 0x00035900, Loading .text...done  
 0x00035900 0x000005cc, Loading .elfldr...done  
 0x00035ed0 0x000064f8, Loading .data...done  
 0x0003c3c8 0x00000214, Loading .got2...done  
 0x0003c5e0 0x0000006c, Loading .sdata...done  
 0x0003c650 0x00008a38, Loading .rodata...done  
 0x00045088 0x0000002c, Loading .eh\_frame\_hdr...done  
 0x000450b4 0x0000011c, Loading .eh\_frame...done  
 0x000451e0 0x00722d04, Clearing .bss...done  
 0x00767ee4 0x00000084, Clearing .sbss...done  
 * GO (entrypoint: 0000000000009800)  
 Xenos GPU ID=5841  
 ! SFCX: Unsupported Type A-0  
 ! config: sfcx not initialized  
 unknown SMC bulk msg  
 DVD cover state: 62  
 AVPACK detected: 5c  
 . ana disable  
 . ana enable  
 .................................................. ................................. . f1  
 . f2  
 * Xenos FB with 74x27 (640x480) at 0x9e000000 initialized.  
   
 XeLL - Xenon linux loader second stage 0.99-git- 2011-09-23 (root@x360dev i686)  
 *  
 ! SFCX: Unsupported Type A-0  
 ! sfcx initialization failure  
 ! nand related features will not be available  
 ! SFCX: Unsupported Type A-0  
 ! config: sfcx not initialized  
 * network init  
 * initializing lwip 1.4.0...  
 Reinit PHY...  
 Waiting for link...link still down.  
 * requesting dhcp.................................failed  
 * now assigning a static ip  
 * starting httpd server...success  
 * usb init  
 * Initialising USB EHCI...  
 Initialising EHCI bus 0 at 0xea003000  
 Initialising EHCI bus 1 at 0xea005000  
 EHCI bus 1 port 1: low speed, releasing to OHCI  
 * Initialising USB OHCI...  
 USB bus 0 device 1: vendor 0000 product 0000 class 09: USB Hub  
 USB bus 1 device 1: vendor 0000 product 0000 class 09: USB Hub  
 USB: New device connected to bus 1 hub 1 port 1  
   
 Cannot show DVD key.....  
   
 can someone help me to fix ?

## 2012-08-09 06:00:31, posted by: sk1080

How bout build a RECENT xell and disable the stuff that doesn't work

## 2012-08-09 09:15:13, posted by: orkid1818

[quote="sk1080"]  
 How bout build a RECENT xell and disable the stuff that doesn't work  
 [/quote]  
   
 How to disable the stuff ? KV read error also ....

## 2012-08-09 09:16:39, posted by: sk1080

comment out things that don't work  
 dvd key errors because kv read errors because sfcx(nand) doesn't work

## 2012-08-09 09:18:16, posted by: orkid1818

! SFCX: Unsupported Type A-0  
 ! config: sfcx not initialized  
 unknown SMC bulk msg  
 DVD cover state: 62  
 AVPACK detected: 5c  
 . ana disable  
 . ana enable  
 ..................................  
   
 i think this is the problem ....

## 2012-08-09 09:19:58, posted by: orkid1818

[quote="sk1080"]  
 comment out things that don't work  
 dvd key errors because kv read errors because sfcx(nand) doesn't work  
 [/quote]  
   
 Have to fix this sfcx ... 4g use eMMC nand .

## 2012-08-09 09:20:46, posted by: sk1080

afaik, corona 4gb nand stuff was never figured out...

## 2012-08-09 09:38:17, posted by: orkid1818

[quote="sk1080"]  
 afaik, corona 4gb nand stuff was never figured out...  
 [/quote]  
   
 You about build.by edit ? 4gb nand data no need set bad block area .

## 2012-08-09 09:41:30, posted by: sk1080

Try adding the nand type then......

## 2012-08-09 09:46:27, posted by: orkid1818

[quote="sk1080"]  
 Try adding the nand type then......  
 [/quote]  
   
 I am new ..dont know how to do . hardware i have done booting Xell.

## 2012-08-09 09:49:27, posted by: sk1080

Basically I am saying:  
 Since corona 4gb(and corona at that) are not officially supported at this time, and we do not have anyone activly working on them(very few of us have a 4gb), you either wait for us to officially support them, compile the toolchain and make a reduced xell build, or fix it yourself.

## 2012-08-09 09:54:58, posted by: orkid1818

[quote="sk1080"]  
 Basically I am saying:  
 Since corona 4gb(and corona at that) are not officially supported at this time, and we do not have anyone activly working on them(very few of us have a 4gb), you either wait for us to officially support them, compile the toolchain and make a reduced xell build, or fix it yourself.  
 [/quote]  
   
 Ok Thank

## 2012-08-09 12:07:06, posted by: tuxuser

[quote="orkid1818"]  
 You about build.by edit ? 4gb nand data no need set bad block area .  
 [/quote]  
   
 You added Corona 4GB support by editing build.py? Could you explain a little more how you got your console glitched? How did you dump the NAND.. how was the Image created.. etc?

## 2012-08-10 06:36:18, posted by: orkid1818

XeLL - First stage  
 * Attempting to wakeup all CPUs...  
 CPUs online: 03..  
 CPUs online: 3f..  
 * success.  
 * Decompressing stage 2...  
 * Loading ELF file...  
 0x00000000 0x00035900, Loading .text...done  
 0x00035900 0x000005cc, Loading .elfldr...done  
 0x00035ed0 0x000064f8, Loading .data...done  
 0x0003c3c8 0x00000214, Loading .got2...done  
 0x0003c5e0 0x0000006c, Loading .sdata...done  
 0x0003c650 0x00008a38, Loading .rodata...done  
 0x00045088 0x0000002c, Loading .eh\_frame\_hdr...done  
 0x000450b4 0x0000011c, Loading .eh\_frame...done  
 0x000451e0 0x00722d04, Clearing .bss...done  
 0x00767ee4 0x00000084, Clearing .sbss...done  
 * GO (entrypoint: 0000000000009800)  
 Xenos GPU ID=5841  
 ! SFCX: Unsupported Type A-0  
 ! config: sfcx not initialized  
 unknown SMC bulk msg  
 DVD cover state: 62  
 AVPACK detected: 5c  
 . ana disable  
 . ana enable  
 ................................................................................... . f1  
 . f2  
 * Xenos FB with 74x27 (640x480) at 0x9e000000 initialized.  
   
 XeLL - Xenon linux loader second stage 0.99-git- 2011-09-23 (root@x360dev i686)  
 *  
 ! SFCX: Unsupported Type A-0  
 ! sfcx initialization failure  
 ! nand related features will not be available  
 ! SFCX: Unsupported Type A-0  
 ! config: sfcx not initialized  
 * network init  
 * initializing lwip 1.4.0...  
 Reinit PHY...  
 Waiting for link...link still down.  
 * requesting dhcp.................................failed  
 * now assigning a static ip  
 * starting httpd server...success  
 * usb init  
 * Initialising USB EHCI...  
 Initialising EHCI bus 0 at 0xea003000  
 Initialising EHCI bus 1 at 0xea005000  
 EHCI bus 1 port 1: low speed, releasing to OHCI  
 * Initialising USB OHCI...  
 USB bus 0 device 1: vendor 0000 product 0000 class 09: USB Hub  
 USB bus 1 device 1: vendor 0000 product 0000 class 09: USB Hub  
 USB: New device connected to bus 1 hub 1 port 1  
 0000000000000600  
 PIR=0000000000000000  
 sr0=000000008001c7c8  
 lr =000000008001c7a0  
 sr1=1000000002003030  
 DAR=00000000c6d2f869  
 r00=000000008005dd00  
 r01=000000008fffee30  
 r02=800000001c00a0e0  
 r03=0000000006000000  
 r04=ffffffffffffffc8  
 r05=000000008005fc80  
 r06=0000000000000000  
 r07=00000000000fb8e0  
 r08=000000008005e3f8  
 r09=00000000c6d2f869  
 r10=00000000c6d2f871  
 r11=000000008fffee60  
 r12=0000000044000084  
 r13=0000000002000000  
 r14=0000000000000000  
 r15=00000000c8100000  
 r16=0000000000000000  
 r17=0000000000000000  
 r18=0000000080043ee5  
 r19=0000000080043fd4  
 r20=0000000080043e08  
 r21=0000000080767ea0  
 r22=0000000000000000  
 r23=000000008005fbb0  
 r24=000000008005fc80  
 r25=000000008005fc40  
 r26=0000000000000006  
 r27=0000000000000001  
 r28=00000000c6d2f869  
 r29=00000000b51faf30  
 r30=00000000ffffffff  
 r31=000000008005d858  
   
 Stack  
 000000000fffee30=8fffee6080767ea0  
 000000000fffee38=000000008005fbb0  
 000000000fffee40=8005fc808005fc40  
 000000000fffee48=0000000800000001  
 000000000fffee50=8005fbe08005fcb8  
 000000000fffee58=000000808005fcb8  
 000000000fffee60=8fffee708001d750  
 000000000fffee68=000000008005f8e0  
 000000000fffee70=8fffee908001d880  
 000000000fffee78=0000000800000001  
 000000000fffee80=8005fbe000000006  
 000000000fffee88=000000808005fae8  
 000000000fffee90=8fffeed08001db4c  
 000000000fffee98=0000000000000008  
 000000000fffeea0=000000018001e628  
 000000000fffeea8=80043f238005fb80  
 000000000fffeeb0=80767ea08005fae8  
 000000000fffeeb8=8005f9588005fae8  
 000000000fffeec0=8005fb8080767ea0  
 000000000fffeec8=8005fbe000000008  
 000000000fffeed0=8fffef008001dee4  
 000000000fffeed8=000000008005fae8  
 000000000fffeee0=8fffef008001d69c  
 000000000fffeee8=8005f95880760000  
 000000000fffeef0=8005f95800000001  
 000000000fffeef8=8005fab08005f818  
 000000000fffef00=8fffef608001edb4  
 000000000fffef08=8005f9588005f818  
 000000000fffef10=8fffef508001ea30  
 000000000fffef18=010000198005f960  
 000000000fffef20=8fffef5000000000  
 000000000fffef28=0000000000000000

## 2012-08-10 06:41:05, posted by: sk1080

Stack dump doesn't help without xell symbols  
 Also, we need more infromation, as in how you built this image, how you glitched a corona 4gb, etc.

## 2012-09-02 18:44:49, posted by: orkid1818

SFCX error

### Attachments

[photo.JPG](photo.JPG)