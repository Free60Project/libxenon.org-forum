# Hanging at &quot;fat mount uda0&quot;

## 2012-12-09 01:31:49, posted by: XenonBliss

So, I have just compiled GliGli's Libxenon and toolchain, and free60projects XeLL. I flashed my nand with xell by renaming xell-gggggg.bin to updxell, and when I turn it on, it works but justs hangs at fat mount uda0. Is this a known problem or did I do something wrong?

## 2014-02-10 01:33:46, posted by: oleost

Hi, got the same issue. tried both Xellous and Xell reloaded flash using ***. Hangs on "fat mount ud0"  
   
 I need to remove dvd drive and then it boots :/  
   
 Edit:  
   
 Im looking at some of the latest commits to github, and it mentions something about disabling the dvd drive using config.h. Anyone know how I do it? https://github.com/Free60Project/xell/blob/Swizzy/source/lv2/config.h  
   
 Edit2: Just want to say, to "fix" it I replaced the xell files in xebuild with and older Xell(XeLL\_Reloaded-2stages-v0\_991.tar.gz) since I dont have any HDMI anyways (Xenon xbox)

## 2014-02-18 23:21:39, posted by: Swizzy

This is a known issue... i've sorta fixed it in the newer libxenon code... it seems to mainly effect Hitachi drives and/or Liteon drives (when the tray is open)