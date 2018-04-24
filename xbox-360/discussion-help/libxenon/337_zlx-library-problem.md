# zlx library problem

## 2012-07-21 03:00:01, posted by: ravendrow

so reformatted to see if a completely fresh install sorted some of my probs but i noticed when trying to reinstall ZLX Library i get this error [code]* *ravendrow@ravendrow-Satellite-A205:~/zlx$ make -f Makefile\_lib [Bgshader.cpp] [Browser.cpp] /home/ravendrow/zlx/zlx/Browser.cpp: In member function 'void ZLX::Browser::Run(const char*)': /home/ravendrow/zlx/zlx/Browser.cpp:446:38: error: 'bdev\_enum' was not declared in this scope /home/ravendrow/zlx/zlx/Browser.cpp: In member function 'void ZLX::Browser::Update()': /home/ravendrow/zlx/zlx/Browser.cpp:580:58: error: 'bdev\_enum' was not declared in this scope /home/ravendrow/zlx/zlx/Browser.cpp:640:13: warning: comparison between signed and unsigned integer expressions [-Wsign-compare] /home/ravendrow/zlx/zlx/Browser.cpp: At global scope: /home/ravendrow/zlx/zlx/Browser.cpp:114:18: warning: 'ZLX::FileInfoPanelPosition' defined but not used [-Wunused-variable] make[1]: *** [Browser.o] Error 1 make: *** [build] Error 2 [/code] was just wondering is there a fix? i did correct the select/back issue cause that came up to but this is what i got after fixing that

## 2012-07-21 10:12:27, posted by: ravendrow

k so i think i fixed it  
   
 i commented both instance of   
 [code]* *handle = bdev\_enum(handle, &s); [/code] in zlx/browser.cpp  
   
 changed [code]* * #include <diskio/diskio.h> [/code] to [code]* * #include <diskio/disc\_io.h> [/code] in zlx/hw.cpp  
   
 seems to compile ok now, can someone double check for me though? I just wanna make sure this got installed properly

## 2012-07-21 14:10:30, posted by: tuxuser

it compiles but it wont enumerate any devices now... you could use the mount code from xmplayer for example and integrate it into zlxbrowser.

## 2012-07-21 21:24:59, posted by: ravendrow

ok so just playing around i did  
 [code]* *#include <mount.c> [/code] in zlx/browser.cpp  
   
 tried to compile and it complained about issues with XTAF mounting so i commented that stuff and got it to compile again not even sure i am on the right path we will see i guess