# Using Xenos Sound Driver ?

## 2013-01-20 18:41:00, posted by: shortstop

I just would like to play simple fx sounds and musics in my homebrew game.  
 I am not able to find an example or tutorial on using the xenon\_sound driver.  
   
 Here follows the code i use today ( copy from the megadrive emulator sound engine found by googling ). [code]* *#include <xenon\_sound/sound.h> ... if ( xenon\_sound\_get\_unplayed() > 0 ) { // attends que ce soit libre } else { xenon\_sound\_submit( pcm\_data, pcm\_length ); } [/code] For my first test, the buffer array "**[b]pcm\_data[/b]**" and its size "**[b]pcm\_length[/b]**" were obtained by using a command line : "**[b]raw2c.exe sfx.wav[/b]**" with a sound wav file. As expected, i obtain a sound but not the good one so i have made some mistake !!  
   
 [u]Question : [/u]How to make it work ? Do i just have to transform my wav file in a RAW PCM format with special frequency and bit rate ?  
   
 Thank you for your help.

## 2013-01-22 15:52:41, posted by: Ced2911

the sound must use the good format,  
   
 from:  
 https://github.com/Ced2911/libxenon/blob/master/libxenon/drivers/xenon\_sound/sound.h#L8  
   
 48khz, signed 16bit stereo.  
   
 you must stream the sound if the length is big