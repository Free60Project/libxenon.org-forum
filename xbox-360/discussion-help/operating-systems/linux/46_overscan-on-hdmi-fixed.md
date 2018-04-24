# Overscan on HDMI fixed!

## 2011-03-18 04:01:43, posted by: Cancerous1

thanks to Tuxuser for helping me get the kernel building down, I was able to fix overscan on hdmi! the desktop now fits the screen properly, at least on my tv ;)  
   
   
 [url=http://homebrew.allowed.org/free60/overscan\_fixed/zImage.xenon]zImage.xenon[/url]  
   
 rename it to xenon.elf, put on USB with xell.bin, launch with XellLaunch, enjoy!  
   
 *this kernel is 2.6.36.4, set to load HDD installations like Mint that reside on sda2*  
   
 **[b]Fixed composit/scart mode, this [u]will[/u] correct overscan on HDMI, but [u]not[/u] composit or scart although the garbled display in that mode is fixed.[/b]**

## 2011-03-18 04:24:34, posted by: redxs

thanks my plasma have that problem.  
   
 i try compile kernel now.  
   
 this kernel crash in web browser?  
   
 Edit:  
   
 the crash was for packet gnash(flash equal in linux) al ok .

## 2011-03-18 04:27:19, posted by: Cancerous1

its a pre-compiled kernel, ready to use :)   
   
 crashing in webbrowser? which distro are you using? any flash will probably crash the browser, unless you update it, and even then it's maybe still possible. anyway, I'm using debian mint, and i use pastebin.com and shared2.com in the webbrowser all the time, so no?

## 2011-03-18 04:48:04, posted by: redxs

yes crash probably is flash , i use debian squeeze in hdd(metod free60)  
   
   
 i see resources in debian and you compile the kernel for 1 cpu , is fine?

## 2011-03-18 04:57:27, posted by: Cancerous1

Yep, just trying 1 cpu to see if it brought more stability, let me know what you think :D it runs ok for me.   
   
 ***Does it look better on your plasma?

## 2011-03-18 05:16:37, posted by: redxs

i need probe more time for compare but for now it almost feels like all and the plasma look more better, fits well thks  
   
 what changed in kernel for fits tv ?  
 make xconfig or edit direct nano.  
   
 I want compile the kernel with adaptation for TV and USB wireless modules

## 2011-03-20 17:40:41, posted by: Cancerous1

