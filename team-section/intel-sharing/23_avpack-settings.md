# AVPACK settings

## 2011-03-03 21:55:49, posted by: tuxuser

These are AV-Pack IDs from XeLL  
   
 Proper AVPACK detection, probably just missing some IDs.. besides that -> works great ;) 
  ```
  void xenos\_autoset\_mode(void)  
 {  
 int mode = VIDEO\_MODE\_HDMI\_720P;  
 int avpack = xenon\_smc\_read\_avpack();  
   
 printf("AVPACK detected: %02xn", avpack);  
 switch (avpack)  
 {  
 case 0x13: // HDMI\_AUDIO  
 case 0x14: // HDMI\_AUDIO - GHETTO MOD  
 case 0x1C: // HDMI\_AUDIO - GHETTO MOD  
 case 0x1F: // HDMI  
 mode = VIDEO\_MODE\_HDMI\_720P;  
 break;  
 case 0x43: // COMPOSITE - TV MODE  
 case 0x47: // SCART  
 case 0x54: // COMPOSITE + S-VIDEO  
 case 0x57: // NORMAL COMPOSITE  
 mode = VIDEO\_MODE\_PAL60;  
 break;  
 case 0x0F: // COMPONENT  
 case 0x4F: // COMPOSITE - HD MODE  
 mode = VIDEO\_MODE\_YUV\_720P;  
 break;  
 case 0x5B: // VGA  
 mode = VIDEO\_MODE\_VGA\_1024x768;  
 break;  
   
 default:  
 mode = VIDEO\_MODE\_PAL60;  
 printf("unsupported AVPACK!n");  
 {  
 int table[] = {0xf, 0x1, 0x3, 0x7};  
 xenon\_smc\_set\_led(1, 0xff);  
 mdelay(1000);  
 xenon\_smc\_set\_led(1, table[(avpack>>6) & 3]);  
 mdelay(1000);  
 xenon\_smc\_set\_led(1, table[(avpack>>4) & 3]);  
 mdelay(1000);  
 xenon\_smc\_set\_led(1, table[(avpack>>2) & 3]);  
 mdelay(1000);  
 xenon\_smc\_set\_led(1, table[(avpack>>0) & 3]);  
 mdelay(1000);  
 xenon\_smc\_set\_led(1, 0xff);  
 mdelay(1000);  
 xenon\_smc\_set\_led(0, 0);  
 }  
 break;  
 }  
 xenos\_set\_mode(&xenos\_modes[mode]);  
 }
 ```

## 2011-03-12 22:41:35, posted by: Cancerous1

0x59  
 0x1B  
   
 have also turned up as VGA avpacks  
   
 LAN-S confirms, 1B hdmi+ optical for his setup and 1F without optical  
   
 further research is needed :S, for now he's ok with not using the optical adapter so all the testers can see

## 2011-03-20 12:51:48, posted by: tuxuser

Info tmbinc gathered  
```
8340 - AV pack 1f - no 1b - VGA
.rdata:10008360 .long aStandard\_1 # "Standard" 8
.rdata:10008364 .long aScart # "SCART" 9
.rdata:10008368 .long aReserved # "Reserved" a
.rdata:1000836C .long aHdtv # "HDTV" b
.rdata:10008370 .long aDvi # "DVI" c
.rdata:10008374 .long aStandard\_1 # "Standard" d
.rdata:10008378 .long aVga # "VGA" e
.rdata:1000837C .long aNone # "None" f
```

## 2011-06-05 13:33:37, posted by: tuxuser

```
bool hdmiDetected = !(avpack & 0x40);
int currentAVPack = avpack & 0x70;
int currentAVSubMode = avpack & 0x3;
printf("AVPACK hdmi: %i pack: %02X submode: %02Xn", hdmiDetected, currentAVPack, currentAVSubMode);
```

gonna do a new troubleshooting xell soon