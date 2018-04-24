# LibXenon toolchain

## 2017-08-01 22:49:08, posted by: <Unknown User>

Hi,  
   
 I tryed to install LibXenon toolchain on my windows under MySYS2 with this [url ="http://free60.org/wiki/Xenon\_Toolchain"]link[/url]  
   
 ToolChain installed successfull and add the 2 line in my bash file and reboot cmd command for take effect  
   
 When I try to compile xell-reloaded I have error message   
 [code]Dev@Dev-PC MINGW64 ~/xell-reloaded $ make Building xell-1f ... [startup.S] make[1]: xenon-gcc: Command not found make[1]: *** [Makefile:48: source/lv1/startup.o] Error 127 make: *** [Makefile:40: xell-1f.build] Error 2[/code] And under /usr/local/xenon I have nothing, the folder is empty maybe it's not normaly   
   
 Thx for your help

## 2017-11-02 13:19:49, posted by: <Unknown User>

Would suggest dumping the mingw environment and using an Ubuntu virtualbox to run a true linux system. I never could get the toolchain to run or compile properly on Windows. Somewhere out there is a virtualbox disk image with the latest (still very old at this point) Xenon toolchain already installed and fully configured in the compile paths. If I find it I will post it here.