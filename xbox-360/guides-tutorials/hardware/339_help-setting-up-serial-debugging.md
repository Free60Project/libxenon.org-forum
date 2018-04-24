# help setting up serial debugging

## 2012-07-24 22:59:05, posted by: ravendrow

ok so i was going threw some of my stuff and i found and old liteon 7 series probe and i remembered that this probe uses the PL2303 driver and is a usb to serial converter. here are some pictures   
 http://imageshack.us/photo/my-images/715/dscn1273g.jpg/  
   
 http://imageshack.us/photo/my-images/811/dscn1274h.jpg/  
   
   
   
 there are 8 connection pads the ones on the top read  
 GND  
 RX  
 DTR  
 TX  
 VCC  
   
 when it was set up as a probe the DTR pad was bridged with the pad directly under DTR  
 and the bottom VCC pad was connected to the bottom Rx pad and bridged to Ground  
   
 can i use this to set up serial debugging and if i can how would i go about connecting it  
   
 i did try removing the wire that connected RX to VCC then i wired up RX TX and GND to my mobo but no love thanks in advance for any help you guys can give

## 2012-07-24 23:03:51, posted by: sk1080

try swaping rx and tx

## 2012-07-25 22:54:04, posted by: ravendrow

thanks bro worked perfect