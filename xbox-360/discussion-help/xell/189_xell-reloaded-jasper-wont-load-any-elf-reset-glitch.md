# Xell Reloaded (jasper) wont load any .elf reset glitch

## 2011-10-04 02:03:58, posted by: bob9595

Hello, i am having some trouble with my recently reset glitched falcon motherboard. I am on the latest Xell reloaded (as of 10/3/11) and am having some trouble. I have tried 3 usb sticks, 2 brands of dvd but can't seem to get any .elf files to load. I always get the "executing...." when its loading, but never farther than that, other times i just have xell reloaded reset on me. Anybody have any ideas ;D?

## 2011-10-04 02:11:08, posted by: Cancerous1

try using this one http://libxenon.org/index.php?action=dlattach;topic=157.0;attach=86

## 2011-10-04 02:27:23, posted by: bob9595

No go, i tried the new mupen64-360.elf and it just resets the console over and over again. Any other ideas?

## 2011-10-04 02:38:23, posted by: Cancerous1

did you already try using the xell i linked instead of the most recent?

## 2011-10-04 02:50:38, posted by: bob9595

Yup tried that one, its the 3rd version i have tried. Thanks for help by the way :)

## 2011-10-04 02:58:05, posted by: Cancerous1

are you trying the releases of mupen and pcsx-r, or are you building these yourself?  
   
 how is your usb stick formatted?

## 2011-10-04 03:07:25, posted by: bob9595

Formating in fat32, and there pre-built, and god i am a moron, i was just doing a jasper so i had jasper on the brain, this is a falcon sorry >.<.

## 2011-10-04 03:14:46, posted by: Cancerous1

if you're sure you replaced and tried those different versions of xell, the only thing left I can think of would be to try would be look for any debug info on uart if you have a device for that installed. Did this xbox work before you exploited it?

## 2011-10-04 04:00:37, posted by: Juggahaxor

What about the proper data files? You need the pcsxr folder and mupen64 folder with the background images etc or it also won't work. That is included with the release of Mupen64, not sure where I found them for pcsxr, but it will do the same thing you are describing if you don't have them, reloads Xell, or just crashes.  
   
 UART is very handy for figuring out the exact point at which it is crashing, and it's about $7 or less to get the proper level shifter. I use a 1TB fat32 formatted USB drive, and never have problems with detection unless the glitch takes so long the drive spins down, USB is a lot better than it used to be with Xell.

## 2011-10-04 12:47:46, posted by: bob9595

This motherboard did have a history with e74, got it fixed though (well, as well as somebody at home can "Fix it") ill try normal firmware tonight and see if it will boot that.  
   
 EDIT: re flashed to OFW, booted fine no e74, put back the xell-ecccc.bin, still no dice, kinda stumped, i must just be unlucky ;D. O and i have tried various .elfs, not just the psx or n64 emu, none of them seem to work   
   
 EDIT2: I got Linux\_basic to boot, and i could dump my 1bl nand and fuseset.. so the big question is, why wont anything else boot!