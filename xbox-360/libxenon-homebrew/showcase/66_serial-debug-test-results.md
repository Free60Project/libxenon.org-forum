# Serial debug test results

## 2011-04-19 12:16:38, posted by: UNIX

Hello everyone!   
   
 I received my RS232 to TTL converter yesterday in the mail. As it stands, I do not have any solder, so resting the wires on top of the correct points, I was able to data from the console. XeLL reported the serial interface as a device, this information was displayed before the USB polling. The data I received from the console was hexidecimal values, I only get fragments of text but this is most likely because I did not solder the wires down yet.   
   
 I just wanted to quickly post these results, and also thank everyone who helped me correctly set up my interface. I am getting some solder today to connect the wires properly.

## 2011-04-19 13:31:55, posted by: Meluxe

Hey there,  
   
 what about making some pictures? Maybe sb will do a proper tutorial for this site in future?!  
   
 thanks for working on it ;)

## 2011-04-19 15:39:22, posted by: tuxuser

[quote=""UNIX""] XeLL reported the serial interface as a device, this information was displayed before the USB polling.[/quote]  
 How's that possible?   
 XeLL does not output any additional info if you got a serial adapter soldered to the mainboard... it cant recognize it...  
   
 About the hex values.. which baudrate are you using.. and which image? Pure XeLL or a reb***er image?

## 2011-04-19 19:15:43, posted by: UNIX

Booting XeLLous from the nand, before USB polling it was printing a new line, I can't exactly remember what it was, all I remember was that it said something about CMD 12... I had never seen this up until now so I assumed it was because my serial adapter was attached... Anyway, I realised that my minicom settings were set to hexidecimal by default, which would explain why that's all I was receiving.