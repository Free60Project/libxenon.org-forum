# HDMI issues (Video boot order)

## 2011-12-20 21:35:50, posted by: GhaleonX

Ok, so I realize that many, if not most people have a different video setup than I, so it's probably not been an issue for anyone other than myself.  
   
 Can we change the order of which connection it checks for to use (for video display)? I have a monitor hooked up via HDMI, but I use the audio breakout cable (which registers as a composite video adapter, iirc) to hook my speakers up. If I boot with both HDMI and my audio cable plugged in, then I will get no display, however if I boot with just HDMI, then later insert my audio cable, all is good. If I hook my audio cable up after xell loads, but before I load my elf, then I will get no display, also.  
   
   
 Also, would be nice if we could disable audio from HDMI completely, as my monitor seems to have come with some shitty speakers I'd rather not hear (I suppose I could take it apart and just cut the wires or even wire up a toggle).   
   
 Cheers.

## 2011-12-21 00:25:13, posted by: tuxuser

The way that Xbox sees the AVPacks (Videocables): Certain pins on the Connector are bridged so the XBox can differ the different types of cables. you could rip apart your adapter, remove the bridge of it and see if sound still works. If no bridge is present the 360 should see just the "avpack" ID of the HDMI cable.. and XeLL and other homebrews will set the correct mode.