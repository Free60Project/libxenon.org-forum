# HDD - Partitions, Data etc.

## 2013-12-08 11:27:30, posted by: tuxuser

As you know, the Xbox One includes an internal 500GB 2,5" SATA HDD.   
 Our Team-Member "Juvenal" looked into the HDD layout shortly after release and found 5 NTFS-Partitions... a few hours later he released the [url=http://libxenon.org/http://libxenon.org//viewtopic.php?t=6]Xbox HDD Tools[/url] to make every SATA HDD "Xbox One"-compatible.  
   
 So far, only encrypted XVD files were found on HDD...

## 2013-12-08 19:38:22, posted by: Swizzy

Some details about the HDD:  
   
 The partitioning table type is GPT (GUID Partition Table)  
 Disk GUID: a2344bdb-d6de-4766-9eb5-4109a12228e5  
 Partition 1 (Temp Content) GUID: b3727da5-a3ac-4b3d-9fd6-2ea54441011b  
 Partition 2 (User Content) GUID: 869bb5e0-3356-4be6-85f7-29323a675cc7  
 Partition 3 (System Support) GUID: c90d7a47-ccb9-4cba-8c66-0459f6b85724  
 Partition 4 (System Update) GUID: 9a056ad7-32ed-4141-aeb1-afb9bd5565dc  
 Partition 5 (System Update) GUID: 24b2197c-9d01-45f9-a8e1-dbbcfa161eb2  
   
 The "dynamic" partition here is Partition 2, the rest must be the following sizes (exact bytes!):  
 Partition 1 (Temp Content): 85 985 280 (HEX: 0x5200800)  
 Partition 3 (System Support): 83 886 080 (HEX: 0x5000000)  
 Partition 4 (System Update): 25 165 824 (HEX: 0x1800000)  
 Partition 5 (System Update 2): 14 680 064 (HEX: 0xE00000)  
   
 The labels are as you've already guessed:  
   
 Partition 1: Temp Content  
 Partition 2: User Content  
 Partition 3: System Support  
 Partition 4: System Update  
 Partition 5: System Update 2  
   
 Once you've replaced your harddrive you need the following files in Partition 4 (in order for it to work):  
   
 [attachimg=1]  
   
 the list is taken from: https://github.com/juvenal1/xboxonehdd

### Attachments

[partitiontable_xbone.png](partitiontable_xbone.png)

## 2015-03-12 18:19:18, posted by: <Unknown User>

http://www.ludvikjerabek.com/2014/07/14/xbox-one-fun-with-gpt-disk/