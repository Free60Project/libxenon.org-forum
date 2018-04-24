# xRick for libxenon (source only)

## 2012-09-24 21:59:12, posted by: MagicSeb

Hello,  
   
 I have made a very fast port of xrick [url=http://www.bigorno.net/xrick/]http://www.bigorno.net/xrick/[/url]  
   
 It's working as is but, sound is scratched, i think SDL restitution on 8 bit sample is not working or something like that  
   
 You can disable sound by modifying config.h in source/main/  
   
 **[b]* If someone (gligli, tuxuser, ced ???) can fix the buggy sound, it will be great :D *[/b]**  
   
 INSTRUCTIONS :  
 You need libSDLxenon installed, then make and you got RickLXN,elf32  
 Put data.zip on root of usb drive (uda:/data.zip)  
 Then run the baby with zlx browser OR rename RickLXN.elf32 to xenon.elf  
   
 edit by tuxuser: attached file to post

### Attachments

[RickLXN_src.tar.gz](RickLXN_src.tar.gz)

## 2012-10-25 20:13:40, posted by: lantus360

great work :D  
   
 i havent checked in here in a while. you are correct that the issue with sound is that libSDLXenon currently doesnt handle 8 bit mono up-conversion. Currently only 16 bit formats are supported