# Ubuntu 11.10 kboot help

## 2012-02-24 03:58:55, posted by: mitch_thepcman

I am trying to install Ubuntu 11 from [url=http://free60.org/Ubuntu11.10]http://free60.org/Ubuntu11.10[/url]. I install it using the gentoo live cd, but i cannot seem to create a kboot.conf file that will allow the system to boot into GNOME. Edit after edit it keeps doing kernel panics or it will appear to freeze and not do anything. Any help?   
   
 Thanks

## 2012-02-24 15:04:35, posted by: tuxuser

hey,  
 You probably need to provide more information:  
   
 1. Did the debootstrap of Ubuntu give any errors?  
 2. How does your kboot.conf look?  
 3. What exact kernel panics are appearing?  
   
 Greetz  
 tux

## 2012-02-24 18:04:36, posted by: mitch_thepcman

I don't think the deb bootstrap gave any errors. I just ran the script and left the room while it was installing. My kboot.conf is  
 [code]ubuntu\_from\_hdd="uda:/latest\_kern root=/dev/sda2 video=xenonfb panic=60 maxcpus=3 --"[/code] and it was only kernel panicking when there was a line in the boot pointing to a nonexistent initrd or an incorrect root partition. now it just hangs...

## 2012-02-24 18:43:28, posted by: tuxuser

Does it hang with a blackscreen maybe and error about plymouth before?  
 It could be also te xenosfb giving you a blackscreen.. have to admit that I didnt have to time to test the script by myself.  
   
 If plymouth is the problem you can try to append "noplymouth nosplash" to the bootarguments in kernel config.  
   
 To try if its xenosfb, you can try to rename the xenosfb driver temporarily.

## 2012-02-24 22:52:37, posted by: mitch_thepcman

The last I remember it hung on something about NTP- no black screen. I am currently trying to reinstall it see If that would help  
   
 Edit: The maxcpus=3 line in the boot is causing it to kernel panic with the message "Not Syncing: Attemped to kill init". Otherwise it hangs at "Starting ntp server ntpd"  
   
 Sent from my iPhone 4S using Tapatalk

## 2012-03-01 03:53:04, posted by: whiskthecat

Same problem here. Logged in through SSH at the NTP frozen screen. System was actually running and xorg just failed to start. Fixed it by running apt-get update / upgrade then installing a package. Next reboot xorg started.

## 2012-03-01 06:42:03, posted by: tuxuser

@whisktecat  
 Thx for the hint! Do you happen to still have the Xorg log for the situation it failed?

## 2012-03-01 12:53:47, posted by: whiskthecat

Nope, sorry. Hard drive has been formatted multiple times since then and I am now struggling with this yellow tint on SDL games.