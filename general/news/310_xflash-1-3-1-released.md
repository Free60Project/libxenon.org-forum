# XFlash 1.3.1 Released!

## 2012-04-04 17:09:00, posted by: Juvenal

**[b]UPDATE:[/b]** 1.3.1 has been released, but contains no new features, it simply fixes a dependency error on pyusb. If you had trouble installing or using 1.3, please update to 1.3.1. If you have 1.3 already installed and working, then there is no need to update.  
   
 You can update with the following command or download and install manually from the attachment on this post [code]* *sudo pip install --upgrade xflash [/code] XFlash is a nandpro alternative written in python. I have recently updated it to be more robust, and add new features to keep it current with the feature set of nandpro (or closer anyway). It is rather handy if you don't like to boot into windows to dump/flash a nand.  
   
 Features for this release include: [code]* ** read/write/erase all size nands - 16mb, 64mb, 256mb, 512mb * flash xsvf's to your CPLD (assuming your nandflasher supports that) - Nand-X * power on/off the console (assuming your nandflasher supports that and is wired correctly) * supports armV1 and armV3 flashers (where nandpro only supports armV3) [/code] XFlash can be installed via the pypi (Python Package Index) or downloaded directly from here and installed manually.  
   
 to install with pip on debian/ubuntu: [code]* *sudo apt-get install python-pip libusb-1.0-0 sudo pip install xflash [/code] 'xflash' will then be available on the command line for use  
 [code]* *$xflash --help usage: xflash [-h] {read,write,erase,xsvf,update,poweroff,poweron} ... XBox 360 NAND Flasher optional arguments: -h, --help show this help message and exit Operations: {read,write,erase,xsvf,update,poweroff,poweron} read Dumps an image from the NAND write Writes an image into the NAND erase Erases blocks in the NAND xsvf Flash a CPLD with an xsvf file update Jumps into the bootloader of the NAND Flashing device for updating the firmware poweroff Shuts down the attached XBox 360 poweron Powers up the attached XBox 360 [/code] detailed usage for each command can be had by executing [code]xflash <command> --help[/code] as a quick start, some example commands are below with comments dictating what they do  
 [code]* *# dump the full sized nand to 'nanddump.bin' $sudo xflash read nanddump.bin # write the full sized nand from 'nandflash.bin' $sudo xflash write nandflash.bin # dump the first 50 blocks worth of nand to shortdump.bin $sudo xflash read shortdump.bin 0 50 # write the first 50 blocks of nand from image.ecc $sudo xflash write image.ecc 0 50 [/code] Thanks/Credits: [code]* *-Whoever wrote the original XFlash.py script -Anyone else involved the Free60 Project -The Makers of NandPro and the PIC Flashing code -G33KatWork (https://github.com/G33KatWork/XBox-360-AVR-flasher) - for his modifications to XFlash.py -Juvenal - current author of XFlash 1.3 [/code]

### Attachments

[xflash-1.3.1.tar.gz](xflash-1.3.1.tar.gz)

## 2012-04-05 12:41:33, posted by: barnhilltrckn

Nice :D Im going to have to try this out soon.

## 2012-04-21 09:54:15, posted by: Electron^-

Thank you for this tool.  
   
 I'm trying it on my Fedora14 x64 with python 2.7... It recognize the Olimex via USB, but it goes in error with the following message: [code][mpre@mpre-probook ~]$ sudo xflash read nand.bin [sudo] password for mpre: Traceback (most recent call last): File "/usr/bin/xflash", line 9, in <module> load\_entry\_point('xflash==1.3.1', 'console\_scripts', 'xflash')() File "/usr/lib/python2.7/site-packages/xflash/\_\_init\_\_.py", line 107, in main print "Using XFlash @ [%s:%s]" % (xf.dev.bus, xf.dev.address) AttributeError: 'Device' object has no attribute 'bus' [/code]   
   
 Anyone can help me to resolve this issues? I'm ready to help in testing.

