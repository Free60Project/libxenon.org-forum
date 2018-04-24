# Best way for fast prototyping

## 2011-09-08 20:19:14, posted by: SynTeX

Hi,  
   
 i'm pretty new to libxenon so i do a lot of try and error coding... which means:  
   
 1. Code at the pc  
 2. Make & rename & Copy to USB-Stick & Umount   
 3. unplug usb-stick  
 4. stand up  
 5. plug in usb-stick into 360 & unplug/plug back in psu  
 6. run  
 --- And again  
   
 What is the best way to test software? i gues it's TFTP but then i need a way to boot my 360 from remote into xell...   
   
 Thanks a lot! :)

## 2011-09-08 21:00:03, posted by: Juvenal

TFTP is by far the best.  
   
 Also, if you flash a xell only image, xell will boot by default every time.  
   
 Also, if you have a properly built spi flasher you can trigger the console to power on/off using it.  
   
 Another option would be to rig up a simple circuit to 'press' the power or eject button when a pin on the parallel/serial port on your PC goes high.  
 Meaning you could trigger the pin to go high for 500ms or so in a bash script.

## 2011-09-08 21:19:34, posted by: tuxuser

[url=http://libxenon.org/http://libxenon.org//viewtopic.php?t=2]FTDI RemoteControl[/url] can be also used for remote shutdown/poweron. Personally I use an FT232R which supports UART.. but once I enter the bitbang mode with this little application the UART function breaks down :/ Maybe there's another way to trigger it?!  
   
 Anyway, have fun with it :P

## 2011-09-09 01:02:27, posted by: Echelo

If you have dash launch installed, and boot direct to xexmenu, you can use scripted ftp, and xelllaunch. Simple as ./send\_prototype.sh.  
   
 send\_prototype.sh should look like this.  
 [quote] ftp -v -n "192.168.0.100" << cmd  
 user "xbox" "xbox"  
 bin  
 put prototype.elf32 /Usb0/xenon.elf  
 dis  
 quit  
 cmd [/quote] Then just make sure you mapped xenon\_smc\_power\_reboot() to a button in your prototype.

## 2011-09-09 14:56:23, posted by: SynTeX

I'm now using DashLaunch with XellLaunch and FTP.. so if i press X it launches Xell Reloaded and everything works fine :)  
 Now since my toolchain is running, and mupen64 is compiling and running fine, i can start coding on my own :D  
   
 thanks a lot guys!