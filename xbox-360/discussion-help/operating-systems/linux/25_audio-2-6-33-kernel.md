# Audio 2.6.33 kernel

## 2011-03-06 15:34:22, posted by: Chrisoldinho

Hello,  
   
 2.6.33 kernel has audio support which is great :D but the kernel fails a lot, and when sound does play it crackles.  
   
 Does anyone else experience this?  
   
 It seems to be the same with HDMI and VGA.  
   
 Chris.

## 2011-03-06 23:25:22, posted by: tuxuser

You get sound over HDMI??? With the HDMI cable or the additional audio adapter?  
   
 Crashing is cause of the spinlock issues in the kernel.. or the audio driver itself.. I am not sure about that currently.

## 2011-03-07 17:28:47, posted by: Juggahaxor

From my experience it does seem to be related to sound ... anytime i try to play a sound it most definitely deadlocks. However it also does it randomly , then again it didn't start doing it so frequently until i installed a full OS the Gentoo Live disc was fine and it didn't lock up at all during the Debian install, but as soon as i got gnome and KDE installed and had sound working again, BAM it started doing it again. It also seems to do it right after the sound is initialized during boot sometimes.

## 2011-03-07 20:18:29, posted by: Chrisoldinho

i love typing posts whilst using my 360 :)  
   
 Yes, sound kind of works via HDMI, no optical connector, just straight into TV.  
   
 However, when I say it works, it is not useable due to system freezes and errors with kernel on playback. I have just heard it a couple of times when logging into Gnome on debian.

## 2011-03-15 19:55:47, posted by: kpozn360

when it boots, i have jingle sound, but when it runs after login i can't play sounds, alarm clock runs one time and crash§  
 i use vga  
 debian 6 squeeze

## 2011-03-16 01:38:53, posted by: charlo.charli

I got a Jasper and i got no sound using HDMI (don't have optical device to test)... I've tested ubuntu 10.10 BETA, didn't tried the last gentoo.