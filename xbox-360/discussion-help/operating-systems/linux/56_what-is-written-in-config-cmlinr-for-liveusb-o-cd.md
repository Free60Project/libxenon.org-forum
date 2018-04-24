# What is written? in CONFIG_CMLINR for liveusb o cd

## 2011-03-21 02:28:18, posted by: redxs

what be amended to make the kernel run as liveusb?  
   
 I would be very helpful thansk.

## 2011-03-21 20:37:44, posted by: tuxuser

The main parameter is   
 [code]* *boot=casper [/code] Take care that NO ROOT PARAMETER is set. Also make sure you include a casper-initramfs inside the linux-kernel.  
   
 Edit: I guess that should be pretty interesting for you: http://libxenon.org/http://libxenon.org//viewtopic.php?p=221#p221

## 2011-03-22 00:08:33, posted by: redxs

Good, tuxuser helpful always proves this, thank you very much.