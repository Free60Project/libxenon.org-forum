# nulldc compiling - issue [RESOLVED]

## 2012-10-05 16:22:21, posted by: OOKAMI

hello :)  
   
 after many days to have a proper xenon toolchain, libs, zlx and all needed (thanks for the tutorial :) ) a finally managed to complete and compiling nulldc :)  
   
 i have however a question about  
 indeed, nulldc can't be compiled correctly by make  
   
   
 i mean  
 if i choose the command make -B => elf creation ok, emu launch ok but when i launch a gdi, red screen for a fatal crash  
 if i choose the command make => compilation can't be completed successfully  
   
 here the logs of compiling  
   
 ookami@ookami-VirtualBox:~/nulldc/nulldc-360$ make  
 linking ... nulldc-360.elf  
   
 /home/ookami/nulldc/nulldc-360/ => many undefined reference to many things  
   
 collect2: error: ld returned 1 exit status  
 make[1]: *** [/home/ookami/nulldc/nulldc-360/nulldc-360.elf] Error 1  
 make: *** [build] Error 2  
 ookami@ookami-VirtualBox:~/nulldc/nulldc-360$   
   
 you can find in attachment the complete report  
 if someone can give some help about :)  
 thanks and have a great week end all :)  
   
 .

### Attachments

[New Empty File.rtf](New Empty File.rtf)

## 2012-10-05 17:02:23, posted by: MagicSeb

Tu n'as pas compilé les libs nécessaires :  
   
 ./build-xenon-toolchain zlib  
 ./build-xenon-toolchain libpng  
 ./build-xenon-toolchain bzip2  
 ./build-xenon-toolchain freetype  
 ./build-xenon-toolchain filesystems

## 2012-10-05 17:37:40, posted by: OOKAMI

c'est pourtant ce que j'ai fait et refaits  
   
 merci, je vais refaire l'install de ces éléments :)  
   
 PS : vu que tu m'aides beaucoup faudra que je t'invite un de ces quatres lol ;D

## 2012-10-05 22:34:59, posted by: MagicSeb

bin2s doit etre manquants dans ton install  
 il se trouve la : /usr/local/xenon/bin  
   
 si absent, recompiles la libxenon

## 2012-10-06 09:44:50, posted by: OOKAMI

Hello  
   
 Je viens de vérifier et il est bien présent  
   
 il fait 11,5KB (11,811 Bytes)  
   
 ce dossier est composé de 27 pkg comme le bin2s ainsi qu'un fichier nommé xenon-embedspu  
   
 j'ai bien tout refait et toujours la même chose  
   
 pour info, j'ai directement compilé le libxenon et toolchain de gligli, pas celui de free60  
   
 j'ai aussi compilé le ZLX  
 je ne vois pas ce qui me manques pour finaliser :p

## 2012-10-06 09:49:35, posted by: OOKAMI

[attach=2]changement de dernière seconde  
   
 j'ai laissé compilé à tout hasard le nulldc durant mon abscence (j'ai bossé de nuit) mais aussi lancé le toolchain de free60 et ca a l'air d'avoir marché cette fois ci :)  
   
 linking ... nulldc-360.elf  
 converting and stripping ... nulldc-360.elf32  
   
 Done  
   
 du coup, je pense qu'il aurait fallu d'abord compiler le free60 et après celui de gligli qui doit être complémentaire  
   
 si c'est le cas ba on le sait maintenant :)  
   
 je vais faire un test tout de suite et je te tiens au jus :)  
   
   
   
 EDIT  
 bon, toujours le red screen, je vais refaire de zero la compilation mais je vais rebooter avant car il m'interdit maintenant de créer les dossiers pour compiler le bougre ;D  
   
 vé y arriver :)  
   
   
 EDIT 2  
 bon  
 ma machine virtuelle a planté car lors du redémarrage, elle a plus voulu fonctionner et les snapshots m'ont pas sauvé :p  
 je viens de tout recommencer et je refais la compilation :)  
   
 cette fois ci je fais le toolchain de Free60  
 après toolchain fait, je ferais le libxenon de gligli :)  
   
 je vous tiens au jus :)  
 .  
   
   
 EDIT 3  
   
 ok, after   
   
 a full reinstallation of virtualbox  
 downloading and set up the free60 libxenon toolchain and libs  
 downloading and set up the gligli libxenon  
 downloading and compiling nulldc  
   
 first compilation was success but still have a red screen you can see in attachment  
 as i thought, installing free60 toolchain before gligli libxenon is needed to perform it :)  
   
 compiling is successfull at the first time (some warning showed on terminal but nothing happened to stop compilation)  
   
 regarding this link  
 http://libxenon.org/http://libxenon.org//viewtopic.php?p=1098#p1098  
   
 i made what is required and still having same issue  
   
 maybe something missing :p  
   
 thanks for your help :)  
   
 .

### Attachments

[IMG_20121008_114958.jpg](IMG_20121008_114958.jpg)

## 2012-10-09 03:21:16, posted by: OOKAMI

SOLVED ;D  
   
 tested first with HDD with 2 partitions and make the red crash  
   
 now tested with usb key 32gb and now it's running :)  
   
 i perform now new one partition on HDD external in order to see how it work :)