# Several questions about libXenon

## 2012-02-29 06:39:15, posted by: andrewd207

Hi, this is my first post so please be nice :)  
   
 I'm sure this stuff is common knowledge if you've been here for a while but I couldn't find up to date answers with the Search Button :(  
   
 Q: What is libXenon? Is it linux? It seems very similar to linux when booting. A quick look at the sources didn't reveal linux.  
   
 Q: Is every libXenon app essentially a kernel? I.e each libXenon application contains code to access the hardware on the lowest level.  
   
 Q: Does libXenon provide gpu accelerated 3D graphics? OpenGL?  
   
   
 Finally thanks everyone for the obviously huge amount of work putting libXenon together!

## 2012-03-04 03:37:09, posted by: Cancerous1

libxenon is a set of tools/libs to build open source homebrew  
   
 yes it is low level, unmanaged code  
   
 no it isnt a kernel  
   
 3d is possible, there is no OpenGL support.  
   
 I suggest if you're thinking about using it, follow the tutorials to build libxenon and get the environment set up, then just jump in, if you need help from there don't be afraid to ask!

## 2012-03-04 03:53:40, posted by: andrewd207

Okay found the answers to some of my questions.  
   
 [quote="andrewd207"]  
 Q: What is libXenon? Is it linux? It seems very similar to linux when booting. A quick look at the sources didn't reveal linux.  
 [/quote]  
   
 It's not linux in any way. It's a from scratch development platform that is statically linked into your program you create.  
 libXenon is a hardware access layer that uses the hardware directly and doesn't require an OS.   
   
 [quote="andrewd207"]  
 Q: Is every libXenon app essentially a kernel? I.e each libXenon application contains code to access the hardware on the lowest level.  
 [/quote]  
   
 Programs made with libXenon are standalone ELF executables that are totally self sufficient once loaded into memory.  
   
 [quote="andrewd207"]  
 Q: Does libXenon provide gpu accelerated 3D graphics? OpenGL?  
 [/quote]  
   
 This one is less clear to me. I think yes but I've not yes looked at how graphics are drawn at the highest level api. No OpenGL layer exists though it would be possible to write one on top of what exists already. (Which is a very low level api)  
   
 As I was writing this there was an answer to my post. Thanks :)