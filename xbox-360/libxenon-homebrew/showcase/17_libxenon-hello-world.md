# LibXenon Hello World?

## 2011-02-25 11:48:57, posted by: UNIX

First of all I'd like to express how excited I am that such a forum has been started, I have been wanting to get started with LibXenon for quite some time now but haven't really known where to start.  
   
 I have everything installed correctly and such, but the only code I can get to run is the auto compiled cube sample. I've tried using the sample on [url=http://www.free60.org/LibXenon\_Examples]http://www.free60.org/LibXenon\_Examples[/url] but it fails to compile due to 'xenos\_init();' having too few arguments.   
   
 I am just looking for some simple code which will just give me some kind of starting point. I have some experience with programming across multiple languages but have never used anything like this. I have many ideas I would like to start working on once I have an idea of where to start :D

## 2011-02-25 11:57:45, posted by: tuxuser

As new libxenon code from GliGli's github got pushed recently, the xenos\_init(); function slightly changed.  
 Try to make it:  
 [code]xenos\_init(-1);[/code] That will execute xenos\_autoset\_mode(); and the code should compile ;)

## 2011-02-25 12:07:27, posted by: UNIX

Thanks so much! I'm grabbing LibXenon now from gligli's github and installing the toolchain. I'll try to compile as soon as everything is installed and good to go :)

## 2011-02-25 13:03:16, posted by: UNIX

Nope, still nothing. When I change xenos\_init(); to xenos\_init(-1); I get undeclared references to everything else...   
 [code]undefined reference to `xenos\_init' undefined reference to `console\_init' undefined reference to `get\_controller\_data' [/code]

## 2011-02-25 14:13:27, posted by: tuxuser

Could you post your Makefile ?

## 2011-02-25 22:57:25, posted by: UNIX

I'm not using a makefile, I'm just using GCC to compile from the command line as I am only trying to compile the one file.

## 2011-02-26 04:49:00, posted by: UNIX

Thanks for providing that source code for me, it compiled and ran fine. I think I am beginning to understand more now. :)