## 2012-04-21 12:33:28, posted by: tuxuser

Go for python-usb version 1.0

## 2012-04-24 21:09:22, posted by: Electron^-

Thank's for reply.  
   
 I've installed pyusb 1.0 but the problem still remain...   
 I've also tryed version 0.4 without success...  
   
 There's anything else which I can try?  
   
 PS: I've Python 2.7, could is that the problem?  
   
 I've tried on another computer with ubuntu 10.10 and it works but there I've python 2.6...

## 2012-04-24 21:34:19, posted by: Juvenal

Try editing the file /usr/lib/python2.7/site-packages/xflash/\_\_init\_\_.py you will need sudo access to do that,  
 [code]sudo gedit /usr/lib/python2.7/site-packages/xflash/\_\_init\_\_.py[/code] then find line 107 and delete it, save and try running xflash again. If this solves the problem let me know.  
   
 [quote="Electron^-"]  
 Thank you for this tool.  
   
 I'm trying it on my Fedora14 x64 with python 2.7... It recognize the Olimex via USB, but it goes in error with the following message: [code][mpre@mpre-probook ~]$ sudo xflash read nand.bin [sudo] password for mpre: Traceback (most recent call last): File "/usr/bin/xflash", line 9, in <module> load\_entry\_point('xflash==1.3.1', 'console\_scripts', 'xflash')() File "/usr/lib/python2.7/site-packages/xflash/\_\_init\_\_.py", line 107, in main print "Using XFlash @ [%s:%s]" % (xf.dev.bus, xf.dev.address) AttributeError: 'Device' object has no attribute 'bus' [/code]   
   
 Anyone can help me to resolve this issues? I'm ready to help in testing.  
 [/quote]

## 2012-04-24 22:13:44, posted by: Electron^-

[quote="Juvenal"]  
 Try editing the file /usr/lib/python2.7/site-packages/xflash/\_\_init\_\_.py you will need sudo access to do that,  
 [code]sudo gedit /usr/lib/python2.7/site-packages/xflash/\_\_init\_\_.py[/code] then find line 107 and delete it, save and try running xflash again. If this solves the problem let me know.  
 [/quote]  
 Thank you, unfortunately now there are more error message:  
 [code][root@mpre-probook xflash-1.3.1]# xflash read nand.bin Traceback (most recent call last): File "/usr/bin/xflash", line 9, in <module> load\_entry\_point('xflash==1.3.1', 'console\_scripts', 'xflash')() File "/usr/lib/python2.7/site-packages/xflash/\_\_init\_\_.py", line 103, in main xf.deviceReset() File "/usr/lib/python2.7/site-packages/xflash/XFlash.py", line 46, in deviceReset self.dev.reset() File "/usr/lib/python2.7/site-packages/usb/core.py", line 565, in reset self.\_ctx.backend.reset\_device(self.\_ctx.handle) File "/usr/lib/python2.7/site-packages/usb/\_debug.py", line 52, in do\_trace return f(*args, **named\_args) File "/usr/lib/python2.7/site-packages/usb/backend/libusb10.py", line 557, in reset\_device \_check(\_lib.libusb\_reset\_device(dev\_handle)) File "/usr/lib/python2.7/site-packages/usb/backend/libusb10.py", line 357, in \_check raise USBError(\_str\_error[retval.value]) usb.core.USBError: Entity not found [/code] I've tried to install python 2.6, but it miss every module and it's unusable.

## 2012-04-24 22:19:04, posted by: Juvenal

pyusb is installed for sure, but are you sure libusb is installed on the system?  
   
 run this and post here what it returns [code]whereis libusb.so[/code] if that doesnt find anything, you need to install the libusb rpm from fedora.

## 2012-04-25 09:45:41, posted by: Electron^-

I've installed libusb at first...  
   
 I've tried also to install the the i386 package but the problem still be here...  
   
 I've 2 version of libusb installed, 0.1 (libusb) and 1.0 (libusb1).  
 Could be that the problem?