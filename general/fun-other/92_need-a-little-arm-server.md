# Need a little ARM Server?

## 2011-06-21 15:41:41, posted by: tuxuser

Hi everybody,  
   
 Maybe somebody of you would be interested in getting a little 1.2GhZ ARM Server with little power consumption, 2x SATA, 1x USB, 128MB RAM, 512MB Flash and Gigabit Ethernet?  
   
 I just bought one recently and its perfect for all my needs: Serial Adapter via minicom, NFS, TFTP, Samba, MPD (w/ USB-Soundcard), FTP, External USB Drive etc. (USB Hub needed)  
   
 The device is called: **[b]Seagate GoFlex Net[/b]**  
   
 Prior to using it properly you need to "unlock" the bootloader by overflashing it so it accepts the OS from USB, NFS etc. Then you can also install (Em)Debian onto the NAND.  
   
 If you are interested, you can get alot of information here: http://jeff.doozan.com/debian/   
   
 Alternative to the Device: **[b]Seagate Dockstar[/b]**  
   
 Greetz  
 tux

## 2011-06-21 23:18:24, posted by: Chrisoldinho

Pretty cool Tux, I use a router to accomplish most of my needs...It's an Asus RT-N16 (533Mhz processor when overclocked, 128MB RAM) with DD-WRT firmware flashed in place of the standard Asus Firmware (Kong mod build 17140 for the K26 kernel with MiniDLNA built in to be precise ;D) along with OTRW (Optware the Right Way) on a 3GB Flash drive (512MB SWAP, 2.5GB for Optware).  
   
 In effect I get:  
 [list] - [*]Samba
 - [*]BitTorrent (Transmission)
 - [*]Asiablock
 - [*]Stophack & Stophammer
 - [*]Much more
[/list] You can install loads more via ipkg also.   
   
 Attached to the router I have a 2TB USB HDD. I can in effect download anything from anywhere without ever turning my PC on (well I need to get to shell / web GUI I guess :))  
   
 I have also installed pyLoad (similar to JDownloader but can be used on routers). Overall it's pretty amazing...I thought I would overload it a little having all of this Optware installed but quite frankly it doesn't seem to make a scrap of difference, SWAP never even gets used despite setting swapiness to 25%.  
   
 Sorry to go off at a slight tangent, but for users wanting an enterprise level router /server with all the bells and whistles, the price is hard to beat.  
   
 EDIT forgot to add if you get a build other than the kong mod (as it is not included with this) you can run KAID direct from the router, i.e. no PC to use Xlink. If doing this though you need to use Optware the Right Way otherwise it won't work (the LD\_LIBRARY PATH needs to be updated and it requires Optwares uClibc (a script is included in OTRW that I researched and frater built and included). I've not had a great deal of success admittedly as the kaid engine for MIPS based architecture is a little out of date, but now and again it works...

## 2011-06-22 14:23:43, posted by: tuxuser

Had my Router configured before, a Linksys E3000 Dualmode. The transfer rates were around ~10MB/s even if it had gigabit ethernet... now I am getting ~32/MBs. Also NFS was kinda slow with the linksys.