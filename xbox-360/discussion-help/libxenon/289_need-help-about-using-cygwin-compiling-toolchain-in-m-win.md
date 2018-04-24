# need help about using cygwin compiling toolchain in m$win.....

## 2012-02-20 18:41:19, posted by: kryso

rm -f lib.a  
 xenon-ar cru lib.a lib\_a-dummy.o lib\_a-argz\_add.o lib\_a-argz\_add\_sep.o lib\_a-argz\_append.o lib\_a-argz\_count.o lib\_a-argz\_create.o lib\_a-argz\_create\_sep.o lib\_a-argz\_delete.o lib\_a-argz\_extract.o lib\_a-argz\_insert.o lib\_a-argz\_next.o lib\_a-argz\_replace.o lib\_a-argz\_stringify.o lib\_a-buf\_findstr.o lib\_a-envz\_entry.o lib\_a-envz\_get.o lib\_a-envz\_add.o lib\_a-envz\_remove.o lib\_a-envz\_merge.o lib\_a-envz\_strip.o   
 xenon-ar: lib\_a-dummy.o: No such file or directory  
 Makefile:353: recipe for target `lib.a' failed  
 make[8]: *** [lib.a] Error 1  
   
 seens the lib\_a*.o file could not be compile  
   
 xenon-gcc -B/cygdrive/e/source/xbox360/free60/toolchain/build/xenon/32/newlib/ -isystem /cygdrive/e/source/xbox360/free60/toolchain/build/xenon/32/newlib/targ-include -isystem /cygdrive/e/source/xbox360/free60/toolchain/newlib-1.17.0/newlib/libc/include -B/cygdrive/e/source/xbox360/free60/toolchain/build/xenon/32/libgloss/powerpc64 -L/cygdrive/e/source/xbox360/free60/toolchain/build/xenon/32/libgloss/libnosys -L/cygdrive/e/source/xbox360/free60/toolchain/newlib-1.17.0/libgloss/powerpc64 -m32 -fPIC -mstrict-align -DPACKAGE\_NAME=\"newlib\" -DPACKAGE\_TARNAME=\"newlib\" -DPACKAGE\_VERSION=\"1.17.0\" -DPACKAGE\_STRING=\"newlib\ 1.17.0\" -DPACKAGE\_BUGREPORT=\"\" -I. -I../../../../../../newlib-1.17.0/newlib/libc/argz -O2 -DMISSING\_SYSCALL\_NAMES -fno-builtin -g -DHAVE\_BLKSIZE -m32 -fPIC -mstrict-align -c -o lib\_a-dummy.o `test -f 'dummy.c' || echo '../../../../../../newlib-1.17.0/newlib/libc/argz/'`dummy.c  
   
 do not report any error,   
 please help, sorry for my poor english...

## 2012-02-22 16:45:20, posted by: kryso

gave up, finally I use vmvare to run unbuntu, and everything is OK now.