# Proplerly setting up SDL?

## 2011-06-25 05:39:06, posted by: UNIX

Hey guys,  
   
 I want to know if anyone knows how to properly set up SDL with LibXenon. I have done a lot of experimentation with using LibXenon alone to utilize the GPU, but the process is very long. Writing an HLSL shader, compiling it into binary format which requires a virtual machine, converting images to arrays.. I have tried already to set up SDL in the /usr/local/xenon/usr/include directory, and also made sure that I am using -lSDL in my makefile, but I always get syntax errors in building as if SDL is not included. Normal projects including SDL work fine, it is only with LibXenon that I have build errors.   
   
 Has anyone successfully used SDL in any of their own projects? If so care to share how? :)

## 2011-06-25 05:53:39, posted by: Juvenal

just taking a quick look at the source i dont think it would work properly with libxenon right now anyway.  
   
 i see mutex and threading, which is the same reason lwip's netconn api doesnt work in libxenon.  
   
 correct me if i'm wrong.

## 2011-06-25 20:19:59, posted by: dreamboy

[quote="UNIX"]  
 Hey guys,  
   
 I want to know if anyone knows how to properly set up SDL with LibXenon. I have done a lot of experimentation with using LibXenon alone to utilize the GPU, but the process is very long. Writing an HLSL shader, compiling it into binary format which requires a virtual machine, converting images to arrays.. I have tried already to set up SDL in the /usr/local/xenon/usr/include directory, and also made sure that I am using -lSDL in my makefile, but I always get syntax errors in building as if SDL is not included. Normal projects including SDL work fine, it is only with LibXenon that I have build errors.   
   
 Has anyone successfully used SDL in any of their own projects? If so care to share how? :)  
 [/quote]  
   
 Tuxuser managed to set and compile SDL library by using the following SDL tutorial in Tutorials section:  
   
 [url=http://libxenon.org/http://libxenon.org//viewtopic.php?t=4]SDL Setup Tutorial[/url]

## 2011-06-26 01:53:36, posted by: tuxuser

[quote="dreamboy"]  
   
 Tuxuser managed to set SDL library **[b]and compiled sdl\_demo by using the following steps[/b]**  
 [/quote]  
   
 Where did you get that info? I compiled SDL, yes.. but not the demo itself

## 2011-06-26 04:45:14, posted by: dreamboy

[quote="tuxuser"]  
 [quote="dreamboy"]  
   
 Tuxuser managed to set SDL library **[b]and compiled sdl\_demo by using the following steps[/b]**  
 [/quote]  
   
 Where did you get that info? I compiled SDL, yes.. but not the demo itself  
 [/quote]  
   
 sorry my mistake ;)

## 2011-06-26 07:19:41, posted by: UNIX

I'll try and write something up from scratch later today. I just can't seem to get that particular sample to compile. I tried to take an easy way out, and compile an SDL program using Debian on my 360, then running via XeLL.. :p

## 2011-06-26 10:27:43, posted by: dreamboy

[quote="UNIX"]  
 I'll try and write something up from scratch later today. I just can't seem to get that particular sample to compile. I tried to take an easy way out, and compile an SDL program using Debian on my 360, then running via XeLL.. :p  
 [/quote]  
   
 yeah i couldnt compile it sdl demo either, but got new libraries that i was missing on ubuntu, Ced2911 sent them to me yesterday, gonna give a try after i sleep a bit cause i just got home from work..