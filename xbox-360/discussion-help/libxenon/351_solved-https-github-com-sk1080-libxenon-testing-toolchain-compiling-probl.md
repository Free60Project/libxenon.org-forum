# [solved] https://github.com/sk1080/libxenon-testing - toolchain compiling probl.

## 2012-08-16 03:28:58, posted by: nessy74

https://github.com/sk1080/libxenon-testing - toolchain compiling problems  
   
 ./build-xenon-toolchain toolchain  
 No LSB modules are available.  
 Ubuntu or Debian is detected.  
 The build-essential package was detected on your system  
 Creating final xenon toolchain directory: /usr/local/xenon  
 Extracting binutils...  
 **[b]cat: binutils.diff: No such file or directory[/b]**  
 Configuring binutils...  
   
 ====================  
 Probably need to rename these files in folder /toolchain:  
 binutils-2.22.diff > binutils.diff  
 newlib-1.17.0.diff > newlib.diff  
 ====================  
   
 After that:  
 ./build-xenon-toolchain libs  
 Downloading zlib-1.2.6.tar.bz2  
 --2012-08-16 05:06:58-- http://zlib.net/zlib-1.2.6.tar.bz2  
 Resolving zlib.net (zlib.net)... 69.73.181.135  
 Connecting to zlib.net (zlib.net)|69.73.181.135|:80... connected.  
 HTTP request sent, awaiting response... **[b]404 Not Found[/b]**  
 2012-08-16 05:06:59 ERROR 404: Not Found.  
   
 ====================  
 Probably need to make changes in "build-xenon-toolchain":  
 line 16: ZLIB=zlib-1.2.6 > ZLIB=zlib-1.2.7  
 ====================

## 2012-08-16 03:30:38, posted by: sk1080

Don't build to toolchain off my repo, just build libxenon off it then, I have never used my repo to compile the toolchain so I guess I didn't notice missing stuff

## 2012-08-16 04:22:30, posted by: nessy74

[quote="sk1080"]  
 Don't build to toolchain off my repo, just build libxenon off it then, I have never used my repo to compile the toolchain so I guess I didn't notice missing stuff  
 [/quote]  
   
 Understood.  
 But after I have described changes Toolchain compiled successfully without any errors.  
   
 ./build-xenon-toolchain cube  
 Downloading Cube Sample  
 Building Cube Sample...  
 cube.elf32 compiled, run it via xell

## 2012-08-16 04:25:12, posted by: sk1080

feel free to make a pull request  
 also, make sure you are using the gdb branch

## 2012-08-16 14:43:42, posted by: nessy74

[quote="sk1080"]make sure you are using the gdb branch[/quote]  
   
 ok, I use this repo: https://github.com/sk1080/libxenon-testing/tree/gdb&nbsp; (sk1080-libxenon-testing-70cd89b.zip)  
   
 toolchain and libs compiled successfully.  
 after that I have installed these libs:  
   
 https://github.com/LibXenonProject/xtaflib  
 https://github.com/LibXenonProject/ext2fs-xenon  
 https://github.com/LibXenonProject/ntfs-xenon  
 https://github.com/LibXenonProject/fat-xenon  
 https://github.com/LibXenonProject/ZLX-Library  
   
 were created and filled these folders:  
 /usr/local/xenon/usr/include/libfat  
 /usr/local/xenon/usr/include/libntfs  
 /usr/local/xenon/usr/include/libext2  
 /usr/local/xenon/usr/include/libxtaf  
 /usr/local/xenon/usr/include/zlx  
   
 ./build-xenon-toolchain cube  
 Downloading Cube Sample  
 Building Cube Sample...  
 cube.elf32 compiled, run it via xell  
   
 copy to usb stick, rename to xenon.elf > on Xbox 360 running successfully.