# Microcontroller for Xbox360 slim sound files

## 2011-09-11 23:34:41, posted by: homebrew360

With the release of all the special edition xbox 360 consoles which have different sound files associated with the eject and power functions. I was wondering if anyone has located , or experimented with the controller that initiates the files.

## 2011-09-11 23:58:31, posted by: tuxuser

[quote="l\_oliveira"]  
 It's NOT at the RF board guys...  
   
 Here's the culprit:  
 ISD2110 (21**[b]10[/b]** means it has enough memory for 10 seconds of playback at 8khz) which is a variation of ISD2100: "Digital ChipCorder with Multi Time Programing and Digital Audio Interface"  
   
 http://www.nuvoton-usa.com/downloads/isd2100datasheet.pdf  
 [/quote]  
   
 Source: [url=http://www.xboxhacker.org/http://libxenon.org//viewtopic.php?p=126672#p126672]http://www.xboxhacker.org/http://libxenon.org//viewtopic.php?p=126672#p126672[/url]  
   
 Chip is located here:  
   
 [attachimg=1]  
   
 Source: [url=http://forums.xbox-scene.com/index.php?showtopic=736761#]http://forums.xbox-scene.com/index.php?showtopic=736761#[/url]

### Attachments

[p1000924copy.jpg](p1000924copy.jpg)

## 2011-09-12 00:15:57, posted by: homebrew360

Thanks Tux this is just what i was looking for. ;D

## 2012-01-19 05:22:29, posted by: superspeed

[quote="tuxuser"]  
 [quote="l\_oliveira"]  
 It's NOT at the RF board guys...  
   
 Here's the culprit:  
 ISD2110 (21**[b]10[/b]** means it has enough memory for 10 seconds of playback at 8khz) which is a variation of ISD2100: "Digital ChipCorder with Multi Time Programing and Digital Audio Interface"  
   
 http://www.nuvoton-usa.com/downloads/isd2100datasheet.pdf  
 [/quote]  
   
 Source: [url=http://www.xboxhacker.org/http://libxenon.org//viewtopic.php?p=126672#p126672]http://www.xboxhacker.org/http://libxenon.org//viewtopic.php?p=126672#p126672[/url]  
   
 Chip is located here:  
   
 [attachimg=1]  
   
 Source: [url=http://forums.xbox-scene.com/index.php?showtopic=736761#]http://forums.xbox-scene.com/index.php?showtopic=736761#[/url]  
 [/quote]  
 EDIT: After doing some quick research on programming these you would 2 things.   
 1. A Elnec Beeprog+ {retail price $999.00}http://www.elnec.com/products/universal-programmers/beeprogplus/  
   
 2. A Elnec adapter "DIL48/QFN20-1 ZIF-CS ISD-1" {retail price $308} http://www.elnec.com/products/programming-adapters/?f=DIL48\_QFN20-1\_ZIF-CS\_ISD-1  
   
 There has got to be a cheaper way of programming these. If anyone finds out anymore info I would really like to know. It would also be pretty cool if we could upgrade the chip to the 2130 and have a full 30 second recording.

## 2012-09-22 17:54:16, posted by: tuxuser

https://github.com/georgepatterson/ISD17xx  
   
 The SPI protocol should be close (or identical?) to the x360 Chip: ISD2110  
   
 Somebody with arduino or similar wants to try? :D

### Attachments

[georgepatterson-ISD17xx-0b9004f.zip](georgepatterson-ISD17xx-0b9004f.zip)

## 2012-09-23 18:10:28, posted by: peshkohacka

It won't work Tux, the 21 family uses different command IDs. I would've played with it but my microcontrollers are dead and gone, here's however the official guide that list the commands for interfacing with the ISD21k: [url=http://www.scribd.com/doc/106699770/ISD21k]ISD2100 Design Guide[/url]

## 2012-09-28 17:28:12, posted by: mikeman

The pic above is not the isd chip[attachimg=1][attachimg=2]

### Attachments

[DSC01254.JPG](DSC01254.JPG)[DSC01256.JPG](DSC01256.JPG)

## 2012-10-08 23:40:30, posted by: g33k

Got bored, dug out my dusted AVR-USB-162 and started a little project.  
 [quote]This ISD2100 flash-library is neither complete nor extensively tested.  
 Take it as it is and use it at your own risk!!  
   
 The firmware was developed on an AT90USB162 (Olimex AVR-USB-162), but similar AVRs supported by LUFA may be compatible as well.  
   
   
 Requirements:  
 *) AT90USB162 or similar @ 3V3  
 *) LUFA-120730 or later (http://www.fourwalledcubicle.com/LUFA.php)  
 *) python-usb version 1.0  
   
   
 Pinouts:  
 PIN AT90USB162 ISD2100  
 SS PB0 (14) (3)  
 SCK PB1 (15) GPIO1 (2)  
 MOSI PB2 (16) GPIO0 (4)  
 MISO PB3 (17) GPIO2 (1)  
 BSY PB4 (18) GPIO4 (12)  
   
   
 usage: isd2100.py  
 status Shows status  
 int Shows interrupt status  
 pwrup Powerup device  
 pwrdwn Powerdown device  
 reset Reset device  
 id Shows device id  
 read Dumps device  
 write Writes device  
 flush Flushs device  
 voice Plays voice prompt  
 voicerg Plays voice prompt in register  
 macro Plays voice macro  
 macrorg Plays voice macro in register  
 stop Stops play  
 help Prints help  
   
   
 Thanks/Credits:  
 Thx to all who provided infos and of whom i may have borrowed code/ideas from.[/quote]   
 Didnt go deep into it, but my Trinity used following voice prompts and macros:  
   
 macros:  
 # description actions  
 3 tray open/close set volume, play sound, power down chip  
 4 power on/off set volume, play sound, power down chip  
 sounds:  
 # description  
 5 on/off sound  
 6 tray open/close 

### Attachments

[isd2100_20121008.tar.gz](isd2100_20121008.tar.gz)

## 2012-10-09 04:30:22, posted by: tuxuser

wow g33k, that looks great. thx alot. Can somebody borrow me an AVR162 pls? :D

## 2012-10-10 19:34:57, posted by: Juggahaxor

I tried last night and couldn't get this to compile using Atmel Studio 6.0 .... It wants to use the makefile to set the cpu type and something else :( ... Thank you for the release though i'm sure i'll get it working eventually.

## 2012-10-10 23:20:10, posted by: g33k

@Juggahaxor  
 MCU, frequency, ... are defined in Makefile. Unfortunately i cant help you with Atmel Studio but you might just use the cli-tools.  
   
   
 @all  
 attached a little script so show some info about dump.

### Attachments

[info.py](info.py)

## 2012-10-10 23:36:31, posted by: Juggahaxor

Yea after a nap I had a little more time to think about it .... Atmel studio does have an extension to get info from a Makefile but it does not like the one for this project , and I don't know enough about this IDE to make it work.  
   
 I am just going to define it in the code ;) Since it's the code that is bitching about it needing to be in a Makefile I am not going to use ...  
   
 I may end up actually getting one of those AVR jobs if I can find one , but for now I am attempting to compile for at ATmega328P - AKA Arduino 5v/16MHZ , but I am compiling it for the chip and not using the Arduino IDE.  
   
   
 Thanks for the reply i'll be back if I get anywhere with it.

## 2013-08-28 17:48:52, posted by: peshkohacka

I'm sorry to bump such an old thread, but here it goes...  
   
 Has anyone successfully programmed the ISD with the python script?  
   
 I've build the firmware for ATMega32U4, everything works fine, but i get random "Unknown device", even though everything is connected, shielded and grounded. I can read fine, but the result is 44.4 (instead of 44) KB and writing is incomplete (even writing the backup is not working correctly).  
   
 Is reading/writing bugged?  
   
 EDIT::  
   
 Correction. The writing works perfectly, the problems was my Python version was including 0xDA/0xAA randomly throughout the file and thus the size was exceeding the 0xB000 (44KB) of the ISD. If you don't use AT90USB162 keep a close eye on your PB ports and your OSC.