# NANDOne

## 2013-11-30 11:48:59, posted by: tuxuser

[quote] NANDOne v0.02  
 ===========  
   
 Xbox One NAND Filesystem tool  
   
 Parses Xbox One Nanddumps for file-adresses and extracts the binary  
 files. As I only had two dumps to work with, it's probably not  
 universally compatible and contains bugs for sure :P  
   
 Enjoy!  
   
   
 Requirements  
 ===========  
 * Python 2.7  
 * Xbox One eMMC NAND Dump  
   
   
 Actions  
 ===========  
 info Reads adresses from SFBX and GFCU Table and prints them  
 to screen  
   
 extract Extracts the parsed entries from SFBX Table  
   
 sfbxscan If the SFBX adress of your NAND isn't contained, scan  
 for the MAGIC/Header and append it to the list in the  
 python script  
   
   
 Usage  
 ===========  
 Usage:  
 NANDOne.py [action] [dump]  
   
 Available Action:  
 sfbxscan Scans for SFBX address  
 info Prints the parsed entries  
 extract Extracts nand content  
   
 Example:  
 NANDOne.py sfbxscan nanddump.bin [/quote] Author: tuxuser  
 Source: [url=https://github.com/tuxuser/xboxonenand]Github[/url]

### Attachments

[NANDOne-v002.zip](NANDOne-v002.zip)