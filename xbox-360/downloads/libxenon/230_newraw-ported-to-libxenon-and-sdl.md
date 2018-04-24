# NewRAW -ported to libxenon and SDL-

## 2011-11-15 19:58:00, posted by: MagicSeb

Hi, i have tried to make a runnable version of RAW -Another world Interpretor-  
   
 Actually, these things works :  
   
 - Protection Wheel  
 - In-game save and load  
 - Joystick  
 - Audio sound  
 - Bypass protection test=> on my personal dump  
   
   
 Things doesn't work :  
 all ok  
   
 Things still buggy :   
   
 Sound  
   
 I have used the latest gligli libxenon, and libSDLXenon from lantus.  
   
 Original another world files should be put in "raw" directory on uda:  
   
 If someone can fix the latest bugs ?  
   
 Fixed :   
   
 Most of bugs except sound, still little bit jerky.

### Attachments

[NewRAW.zip](NewRAW.zip)

## 2011-11-15 20:24:46, posted by: Cancerous1

cool thanks for sharing, i always liked that game, as frustrating as it was to beat

## 2011-11-15 21:05:29, posted by: lantus360

nice port.  
   
 interesting that the sound isnt working for you. I will take a closer look and see whats up  
   
 cheers!

## 2011-12-02 01:49:12, posted by: Pa0l0ne

Much Appreciated!!! :) :) :)  
   
 I have compiled succesfully on my Ubuntu 10.04  
 latest GliGli libxenon (gligli-libxenon-a7c88d8)  
 Lantus libSDLXenon  
 Lantus SDL\_Mixer  
   
 The Sound Play correctly and i have not segmentation fault  
   
 P.S. Using the protection wheel remind me when i play this game for the first time on Amiga 500 in the 90'....

## 2011-12-02 17:58:08, posted by: MagicSeb

Can you play after level 1 ?  
   
 And can you post your elf too ^^

## 2011-12-02 19:40:10, posted by: MagicSeb

Yes ! Finally it's working !  
   
 NO change in my main code, probably a bad compile of libxenon AND:OR bad compile of SDL  
   
 Big thanks to Pa0l0ne, for showing me the mistake.  
   
 Enjoy now, Another World in a fully libxenon version.

### Attachments

[NewRAW.elf32.zip](NewRAW.elf32.zip)

## 2011-12-02 19:42:46, posted by: lantus360

i think gligli's changes to thread safe malloc() in libxenon fixed this.  
   
 excellet work MagicSeb. This game is a classic

## 2011-12-02 19:45:46, posted by: Ced2911

there is some issue with sound, i don't know why but you need to check that hdmi sound is set to stereo in dashboard, the settings seem to change for me

## 2011-12-02 22:38:15, posted by: MagicSeb

I have also made a port of REminiscene engine. Still buggy sounds... I will post it later.