Ok, I haven't made a patch yet, but here is my overscan fix for the 2.6.36.4 kernel, replace drivers/video/xenonfb.c, with this. report bugs here.   
 [code]* */* * framebuffer driver for Microsoft Xbox 360 * * (c) 2006 ... * Original vesafb driver written by Gerd Knorr <kraxel@goldbach.in-berlin.de> * */ #include <linux/delay.h> #include <linux/errno.h> #include <linux/fb.h> #include <linux/kernel.h> #include <linux/init.h> #include <linux/ioport.h> #include <linux/mm.h> #include <linux/module.h> #include <linux/platform\_device.h> #include <linux/screen\_info.h> #include <linux/slab.h> #include <linux/string.h> #include <linux/dmi.h> #include <asm/io.h> #include <video/vga.h> /* --------------------------------------------------------------------- */ static struct fb\_var\_screeninfo xenonfb\_defined \_\_initdata = { .activate = FB\_ACTIVATE\_NOW, .height = -1, .width = -1, .right\_margin = 32, .upper\_margin = 16, .lower\_margin = 16, .vsync\_len = 4, .vmode = FB\_VMODE\_NONINTERLACED, }; static struct fb\_fix\_screeninfo xenonfb\_fix \_\_initdata = { .id = "XENON FB", .type = FB\_TYPE\_PACKED\_PIXELS, .accel = FB\_ACCEL\_NONE, .visual = FB\_VISUAL\_TRUECOLOR, }; typedef struct { uint32\_t unknown1[4]; uint32\_t base; uint32\_t unknown2[8]; uint32\_t width; uint32\_t height; } ati\_info; #define DEFAULT\_FB\_MEM 1024*1024*16 /* --------------------------------------------------------------------- */ static int xenonfb\_setcolreg(unsigned regno, unsigned red, unsigned green, unsigned blue, unsigned transp, struct fb\_info *info) { /* * Set a single color register. The values supplied are * already rounded down to the hardware's capabilities * (according to the entries in the `var' structure). Return * != 0 for invalid regno. */ if (regno >= info->cmap.len) return 1; if (regno < 16) { red >>= 8; green >>= 8; blue >>= 8; ((u32 *)(info->pseudo\_palette))[regno] = (red << info->var.red.offset) | (green << info->var.green.offset) | (blue << info->var.blue.offset); } return 0; } #define XENON\_XY\_TO\_STD\_PTR(x,y) ((int*)(((char*)p->screen\_base)+y*p->fix.line\_length+x*(p->var.bits\_per\_pixel/8))) #define XENON\_XY\_TO\_XENON\_PTR(x,y) xenon\_convert(p, XENON\_XY\_TO\_STD\_PTR(x,y)) inline void xenon\_pset(struct fb\_info *p, int x, int y, int color) { fb\_writel(color, XENON\_XY\_TO\_XENON\_PTR(x,y)); } inline int xenon\_pget(struct fb\_info *p, int x, int y) { return fb\_readl(XENON\_XY\_TO\_XENON\_PTR(x,y)); } void xenon\_fillrect(struct fb\_info *p, const struct fb\_fillrect *rect) { \_\_u32 x, y; for (y=0; y<rect->height; y++) { for (x=0; x<rect->width; x++) { xenon\_pset(p, rect->dx+x, rect->dy+y, rect->color); } } } void xenon\_copyarea(struct fb\_info *p, const struct fb\_copyarea *area) { /* if the beginning of the target area might overlap with the end of the source area, be have to copy the area reverse. */ if ((area->dy == area->sy && area->dx > area->sx) || (area->dy > area->sy)) { \_\_s32 x, y; for (y=area->height-1; y>0; y--) { for (x=area->width-1; x>0; x--) { xenon\_pset(p, area->dx+x, area->dy+y, xenon\_pget(p, area->sx+x, area->sy+y)); } } } else { \_\_u32 x, y; for (y=0; y<area->height; y++) { for (x=0; x<area->width; x++) { xenon\_pset(p, area->dx+x, area->dy+y, xenon\_pget(p, area->sx+x, area->sy+y)); } } } } static struct fb\_ops xenonfb\_ops = { .owner = THIS\_MODULE, .fb\_setcolreg = xenonfb\_setcolreg, .fb\_fillrect = xenon\_fillrect, .fb\_copyarea = xenon\_copyarea, .fb\_imageblit = cfb\_imageblit, }; static int \_\_init xenonfb\_probe(struct platform\_device *dev) { struct fb\_info *info; int err; unsigned int size\_vmode; unsigned int size\_remap; unsigned int size\_total; volatile int *gfx = ioremap(0x200ec806000ULL, 0x1000); volatile ati\_info *ai = ((void*)gfx) + 0x100; /* setup native resolution, i.e. disable scaling */ int vxres = gfx[0x134/4]; int vyres = gfx[0x138/4]; int black\_top = gfx[0x44/4]; int offset = gfx[0x580/4]; int offset\_x = (offset >> 16) & 0xFFFF; int offset\_y = offset & 0xFFFF; int nxres, nyres; int scl\_h = gfx[0x5b4/4], scl\_v = gfx[0x5c4/4]; /*if ((((ai->height+31)>>5)<<5) <= 576) { offset\_x = (ai->width/100); //50; offset\_y = (ai->height/100); //50; }*/ if ((((ai->width+31)>>5)<<5) > 1024) { offset\_x = (ai->width/40); offset\_y = (ai->height/40); } if (gfx[0x590/4] == 0) scl\_h = scl\_v = 0x01000000; nxres = (vxres - offset\_x * 2) * 0x1000 / (scl\_h/0x1000); nyres = (vyres - offset\_y * 2) * 0x1000 / (scl\_v/0x1000) + black\_top * 2; printk("virtual resolution: %d x %dn", vxres, vyres); printk("offset: x=%d, y=%dn", offset\_x, offset\_y); printk("black: %d %d, %d %dn", gfx[0x44/4], gfx[0x48/4], gfx[0x4c/4], gfx[0x50/4]); printk("native resolution: %d x %dn", nxres, nyres); screen\_info.lfb\_depth = 32; screen\_info.lfb\_size = DEFAULT\_FB\_MEM / 0x10000; screen\_info.pages=1; screen\_info.blue\_size = 8; screen\_info.blue\_pos = 24; screen\_info.green\_size = 8; screen\_info.green\_pos = 16; screen\_info.red\_size = 8; screen\_info.red\_pos = 8; screen\_info.rsvd\_size = 8; screen\_info.rsvd\_pos = 0; /*if ((((ai->height+31)>>5)<<5) <= 576) { gfx[0x44/4] = 6; // overscan black bar gfx[0x48/4] = 6; gfx[0x4c/4] = 10; gfx[0x50/4] = 10; }*/ if ((((ai->width+31)>>5)<<5) > 1024) { gfx[0x44/4] = 18; // overscan black bar gfx[0x48/4] = 18; gfx[0x4c/4] = 28; gfx[0x50/4] = 28; } else { gfx[0x44/4] = 0; // disable black bar gfx[0x48/4] = 0; gfx[0x4c/4] = 0; gfx[0x50/4] = 0; } gfx[0x590/4] = 0; // disable scaling gfx[0x584/4] = (nxres << 16) | nyres; gfx[0x580/4] = 0; // disable offset gfx[0x5e8/4] = (nxres * 4) / 0x10 - 1; // fix pitch gfx[0x134/4] = nxres; gfx[0x138/4] = nyres; ai->base &= ~0xFFFF; // page-align. screen\_info.lfb\_base = ai->base; screen\_info.lfb\_width = ai->width; screen\_info.lfb\_height = ai->height; screen\_info.lfb\_linelength = screen\_info.lfb\_width * screen\_info.lfb\_depth/4; gfx[0x120/4] = screen\_info.lfb\_linelength / 8; /* fixup pitch, in case we switched resolution */ printk(KERN\_INFO "xenonfb: detected %dx%d framebuffer @ 0x%08xn", screen\_info.lfb\_width, screen\_info.lfb\_height, screen\_info.lfb\_base); iounmap(gfx); xenonfb\_fix.smem\_start = screen\_info.lfb\_base; xenonfb\_defined.bits\_per\_pixel = screen\_info.lfb\_depth; xenonfb\_defined.xres = screen\_info.lfb\_width; xenonfb\_defined.yres = screen\_info.lfb\_height; xenonfb\_defined.xoffset = 0; xenonfb\_defined.yoffset = 0; xenonfb\_fix.line\_length = screen\_info.lfb\_linelength; /* size\_vmode -- that is the amount of memory needed for the * used video mode, i.e. the minimum amount of * memory we need. */ size\_vmode = xenonfb\_defined.yres * xenonfb\_fix.line\_length; /* size\_total -- all video memory we have. Used for * entries, ressource allocation and bounds * checking. */ size\_total = screen\_info.lfb\_size * 65536; if (size\_total < size\_vmode) size\_total = size\_vmode; /* size\_remap -- the amount of video memory we are going to * use for xenonfb. With modern cards it is no * option to simply use size\_total as that * wastes plenty of kernel address space. */ size\_remap = size\_vmode * 2; if (size\_remap < size\_vmode) size\_remap = size\_vmode; if (size\_remap > size\_total) size\_remap = size\_total; xenonfb\_fix.smem\_len = size\_remap; if (!request\_mem\_region(xenonfb\_fix.smem\_start, size\_total, "xenonfb")) { printk(KERN\_WARNING "xenonfb: cannot reserve video memory at 0x%lxn", xenonfb\_fix.smem\_start); /* We cannot make this fatal. Sometimes this comes from magic spaces our resource handlers simply don't know about */ } info = framebuffer\_alloc(sizeof(u32) * 16, &dev->dev); if (!info) { err = -ENOMEM; goto err\_release\_mem; } info->pseudo\_palette = info->par; info->par = NULL; info->screen\_base = ioremap(xenonfb\_fix.smem\_start, xenonfb\_fix.smem\_len); if (!info->screen\_base) { printk(KERN\_ERR "xenonfb: abort, cannot ioremap video memory " "0x%x @ 0x%lxn", xenonfb\_fix.smem\_len, xenonfb\_fix.smem\_start); err = -EIO; goto err\_unmap; } printk(KERN\_INFO "xenonfb: framebuffer at 0x%lx, mapped to 0x%p, " "using %dk, total %dkn", xenonfb\_fix.smem\_start, info->screen\_base, size\_remap/1024, size\_total/1024); printk(KERN\_INFO "xenonfb: mode is %dx%dx%d, linelength=%d, pages=%dn", xenonfb\_defined.xres, xenonfb\_defined.yres, xenonfb\_defined.bits\_per\_pixel, xenonfb\_fix.line\_length, screen\_info.pages); xenonfb\_defined.xres\_virtual = xenonfb\_defined.xres; xenonfb\_defined.yres\_virtual = xenonfb\_fix.smem\_len / xenonfb\_fix.line\_length; printk(KERN\_INFO "xenonfb: scrolling: redrawn"); xenonfb\_defined.yres\_virtual = xenonfb\_defined.yres; /* some dummy values for timing to make fbset happy */ xenonfb\_defined.pixclock = 10000000 / xenonfb\_defined.xres * 1000 / xenonfb\_defined.yres; xenonfb\_defined.left\_margin = (xenonfb\_defined.xres / 8) & 0xf8; xenonfb\_defined.hsync\_len = (xenonfb\_defined.xres / 8) & 0xf8; if ((((ai->width+31)>>5)<<5) > 1024) { xenonfb\_defined.left\_margin = offset\_x; //xenonfb\_defined.hsync\_len = offset\_x; } printk(KERN\_INFO "xenonfb: pixclk=%ld left=%02x hsync=%02xn", (unsigned long)xenonfb\_defined.pixclock, xenonfb\_defined.left\_margin, xenonfb\_defined.hsync\_len); xenonfb\_defined.red.offset = screen\_info.red\_pos; xenonfb\_defined.red.length = screen\_info.red\_size; xenonfb\_defined.green.offset = screen\_info.green\_pos; xenonfb\_defined.green.length = screen\_info.green\_size; xenonfb\_defined.blue.offset = screen\_info.blue\_pos; xenonfb\_defined.blue.length = screen\_info.blue\_size; xenonfb\_defined.transp.offset = screen\_info.rsvd\_pos; xenonfb\_defined.transp.length = screen\_info.rsvd\_size; printk(KERN\_INFO "xenonfb: %s: " "size=%d:%d:%d:%d, shift=%d:%d:%d:%dn", "Truecolor", screen\_info.rsvd\_size, screen\_info.red\_size, screen\_info.green\_size, screen\_info.blue\_size, screen\_info.rsvd\_pos, screen\_info.red\_pos, screen\_info.green\_pos, screen\_info.blue\_pos); xenonfb\_fix.ypanstep = 0; xenonfb\_fix.ywrapstep = 0; /* request failure does not faze us, as vgacon probably has this * region already (FIXME) */ request\_region(0x3c0, 32, "xenonfb"); info->fbops = &xenonfb\_ops; info->var = xenonfb\_defined; info->fix = xenonfb\_fix; info->flags = FBINFO\_FLAG\_DEFAULT; if (fb\_alloc\_cmap(&info->cmap, 256, 0) < 0) { err = -ENOMEM; goto err\_unmap; } if (register\_framebuffer(info)<0) { err = -EINVAL; goto err\_fb\_dealoc; } printk(KERN\_INFO "fb%d: %s frame buffer devicen", info->node, info->fix.id); return 0; err\_fb\_dealoc: fb\_dealloc\_cmap(&info->cmap); err\_unmap: iounmap(info->screen\_base); framebuffer\_release(info); err\_release\_mem: release\_mem\_region(xenonfb\_fix.smem\_start, size\_total); return err; } static struct platform\_driver xenonfb\_driver = { .probe = xenonfb\_probe, .driver = { .name = "xenonfb", }, }; static struct platform\_device xenonfb\_device = { .name = "xenonfb", }; static int \_\_init xenonfb\_init(void) { int ret; ret = platform\_driver\_register(&xenonfb\_driver); if (!ret) { ret = platform\_device\_register(&xenonfb\_device); if (ret) platform\_driver\_unregister(&xenonfb\_driver); } return ret; } module\_init(xenonfb\_init); MODULE\_LICENSE("GPL"); [/code]

