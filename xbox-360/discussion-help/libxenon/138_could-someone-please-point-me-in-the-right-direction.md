# Could someone please point me in the right direction?

## 2011-08-15 02:51:22, posted by: mrkleen340

Hello, I may be late to the game but I am trying to get up to speed as fast as I can. I just got my hands on an exploitable xbox. I've been programming for several years but unfortunately my experience lies in Java and not C. My goal is to either make utilities or games for the xbox. From what I understand the elf can only be run from xell and is made using libxenon. Where as the xex is made from the SDK/dev kit and can run unsigned on JTAGs and Dev kits. Have I misunderstood or is libxenon more aimed for consoles running a linux distribution vs a dashboard. To clarify what I am asking, how are utilities xexmenu made? Is it using this or did those developers have the SDK?  
   
 Thanks for the help and please excuse my n00b-ness. :-\

## 2011-08-15 03:14:09, posted by: UNIX

First of all, welcome! :)  
   
 I am in the same boat as you, I have WAY more experience in Java than C, but I am slowly starting to get acclimated to it. To touch on your other two points:  
   
 You're right about the executeable formats. .elf files can only be run from XeLL, .xex files can only be run via a dashboard. However, you're semi-incorrect about the aim of XeLL. XeLL is essentially a bootloader for exploitable consoles, which can load .elf binaries; Be it Linux or Homebrew. All exploitable consoles need XeLL to be able to reboot into a modified kernel. So you can have a console with a version of XeLL and the latest modified dashboard. LibXenon itself aims to provide a legal and free way to create 360 homebrew. It can do much of what the SDK provides, but produce a completely free and redistributable binary. So you could make a utility like XeXMenu that is LibXenon based if you wanted to (a few of which are currently in development)  
   
 Programs like XeXMenu, FreeStyle Dash, etc are all made using the SDK, though, to touch on your final question.

## 2011-08-15 03:56:33, posted by: mrkleen340

Hey thanks for the clarification. I've been meaning to learn c and I guess this is a good a way as any. Now all I need is a project.

## 2011-08-15 04:58:44, posted by: UNIX

Well, there's plenty of example code around to learn from :)   
   
 Here is a small repository of some examples I compiled:  
   
 [url=https://github.com/IUNIXI/Xbox-360-Homebrew]https://github.com/IUNIXI/Xbox-360-Homebrew[/url]

## 2011-08-16 18:08:16, posted by: mrkleen340

Thanks for the reference, I've looked in to them and had a question about the temperature one. I am thinking it is my tv setup but Sometimes the text is crystal clear and perfectly scaled but other times it gets very blurry and goes back and fourth between these states. Also, I'm fairly certain I've setup the project correctly in NetBeans, it can't find xenos\_smc/xenon\_smc.h The project has the libxenon from the git and /usr/local/xenon so I'm not sure what other folders it needs.  
   
 p.s. While I know it already exists, I've decided I am going to make a file utility that is the xenon.elf which explores the rest of the device and allows you to boot other projects from various folders all the while displaying various system info and perhaps at some point also offer ftp. This should give me a good C starting point.