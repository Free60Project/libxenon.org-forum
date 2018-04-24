# Problems when compiling kbootconf.c

## 2012-08-23 23:53:42, posted by: XenonBliss

XeLL is giving me an error when I build it, here is what Terminal is giving me.  
 [quote]root@ubuntu:/home/kai/libxenon/xell# make  
 Building xell-1f ...  
 [mount.c]  
 /home/kai/libxenon/xell/source/lv2/mount.c:469:13: warning: 'UnmountPartitions' defined but not used [-Wunused-function]  
 /home/kai/libxenon/xell/source/lv2/mount.c: In function 'FindPartitions':  
 /home/kai/libxenon/xell/source/lv2/mount.c:448:17: warning: 'interface' may be used uninitialized in this function [-Wuninitialized]  
 [kbootconf.c]  
 In file included from /usr/local/xenon/usr/include/lwip/udp.h:42:0,  
 from /usr/local/xenon/usr/include/lwip/dhcp.h:12,  
 from /usr/local/xenon/usr/include/network/network.h:9,  
 from /home/kai/libxenon/xell/source/lv2/kboot/kbootconf.c:20:  
 /usr/local/xenon/usr/include/lwip/ip.h:130:3: warning: 'packed' attribute ignored for field of type 'u8\_t' [-Wattributes]  
 /usr/local/xenon/usr/include/lwip/ip.h:132:3: warning: 'packed' attribute ignored for field of type 'u8\_t' [-Wattributes]  
 /usr/local/xenon/usr/include/lwip/ip.h:136:3: warning: 'packed' attribute ignored for field of type 'ip\_addr\_p\_t' [-Wattributes]  
 /usr/local/xenon/usr/include/lwip/ip.h:137:3: warning: 'packed' attribute ignored for field of type 'ip\_addr\_p\_t' [-Wattributes]  
 In file included from /usr/local/xenon/usr/include/network/network.h:9:0,  
 from /home/kai/libxenon/xell/source/lv2/kboot/kbootconf.c:20:  
 /usr/local/xenon/usr/include/lwip/dhcp.h:78:3: warning: 'packed' attribute ignored for field of type 'u8\_t' [-Wattributes]  
 /usr/local/xenon/usr/include/lwip/dhcp.h:79:3: warning: 'packed' attribute ignored for field of type 'u8\_t' [-Wattributes]  
 /usr/local/xenon/usr/include/lwip/dhcp.h:80:3: warning: 'packed' attribute ignored for field of type 'u8\_t' [-Wattributes]  
 /usr/local/xenon/usr/include/lwip/dhcp.h:81:3: warning: 'packed' attribute ignored for field of type 'u8\_t' [-Wattributes]  
 /usr/local/xenon/usr/include/lwip/dhcp.h:85:3: warning: 'packed' attribute ignored for field of type 'ip\_addr\_p\_t' [-Wattributes]  
 /usr/local/xenon/usr/include/lwip/dhcp.h:86:3: warning: 'packed' attribute ignored for field of type 'ip\_addr\_p\_t' [-Wattributes]  
 /usr/local/xenon/usr/include/lwip/dhcp.h:87:3: warning: 'packed' attribute ignored for field of type 'ip\_addr\_p\_t' [-Wattributes]  
 /usr/local/xenon/usr/include/lwip/dhcp.h:88:3: warning: 'packed' attribute ignored for field of type 'ip\_addr\_p\_t' [-Wattributes]  
 /usr/local/xenon/usr/include/lwip/dhcp.h:89:3: warning: 'packed' attribute ignored for field of type 'u8\_t[16]' [-Wattributes]  
 /usr/local/xenon/usr/include/lwip/dhcp.h:90:3: warning: 'packed' attribute ignored for field of type 'u8\_t[64]' [-Wattributes]  
 /usr/local/xenon/usr/include/lwip/dhcp.h:91:3: warning: 'packed' attribute ignored for field of type 'u8\_t[128]' [-Wattributes]  
 /usr/local/xenon/usr/include/lwip/dhcp.h:103:3: warning: 'packed' attribute ignored for field of type 'u8\_t[68]' [-Wattributes]  
 /home/kai/libxenon/xell/source/lv2/kboot/kbootconf.c: In function 'kboot\_set\_config':  
 /home/kai/libxenon/xell/source/lv2/kboot/kbootconf.c:94:18: warning: the comparison will always evaluate as 'false' for the address of 'ipaddr' will never be NULL [-Waddress]  
 /home/kai/libxenon/xell/source/lv2/kboot/kbootconf.c:100:18: warning: the comparison will always evaluate as 'false' for the address of 'netmask' will never be NULL [-Waddress]  
 /home/kai/libxenon/xell/source/lv2/kboot/kbootconf.c:106:18: warning: the comparison will always evaluate as 'false' for the address of 'gateway' will never be NULL [-Waddress]  
 /home/kai/libxenon/xell/source/lv2/kboot/kbootconf.c: In function 'user\_prompt':  
 /home/kai/libxenon/xell/source/lv2/kboot/kbootconf.c:415:49: error: 'struct controller\_data\_s' has no member named 'select'  
 /home/kai/libxenon/xell/source/lv2/kboot/kbootconf.c:415:67: error: 'struct controller\_data\_s' has no member named 'select'  
 make[3]: *** [kbootconf.o] Error 1  
 make[2]: *** [build] Error 2  
 make[1]: *** [stage2.elf32.gz] Error 2  
 make: *** [xell-1f.build] Error 2 [/quote] I am just trying to compile the latest build to test it and this happens.  
   
 Any reason as to why this happens?

## 2012-08-24 01:07:33, posted by: sk1080

Use tuxuser's libxenon branch  
   
 OR one of these days someone would look at the struct and realize that select has been renamed to back.....  
   
 OR one of these days people would search the forum for the compile error and realize that this has been answered before