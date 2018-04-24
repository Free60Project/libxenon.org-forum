# srand, time and the D-PAD

## 2011-07-28 07:13:40, posted by: zouloum

Hi, for some reason when I try to seed the random number generator, I get a "linking" error in the function \_gettimeofday\_r [code]srand(time(NULL));[/code] and also, for some reason, when I press down on the D-PAD, nothing happens.   
 The D-PAD needs to be pressed diagonally to register a value.  
   
 Also, here is the source if you want to take a look at it.  
 Its not really commented, but its only 150 lines.  
 [url=http://dl.dropbox.com/u/5921391/GuessMyNumberLibxenon/main.c]http://dl.dropbox.com/u/5921391/GuessMyNumberLibxenon/main.c[/url]  
   
 And here is the binary  
 [url=http://dl.dropbox.com/u/5921391/GuessMyNumberLibxenon/guessMyNumber.elf32]http://dl.dropbox.com/u/5921391/GuessMyNumberLibxenon/guessMyNumber.elf32[/url]