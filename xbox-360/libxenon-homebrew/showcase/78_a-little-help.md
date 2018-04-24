# A little Help

## 2011-06-05 12:33:11, posted by: gomson

Hi guys,  
 I'm looking to purchase a serial port interface for sending debugging info from my jtag 360 to my pc. I was wonding if this would be okay:  
   
 [url=http://cgi.ebay.co.uk/USB-serial-adapter-PL2303-TTL-console-Recovery-RS232-/180642501560?pt=UK\_Computing\_CablesConnectors\_RL&hash=item2a0f21d3b8]http://cgi.ebay.co.uk/USB-serial-adapte ... 2a0f21d3b8[/url]  
   
 Please any info would be appreciated..  
   
 Thanks

## 2011-06-05 13:20:49, posted by: tuxuser

According to the datasheet it supports 3,3V on TTL so it *should* be fine  
 [url=http://www.stkaiser.de/anleitung/files/PL2303.pdf]http://www.stkaiser.de/anleitung/files/PL2303.pdf[/url]

## 2011-06-05 14:32:32, posted by: gomson

[quote=""tuxuser""]According to the datasheet it supports 3,3V on TTL so it *should* be fine  
 [url=http://www.stkaiser.de/anleitung/files/PL2303.pdf]http://www.stkaiser.de/anleitung/files/PL2303.pdf[/url][/quote]  
   
 Thanks for the reply....  
   
 I have a few more questions that just popped into my head...  
   
 1: Since the USB will be self powered, I shouldn't need to connect the two 3.3v cables to the xbox 360 motherboard but do I still need to connect the GND cable.  
 2: How exactly does the debugging code get sent back. I mean, if for example, I use one of the sample files from the Xbox SDK installation, I should be able to insert debugging code into the source code, compile it in visual studio, copy it over to the jtagged xbox 360, run the *.xex file and any debug info I've written should get sent back to the PC.....right..?  
 3: Also assuming that I buy the cable from the link in my earlier post, all I just need to do to get it working is: solder it to my jtag 360 and everything should be fine (plus also install drivers, Minicom or alternatives)... right..?  
   
 Just FYI, I'm not new to jtagging, I did everything myself but I am new to how to send debug info using a jtagged xbox, I've always been told only a dev kit can do it..  
   
 Please any info would be helpful.  
   
 Thanks.

## 2011-06-05 16:57:07, posted by: tuxuser

[quote=""gomson""]  
 1: Since the USB will be self powered, I shouldn't need to connect the two 3.3v cables to the xbox 360 motherboard but do I still need to connect the GND cable.  
 [/quote]  
 - From electrical view you should, yes. However, I had the problem when I joined the GND connections to not get any output from the UART so I am just using RX/TX from the box.  
   
 [quote=""gomson""]  
 2: How exactly does the debugging code get sent back. I mean, if for example, I use one of the sample files from the Xbox SDK installation, I should be able to insert debugging code into the source code, compile it in visual studio, copy it over to the jtagged xbox 360, run the *.xex file and any debug info I've written should get sent back to the PC.....right..?  
 [/quote]  
 - I can only say for printfs, they display over serial, yes. But please note that LibXenon.org does NOT support SDK Stuff!!! We are all about LEGAL/FREE homebrew.  
   
 [quote=""gomson""]  
 3: Also assuming that I buy the cable from the link in my earlier post, all I just need to do to get it working is: solder it to my jtag 360 and everything should be fine (plus also install drivers, Minicom or alternatives)... right..?  
 [/quote]  
 - Right!

## 2011-06-05 17:01:35, posted by: gomson

Thanks txmuxer..., and many apologies for the SDK stuff..point taken..  
   
 I'm planning to start using libXenon myself, there seems to a growing support for it and people willing to help you out..  
   
 Thanks again...  
 :D