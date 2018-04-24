# Question about screen resolution.

## 2011-03-17 01:34:17, posted by: val532

How to use an other resolution of 1024*768 ? Like 1280*720, 1680*1050 or 1920*1080.  
   
 And is it posible ?

## 2011-03-22 07:37:26, posted by: val532

Any info ?

## 2011-03-22 15:14:53, posted by: Chrisoldinho

haven't done this myself as it seemed to just detect 720p on HDMI as the native resolution but in previous versions of ubuntu you could:-  
   
 dpkg-reconfigure xserver-xorg  
   
 and set the screen resolution in this.

## 2011-03-22 19:31:53, posted by: Sonic-NKT

GliGli wrote this about resolutions for libxenon: [quote] Anyway I was able to add 1280x720, 1440x900 and 1280x1024 (all VGA). 1440x900 is rendered as 1440x896 because EDRAM isn't big enough to render it. This is the highest resolution I can add for now because unlike the official games, libxenon doesn't render 3d as 1280x720 and then scale it up, instead it renders to the native resolution directly.[/quote] It should be the same for xell/linux...

## 2011-03-22 20:12:51, posted by: Juggahaxor

VGA output has been hardcoded too 1024x768. I can't say anything for HDMI as I don't have an HDMI console. You won't be able to change the resolution with the current framebuffer driver in linux, but I would suspect at some point this may be changed .. but for right now 1024x768 is safe for everyone, their we're issues where some of us who test could not display on our tiny screen (me). Hope that answers your question ... in short you can't right now.

## 2011-03-23 11:28:55, posted by: Sonic-NKT

HDMI is 1280x720 fixed, atleast thats on my arcade jasper.