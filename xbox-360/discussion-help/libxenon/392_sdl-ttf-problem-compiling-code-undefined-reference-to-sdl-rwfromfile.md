# SDL_ttf problem compiling code (undefined reference to `SDL_RWFromFile')

## 2013-02-01 03:27:05, posted by: Mac1512

Hello, I turn to you, because I have a problem compiling code using SDL\_ttf.  
   
 The problem is as follows:  
 [code]* *linking ... Letras.elf /usr/local/xenon/usr/lib/libSDL\_ttf.a(SDL\_ttf.o): In function `TTF\_OpenFontIndex': SDL\_ttf.c:(.text.TTF\_OpenFontIndex+0x2c): undefined reference to `SDL\_RWFromFile' collect2: ld returned 1 exit status make[1]: *** [/home/mac1512/Letras.elf] Error 1 make: *** [build] Error 2 [/code] I would be grateful if I lend a hand with the problem.  
   
 P.D sorry for my English using google translator  
   
 Best Regards

## 2013-02-04 08:40:28, posted by: Ced2911

try to change lib order

## 2013-02-05 20:48:46, posted by: Mac1512

You're right, I changed lib order and I could successfully compile the code ....  
   
 Thank you very much !!! :)