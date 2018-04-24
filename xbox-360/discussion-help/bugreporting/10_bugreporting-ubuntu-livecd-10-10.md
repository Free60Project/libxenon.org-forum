# [BUGREPORTING] Ubuntu LiveCD 10.10

## 2011-02-21 20:16:02, posted by: tuxuser

Hi,  
   
 Please post all the bugs you get with using the Ubuntu 10.10 LiveCD **Xenon**. Please write into the post which build you are using (e.g. beta2, beta3 etc.). Also do logfiles if possible, they can be really helpful :) :) :)   
   
 Latest LiveCD build is always: [url=http://libxenon.org/http://libxenon.org//viewtopic.php?t=1]HERE[/url]  
   
 THX!  
   
 PS: I am aware that sound does not work currently, I am on it.  
   
 **[b]If you are doing bugreports please fill out the following[/b]**  
 [quote] LiveCD Revision: *Beta 5*  
 Console Type: *Retail/Devkit/...*  
 Console Revision: *Xenon/...*  
 Hack-Version: *JTAG/King Kong/...*  
 Boot-Method: *Native/XeLL-Launch/HvXBootOS/...*  
 Videocable: *Composite/YUV - in YUV MODE/...*  
 Error-Description: *Describe your error as good as possible*  
 Logfile: *Attach logfiles from /var/log/syslog - dmesg - etc. If you are unsure which log could hold an error description feel free to ask* [/quote]

## 2011-02-22 17:25:15, posted by: Mojjio

testsystem: xenon, samsung drive with magical fw ...  
 Ubuntu 10.10 livecd beta4 on verbatim dvd-r  
 boot time bout 5-7minutes didnt time it.  
 dhcp makes the boot process slower.   
   
 pro:  
 runs smother than any other livecd i've ran on a 360 before even though a beta.  
   
 cons:  
 gnome is a little heavy on the machine... better to run with lightweight wm.   
 its probably compiz that make it heavy.  
   
 fuse is not present, we like fuse. :(   
 *edit can't mount any device atm* just goes "FATAL: Module fuse not found. fuse: device not found, try 'modprobe fuse' first.  
   
 no auto-mount on usb drives which probably most turds like from x86 systems.   
 fuse is needed for apps like sshfs etc.   
   
 would like to see next round or final with extra functions and apps like  
 fuse  
 sshfs  
 irssi  
 mc (just to make terminal life easier )   
 and some lightweight wm !

## 2011-02-27 04:27:35, posted by: Magnus_Hydra

Sweet tuxuser! I will test it out and get back to u. I doubt u remember me though :cry: .

## 2011-02-27 04:38:33, posted by: mojobojo

System: Jasper 512  
 Revision: Ubuntu 10.10 Beta 4  
 Media: CD-R (Couldn't find any DVDs)  
 Notes: This is going in through my component cables and I loaded it up with the old xellous.  
   
 The image was too big in the img tags so I am just providing a direct link.  
   
 There is a graphics glitch on the top left corner of my screen.   
 [attachment=1:1untltr1]  
   
 I moved terminal to the side and this happened.  
 [attachment=0:1untltr1]  
   
 The system hangs on shutdown.  
   
 EDIT by tuxuser: Attached the pictures into the post

### Attachments

[graphicsbug.JPG](graphicsbug.JPG)[graphicsbug2.JPG](graphicsbug2.JPG)

## 2011-02-27 11:27:15, posted by: Chrisoldinho

Hello,  
   
 I believe most of us are aware of the random freeze that seems to happen when using Linux on the 360.  
   
 I am wondering if anyone has any ideas as to what causes this, and if there is a possible fix in the works?  
   
 Following installing squeeze last night, I installed KDE 4.4, immediately after logging in every time it just freezes. If I run Gnome, it does work to a degree, but it still happens intermittently.  
   
 Does Cancerous1's Debian Mint perform any better, or does that suffer as well?  
   
 Thanks, Chris.

## 2011-02-27 11:46:35, posted by: MaDMaLKaV

There is a bug in the CPU on simetric multithreading, where cache cohenrecy is not maintained in certain atomic operations. The problem is located and some people is trying to replicate the bugfix MS uses for implementing in the kernel patches.

## 2011-02-28 11:09:31, posted by: Chrisoldinho

Thanks for the information.  
   
 I hope this issue can be resolved.

## 2011-03-04 20:28:07, posted by: Mr.Gorillaz

Hi!  
 At first thanks for the Great Work of Porting Ubuntu 10.10 on the Xbox360.  
 Here is a Bug that I Notices so far.  
   
 If you Use the Terminal the picture is sometimes flickering.  
   
 I use a JTAG-Falcon Box.

## 2011-03-06 14:09:06, posted by: tuxuser

You got maybe a hint how I can provoke those graphic-bugs? I cant get them happen here...  
   
 Maybe you got a log which shows some graphic related errors?  
   
 edit: It seems like a xenosfb problem...

## 2011-03-08 16:30:02, posted by: Meluxe

Can`t thank you guys enough! When you see me just fell free to ask for a beer or whatever you need! :roll:   
   
   
   
 LiveCD Revision: Ubuntu Live CD 10.10 Betatest!?  
 Console Type: retail  
 Console Revision: Falcon  
 Hack-Version: JTAG  
 Boot-Method: Xell-launch  
 Videocable: S-Video and Scart and hdmi  
 Error-Description: cutted edges up and downsides, S-Video no color  
 Logfile: ist that meaning a Debug-log done with the Serial-console discribed on [url=http://www.free60.org/Serial\_Console]http://www.free60.org/Serial\_Console[/url] ?? Witch software do i need to log that input(PC side)?  
   
   
 So here is a short discripition of the bug:  
   
 Booting works well (Graphics work very well too ^^) since the XeLL (Testing) - lwip 1.4 upload on 360hacks.de. Once Linux appears my S-Video plug provides only black an white, no color, while the scart plugs picture is colored.  
   
 Both plugs provide a cutted picture on the buttom and the top side of the screen for about a half "bar".  
   
 HDMI is still cutting all edges. Color works, sound not working may be an issue of settings, not figured out yet.  
 At the beginning of the boot process the picture is *yellowed* till it adjusts about five times, form fitting the screen to overlaying it again  
   
   
   
 Btw: I saw that the Rols first two leds are red and orange and the third is green. Is there a reason for that?  
 ...and finaly the probably most clear bugs: The controller isn`t connecting again after turnig it off an on and shoutdown doesn`t work.  
   
   
 edit- just tried to solve the edge-problem in HDMI mode by changing my TVs setting with no success

## 2011-09-02 07:23:30, posted by: lazarusjx

@Meluxe  
 I've also experienced those cut screen edges when using HDMI (on an Aquos LCD TV) what I've done is to set my screen size to "underscan" (TV's Settings) and that solved it, maybe your TV has that setting too...  
   
 my setup:  
   
 LiveCD Revision: Ubuntu Live CD 10.10 Betatest5  
 Console Type: retail  
 Console Revision: Falcon  
 Hack-Version: JTAG  
 Boot-Method: Xell-Reloaded  
 Videocable: HDMI  
 Error Experienced: Locks up on Shutdown, have to shutdown manually by turning console off...

## 2012-01-30 09:16:09, posted by: sowa99

LiveCD Revision: Ubuntu Live CD 10.10 Betatest5  
 Console Type: retail  
 Console Revision: Falcon  
 Hack-Version: RGH  
 Boot-Method: Xell-Reloaded  
 Videocable: composite  
 Error Experienced: Please provide a name for this Disc, such as 'Debian ...' at startup. Keyboard is not workinkg so I can't type anything. Any ideas?

## 2012-05-10 12:04:45, posted by: wienio

my setup:  
   
 LiveCD Revision: Ubuntu Live CD 10.10 Betatest5  
 Console Type: retail  
 Console Revision: Jasper 512  
 Hack-Version: RGH 1.0  
 Boot-Method: Xell-Reloaded  
 Videocable: HDMI  
 keyboard: geniusslim star 110  
 mouse: logitechm180   
 so far no bugs

## 2012-07-21 09:09:31, posted by: orangperai

My RGH Jasper Elite with HDMI. running with Linux, No Bug ...  
   
 Thanks, its will make happy