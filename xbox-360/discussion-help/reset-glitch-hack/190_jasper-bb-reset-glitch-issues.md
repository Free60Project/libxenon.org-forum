# Jasper BB Reset Glitch issues

## 2011-10-06 12:55:13, posted by: xb0xguru

Hi  
   
 I hate my first post to be asking for help, but I feel I've exhausted all other options.  
   
 I have a BB Jasper here which I'm trying to get the CPU key from.  
   
 I've programmed my CPLD with the latest jasper.jed successfully.  
 My wiring is all good. I'm using 30AWG for everything apart from 3.3v, not that I think this matters. Continuity all good and double checked. I can solder :) I'm also keeping my wires as short as possible.  
 My 64MB NAND dump is good - no bad blocks anywhere and checks out.  
 My ecc build using the latest 1.1 release is also good:  
   
 http://pastebin.com/C7egpHSZ  
   
 I've tried with CD and CDjasper with no change.  
   
 I can also flash the original 50 blocks back and it boots fine.  
   
 Finally, I've already managed to do 2 falcons which we no bother at all - both fire up in less than 5 secs every time.  
   
 Any advice or help would be grateful - I did ask on IRC and Cancerous tried his best to assist, but time was against me (it was 5am here when I signed off).  
   
 The only thing about this Jasper is that it has a CB of 7651.  
   
 I can supply whatever might be needed APART from POST codes as I don't have an LED board yet!  
   
 Martin

## 2011-10-06 23:27:28, posted by: tydye81

Can you post your build.py output?

## 2011-10-07 01:32:09, posted by: xb0xguru

It's in the pastebin link in the first post.  
   
 I've since tried also with a donor CB.6750.bin file to see whether it helps or not, but still no joy:  
   
 http://pastebin.com/7Qn5pLai  
   
 Tried both with CD and CDJasper.

## 2011-10-07 04:35:16, posted by: hdtvman

any ideas on this? I have a BB 512 I'm not able to do either....

## 2011-10-08 14:52:38, posted by: covenant

Worth having thicker (than 30 AWG) wire on the ground (as well as VCC) from the CPLD to the XBox chassis. I used some cable from an old Molex connector I had and it works well.  
   
 That may not be the root problem but easy to put in and at least rules it in/out. HTH.

## 2011-10-08 15:00:48, posted by: xb0xguru

[quote="covenant"]  
 Worth having thicker (than 30 AWG) wire on the ground (as well as VCC) from the CPLD to the XBox chassis. I used some cable from an old Molex connector I had and it works well.  
   
 That may not be the root problem but easy to put in and at least rules it in/out. HTH.  
 [/quote]  
   
 I've tried about every configuration of wiring so I really don't think that's the problem. I have an LED on the debug pin 15 and it pulses away nicely. The last thing I saw on the IRC channel was from Gligi stating that CB 6751> are not do-able yet. This would make more sense since I've happily had three other consoles up and running (Falcon) in the last week.

## 2011-10-22 18:54:38, posted by: seanr28

i have had a similar issue, 512mb Jasper takes some time to glitch and in some instances does'nt glitch at all, usually after many reboots it does finally glitch and work very well

## 2011-10-24 19:14:43, posted by: xb0xguru

Well I used this CPLD exactly as wired previously (but re-programmed to Falcon) on another board and it glitched right away. I can NOW see what the LED should do. It lights for about .5 seconds and then I get the blue screen. With the BB Jasper I had, it wasn't lighting as such, just a very faint but quick flicker every 4-5 secs. So it was definitely trying to do it but not succeeding.

## 2011-10-30 23:31:35, posted by: seanr28

your saying that you used the jed file for a falcon and it worked for the jasper?

## 2011-10-31 17:18:54, posted by: xb0xguru

No, it's still a Jasper-programmed CPLD.  
   
 CPU\_PLL\_BYPASS is definitely the culprit here. A longer wire (30-50cm) and perhaps swapping the 22k resistor on Pin 13 with a 10k might prove to give you better results.  
   
 EDIT: It's either CPU\_PLL\_BYPASS or CPU\_RST :)

## 2013-08-09 10:57:34, posted by: ArnoldCaldwell

[quote="xb0xguru"]  
 [quote="covenant"]  
 [u]Worth having thicker (than 30 AWG) wire on the ground (as well as VCC) from the CPLD to the XBox chassis. I used some cable from an old Molex connector I had and it works well.  
   
 That may not be the root problem but easy to put in and at least rules it in/out. HTH.[/u]  
 [/quote]  
   
 [u]I've tried about every configuration of wiring so I really don't think that's the problem. I have an [url=http://www.niceledlights.com][color=black]led light[/color][/url] on the debug pin 15 and it pulses away nicely. The last thing I saw on the IRC channel was from Gligi stating that CB 6751> are not do-able yet. This would make more sense since I've happily had three other consoles up and running (Falcon) in the last week.[/u]  
 [/quote]  
   
 Nice thought of using led.. I will now try it and hopefully it works fine for me..