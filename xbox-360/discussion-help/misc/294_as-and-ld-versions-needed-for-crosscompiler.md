# as and ld versions needed for crosscompiler?

## 2012-03-01 09:59:49, posted by: Xplorer4x4

Not sure where to post this so throwing it here. Trying to get a working cross compiler on my system(Debian latest) but when it comes time to run the compilation script for the powerpc target using crosstool 0.43 I get: [quote]*** These critical programs are missing or too old: as ld  
 *** Check the INSTALL file for required versions.[/quote] First problem, there is no INSTALL file from what I see.   
 Secondly, I am running Binutils 2.20.1 which is the latest version offered in the official debian repos and was released August 2011 which is much newer then the version of crosscompiler recommended in the wiki if memory serves me right. Maybe I missed something so here is the version info for as and ld. [quote] root@debian:~# as -version  
 GNU assembler (GNU Binutils for Debian) 2.20.1-system.20100303  
 Copyright 2009 Free Software Foundation, Inc.  
 This program is free software; you may redistribute it under the terms of  
 the GNU General Public License version 3 or later.  
 This program has absolutely no warranty.  
 This assembler was configured for a target of `i486-linux-gnu'.  
 root@debian:~# ld -version  
 GNU ld (GNU Binutils for Debian) 2.20.1-system.20100303  
 Copyright 2009 Free Software Foundation, Inc.  
 This program is free software; you may redistribute it under the terms of  
 the GNU General Public License version 3 or (at your option) a later version.  
 This program has absolutely no warranty.[/quote] How can I get this resolved as I really do not believe binutils is actually the issue.

## 2012-03-05 00:53:13, posted by: Xplorer4x4

So no one has ever successfully got the crosscompiler set up and can help some one trying to get a dev environment set up and be self sufficient?