# LibXenon Reorganization

## 2012-03-06 22:39:16, posted by: tuxuser

Layout is pretty much from devkitPPC / wii - hope everybody is okay with that?  
### Sourceforge - Mainly For Binaries  
 1. Precompiled devkitPPC / devkitXenon / devkit360 / XenonToolchain (no idea how it will be called) -- Linux x86 / x86\_64 - Windows i386 - ?Mac OSX?  
 -- Documentation  
 -- Toolchain includes libs (portlibs) like: Expat, FreeType, libjpeg, libpng, Mini-XML, libtremor, zlib  
 -- Also a tool to upload files via UART and debug via GDB?  
   
 2. Precompiled LibXenon - ?Milestones?  
 -- Documentation / examples  
   
 3. Precompiled tools repo (imgbuild scripts JTAG/RGH, Pic SPI Flasher, POST Reader whatever)  
   
 4. Library sourcecode (the ones included in devkitPPC/*/* - /portlibs/ )  
   
 5. Sourcecode of toolchain applications (gcc,binutils,newlib,gdb etc.)  
   
 5. Other essential precompiled libraries (libfdt, lwip, libelf etc.)  
   
   
### Github - For sources (:P)  

   
 1. "devkitPPC Repository" - includes toolchain sources + patches + install script + documentation + portlibs  
 2. "LibXenon Repository" - LibXenon sourcecode + examples + documentation  
 3. Seperate git repos for other libs  
   
   
### Wiki - free60.org
   
 XX. We will see later :P [/quote] Would appreciate some input/recommendations etc.