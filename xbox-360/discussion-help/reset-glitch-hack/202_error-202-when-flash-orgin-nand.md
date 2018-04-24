# Error 202 when flash orgin nand

## 2011-10-15 08:02:22, posted by: changbom

I had sucess to reset Glitch in my xbox to get the DVD key. Affter done reset glitch i try to flash back to my orgin nand but got error 202 in block 1A40. Flash done but when power up xbox got 3 red light error. I've read nand 2 time before and there no difrent. I still can boot into xell if i flash .ecc file back :(. Check and no bad block in my dump nand. any one help me. Sorry for my bad english

## 2011-10-17 02:32:59, posted by: xb0xguru

0x1A40 shouldn't even be a problem. You only wrote to the 1st 50 blocks so you should only need to write these back. At it stands you only needed to dump the 1st 1000 blocks on a BB NAND.   
   
 If you're getting RRoD then there's possibly something else wrong.

## 2011-10-22 11:13:36, posted by: moco

Hey buddy, from my understanding, I'm pretty sure you gotta remove the glitcher and any nand programmer by way of de-soldering once you back to your original nand. I read somewhere that the xbox will go rrod if you try booting it with anything else attched with a stock nand. Hope this helps!