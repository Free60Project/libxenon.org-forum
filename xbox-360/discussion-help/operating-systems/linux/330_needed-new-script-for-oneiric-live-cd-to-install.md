# Needed new script for Oneiric Live CD to install

## 2012-06-25 18:36:35, posted by: kikofras

Hello guys!  
   
 First of allo thanks for all your efforts, they're well apreciated :P  
   
 Then, i've succesfully installed 7.10 on my box, but i want to install th 10.10 beta or 11.10, and there's no working scripts for that.  
   
 Can anyone post new script so we can install correctly the 11.10 ubuntu?  
   
 Thanks a lot.

## 2012-09-09 20:14:21, posted by: TBsparky

Yeah, I tried to install 11.10 as well until I noticed one of the files had been removed from the server the script tried to access. I've found a replacement server for the file and the script can be found at:  
   
 [url=https://rapidshare.com/files/912593008/ubuntu\_oneiric.sh]https://rapidshare.com/files/912593008/ubuntu\_oneiric.sh[/url]  
   
 The only problem was that I needed to open the script while running the Live-CD to add a new line (blank) between the:  
 "debar -xf" as it picks up ar -xf as one command and fails to retrieve the file, so it would look like this:  
   
 wget http://160.26.2.181/ports/pool/main/d/debootstrap/debootstrap\_1.0.38\_all.deb  
 ar -xf debootstrap\_1.0.38\_all.deb