## 2011-03-20 19:03:11, posted by: sbarrenechea

![](http://i53.tinypic.com/8xq92f.jpg)[img]http://i53.tinypic.com/8xq92f.jpg[/img]  
   
 Nice, huh? xDDD  
   
 That happened when I rename the file zImage.xenon to xenon.elf and get started via Xell-Reloaded... I don't know if zImage.xenon is updated with the overscan fix "drivers/video/xenonfb.c" but... Anyway, that's what I get with the zImage.xenon kernel in a normal TV hahaha

## 2011-03-20 19:21:21, posted by: Cancerous1

that was with the attached kernel from this thread? thanks for testing and i'll work on correcting it. It should look good on hdmi tho :S

## 2011-03-20 19:23:00, posted by: sbarrenechea

[quote=""Cancerous1""]that was with the attached kernel from this thread? thanks for testing and i'll work on correcting it. It should look good on hdmi tho :S[/quote]  
   
 I can't test with mi HDTV right now, but with the Ubuntu 10.10 beta 5 default kernel with the HDMI connected gets crashed loading... :S  
   
 I'm gonna attach some pics later...

## 2011-03-21 13:01:03, posted by: Cancerous1

fixed messed up display in composit mode, link/source updated

## 2011-03-21 18:33:04, posted by: sbarrenechea

[quote=""Cancerous1""]fixed messed up display in composit mode, link/source updated[/quote]  
   
 I'm getting a kernel panic... So, is no solution for screen-fit with composit? :(

## 2011-03-22 02:55:27, posted by: Cancerous1

Idk the kernel is open source, I just reverted the changes I tried for the composit mode since they messed the screen up. I may give it another shot, but at least having it fixed on HDMI without introducing new bugs, is progress.  
   
 When/where/why did the kernel panic?

## 2011-03-22 19:47:05, posted by: sbarrenechea

![](http://i53.tinypic.com/9i4a5t.jpg)[img]http://i53.tinypic.com/9i4a5t.jpg[/img]  
   
 :B

## 2012-02-27 15:57:08, posted by: fentis

sorry to bump a 1 year old thread...  
   
 This is kernel 2.6.38.8 with a slightly modified HDMI overscan fix posted by Cancerous.  
   
 [attachmini=1]

### Attachments

[vmlinux.rar](vmlinux.rar)

## 2012-05-05 20:29:36, posted by: speed3r

[quote="fentis"]  
 sorry to bump a 1 year old thread...  
   
 This is kernel 2.6.38.8 with a slightly modified HDMI overscan fix posted by Cancerous.  
   
 [attachmini=1]  
 [/quote]  
   
 Do someone got a fix because i still get a kernel panic! :-[