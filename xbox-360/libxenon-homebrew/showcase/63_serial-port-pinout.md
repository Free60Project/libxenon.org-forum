# Serial Port Pinout

## 2011-04-10 11:13:40, posted by: UNIX

I'm looking to assemble a serial port interface so that it is easier to debug my code. There is an article of [url=http://free60.org/Serial\_Console]Free60[/url], but it isn't very in depth. Can anybody explain to me where the wires on the board should be connected to the serial port itself?   
   
 Thanks :)

## 2011-04-10 13:29:52, posted by: tuxuser

Hi,  
   
 It depends on your serial converter.  
 If it needs an external power source (VCC) you connect the + line (3,3V) and GND to it.  
 If it has its own power supply, you dont connect it.  
   
 In any case you connect RX / TX to the according pins on your serial adapter. If you are unsure where these pins are, consult the datasheet.  
   
 Greetz  
 tux

## 2011-04-11 01:20:01, posted by: UNIX

Thanks Tux,  
   
 Just looked at the serial port I will be connecting to and I should be fine just using the RxD and TxD pins. I was just a little unsure about the 3.3v and GND pins and where they should go. I'll get my DB9 connector and serial cable tomorrow and I will port results of the installation :)

## 2011-04-11 23:55:55, posted by: Gene

Please do notice that you need TTL adapter in order to use that serial port of 360.  
 Without that you will fry either one, COM or 360's serial.  
   
 Here is DIY version of the adapter if you dont want to buy pre-made adapter from e.g. ebay:  
 [url=http://picprojects.org.uk/projects/simpleSIO/ssio.htm]http://picprojects.org.uk/projects/simpleSIO/ssio.htm[/url]

## 2011-04-12 02:20:21, posted by: UNIX

Even though my PC serial port is self powered? All I plan on using is a standard female serial cable cut in half and connecting the 3 needed wires to the board.. Is it absolutely necessary to get one of these?

## 2011-04-12 08:38:03, posted by: Gene

Yes it is. PC serial port (RS232) uses -12V/+12V when the Xbox's serial uses TTL logic levels (0V/3.3V).  
   
 I've used similar to this one with my routers:  
 [url=http://cgi.ebay.com/New-MAX232-RS232-TTL-Converter-Adapter-Module-Board-/220740156970?pt=LH\_DefaultDomain\_0&hash=item3365237e2a]http://cgi.ebay.com/New-MAX232-RS232-TT ... 3365237e2a[/url]

## 2011-04-12 19:06:46, posted by: UNIX

Alright, well thanks for informing me before I fried either my JTAG or my PC haha! I'll see if I can pick one of those up :)

## 2011-04-14 23:08:26, posted by: ddxcb

Ive been using one of these  
   
 [url=http://cgi.ebay.com/USB-RS232-TTL-Module-cp2102-/280556942025?pt=BI\_Electrical\_Equipment\_Tools&hash=item41527f32c9]http://cgi.ebay.com/USB-RS232-TTL-Modul ... 41527f32c9[/url]  
   
 cheap and work great.

## 2011-04-15 05:08:07, posted by: UNIX

I ended up going with this one:  
 [url=http://cgi.ebay.com/RS232-Serial-Port-TTL-Converter-Module-SP3232-LED-/380319575807?\_trksid=p5197.m7&\_trkparms=algo%3DLVI%26itu%3DUCI%26otn%3D1%26po%3DLVI%26ps%3D63%26clkid%3D8462783874687676565]http://cgi.ebay.com/RS232-Serial-Port-T ... 4687676565[/url]  
   
 A few dollars more expensive, but the ones you guys referred me to are in China, take forever to ship to here :P  
   
 RxT, DxT, and 3.3/5v input. Can't wait to start debugging proper. Thanks everyone for item suggestions and clarification!

## 2011-04-16 13:22:55, posted by: UNIX

One more question, what program (Linux) do you guys recommend for capturing the debug strings from the console? Is Minicom ok?  
   
 Thanks :)

## 2011-04-16 14:16:44, posted by: tuxuser

Yes, minicom is great for that :)

## 2011-04-16 19:19:15, posted by: UNIX

Cool, just wanted to make sure. Thanks Tux and everyone for all your help!