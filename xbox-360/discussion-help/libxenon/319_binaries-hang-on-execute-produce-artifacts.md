# Binaries hang on execute, produce artifacts.

## 2012-05-04 09:21:03, posted by: UNIX

Hello everyone!  
   
 Well, I am back working on code after a while. School and work took a priority in my life. Now that I have a development console again, I'm picking up projects I left, as well as starting new ones.   
   
 It would seem that for some unknown reason, any new code that I compile does 1 of 2 things. Either 1: XeLL hangs at "Executing..." when loading my xenon.elf files, or 2: It hangs at "Executing..." and creates bizarre graphical artifacts. I'm not sure if this is a know issue with the latest toolchain or what, but I can't seem to get anything to run anymore. I get no UART feedback from my code, XeLL seemingly does not even execute it.  
   
 I'm using the latest version of XeLL Reloaded, and the latest version of the toolchain from gligli's repository. The platform 360 I'm developing on is a Xenon RGH. Any ideas?   
   
 -UNIX

## 2012-05-04 09:25:47, posted by: Cancerous1

try with Ced2911's repo

## 2012-05-05 07:51:13, posted by: UNIX

Will do. I was reluctant to use Ced's repository since it is labeled as experimental. Is XeLL compiled using his fork? I'll deinstall gligli's toolchain and try compiling with Ced's, and report results.

## 2012-05-05 07:55:22, posted by: sk1080

The only time I remember this reported was people running the .elf and not the .elf32, idk what else would cause it.  
 Ced's repo should work(threaded or non-threaded branch are both fine, depending on network usage)  
   
 EDIT: and with all the changes ced's repo has made since you probably last used it, I would recommend completly emptying $DEVKITXENON/usr

## 2012-05-07 19:13:10, posted by: UNIX

Success! Using Ced's toolchain did in fact work. Since when did the execution of xenon.elf change? and why?

## 2012-05-09 06:09:22, posted by: sk1080

I have no clue, new elfs still work on ancient xells, so idk what has changed

## 2012-05-20 21:32:54, posted by: c01eman.360

ive got the same problem using ceds toolchain