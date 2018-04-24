# Jasper 521Mb Glitch issue

## 2011-09-17 13:44:49, posted by: seanr28

I have completed the Glitch hack on my jasper, I have sucessfully flashed the CPLD device for the jasper 360, wiring is perfect, and has been checked many times. I have created and flashedd the ECC file created using a copy of the original Nand, yet it turns on and just sits there doing nothing, solid green light in middle but thats it....no RROD either. I have not used the glitch generators by bestpig or sneakypeanut   
   
 I have left it running for over 5 minutes and still nothing changes.  
   
 Anybody shed any light?  
   
 Its not my soldering, I have been modding consoles for years, sold loads of jtags etc. But clearly something is not right.........

## 2011-09-17 14:45:36, posted by: Diggs

Out of curiosity how are you connecting the xbox to your tv? HDMI didn't work for me originally (required changes to libxenon). Have you tried normal composite av leads?

## 2011-09-17 18:40:14, posted by: Cancerous1

if the ecc image you flashed is correct pin 30 on the CMOD going to post\_out should be alternating from 1v and 0v  
 what version is CB if you open your original dump in flash tool?

## 2011-09-17 19:28:18, posted by: ar1424

what is your wiring AGW...I had the same problem I changed all my wiring to 26agw and 22agw for the ground and it worked.

## 2011-09-17 22:42:00, posted by: seanr28

[quote="Cancerous1"]  
 if the ecc image you flashed is correct pin 30 on the CMOD going to post\_out should be alternating from 1v and 0v  
 what version is CB if you open your original dump in flash tool?  
 [/quote]  
   
 ok its CB: 6750  
   
   
 willl check pin 30 asap

## 2011-09-17 22:43:31, posted by: seanr28

[quote="ar1424"]  
 what is your wiring AGW...I had the same problem I changed all my wiring to 26agw and 22agw for the ground and it worked.  
 [/quote]  
   
 not sure I used an old IDE cable as I have seen many other do without an issue.

## 2011-09-22 00:36:21, posted by: seanr28

>:(

## 2011-09-22 00:47:14, posted by: seanr28

finally got it working.......well it workked once, then after a reboot it wont work again!! any ideas?

## 2011-11-02 21:06:55, posted by: ddsdavey

It was probably always working Sean,half the battle with RGH issues (imo) is the head games lol that come with it.It dosnt help that when perfect the glitch is still not perfect!  
 I couldnt get a slim to boot earlier but im sure it was just slow and i was impatient!  
 So i wrote the image again and it booted intantly...once! Again its head games,coincidence.And no doubt Sean your set up has probably always been correct.  
 Anything but falcons suck from my experience,falcons are amazingly quick every single time!

## 2011-11-11 01:05:52, posted by: seanr28

finally got it glitching much quiker, but now freezes after about 20 mins. any ideas?