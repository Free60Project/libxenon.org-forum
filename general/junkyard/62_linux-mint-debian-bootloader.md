# Linux Mint Debian Bootloader

## 2011-04-06 21:11:01, posted by: eminwargo

Hallo,  
   
 ich sehe schon hier ist langsam totehose...  
   
 ich hab mir jetzt zum 2 mal Linux Mint Debian Edition on 360 auf der internen HDD installiert alles lief gut mit der installation...   
   
 aber dann weiß ich nicht welchen Bootloader ich nehmen soll... damit ich das starten kann und welche Xell version..  
   
   
 kann mir bitte einer helfen ?!  
   
 Danke im voraus...

## 2011-04-06 21:32:44, posted by: tuxuser

Hi,  
   
 Ja hier ist momentan etwas weniger los da ich momentan eher auf XeLL fokusiert bin und außerdem aus privaten Gründen wenig Zeit habe.  
   
 Zur Bootloader-Frage: Wenn du das System auf die zweite Partition, sprich sda2, installiert hast, dann nimmst du einen Bootloader der den Parameter "root=/dev/sda2" hat. Cancerous hatte [url=http://homebrew.allowed.org/free60/overscan\_fixed/zImage.xenon]HIER[/url] einen gepostet... der *müsste* root=/dev/sda2 gesetzt haben... das kannst du zur sicherheit aber nochmal mit einem Hex Editor überprüfen.  
   
 Gruß  
   
 tux

## 2011-06-26 17:43:12, posted by: Doerek

[quote="tuxuser"]  
 Hi,  
   
 Ja hier ist momentan etwas weniger los da ich momentan eher auf XeLL fokusiert bin und außerdem aus privaten Gründen wenig Zeit habe.  
   
 Zur Bootloader-Frage: Wenn du das System auf die zweite Partition, sprich sda2, installiert hast, dann nimmst du einen Bootloader der den Parameter "root=/dev/sda2" hat. Cancerous hatte [url=http://homebrew.allowed.org/free60/overscan\_fixed/zImage.xenon]HIER[/url] einen gepostet... der *müsste* root=/dev/sda2 gesetzt haben... das kannst du zur sicherheit aber nochmal mit einem Hex Editor überprüfen.  
   
 Gruß  
   
 tux  
 [/quote]  
   
 @ tuxuser  
 Tach auch...  
 Ich befinde mich auch gerade in den Vorbereitungen für die Mint Debian Installation.  
 Leider ist der von dir genannte Link "Tot"....Ist der noch relevant?  
 Oder sollen wir uns generell besser am Ursprungs-Thread:  
   
 [url=http://libxenon.org/http://libxenon.org//viewtopic.php?p=410#p410]http://libxenon.org/http://libxenon.org//viewtopic.php?p=410#p410[/url]  
   
 ...orientieren?  
   
 P.s.  
 Simple Machines gefällt mir, sieht super aus & läuft wie geschmiert ![](http://www.evo-x.de/wbb2/img_evox_v3/icons/icon16.gif)[img]http://www.evo-x.de/wbb2/img\_evox\_v3/icons/icon16.gif[/img]  
   
 Greetz  
 DCDoerek