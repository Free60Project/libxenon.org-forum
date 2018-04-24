# [solved] ./build-xenon-toolchain freetype&quot; (install or update freetype) - Error

## 2012-08-03 22:39:29, posted by: nessy74

Hallo.  
   
 I use Windows XP + Cygwin.  
   
 I compiled Libxenon Toolchain from there:  
 http://free60.org/Compiling\_the\_Toolchain  
   
 when I run  
 ./build-xenon-toolchain freetype" (install or update freetype)  
   
 can not succeed  
   
 Error in build.log: "gzip: stdin: not in gzip format"  
   
 file "freetype-2.4.8.tar.gz" is in c:\Cygwin\home\Alex\libxenon\toolchain\freetype-2.4.8.tar.gz  
 size: 12 216 320  
   
 With "Total Commander" "freetype-2.4.8.tar.gz" successfully decompressed,   
 but in Cygwin does not recognize.  
   
 Help me please.

## 2012-08-03 22:48:59, posted by: Juvenal

the freetype 2.4.8.tar.gz archive is 1990395 bytes, roughly 2 MB  
   
 if yours is indeed ~12mb, something is seriously wrong with it.  
   
 delete it and let the script download it again

## 2012-08-03 23:39:32, posted by: nessy74

**[b]the problem is solved.[/b]**  
   
 I deleted the file   
 c:\Cygwin\home\Alex\libxenon\toolchain\freetype-2.4.8.tar.gz  
   
 and again ran the command:  
 ./build-xenon-toolchain freetype  
   
 Extracting freetype...  
 Configuring freetype...  
 Building freetype...  
 Installing freetype...  
 Done  
   
 Thanks for the help.

## 2012-08-03 23:45:57, posted by: ravendrow

for future reference you only need to type   
   
 ./build-xenon-toolchain libs  
   
 and it should install  
   
 zlib  
 libpng  
 bzip2  
 freetype  
 bin2s