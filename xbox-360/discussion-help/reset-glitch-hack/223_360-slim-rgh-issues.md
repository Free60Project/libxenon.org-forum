# 360 Slim RGH issues

## 2011-11-06 22:48:33, posted by: seanr28

Im having a mere of a time with this slim, it just wont glitch! all connections are perfect, i have done 3 falcons and 2 jaspers that work fine, but this will not glich, using 270pf cap, changed the lengh of wires on CU\_rst but makes no difference, any suggestions.  
   
 I have proved all conection by testing continuety from alternative points and resistance......  
   
 Its a newer matte black one but does have the Hana chip.  
   
 regards  
   
 sean

## 2011-11-07 09:40:10, posted by: xb0xguru

What CPLD are you using?

## 2011-11-07 15:58:36, posted by: seanr28

Hauyo electronics at the minute, but to be honest with you, I have tried 2 different ones, I know one definatley works as I was using to test a jasper before hand.  
   
 This one ![](http://i166.photobucket.com/albums/u85/seanr28/red.jpg)[img]http://i166.photobucket.com/albums/u85/seanr28/red.jpg[/img]

## 2011-11-07 16:34:23, posted by: xb0xguru

Well I know from first hand these work fine.  
   
 Make sure you have R2 removed and the right pad of r3 is connected to the right pad of r1.

## 2011-11-07 17:06:30, posted by: seanr28

mmm ok I had right pad of R2 and not R3, I have since changed it, but still not glitching! Driving me mad, I had no trouble with jaspers and falcons at all (although the jasper didnt always glitch at least it did eventually.

## 2011-11-07 17:24:26, posted by: seanr28

just been changing the CPU\_rst wire for different lengths and still wont glitch!

## 2011-11-07 21:06:56, posted by: xb0xguru

Shouldn't matter as R2 and R3 right pads are linked.  
   
 Won't glitch at all? Try my phat 360 fix for CPU\_RST and put a 470pF capacitor in line.   
   
 http://libxenon.org/http://libxenon.org//viewtopic.php?p=1145#p1145

## 2011-11-07 21:46:33, posted by: seanr28

nope stil wont glitch, how quickly should the led illuminate for each time?  
   
 will give your suggestion ago now:)

## 2011-11-07 21:57:00, posted by: seanr28

ok, i dont have any 470s, on now have 220s, 270s and 680s...

## 2011-11-07 22:04:09, posted by: seanr28

something else that I have just noticed is that every few minutes my led illuminates for a about 2 seconds then continues in the normal way.

## 2011-11-07 22:11:00, posted by: a5m

solder 220 and 270 together (parallel) should add capcity.  
 did you try this?

## 2011-11-07 22:53:52, posted by: seanr28

starting to think that this 360 cant be glitched??  
   
   
 :-\  
 One other point, the C3B2 point on this board never had any soldier on,yet all the others I have seen have done, it maybe nothing, but I know all my wiring is good, tried 3 cool runners etc.......is is possible?

## 2011-11-08 00:08:34, posted by: xb0xguru

have you done a slim before ?

## 2011-11-08 00:32:10, posted by: seanr28

no, but I have been doing modchips etc for years, so its not like i have just started doing it. My understanding is that the as the LED is flashing all connections are good?? But clearly something is not right, I was given this to do, but after someone else had a go and pulled FT5R2 off, I have now used the alternative point. I have check and re-soldiered just to be sure. But I am now out of ideas, as I said have done 2 jaspers and a few falcons, they have all glitched, albiet the jaspers are a pain!

## 2011-11-08 02:49:42, posted by: xb0xguru

[quote="seanr28"]  
 no, but I have been doing modchips etc for years, so its not like i have just started doing it. My understanding is that the as the LED is flashing all connections are good?? But clearly something is not right, I was given this to do, but after someone else had a go and pulled FT5R2 off, I have now used the alternative point. I have check and re-soldiered just to be sure. But I am now out of ideas, as I said have done 2 jaspers and a few falcons, they have all glitched, albiet the jaspers are a pain!  
 [/quote]  
   
 Correction: Jaspers USED to be a pain. They're sorted now :)  
   
 Got a pic of your wiring etc?

## 2011-11-08 10:15:39, posted by: seanr28

just used your modifications for my jasper, now booting within 4-5 seconds and accasionally around 8!:) well pleased,  
   
 Ill get some pictures in a bit.

## 2011-11-08 11:28:36, posted by: seanr28

been testing the jasper and it would appear it freezes after about 20 mins or so. Any ideas?

## 2011-11-08 12:39:09, posted by: seanr28

just fitted a TX cool runner, now gllitches within 5 seconds! first time as well, I knew it wasnt my wiring......  
   
 ![](http://i166.photobucket.com/albums/u85/seanr28/P1010175.jpg)[img]http://i166.photobucket.com/albums/u85/seanr28/P1010175.jpg[/img]