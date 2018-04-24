# personal pastebin

## 2011-07-31 04:18:30, posted by: tuxuser

If somebody is bored - Get it up on free60 wiki

```
 Sata HDD:  

 ***************************************************************************  
 StartSector | SectorCount | Partition Name  
 ***************************************************************************  
 0 | AddressableSectors | PhysicalDisk  
 0 | AddressableSectors | Partition0  
 0 | 0 | WindowsPartition  
 400 | 400000 | Cache0  
 400400 | 400000 | Cache1  
 800400 | 107180 | DumpPartition  
 {  
 // Sub partition's within the "DumpPartition"  
 0 | 30000 | SystemURLCachePartition  
 30000 | 10000 | TitleURLCachePartition  
 60000 | 67180 | SystemExtPartition  
 C7180 | 40000 | SystemAuxPartition  
 }  
 907580 | 80000 | SystemPartition  
 987580 | AddressableSectors - PartitionStart | Partition1  
 ***************************************************************************  
   
 NOTES:   
   
 1) "PhysicalDisk" and "Partition0" are a map of the whole HDD  
 2) "WindowsParition" is just a fake partition that has no length  
 3) "\Device\Harddisk0\Partition1" is also mapped to "\Device\UpdateStorage1"  
   
   
 MU:   
   
 **********************************************  
 Offset | Size | Partition Name  
 **********************************************  
 0 | 20000000 | ReservationPartition  
 400 | 8000000 | SystemAuxPartition  
 8000400 | 4000000 | StorageSystem  
 C000400 | 6000000 | SystemURLCachePartition  
 12000400 | CE30000 | SystemExtPartition  
 20000000 | 0 | Storage  
 **********************************************  
   
 Internal MU:  
   
 **********************************************  
 Offset | Size | Parition Name  
 **********************************************  
 0 | 20E30000 | ReservationPartition  
 0 | 8000000 | SystemAuxPartition  
 8000000 | 4000000 | StorageSystem  
 C000000 | 2000000 | TitleURLCachePartition  
 E000000 | 6000000 | SystemURLCachePartition  
 14000000 | CE30000 | SystemExtPartition  
 20E30000 | 0 | Storage  
 **********************************************
```