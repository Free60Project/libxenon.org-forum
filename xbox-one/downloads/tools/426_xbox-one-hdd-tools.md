# Xbox One HDD Tools

## 2013-11-30 11:45:17, posted by: tuxuser

**[b]What this does[/b]**  
 Given any HDD over 500GB in size, you can format it for use with you Microsoft Xbox One console  
   
 **[b]How[/b]**  
 ![](http://i.imgur.com/56WNIjG.gif)[img]http://i.imgur.com/56WNIjG.gif[/img]  
   
 **[b]Instructions[/b]**  
 All of this must be done as root! I HIGHLY suggest you do this on a livecd or usb booted system if you don't 'know linux' and would rather not wipe the wrong hard drive.  
 [list=1] - [*]Connect your HDD and take note of what its called (ex: sda, sdb etc)
 - [*]Run the script with the device name as the first parameter
 - [*]It will bitch about missing partitions etc, but write a file with commands to create said missing partitions
 - [*]Run the created script
 - [*]Copy the correct files to the newly created partitions
 - [*]Unmount the newly created partitions
 - [*]Run the main script again
[/list] **[b]Putting it back together[/b]**  
 When you put the new HDD in your console for the first time and boot up, the console will go the the green "Xbox One" screen, pause for a second or two, then shut down. Boot the console again. This time it should pause at the green screen for a while longer, then go to a black screen for even longer. It can take several minutes before anything happens after this, the xbox is automatically creating temporary files during this time. If you copied everything correctly, it WILL go to the dashboard eventually, just be patient!  
   
 **[b]What is linux?[/b]**  
 Wait for a windows version  
   
 **[b]Required Files[/b]**  
 These can be gotten off your original HDD easily  
   
 [attachimg=2]  
   
 Author: Juvenal  
 Source: [url=https://github.com/Juvenal1/xboxonehdd]Github[/url]

### Attachments

[xboxonehdd-master.zip](xboxonehdd-master.zip)[xbone_hdd_files.jpg](xbone_hdd_files.jpg)