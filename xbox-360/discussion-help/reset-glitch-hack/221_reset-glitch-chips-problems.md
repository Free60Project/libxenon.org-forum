# Reset Glitch chips problems .

## 2011-11-06 11:29:38, posted by: punkfloyd

Hi ,   
 This is my first post so if i mess up please go easy on me . I may be old but i`m delicate ..hehe .  
   
 OK . I bought these chips from ebay (china) for the purposes of the glitch hack . I`ve seen various versions of these and they all have various caps / resistors onboard and are said to be working . As you can see in my pics mine are pretty much blank. When installed all i can get is 0022 . I`ve tried zephyr and falcon . The falcon wouldnt go back to stock after trying and is now rrod but the zephyr flashed back to stock no problems .   
   
 If someone could just spend a little time with me to help me get these working as i`m sure they will eventually i`d be extremely grateful !  
   
 here`s the pics : if i need componants i have thousands !  
   
 ![](http://img.photobucket.com/albums/v474/pinkfloyd81/IMG_0033.jpg)[img]http://img.photobucket.com/albums/v474/pinkfloyd81/IMG\_0033.jpg[/img]  
   
 ![](http://img.photobucket.com/albums/v474/pinkfloyd81/IMG_0032.jpg)[img]http://img.photobucket.com/albums/v474/pinkfloyd81/IMG\_0032.jpg[/img]  
   
 a pic of the diodes etc installed . sorry for the quality  
   
 ![](http://img.photobucket.com/albums/v474/pinkfloyd81/IMG_0029.jpg)[img]http://img.photobucket.com/albums/v474/pinkfloyd81/IMG\_0029.jpg[/img]  
   
 ok ...all thats left to be said is please ...heeellllllllllllllllllp ...lol ..i`m going nuts !

## 2011-11-06 12:02:36, posted by: xb0xguru

First off, I'd address the problem where you can't flash a stock NAND back to a console. This is ultimately more important that anything else you're trying.  
   
 Secondly, you shouldn't be getting RRoD 0022 as the ecc code stops it from happening, which means you've not written it correctly.  
   
 Therefore before we even begin looking at the CPLD, you're having problems reading/writing to the console.  
   
 Take the time and read through the reset glitch guide CAREFULLY and follow ALL steps EXACTLY when writing to the NAND.

## 2011-11-06 12:25:41, posted by: punkfloyd

Hi ,   
 Thanks for the reply .   
 I`m pretty sure i`m doing what it says in the guide . I`m using the 1.1 hack tutorial . I`ll outline what i`ve done .   
   
 I programmed the chip fine and got a "progam succeded" and "verify succeded" using Impact and a parallel 3 cable so no probs there.   
   
 as for the nand :  
   
 I installed python and pycrypto as per the tut , I`m using windows 7 and couldnt get it to work as a comand by adding it to the system variables , tried over and over with no joy so i`m just doing everything within my python dir and it works fine .  
   
 i`ve edited the build.py with "secret\_1BL = "\x00\x11\x22\x33\x44\x55\x66\x77\x88\x99\xAA\xBB\xCC\xDD\xEE\xFF""   
   
 I put my orig nand called "nand.bin" , which i obtained using nandpro and my nand-x ,into the root of python dir and created an output dir .  
   
 I used the python command "python common\imgbuild\build.py nand.bin common\cdxell\CDjasper common\xell\xell-gggggg.bin " and that gave me a "image\_00000000.ecc" into my output dir .  
   
 I wrote that to my nand using nandpro and my nand-x using this command " nandpro usb: +w16 image\_00000000.ecc"  
   
 I think i`m doing it correctly .

## 2011-11-06 18:37:31, posted by: punkfloyd

I`ve now tried the alternetive fat method . Drawing 1.8v from the onboard voltage regulator and thats fixed the rrod but now i just get a black screen . (zephyr) . I`ve checked pin 15 on the chip for a 3.3v output but i get nothing on the multi meter. Can`t hear any change in the fans or a noise from the power supply , there is a slight rev UP on the fans every so often but it doesnt seem regular to me and i`m pretty sure it shuld be a drop in speed.  
   
 Does anyone have any ideas at all ?? i`ve checked my woring a million times and it looks ok .   
 I`m sure the software is good . I`m stumped now.

## 2011-11-06 21:42:29, posted by: AiLEX

I have exactly the same board from china, works fine on my jasper 512, CB 6751.   
 Did you tried command with common\cdxell\CD (not CDjasper)? Also secret\_1BL should be ***. // edit by tuxuser: Please dont post MS copyrighted stuff / encryption keys  
 And be sure that your wire from CPU\_PLL\_BYPASS pin not too close to the throttles on xbox board.

## 2011-11-07 02:23:27, posted by: rockla

Ailex is your console all good since I'm too on cb 6751 and have concerns before performing the glitch

## 2011-11-07 02:24:45, posted by: rockla

Aleix check pm

## 2011-11-07 23:16:21, posted by: punkfloyd

[quote="AiLEX"]  
 I have exactly the same board from china, works fine on my jasper 512, CB 6751.   
 Did you tried command with common\cdxell\CD (not CDjasper)? Also secret\_1BL should be ***. // edit by tuxuser: Please dont post MS copyrighted stuff / encryption keys  
 And be sure that your wire from CPU\_PLL\_BYPASS pin not too close to the throttles on xbox board.  
 [/quote]  
   
 Hello mate   
 Yeah i know the characters arent right in the 1bl but i`m not allowed to post them . starts with xdd i know i got the right ones. I`ve tried both CDjasper and just CD now , same outcome . just a green light and nothing . No sounds of fans slowing down . Nadda. It`s driving me insane because i know i can do this i`ve been jtagging for donkeys years lol . I tried today on a Falcon CB 5771 today and same thing . I just dunno what i`m doing wrong or wether i`m not using these chips right . I`ll know in a couple days as i`ve got some TX coolrunners coming . At least i`ll know they are completely ready to go out of the packet.