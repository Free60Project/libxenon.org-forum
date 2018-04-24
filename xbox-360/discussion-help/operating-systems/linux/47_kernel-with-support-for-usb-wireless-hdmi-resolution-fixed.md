# Kernel with support for USB wireless + HDMI resolution fixed

## 2011-03-18 11:07:43, posted by: redxs

Thanks to**[b] Cancerous1[/b]** for fix error in hdmi and share solutions.  
 [url=http://libxenon.org/http://libxenon.org//viewtopic.php?t=6]Overscan on HDMI fixed![/url]   
   
 Kernel 2.6.36.4 xenon - 3-Cpu active (+ nosmp in CONFIG\_CMLINE)  
 [url=http://www.megaupload.com/?d=D246LZVU]http://www.megaupload.com/?d=D246LZVU[/url]   
   
 orinco  
 prism54  
 zydas zd1211  
 marvell 8388  
 rndis< lot adapters  
 atmel at76c50x  
 atheros ar9170  
 ralink rt250x rt2800 rt30xx  
 rtl8187 rtl81xx  
   
 [url=http://img192.imageshack.us/i/screenshotrkp.png/]![](http://img192.imageshack.us/img192/3449/screenshotrkp.png)[img]http://img192.imageshack.us/img192/3449/screenshotrkp.png[/img][/url]  
   
 kernel 2.6.36.4 for install in Hdd sda

## 2011-03-18 16:32:30, posted by: val532

Rlt818x is a chip for wifi no ?

## 2011-03-18 16:53:11, posted by: Cancerous1

Redxs, what did you change to enable it? and what product is the rtl818x chip in?

## 2011-03-18 20:12:35, posted by: redxs

yes is chip wifi , after of make CROSS\_COMPILE=xenon- ARCH=powerpc oldconfig  
   
 write make CROSS\_COMPILE=xenon- ARCH=powerpc xconfig (need down packet for work libqt3-dev or equal)   
   
 need mark mac8011 and wireless or devices usb there a list de modules wifi to compile if does not appear Rtl8187 or rtl818x(there two realtek usb modules and others) need mark other options wiht relation wireless networks

## 2011-03-19 12:41:17, posted by: eminwargo

Could you say me which linux version is it in the picture ?  
   
 [url=http://img192.imageshack.us/i/screenshotrkp.png/]http://img192.imageshack.us/i/screenshotrkp.png/[/url]

## 2011-03-19 19:50:20, posted by: redxs

i first install debian squeeze , and after Lxde  
   
 that answers your question? not understood well

## 2011-03-20 04:31:15, posted by: sbarrenechea

So... Can we use our Xbox 360 for wifi auditory? :O

## 2011-03-20 05:03:49, posted by: redxs

yes, awesome eh? :D   
   
 I think with ubuntu10.10 (live) also just modifying the kernel and downloading the required packages

## 2011-03-20 05:17:43, posted by: sbarrenechea

You should do a tutorial for Wifi auditory :P and if can enable more wifi chipsets could be great :P

## 2011-03-20 05:33:27, posted by: redxs

In fact, compiling a kernel with all usb wifi which supports the kernel, I upload soon.  
   
 for ubuntu10.10 (live usb) I experience and see what happens.  
   
 but not know, if all supporting monitor mode  
   
 the issue is well known wireless audit and explained, there is nothing different :)

## 2011-03-20 16:05:05, posted by: sbarrenechea

[quote=""redxs""]In fact, compiling a kernel with all usb wifi which supports the kernel, I upload soon.  
   
 for ubuntu10.10 (live usb) I experience and see what happens.  
   
 but not know, if all supporting monitor mode  
   
 the issue is well known wireless audit and explained, there is nothing different :)[/quote]  
   
 Can you explain me in spanish? I'm from Chile xd

## 2011-03-21 02:34:05, posted by: redxs

new kernel added compiled with more usb wireless support  
   
 sbarrenechea  
   
 te digo que tutoriales de auditoria wireless hay por donde sea :) hasta youtube no hay diferencia.  
   
 y otros usb wifi que soporta este kernel no se si entren en modo monitor(de perdida para conectarte a internet de casa por wifi y debian servira ) y para inyectar, minimo mi usb realtek hace de todo.

## 2011-03-22 21:58:49, posted by: schwatter

WLAN-USB-ID  
 [quote] xbox@ubuntu:~$ sudo su  
 root@ubuntu:/home/xbox# sudo lsusb  
 Bus 004 Device 002: ID 045e:02aa Microsoft Corp.  
 Bus 004 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub  
 Bus 003 Device 004: ID 045e:028f Microsoft Corp. Xbox360 Wireless Controller  
 Bus 003 Device 003: ID 0458:0007 KYE Systems Corp. (Mouse Systems)  
 Bus 003 Device 002: ID 046d:c312 Logitech, Inc. DeLuxe 250 Keyboard  
 Bus 003 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub  
 Bus 002 Device 003: ID 045e:0765 Microsoft Corp.  
 Bus 002 Device 002: ID 0781:5566 SanDisk Corp.  
 Bus 002 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub  
 Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub  
 root@ubuntu:/home/xbox# sudo lsusb -d 045e:0765 -v  
   
 Bus 002 Device 003: ID 045e:0765 Microsoft Corp.  
 Device Descriptor:  
 bLength 18  
 bDescriptorType 1  
 bcdUSB 2.00  
 bDeviceClass 0 (Defined at Interface level)  
 bDeviceSubClass 0  
 bDeviceProtocol 0  
 bMaxPacketSize0 64  
 idVendor 0x045e Microsoft Corp.  
 idProduct 0x0765  
 bcdDevice 10.20  
 iManufacturer 1 Marvell  
 iProduct 2 Xbox console USB communication device  
 iSerial 3 0000000000000000  
 bNumConfigurations 1  
 Configuration Descriptor:  
 bLength 9  
 bDescriptorType 2  
 wTotalLength 15360  
 bNumInterfaces 1  
 bConfigurationValue 1  
 iConfiguration 4 Wireless LAN Configuration  
 bmAttributes 0x80  
 (Bus Powered)  
 MaxPower 500mA  
 Interface Descriptor:  
 bLength 9  
 bDescriptorType 4  
 bInterfaceNumber 0  
 bAlternateSetting 0  
 bNumEndpoints 6  
 bInterfaceClass 255 Vendor Specific Class  
 bInterfaceSubClass 255 Vendor Specific Subclass  
 bInterfaceProtocol 255 Vendor Specific Protocol  
 iInterface 5 Wireless LAN Interface  
 Endpoint Descriptor:  
 bLength 7  
 bDescriptorType 5  
 bEndpointAddress 0x01 EP 1 OUT  
 bmAttributes 2  
 Transfer Type Bulk  
 Synch Type None  
 Usage Type Data  
 wMaxPacketSize 0x0002 1x 2 bytes  
 bInterval 0  
 Endpoint Descriptor:  
 bLength 7  
 bDescriptorType 5  
 bEndpointAddress 0x81 EP 1 IN  
 bmAttributes 2  
 Transfer Type Bulk  
 Synch Type None  
 Usage Type Data  
 wMaxPacketSize 0x0002 1x 2 bytes  
 bInterval 0  
 Endpoint Descriptor:  
 bLength 7  
 bDescriptorType 5  
 bEndpointAddress 0x02 EP 2 OUT  
 bmAttributes 2  
 Transfer Type Bulk  
 Synch Type None  
 Usage Type Data  
 wMaxPacketSize 0x0002 1x 2 bytes  
 bInterval 0  
 Endpoint Descriptor:  
 bLength 7  
 bDescriptorType 5  
 bEndpointAddress 0x82 EP 2 IN  
 bmAttributes 2  
 Transfer Type Bulk  
 Synch Type None  
 Usage Type Data  
 wMaxPacketSize 0x0002 1x 2 bytes  
 bInterval 0  
 Endpoint Descriptor:  
 bLength 7  
 bDescriptorType 5  
 bEndpointAddress 0x03 EP 3 OUT  
 bmAttributes 2  
 Transfer Type Bulk  
 Synch Type None  
 Usage Type Data  
 wMaxPacketSize 0x0002 1x 2 bytes  
 bInterval 0  
 Endpoint Descriptor:  
 bLength 7  
 bDescriptorType 5  
 bEndpointAddress 0x83 EP 3 IN  
 bmAttributes 2  
 Transfer Type Bulk  
 Synch Type None  
 Usage Type Data  
 wMaxPacketSize 0x0002 1x 2 bytes  
 bInterval 0  
 Device Qualifier (for other device speed):  
 bLength 10  
 bDescriptorType 6  
 bcdUSB 2.00  
 bDeviceClass 0 (Defined at Interface level)  
 bDeviceSubClass 0  
 bDeviceProtocol 0  
 bMaxPacketSize0 64  
 bNumConfigurations 1  
 Device Status: 0x0000  
 (Bus Powered)  
 root@ubuntu:/home/xbox#  
 [/quote]

## 2011-03-23 00:40:02, posted by: tuxuser

Note to myself:  
 LIBERTAS  
 LIBERTAS\_USB

## 2011-03-23 04:42:08, posted by: redxs

[quote=""schwatter""]WLAN-USB-ID  
 [quote] xbox@ubuntu:~$ sudo su  
 root@ubuntu:/home/xbox# sudo lsusb  
 Bus 004 Device 002: ID 045e:02aa Microsoft Corp.  
 Bus 004 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub  
 Bus 003 Device 004: ID 045e:028f Microsoft Corp. Xbox360 Wireless Controller  
 Bus 003 Device 003: ID 0458:0007 KYE Systems Corp. (Mouse Systems)  
 Bus 003 Device 002: ID 046d:c312 Logitech, Inc. DeLuxe 250 Keyboard  
 Bus 003 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub  
 Bus 002 Device 003: ID 045e:0765 Microsoft Corp.  
 Bus 002 Device 002: ID 0781:5566 SanDisk Corp.  
 Bus 002 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub  
 Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub  
 root@ubuntu:/home/xbox# sudo lsusb -d 045e:0765 -v  
   
 Bus 002 Device 003: ID 045e:0765 Microsoft Corp.  
 Device Descriptor:  
 bLength 18  
 bDescriptorType 1  
 bcdUSB 2.00  
 bDeviceClass 0 (Defined at Interface level)  
 bDeviceSubClass 0  
 bDeviceProtocol 0  
 bMaxPacketSize0 64  
 idVendor 0x045e Microsoft Corp.  
 idProduct 0x0765  
 bcdDevice 10.20  
 iManufacturer 1 Marvell  
 iProduct 2 Xbox console USB communication device  
 iSerial 3 0000000000000000  
 bNumConfigurations 1  
 Configuration Descriptor:  
 bLength 9  
 bDescriptorType 2  
 wTotalLength 15360  
 bNumInterfaces 1  
 bConfigurationValue 1  
 iConfiguration 4 Wireless LAN Configuration  
 bmAttributes 0x80  
 (Bus Powered)  
 MaxPower 500mA  
 Interface Descriptor:  
 bLength 9  
 bDescriptorType 4  
 bInterfaceNumber 0  
 bAlternateSetting 0  
 bNumEndpoints 6  
 bInterfaceClass 255 Vendor Specific Class  
 bInterfaceSubClass 255 Vendor Specific Subclass  
 bInterfaceProtocol 255 Vendor Specific Protocol  
 iInterface 5 Wireless LAN Interface  
 Endpoint Descriptor:  
 bLength 7  
 bDescriptorType 5  
 bEndpointAddress 0x01 EP 1 OUT  
 bmAttributes 2  
 Transfer Type Bulk  
 Synch Type None  
 Usage Type Data  
 wMaxPacketSize 0x0002 1x 2 bytes  
 bInterval 0  
 Endpoint Descriptor:  
 bLength 7  
 bDescriptorType 5  
 bEndpointAddress 0x81 EP 1 IN  
 bmAttributes 2  
 Transfer Type Bulk  
 Synch Type None  
 Usage Type Data  
 wMaxPacketSize 0x0002 1x 2 bytes  
 bInterval 0  
 Endpoint Descriptor:  
 bLength 7  
 bDescriptorType 5  
 bEndpointAddress 0x02 EP 2 OUT  
 bmAttributes 2  
 Transfer Type Bulk  
 Synch Type None  
 Usage Type Data  
 wMaxPacketSize 0x0002 1x 2 bytes  
 bInterval 0  
 Endpoint Descriptor:  
 bLength 7  
 bDescriptorType 5  
 bEndpointAddress 0x82 EP 2 IN  
 bmAttributes 2  
 Transfer Type Bulk  
 Synch Type None  
 Usage Type Data  
 wMaxPacketSize 0x0002 1x 2 bytes  
 bInterval 0  
 Endpoint Descriptor:  
 bLength 7  
 bDescriptorType 5  
 bEndpointAddress 0x03 EP 3 OUT  
 bmAttributes 2  
 Transfer Type Bulk  
 Synch Type None  
 Usage Type Data  
 wMaxPacketSize 0x0002 1x 2 bytes  
 bInterval 0  
 Endpoint Descriptor:  
 bLength 7  
 bDescriptorType 5  
 bEndpointAddress 0x83 EP 3 IN  
 bmAttributes 2  
 Transfer Type Bulk  
 Synch Type None  
 Usage Type Data  
 wMaxPacketSize 0x0002 1x 2 bytes  
 bInterval 0  
 Device Qualifier (for other device speed):  
 bLength 10  
 bDescriptorType 6  
 bcdUSB 2.00  
 bDeviceClass 0 (Defined at Interface level)  
 bDeviceSubClass 0  
 bDeviceProtocol 0  
 bMaxPacketSize0 64  
 bNumConfigurations 1  
 Device Status: 0x0000  
 (Bus Powered)  
 root@ubuntu:/home/xbox#  
 [/quote][/quote]  
   
   
 try with this [url=http://www.mediafire.com/?z2q29mgx201xme6]http://www.mediafire.com/?z2q29mgx201xme6[/url]

## 2011-06-27 19:59:40, posted by: tuxuser

Xbox FAT WiFi Module: VID\_045E&PID\_0292