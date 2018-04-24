# Falcon RGH Issue - Won't boot

## 2011-11-12 10:30:54, posted by: Wabby

Hi,  
   
 Just finished wiring up my falcon, and it wont boot. It just sits there with the green power light on.  
 I can hear the fans change speed every so often, so I assume the CPLD is trying to do the RGH?  
   
 I so far have done the following:  
 [list] - [*]Reflashed the CPLD with the JED file within the v1.1 folder
 - [*]Checked all wiring and its fine (I am, however, using 30AWG Kynar wire for all connections, is this ok?)
 - [*]Tried changing the 1k resistor for a 10k resistor
 - [*]Tried re-flashing the ecc to the nand, again
[/list] Does anybody have any suggestions so that I can get this baby booting?  
   
 Ta

## 2011-11-12 10:53:10, posted by: Wabby

I have also just tried taking 1.8v straight from the mobo - still no glitchy.

## 2011-11-12 13:17:05, posted by: xb0xguru

What CB values do you have in 360 Flash Dump Tool?

## 2011-11-12 13:43:32, posted by: spandaman

I would use thicker wire for vcc and ground, how long have you waited for it to boot?  
   
   
 Sent from my iPhone using Tapatalk

## 2011-11-12 21:08:14, posted by: Wabby

2BL (CB) = 5771  
 4BL (CD) = 8453  
 5BL (CE) = 1888  
   
 Also, in 360 Flash Dump Tool is says bad Key/KV and a bad block @ 00D5 and 0173.  
   
 Do I need to remap block 00D5 from eee.bin to 3FF?

## 2011-11-12 21:20:55, posted by: Cancerous1

use a thicker ground/power than kynar

## 2011-11-12 22:05:11, posted by: Wabby

Just tried that - Still wont boot.  
   
 How do I remap the bad block @ 04D so that the .ecc file will write properly and then Xell should boot?

## 2011-11-13 11:32:49, posted by: Wabby

Got it working.  
   
 For some reason I de-soldered 3.3v when soldering 1.8v - what a n00b!  
   
 Took it off in a rampage, and noticed it wasnt soldered! lol

## 2011-12-11 02:28:28, posted by: xB32

I have had similar problems as you, please could you tell me the current variables under which your Falcon RGH is working?