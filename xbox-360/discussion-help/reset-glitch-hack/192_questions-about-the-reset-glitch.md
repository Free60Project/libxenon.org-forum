# questions about the reset glitch

## 2011-10-09 17:40:49, posted by: PDJ

Hi I'm new to this forum, I have a glitched box, but I have some questions about the glitch wich I couldn't find on the net, maybe someone knows in here.  
   
 First, what's the reason why it doesn't work on a Xenon?, the difference is the ANA and HANA, but that coudn't be the reason, the only thing the coolrunner needs is the 48Mhz clock, and it's on both versions available.  
   
 When the glitch attempt fails, what is the (most likely) reason for that? reset pulse length not right? or is it the timing? (when applied) if it's the last one, is it an idea to count the read cycles of the flash to have a better timing? (just an idea)  
   
 On the coolrunner, what's the purpose of the capacitor? (is the VHDL source also available somewhere?)

## 2011-10-12 17:07:53, posted by: PDJ

anyone?  
   
 Or does somebody know where I can find this info? or a better place to ask these questions?  
   
 Thanks in advance.

## 2011-10-12 17:16:46, posted by: Cancerous1

from what i understand, trying to glitch the xenon most often resulted in the cpu entering a state that it could not be recovered from. At least that is the information i absorbed, recalled to the best of my ability, but you could always try it yourself and see what happens.

## 2011-10-12 17:22:37, posted by: PDJ

Thanks for the answer.  
 Well I wanted to try that, but all the standard tools to build a patched NAND didn't work because they detect it's a xenon and before I put time into it, I wanted to ask first.  
 I tought the CPU is the same as in all other boxes? or are there differences?