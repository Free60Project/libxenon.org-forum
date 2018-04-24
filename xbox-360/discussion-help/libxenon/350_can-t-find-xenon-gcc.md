# Can't find xenon-gcc

## 2012-08-15 13:23:26, posted by: zoontek

Hello everyone :)  
   
 I'm a newbie in libxenon development, and tried for two days to build the toolchain, following this tutorial: http://free60.org/Xenon\_Toolchain  
 No problems with sudo or PATH...but xenon-gcc is never compiled.  
   
 I tried on Debian Wheezy, Ubuntu 12.04, Ubuntu 10.04. Same problem.  
   
 I don't know where to search now...

## 2012-08-15 13:29:00, posted by: sk1080

attach build.log

## 2012-08-15 13:42:48, posted by: zoontek

Sorry, they are in French. I hope you will understand them.

### Attachments

[build_libxenon.log](build_libxenon.log)[build_toolchain.log](build_toolchain.log)

## 2012-08-15 13:48:55, posted by: sk1080

you need the libmpc-dev, libmpfr-dev, and libgmp-dev packages  
 one might be the wrong package name but they should pull eachother in

## 2012-08-15 15:04:38, posted by: zoontek

Thanks, libgmp-dev was missing (I installed libgmp3-dev) ;D  
   
 Now...let's start!