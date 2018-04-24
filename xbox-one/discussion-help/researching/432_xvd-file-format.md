# XVD File Format

## 2013-12-08 11:30:02, posted by: tuxuser

Pretty much every file on Xbox One is packaged in a container file with extension "*.xvd".  
 It's a sort of special version from "*.vhd", the virtual harddisk format from Microsoft.  
   
 The beginning of the file (addr 0x0 - 0x200) is a Hash or Signature block.  
 At addr 0x200 theres the MAGIC "msft-vxd" (length of 0x8).  
   
 That's all for now.