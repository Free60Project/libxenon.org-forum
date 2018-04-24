# PROBLEMS!! Xilinx will not write the Jasper JED to my Glitcher!!

## 2011-10-14 11:31:05, posted by: moco

Hi all, Im using a xilinx usb jtag cable. Xilinx picks up the cable and board no problems, however it wont write the jed file to the chip. it keeps saying that the ID code doesnt match. I have a feeling some of the jasper.jed files out there are faulty. I need help please, Ive been trying to change the ID code of the jed file, but I cant work out how.

### Attachments

[photo.PNG](photo.PNG)

## 2011-10-14 13:25:56, posted by: crisdo98

the prog is a little bit funny and you have to reset it a couple of times sometimes.  
   
 Messing with the ID code is not the solution I know that much as I had identical issues and it was sending me bonkers!  
   
 I could not get it working in Win7 and as soon as I booted into XP and ran Impact it worked right away.

## 2011-10-14 21:50:12, posted by: SynTeX

Had the same problem... making the wires of the Programmer realy short was the solution ^^

## 2011-10-19 19:14:38, posted by: 3asy60lf

Try to Lab tool 12.2 ;)

## 2011-10-22 11:09:34, posted by: moco

Okay cheers guys. I worked it out. I've been in contact with the matrix team over the last 2 weeks about the issue. I found out for myself, that the cpld I got is faulty. Its has a xilinx xc2c64 chip. Its supposed to have a xc2c64A chip on it. The jasper file for the glitch hack is specifically designed for the xc2c64A chip and this is why it wont write to the cpld i have installed. I tried editing the ID code in the jasper file to xc2c64X. When i did that, Xilinx programmed it no problems, but the xbox still didnt glitch.   
   
 The Matrix team have posted me a new matrix glitcher and I'll install that when it comes in.   
 My advice to everyone is DONT buy any modchips from China! . Now, I'm not racist but quite often all you get is some phony rip off chip that doesnt function 100%.   
   
 In the mean time, I'm happy to hear any other possibilites that may get the current glitcher up and running whilst I wait.