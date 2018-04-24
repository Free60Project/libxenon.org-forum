# Serial console documentation

## 2011-06-08 23:41:12, posted by: UNIX

Hey all,   
   
 I took some time to compile basic serial port documentation. Using information on Free60 and from people helping me here, I figured it would be a good idea to provide some in-depth documentation for everybody.  
 [quote] The Xbox 360 Serial Interface  
   
 Contents  
   
 0. Introduction  
   
 1.0 The Serial Console in Depth Look  
   
 2.0 How to Set Up a Debugging Interface  
 2.1 Hardware (What you will need)  
 2.2 Setting Up a Serial Debug Interface  
 2.3 Setting Up a USB Debug Interface  
 2.4 Advantages of USB  
   
 3.0 How to Capture Debug Output from Your Interface  
 3.1 Linux/*NIX  
 3.2 Coming soon - Windows  
 3.3 Coming soon - MacOS  
   
 4.0 Acknowledgments  
   
 Written By:  
 UNIX – LibXenon.org  
 UNIX – XDKForums.com  
   
   
 0. Introduction  
   
   
 The Xbox 360 serial console is located on EVERY Xbox 360 mainboard. However, only Xbox 360 development consoles can actually make use of the code debugging features that the serial console allows. However, a store bought console which has been hacked using the JTAG/SMC exploit can make use of the code debugging features available using the serial console. Debugging is the process of finding bugs in your code to provide faster, easier development. Using the Xbox 360 serial interface, you can interact with your code in real time, to see where the code fails/stops functioning etc. This documentation will describe in depth how to setup a serial debugging interface using a UART.  
   
 *****This documentation assumes that you will be debugging LibXenon, not XDK code! If you are using the XDK, you should really give LibXenon a try! <!-- s;-) -->;-)<!-- s;-) -->*****  
   
   
 1.0 The Serial Console in Depth  
   
 Before getting into connection the serial console to your PC for debugging purposes, it is a good idea to understand it. So what is a serial console? It isn't an Xbox 360 specific term. A serial console is generally an RS232 link to a device terminal. With this link, a user can recieve and send data to the target device. The serial console is a very basic form of device communications, and is popular in embedded device programming.   
   
 The Xbox 360 serial console is utilized in Xbox 360 development kits for debugging. It is connected to the microsoft official sidecar. It is very possible to home brew your own serial interface to the Xbox 360 using almost the same means.   
   
 The serial console on the main board of the Xbox 360 operates on a TTL (Transistor-transistor logic) level; because of this, it cannot be wired directly to a erial port on a PC. Doing so would result in either the PC serial port or the Xbox 360 serial port to be fried. So to connect the two together, a TTL to serial converter is needed.   
   
 As you might have guessed, you can use either a standard serial port or a USB connection to communicate with the Xbox 360 motherboard. Either one will work, and they both need TTL converters, no exceptions. USB is faster than a standard serial port though, and also more common on newer PC's, because the standard serial port is nearly extinct.  
   
 The serial console on the Xbox 360 is located between the Stereo DAC chip, and the GPU heatsink (flat one) It is a 12 pin header. You may take note that two of the points needed to read the NAND chip are on this header.   
   
 *It's also VERY important to note that the serial console operates on a 3.3v level.   
   
 2.0 How to Set Up a Debugging Interface  
   
   
 Setting up a serial interface to the Xbox 360 motherboard is a fairly simple process. In this section I will describe in depth how to use a Standard 9 pin serial setup and a USB setup, what hardware to use, the differences, etc.   
   
   
 2.1 Hardware  
   
 Otherwise known as the "what you will need" section. What you WILL need, is the following:  
 1. Good soldering skills  
 2. Some thin wire  
 3. A TTL to serial/USB converter  
 4. Patience  
   
 If you read any of section 1, then you probably already knew all of that. As far as obtaining a converter goes, I can personally recommend these two:  
   
   
   
   
 For serial connections:   
 <!-- m -->[url=http://cgi.ebay.com/RS232-Serial-Port-TTL-Converter-Module-SP3232-LED-/380319575807?pt=LH\_DefaultDomain\_0&hash=item588cd02eff]http://cgi.ebay.com/RS232-Serial-Port-T ... 588cd02eff[/url]<!-- m -->  
   
 For USB connections:  
 <!-- m -->[url=http://cgi.ebay.com/2pcs-USB-UART-TTL-Cable-module-PL2303-Converter-/190533682059?\_trksid=p5197.m7&\_trkparms=algo%3DLVI%26itu%3DUCI%26otn%3D5%26po%3DLVI%26ps%3D63%26clkid%3D489097430148299424]http://cgi.ebay.com/2pcs-USB-UART-TTL-C ... 0148299424[/url]<!-- m -->  
   
   
 2.2 Setting Up a Serial Debug Interface  
   
 If you're reading this, then you're most likely interested in setting up a standard 9 pin connection to communicate with your Xbox 360 motherboard. Congratulations on having a PC old enough to have a serial port <!-- s;-) -->;-)<!-- s;-) --> Now let's get down to business.  
   
 All RS232 to TTL converters will have 6 pins, a power input, a recieve data pin (RxD), a transfer data pin (TxD), a clear to send pin (CTS), a request to send pin (RTS), and a ground (GND). The only pins needed will be the RxD, TxD, the power supply, and the GND.   
   
 You may be flustered or confused, but matching up the correct pins on the Xbox 360 motherboard is quite simple with good soldering skills. All serial interfaces as a standard, have the same pin layouts, or most of them. The GND, RX, TX, and power are the most basic interface you can set up. So it's only a matter of matching pin for pin on the converter to the Xbox motherboard.  
   
 Use this diagram to guide yourself in the soldering process:  
 <!-- m -->[url=http://free60.org/images/d/d5/J2B1\_SCON.png]http://free60.org/images/d/d5/J2B1\_SCON.png[/url]<!-- m -->  
   
 Looking at that diagram should be fairly easy with understanding the basics of serial communication now. All you have to do is match the pins labeled to the correct pins on your converter.  
   
 You may be wondering where the power supply is on the Xbox side of things. Well, actually there are two. One of them is always powered regardless if the console is powered on on not, and the other is only on when the console is on. Using the standby pin (the pink wire in the diagram) will probably maximize the mileage you get out of your converter.  
   
 You can either plug the converter right into your PC's port, or you can use a regular serial cable as a patch. Although, the less distance from the motherboard to the PC the better.  
   
   
 2.3 Setting Up a USB Debug Interface  
   
 If you're reading this you're likely more interested in taking the more modern approach to setting up your debugging environment. Using the USB approach is easier and requires less soldering on the Xbox side of things as well.  
   
 USB TTL converters are seemingly more diverse than their RS232 elders. The chip which is (at the time of writing) recommended for usage is the PL2303 chip, so I recommend getting a PL2303 converter if you plan on going the USB route. USB converters are either self powered by the host machine, or seperately. For convenience, I suggest getting a converter that is powered by the host. The converter will keep the voltage level down to 3.3 volts to avoid nuking the Xbox 360 serial console.  
   
 If your converter is self powered, and only provides GND, RX, and TX wires, then you will only have to solder the RX and TX wires to the board. Some people have trouble when connecting the GND to the board, sometimes constant rebooting of the console, etc. I advise you to not attach the GND to the board and ONLY use RX and TX.  
   
   
   
   
 If your converter needs an external power source, then you will have to do an extra bit of work. As mentioned in the Serial debug interface section (2.2) you will have to use the standby power or the constant power supply pin on the header. Please see this wiki page:  
 <!-- m -->[url=http://free60.org/Serial\_Console]http://free60.org/Serial\_Console[/url]<!-- m -->  
   
 Cutting the distance as much as possible from the Xbox motherboard to your PC will help a great deal. The shorter the distance, the stronger the connection!  
   
 2.4 Advantages of USB  
   
 USB has many advantages over standard serial in almost every case. USB availability is a lot higher because serial ports are barely made on newer PC's anymore. USB will also be a lot faster than standard serial, especially if you get a USB2.0 or 3.0 capable converter. Keep in mind though that transferring debug output won't need to take more than a few kilobytes per second transfer rate. I highly recommend using USB over regular serial in this case.   
   
   
 3. How to Capture Debug Output from Your Interface  
   
 No matter what your platform is, there is bound to be software you can use to capture input/output from USB or serial interfaces. I will explain what tools you will need on both Linux and Windows*.  
   
 I am not a Windows user at all, if someone knows about capturing serial/USB information on Windows platforms, feel free to add it.  
   
 When debugging LibXenon, when you use printf statements, they are by default sent to the serial console. For example:  
   
 printf(“This is text\n”);  
   
 Would appear on your debugging PC as This is text and create a new line. This is the most basic method of debugging possible. It's a quick, easy way to live debug your code and easily see where your code fails.   
   
 It is possible to inject code into the console, and interact with the kernel and hypervisor. Once I get more experience with this, I will cover it in this documentation.  
   
 3.1 Linux/*NIX  
   
 UNIX-like operating systems are great development systems. For a great development system, there is also great development software. My software of choice while using Linux for debugging LibXenon is Minicom. Minicom is a very easy to use program for capturing data from ANY port, USB, serial, what-have-you. Minicom is also very easy to use, but is terminal based. It does have a BASIC GUI to allow for arrow key configuartion, though.  
   
 *I use Solaris, not Linux, but the steps will likely be the same*  
 Minicom to my knowledge is in MOST major Linux package repositories. So assuming you know how to use your distributions package management system (if you don't, god help you) then you can just do, e.g:  
 apt-get install minicom  
 If not, you can compile from source which will work regardless of your platform! You can get the minicom source code from: <!-- m -->[url=http://alioth.debian.org/frs/download.php/3487/minicom-2.5.tar.gz]http://alioth.debian.org/frs/download.p ... 2.5.tar.gz[/url]<!-- m -->  
   
 Once you have minicom installed, type 'minicom' at the terminal/shell and you will be greeted by the DOS style menu. To set up your default listening port, invoke 'minicom -s' from the terminal/shell. Then, input the path to your device, e.g:  
 /dev/ttyUSB0  
   
 Then, you can use Minicom to hopefully capture the text debugging information from your console.   
   
 4.0 Acknowledgements  
   
 Free60.org - For providing the information needed to compile this documentation, as well as the diagrams used in this document.  
 LibXenon.org - Thank you to everyone who helped me set up my own debugging interface and originally pointed me in   
 the right direction.  
   
 Tuxuser - For giving me a LOT of help, with a lot of things, and being a good guy  
 Hollenengel - For being there for me<3  
 gomson - For pushing me to finish this documentation I started a while ago :p  
   
 Be sure to visit LibXenon.org !   
   
   
 Written by:  
   
 UNIX - LibXenon.org  
 UNIX - XDK-forums.com [/quote] I also exported the documentation as a PDF and it is available for download at [url=http://www.megaupload.com/?d=5650OS01]this link[/url]  
   
 I tried to make it as clean and easy to understand as possible.  
 *If anybody knows anything about Windows/MacOS serial interfacing, feel free to add it in and repost it. I myself use Solaris, so I haven't a clue really. I know a lot of people here are Linux users, which is covered in the document <!-- s;) -->;)<!-- s;) -->  
   
 Let me know what you think, good bad, or if something needs to be added or edited.  
   
 -UNIX

## 2011-06-09 03:52:30, posted by: tuxuser

Very nice and detailed document. Feel free to edit your first post and put the whole text there in quotes.  
   
 Just one thing I noticed, you should write LVTTL everywhere possible as its very important to not use the Serial Port with 5V, it will fry probably RX/TX and if not, it will just give you garbage output on your serial console.  
   
 I can only repeat, great work and thx for taking the time to write and in the end, share it ;)

## 2011-06-09 21:15:38, posted by: UNIX

I will edit that in later tonight for sure, I'll be sure to make it a little more clear in that regard. Glad you liked it, thanks for the feedback :)

## 2011-06-09 23:26:36, posted by: gomson

I just wanna add that "great work, please keep it up"..  
 Many thanks dude..  
 :D

## 2011-06-10 08:17:39, posted by: Meluxe

[quote=""gomson""]I just wanna add that "great work, please keep it up"..  
 Many thanks dude..  
 :D[/quote]  
   
   
 same here, and thanks for clearing up! :)

## 2011-09-19 19:18:18, posted by: peet8989

ist there a backslash missing?:  
   
 printf(“This is text[color=red][size=140]\[/size][/color]n”);

## 2011-09-19 19:22:45, posted by: tuxuser

[quote="peet8989"]  
 ist there a backslash missing?:  
   
 printf(“This is text[color=red][size=140]\[/size][/color]n”);  
 [/quote]  
   
 Good eye ;) It's fixed now.

## 2012-01-03 14:03:33, posted by: covenant

Wondering if anyone can sanity check the following for me as I am trying to get a level shifter set up and connected to my glitched slim but encountering problems.  
   
 I have used J2C3 socket header on slim for the 3V3, RX and TX points by basing the point choices on this image: [url=http://www.free60.org/Serial\_Console]http://www.free60.org/Serial\_Console[/url]. I am using one of the large copper pads near the mainboard screw holes as the GND point because J2C3.12 is a bitch to melt solder on.  
   
 I am using this level shifter which employs a Max2321N: [url=http://www.ebay.co.uk/itm/250944462988?ssPageName=STRK:MEWNX:IT&\_trksid=p3984.m1439.l2649#ht\_500wt\_1362]http://www.ebay.co.uk/itm/250944462988?ssPageName=STRK:MEWNX:IT&\_trksid=p3984.m1439.l2649#ht\_500wt\_1362[/url]  
   
 I am also using a USB to RS232 convertor to connect the PC to the level shifter. The PC is an Ubuntu box and the USB/RS232 convertor is recognised fine (/dev/ttyUSB0) and works perfectly (typed characters in minicom (with local echo set to off) are not echoed unless pins 2 and 3 on the convertor are shorted).  
   
 I hooked up my logic analyzer to the level shifter and monitored the RX and TX lines from both the XBox and the PC:  
   
 [url=http://postimage.org/image/yshkuzdbx/]![](http://s14.postimage.org/yshkuzdbx/RS232_TTL.jpg)[img]http://s14.postimage.org/yshkuzdbx/RS232\_TTL.jpg[/img][/url]  
   
 As you can see, the XBox (booting into Xell Reloaded) provides output on the 'Convertor RX' channel and a bit of keyboard bashing in minicom gives me a signal on the 'DB9 #3' channel which is pin 3 on the DB9 connected to the PC.   
   
 Thus, signals are reaching the level shifter but neither 'Convertor TX' (which should echo DB9 #3) nor DB9 #2 (which should echo Convertor RX) are showing anything. This makes me suspect connections with the MAX232.  
   
 Having checked the PCB on my level shifter compared with the diagram shown here: [url=http://www.free60.org/Level\_Shifter]http://www.free60.org/Level\_Shifter[/url]  
   
 I have noticed that the linked level shifter schematic has:  
 XBox RX -> MAX232 R-OUT   
 XBox TX -> MAX232 T-IN.   
   
 My level shifter PCB has:  
 XBox TX -> MAX232 R-OUT  
 XBox RX -> MAX232 T-IN   
   
 On the PC side of the MAX232, my level shifter matches that in the linked diagram i.e.  
 DB9 pin 2 -> T-OUT  
 DB9 pin 3 -> R-IN  
   
 I have tried switching TX and RX lines from the XBox to the level shifter because I am familiar with the concept of RX/TX dyslexia in diagrams and my thinking!  
   
 Ideas anyone? (in addition to anyone knowing what the best baud rate to choose is - 115200?)

## 2012-01-03 15:07:48, posted by: tuxuser

LVTTL: MAX3232  
   
 TTL: MAX232  
   
   
 for the xbox you need a LVTTL, maybe thats the reason why you dont get the proper voltage shifting done?!  
   
 btw, 115200 is the correct baudrate

## 2012-01-03 16:27:28, posted by: covenant

Thanks for the reply.   
   
 Ahh...that may well be the problem although I have had some more luck which suggests that perhaps it is not.  
   
 Here is the output from my logic analyzer monitoring both sides of the MAX232:  
   
 [url=http://postimage.org/image/ms5blqkpd/]![](http://s16.postimage.org/ms5blqkpd/RS232_TTL_2.jpg)[img]http://s16.postimage.org/ms5blqkpd/RS232\_TTL\_2.jpg[/img][/url]  
   
 I have relabelled the channels to something less unintuitive (for my RX/TX dyslexia!) such that you can see that 'XBox talk' (the RX pin on the XBox side of the level shifter) is exactly reproduced by 'DB9 listen' (pin 2 on the DB9 connector on the level shifter). I think I may have had a bad connection/short in the previous test because this suggests that, apart from inverting the signals, data is passing through the MAX232.  
   
 However, at any baud rate tried, I get nothing from cat /dev/ttyUSB0 which is surprising.  
   
 Do you still think the issue is the MAX232 vs MAX3232 difference? I have a MAX3232CPE sitting around somewhere that I could use, I'll just have to dig out a spare DB9F connector but would prefer to get the above working if possible as it seems to be close to working. Thanks for the quick reply above.   
   
 EDIT: XBox is definitely sending debug info because after correcting the baud value and increasing the sampling frequency, I can convert the logic analyzer output to ASCII and see the boot messages. 

## 2012-01-03 20:14:06, posted by: sk1080

Are you using a usb to serial converter if you are using /dev/ttyUSB0?

## 2012-01-03 20:37:32, posted by: covenant

Yes - see my previous post. The USB to serial works fine.

## 2012-01-04 08:49:49, posted by: sk1080

Sorry for no scrolling up that far. I have heard that the MAX232 will work with 3.3V, but it isn't in the chips spec, so it may be dependent on the particular chip. Other than that, I do not know more at this point. I have a max232 here and I will see if I can get any results from it when I can.

## 2012-01-05 21:42:02, posted by: covenant

Update: Got it working and currently viewing debug output via UART in minicom. I built a shifter from scratch myself using an MAX3232, caps and a DB9F connector and it works perfectly (once I had managed to sort out my RX/TX dyslexia which struck at various points in proceedings).

## 2012-05-26 05:59:43, posted by: mojobojo

I just got a USB to TTL converter and got it working on Windows 7. For use with putty set the "Connection Type" to "Serial" and put your COMX port in "Serial Line" then set the baud rate to 38400.

## 2012-08-16 13:39:58, posted by: jskew

Xbox 360 Devkit 2.0.15574.0  
 HWINIT 090504a  
   
 BL Ready  
 0000€€ý110#€ÿÿÿÿò  
 €ÿÿÿÿÿÿÿ$€#Z`€#Z`ÿÿÿÿ€ €#€#f €#m €#\@àN€ àN€ D"€€  
 ó´ÿÿÿÿ€#nxxboxkrnl.exeª0000€€ý110#€ÿÿÿÿò  
 €ÿÿÿÿÿÿÿ$€#Z`€#Z`ÿÿÿÿ€ €#€#f €#m €#\@àN€ àN€ D"€€  
 ó´ÿÿÿÿ€#nxxboxkrnl.exeª0000€€ý110#€ÿÿÿÿò  
 €ÿÿÿÿÿÿÿ$€#Z`€#Z`ÿÿÿÿ€ €#€#f €#m €#\@àN€ àN€ D"€€  
 ó´ÿÿÿÿ€#nxxboxkrnl.exeª0000€€ý110#€ÿÿÿÿò  
 €ÿÿÿÿÿÿÿ$€#Z`€#Z`ÿÿÿÿ€ €#€#f €#m €#\@àN€ àN€ D"€€  
 ó´ÿÿÿÿ€#nxxboxkrnl.exeª0000€€ý110#€ÿÿÿÿò  
 €ÿÿÿÿÿÿÿ$€#Z`€#Z`ÿÿÿÿ€ €#€#f €#m €#\@àN€ àN€ D"€€  
 ó´ÿÿÿÿ€#nxxboxkrnl.exeª  
   
   
 i got the msg ??

## 2012-08-16 13:42:10, posted by: sk1080

Lol, guess what the forum rules say not to talk about