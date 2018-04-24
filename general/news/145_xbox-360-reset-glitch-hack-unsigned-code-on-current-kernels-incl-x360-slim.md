# Xbox 360 Reset Glitch Hack - Unsigned Code on current Kernels incl. X360 SLIM

## 2011-08-28 15:10:50, posted by: tuxuser

You thought it wouldn't be possible?   
 You thought there are only (a few) JTAGs or total overpriced Devkits to run unsigned Code?  
   
 GliGli & Tiros are proving the opposite! They developed a Hack which glitches all recent Xbox360 Kernels to run unsigned Code on:  
   
 [align=center]**[b]ZEPHYR, FALCON, JASPER .......and...... TRINITY (aka SLIM!).[/b]**[/align]  
 [align=center](no matter which Dashboard/Kernel they are running)[/align]  
   
 [align=center][youtube]http://www.youtube.com/watch?feature=player\_embedded&v=JyYdL4L6vwE[/youtube][/align]  
   
 Here is the detailed technical explaination  
 [quote] **********************************  
 * The Xbox 360 reset glitch hack *  
 **********************************  
   
 Introduction / some important facts  
 ===================================  
   
 tmbinc said it himself, software based approaches of running unsigned code on the 360 mostly don't work, it was designed to be secure from a software point of view.  
   
 The processor starts running code from ROM (1bl) , which then starts loading a RSA signed and RC4 crypted piece of code from NAND (CB).  
   
 CB then initialises the processor security engine, its task will be to do real time encryption and hash check of physical DRAM memory. From what we found, it's using AES128 for crypto and strong (Toeplitz ?) hashing. The crypto is different each boot because it is seeded at least from:  
 - A hash of the entire fuseset.  
 - The timebase counter value.  
 - A truly random value that comes from the hardware random number generator the processor embeds. on fats, that RNG could be electronically deactivated, but there's a check for "apparent randomness" (merely a count of 1 bits) in CB, it just waits for a seemingly proper random number.  
   
 CB can then run some kind of simple bytecode based software engine whose task will mainly be to initialise DRAM, CB can then load the next bootloader (CD) from NAND into it, and run it.  
   
 Basically, CD will load a base kernel from NAND, patch it and run it.  
   
 That kernel contains a small privileged piece of code (hypervisor), when the console runs, this is the only code that would have enough rights to run unsigned code.  
 In kernel versions 4532/4548, a critical flaw in it appeared, and all known 360 hacks needed to run one of those kernels and exploit that flaw to run unsigned code.  
 On current 360s, CD contains a hash of those 2 kernels and will stop the boot process if you try to load them.  
 The hypervisor is a relatively small piece of code to check for flaws and apparently no newer ones has any flaws that could allow running unsigned code.  
   
 On the other hand, tmbinc said the 360 wasn't designed to withstand certain hardware attacks such as the timing attack and "glitching".  
   
 Glitching here is basically the process of triggering processor bugs by electronical means.  
   
 This is the way we used to be able to run unsigned code.  
   
 The reset glitch in a few words  
 ===============================  
   
 We found that by sending a tiny reset pulse to the processor while it is slowed down does not reset it but instead changes the way the code runs, it seems it's very efficient at making bootloaders memcmp functions always return "no differences". memcmp is often used to check the next bootloader SHA hash against a stored one, allowing it to run if they are the same. So we can put a bootloader that would fail hash check in NAND, glitch the previous one and that bootloader will run, allowing almost any code to run.  
   
 Details for the fat hack  
 ========================  
   
 On fats, the bootloader we glitch is CB, so we can run the CD we want.  
   
 cjak found that by asserting the CPU\_PLL\_BYPASS signal, the CPU clock is slowed down a lot, there's a test point on the motherboard that's a fraction of CPU speed, it's 200Mhz when the dash runs, 66.6Mhz when the console boots, and 520Khz when that signal is asserted.  
   
 So it goes like that:  
 - We assert CPU\_PLL\_BYPASS around POST code 36 (hex).  
 - We wait for POST 39 start (POST 39 is the memcmp between stored hash and image hash), and start a counter.  
 - When that counter has reached a precise value (it's often around 62% of entire POST 39 length), we send a 100ns pulse on CPU\_RESET.  
 - We wait some time and then we deassert CPU\_PLL\_BYPASS.  
 - The cpu speed goes back to normal, and with a bit of luck, instead of getting POST error AD, the boot process continues and CB runs our custom CD.  
   
 The NAND contains a zero-paired CB, our payload in a custom CD, and a modified SMC image.  
 A glitch being unreliable by nature, we use a modified SMC image that reboots infinitely (ie stock images reboot 5 times and then go RROD) until the console has booted properly.  
 In most cases, the glitch succeeds in less than 30 seconds from power on that way.  
   
 Details for the slim hack  
 =========================  
   
 The bootloader we glitch is CB\_A, so we can run the CB\_B we want.  
   
 On slims, we weren't able to find a motherboard track for CPU\_PLL\_BYPASS.  
 Our first idea was to remove the 27Mhz master 360 crystal and generate our own clock instead but it was a difficult modification and it didn't yield good results.  
 We then looked for other ways to slow the CPU clock down and found that the HANA chip had configurable PLL registers for the 100Mhz clock that feeds CPU and GPU differential pairs.  
 Apparently those registers are written by the SMC through an I2C bus.  
 I2C bus can be freely accessed, it's even available on a header (J2C3).  
 So the HANA chip will now become our weapon of choice to slow the CPU down (sorry tmbinc, you can't always be right, it isn't boring and it does sit on an interesting bus ;)  
   
 So it goes like that:  
 - We send an i2c command to the HANA to slow down the CPU at POST code D8 .  
 - We wait for POST DA start (POST DA is the memcmp between stored hash and image hash), and start a counter.  
 - When that counter has reached a precise value, we send a 20ns pulse on CPU\_RESET.  
 - We wait some time and then we send an i2c command to the HANA to restore regular CPU clock.  
 - The cpu speed goes back to normal, and with a bit of luck, instead of getting POST error F2, the boot process continues and CB\_A runs our custom CB\_B.  
   
 When CB\_B starts, DRAM isn't initialised so we chose to only apply a few patches to it so that it can run any CD, the patches are:  
 - Always activate zero-paired mode, so that we can use a modified SMC image.  
 - Don't decrypt CD, instead expect a plaintext CD in NAND.  
 - Don't stop the boot process if CD hash isn't good.  
   
 CB\_B is RC4 crypted, the key comes from the CPU key, so how do we patch CB\_B without knowing the CPU key?  
 RC4 is basically:  
 crypted = plaintext xor pseudo-random-keystream  
 So if we know plaintext and crypted, we can get the keystream, and with the keystream, we can encrypt our own code. It goes like that:  
 guessed-pseudo-random-keystream = crypted xor plaintext  
 new-crypted = guessed-pseudo-random-keystream xor plaintext-patch  
 You could think there's a chicken and egg problem, how did we get plaintext in the first place?  
 Easy: we had plaintext CBs from fat consoles, and we thought the first few bytes of code would be the same as the new CB\_B, so we could encrypt a tiny piece of code to dump the CPU key and decrypt CB\_B!  
   
 The NAND contains CB\_A, a patched CB\_B, our payload in a custom plaintext CD, and a modified SMC image.  
 The SMC image is modified to have infinite reboot, and to prevent it from periodically sending I2C commands while we send ours.  
   
 Now, maybe you haven't realised yet, but CB\_A contains no checks on revocation fuses, so it's an unpatchable hack !  
   
 Caveats  
 =======  
   
 Nothing is ever perfect, so there are a few caveats to that hack:  
 - Even in the glitch we found is pretty reliable (25% success rate per try on average), it can take up to a few minutes to boot to unsigned code.  
 - That success rate seems to depend on something like the hash of the modified bootloader we want to run (CD for fats and CB\_B for slims).  
 - It requires precise and fast hardware to be able to send the reset pulse.  
   
 Our current implementation  
 ==========================  
   
 We used a Xilinx CoolRunner II CPLD (xc2c64a) board, because it's fast, precise, updatable, cheap and can work with 2 different voltage levels at the same time.  
 We use the 48Mhz standby clock from the 360 for the glitch counter. For the slim hack, the counter even runs at 96Mhz (incremented on rising and falling edges of clock)  
 The cpld code is written in VHDL.  
 We need it to be aware of the current POST code, our first implementations used the whole 8 bits POST port for this, but we are now able to detect the changes of only 1 POST bit, making wiring easier.  
   
 Conclusion  
 ==========  
   
 We tried not to include any MS copyrighted code in the released hack tools.  
 The purpose of this hack is to run Xell and other free software, I (GliGli) did NOT do it to promote piracy or anything related, I just want to be able to do whatever I want with the hardware I bought, including running my own native code on it.  
   
 Credits  
 =======  
   
 GliGli, Tiros: Reverse engineering and hack development.  
 cOz: Reverse engineering, beta testing.  
 Razkar, tuxuser: beta testing.  
 cjak, Redline99, SeventhSon, tmbinc, anyone I forgot... : Prior reverse engineering and/or hacking work on the 360. [/quote] **[b]Download:[/b]** [url=http://libxenon.org/http://libxenon.org//viewtopic.php?t=5]Thread[/url]  
 **[b]Tutorial:[/b]** [url=http://libxenon.org/http://libxenon.org//viewtopic.php?t=6]SLIM[/url] [url=http://libxenon.org/http://libxenon.org//viewtopic.php?t=4]FAT[/url]

## 2011-08-28 15:29:02, posted by: bestpig

This is great news, thank you for your work.

## 2011-08-28 15:32:00, posted by: LordX

Awesome! Great job ;D

## 2011-08-28 15:36:42, posted by: gomson

OMFG!!!!!!  
 This really big indeed!!!!! 8) 8) 8)

## 2011-08-28 16:02:01, posted by: sajdor

its coming ... tons of libxenon homebrew :)!!!!  
   
 THANK YOU !!!

## 2011-08-28 16:11:16, posted by: chriss179

How exiting! Now comes the million dollar question which is will this bring commercial products (modchips) which are pre programmed and better suited for the job. It doesn't sound too bad already, but infinite boot also takes away the rrod error code right? Also i hope that those 2 minutes can be reduced to the same amount of time of a traditional jtag. Ofcourse if the method simply doesn't allow for a short boot it still is the greatest thing to happen to xbox360 since the dvd drive firmware was hacked.  
   
 P.s. This is truly amazin, even more so if microsoft is now unable to "fix" the issue with future dashboard updates. I have alot of boxes lying around just screaming for unsigned code! Xbmc or the like....... This c/would truly breathe life into the xbox360 homebrew community.  
   
 A million thanx to everyone involved in opening this console!

## 2011-08-28 16:17:57, posted by: Cancerous1

This beats the JTAG hack in a few ways, ;)

## 2011-08-28 16:29:19, posted by: silversid

Bring on the HomeBrew. Maybe we will get a form of XBMC?  
   
 Exciting news.

## 2011-08-28 16:32:28, posted by: dreamboy

Awsome news :P there's no stop now xD

## 2011-08-28 16:33:41, posted by: JaRaBcN

Incredible!!!! Thanks a lot for that work :D

## 2011-08-28 16:39:02, posted by: charlo.charli

Really awesome ;) I was always thinking that LibXenon will write another page of history! Thanks for the hard work, and keep optimise it. You guys are the bests!

## 2011-08-28 16:43:50, posted by: Moon666

Nice One :)

## 2011-08-28 16:58:39, posted by: Telemaque

Wouaaaaa, :o  
   
 Ok, je respecte ce superbe boulot mais j'imagine bien qu'un FreeBoot débarquera d'ici peu.  
 Je me trompe ?  
   
 @+++  
 ::)

## 2011-08-28 17:12:57, posted by: peet8989

what a shiny day for all the fans of homebrew! you revibed the scene! thank you!!! :D

## 2011-08-28 17:30:34, posted by: boflc

congrats to GliGli, Tiros & cOz and all those helping.

## 2011-08-28 17:57:06, posted by: JPizzle

Great work guys :D  
 we appreciate your hard work

## 2011-08-28 17:58:52, posted by: Deany95

Sounds really promising.

## 2011-08-28 18:14:00, posted by: DARKFiB3R

[quote="Cancerous1"]  
 This beats the JTAG hack in a few ways, ;)  
 [/quote]  
 Care to elaborate? :)  
   
 Congrats to everybody involved, this is such great news. Think I'm developing a bit of a man crush on GliGli lol

## 2011-08-28 18:31:12, posted by: DazEB

Haha, amazing, well done to all involved :)

## 2011-08-28 18:35:12, posted by: silversid

Also. The post says ZEPHYR, JASPER .......and...... TRINITY (aka SLIM!).  
   
 Does this include flacon yet?

## 2011-08-28 19:12:40, posted by: Oggy

I have a stock Falcon here if Tiros or GliGli want it?  
   
 UK based, though.  
   
 Excellent work by the way!

## 2011-08-28 19:28:26, posted by: JtagMan

Does the 25% success rate refer to per boot or per console??  
   
 as in does it only boot at 1 in 4 tries   
   
 or  
   
 Does it only work on 1 in 4 consoles?

## 2011-08-28 19:31:05, posted by: WarriorSan

Awesome work! Can't wait what the future brings!

## 2011-08-28 19:46:55, posted by: Doerek

What we all should do next...is...  
 ...do the Homebrew-Scene a favor [size=3]...spread the Word![/size]  
   
 [size=2]Let everyone know what ~> GliGli, Tiros, cOz, Razkar, tuxuser, cjak, Redline99, SeventhSon & tmbinc ...just discovered[/size]

## 2011-08-28 20:15:40, posted by: JtagMan

Is it true that this will not be able to be patched through future updates as CB\_A contains no checks or revocation fuses and only be patched through a new hardware revision??

## 2011-08-28 21:09:55, posted by: Deany95

[quote="JtagMan"]  
 Is it true that this will not be able to be patched through future updates as CB\_A contains no checks or revocation fuses and only be patched through a new hardware revision??  
 [/quote]  
   
 Yes.

## 2011-08-28 21:22:37, posted by: Juggahaxor

Amazing work guys!! Keep up the legal homebrew work.

## 2011-08-28 21:30:34, posted by: charlo.charli

[quote="Telemaque"]  
 Wouaaaaa, :o  
   
 Ok, je respecte ce superbe boulot mais j'imagine bien qu'un FreeBoot débarquera d'ici peu.  
 Je me trompe ?  
   
 @+++  
 ::)  
 [/quote]  
   
 Ici c'est une méthode Hardware et non software. Tu sais le pontage JTAG qu'on devait faire sur la FAT vulnérable? Ben c'est la même chose a l'aide d'une "puce" qui est une board de développement. On verra surement par la suite des puces commercialisé qui reprendront le même schéma :) Mais ça sera difficile de faire moins cher que la board de dev utilisé...

## 2011-08-28 21:41:15, posted by: ddxcb

One sentence, "You can run what ever you guys want".  
   
 Take that MS and let us do what ever we want, it's our system.

## 2011-08-28 22:10:52, posted by: SpkLeader

Thank you gang! :D  
   
 Can't wait to mod my slims... 8)

## 2011-08-28 23:25:45, posted by: GliGli

[quote="JtagMan"]  
 Does the 25% success rate refer to per boot or per console??  
   
 as in does it only boot at 1 in 4 tries   
   
 or  
   
 Does it only work on 1 in 4 consoles?  
 [/quote]  
   
 Each try has 1/4 chance to succeed, a try takes around 5 seconds, then the console will try again, and again and .... you got it ;)  
 That means it takes less than a minute to boot to unsigned code most of the time.

## 2011-08-29 00:19:21, posted by: zyx1141

[quote] ZEPHYR, JASPER .......and...[/quote] We are waiting for schematics for theese boards.   
   
 Glad to run linux on any xbox. ;)  
   
 Thanks in andvance!

## 2011-08-29 00:25:27, posted by: Razkar

[quote="zyx1141"] [quote] ZEPHYR, JASPER .......and...[/quote] We are waiting for schematics for theese boards.   
   
 Glad to run linux on any xbox. ;)  
   
 Thanks in andvance! [/quote] In the hack archive FAT/wiring/ ;)

## 2011-08-29 01:08:18, posted by: zyx1141

[quote="Razkar"]  
 In the hack archive FAT/wiring/ ;)  
 [/quote]  
   
 I have found it, thanks.  
 I am a bit tired on my timezone, and was looking just on tutorial:)  
   
 I have a dvd-rom key to recover, thanks a milion!!!  
   
 On the last picture, with the wiring done there are more wires witch go to CPLD.  
 I assume that there is Spi reader connected and other stuff?

## 2011-08-29 03:23:00, posted by: DARKFiB3R

So... A silly question (silly answers welcome :) ). Are these boxes going to get a new nick name, or will the term JTAG still stick like mud? Pretty sure I remember reading somewhere (probably on xbh) that "JTAG" wasn't really the correct term to use in the first place, but obviously it has become the norm.  
   
 Anyways.... on with my embarrassing suggestions   
   
 **[b]Re[/b]**set **[b]Gli[/b]**tch Hack  
 **[b]Gli[/b]**Gli  
 Trio**[b]s[/b]**  
 c**[b]O[/b]**z  
   
 ReGlitchOS  
 ReGlitched  
 Glitched  
 GlitchBox  
 Gli60  
 360G  
   
 I'll get my coat :-[ lol

## 2011-08-29 03:46:57, posted by: Twisted Impulse

Great news Tux. Knew something like this was in the works for a long time but didn't know when it would be released to the public. :D  
   
 Also, I've been referring to this exploit as the IC hack for the past day, since the 'JTAG' hack is named after part of the exploitation process. The new exploit requires the use of an IC, so why not call it something along the lines of the 'IC Hack'? :P  
   
 Noobs need to realise there IS a difference between the two exploits, and it would be nice to create a term everyone understands to differentiate between the two in a conversation. Do you have any suggestions Tux?

## 2011-08-29 04:23:31, posted by: JtagMan

I've just been calling it Jtagv2 until an official name is released.

## 2011-08-29 04:29:04, posted by: JtagMan

[quote] In the hack archive FAT/wiring/ ;) [/quote] sorry not sure where this is can you elaborate some??

## 2011-08-29 04:34:05, posted by: boflc

[quote="JtagMan"]  
   
 [quote="raz"]  
 In the hack archive FAT/wiring/ ;)  
 [/quote]  
   
 sorry not sure where this is can you elaborate some??  
 [/quote]  
   
 hack archive == the rar file that contains the goodness.

## 2011-08-29 04:42:35, posted by: Cancerous1

[quote="JtagMan"]  
 I've just been calling it Jtagv2 until an official name is released.  
 [/quote]  
   
 It's the glitch hack, the only jtag involved is programming the chip and that part isn't a hack of any sort.

## 2011-08-29 04:45:35, posted by: JtagMan

thats true jtag just seems to be sticking. most people dont actually know what jtag is originally but know what you mean when u say jtag xbox  
   
 I'm fine with a name change just none have really been given to it.

## 2011-08-29 06:29:27, posted by: DARKFiB3R

I'm liking just glitch/glitched as a way to describe this hack.  
   
 "you should glitch it"  
 "get a glitched box"  
 "only runs on glitched boxes"  
   
 Nice and simple, a bit more accurate, and sounds kinda cool if you ask me. :)

## 2011-08-29 10:37:11, posted by: GliGli

Hmm, that probably means peoples didn't even read the title: https://github.com/gligli/tools/blob/master/reset\_glitch\_hack/reset\_glitch\_hack.txt#L2&nbsp; :P  
   
 Glitch/glitching/glitched/glitcher sounds good too, but please don't call it anything like JTAG :)

## 2011-08-29 12:03:53, posted by: lazarusjx

Thanks to GliGli, Tiros and cOs for this new hack, you guys are AWESOME!!!  
 BTW, why is it not compatible with xenon and falcon boards? is it because of different board layout?

## 2011-08-29 12:59:55, posted by: MADROX

This is news to warm the soul. Great work guys!

## 2011-08-29 16:32:02, posted by: Juggahaxor

[quote="lazarusjx"]  
 Thanks to GliGli, Tiros and cOs for this new hack, you guys are AWESOME!!!  
 BTW, why is it not compatible with xenon and falcon boards? is it because of different board layout?  
 [/quote]  
   
 Falcon support is coming, I think GliGli just doesn't have a Falcon to test it on...Xenon will not be supported because of the different hardware.

## 2011-08-29 16:34:55, posted by: JtagMan

Could also be  
 a "Chipped Xbox"  
 or "HBE Xbox"(HomeBrew Enabled)  
   
 I dont know glitched xbox just sounds like its broken to me. I mean in the scene it would make since but like if you were talking to friends or whatever and told them your xbox was glitched, they would probably think it was broke.  
   
 Honestly I dont care what we call them this is a great step forward.

## 2011-08-29 16:43:47, posted by: SHiTONLYGERMAN

Just a quick question....  
   
 Is it possible that MS will patch this glitch on fat consoles with updating the cb?? (e.g cb 6750 was unexploitable because of the CD 8453, like they did it before with the smc hack !)  
   
 Yours sincerely.. :)

## 2011-08-29 19:22:31, posted by: DARKFiB3R

[quote="SHiTONLYGERMAN"]  
 Just a quick question....  
   
 Is it possible that MS will patch this glitch on fat consoles with updating the cb?? (e.g cb 6750 was unexploitable because of the CD 8453, like they did it before with the smc hack !)  
   
 Yours sincerely.. :)  
 [/quote]  
 "Now, maybe you haven't realised yet, but CB\_A contains no checks on revocation fuses, so it's an unpatchable hack !"  
   
 Pretty sure that means no. :)

## 2011-08-29 19:50:09, posted by: JtagMan

it looks like cb\_a is only used on slims tho. so no confirmation has been given on phats.

## 2011-08-29 19:58:42, posted by: GliGli

On fats, you can do the efuse write disable mod (eg removing r6t3 or other techniques).  
   
 CB\_A can run on fats too so it might very well be possible the slim hack also work on them :)

## 2011-08-29 20:28:29, posted by: SHiTONLYGERMAN

Thanks for your reply! ;)  
   
 So there is the possibility of fixing this glitch by updating the cb until we can run cb\_a on fats?

## 2011-08-29 22:25:08, posted by: RAID

Thanks for great job.  
   
 There is a possibility to obtain the VHDL code to program another device?, And I use Altera Max + PlusII.  
   
 Regards, RAID.  
   
 Edit: [url=https://github.com/gligli/tools/tree/master/reset\_glitch\_hack/cpld/glitchslimnodp]https://github.com/gligli/tools/tree/master/reset\_glitch\_hack/cpld/glitchslimnodp[/url]

## 2011-08-29 22:28:40, posted by: chriss179

[quote="Juggahaxor"]  
   
 ...Xenon will not be supported because of the different hardware....  
 [/quote]  
   
 I hope this hack does not end the efforts on opening the xenons for homebrew then... But i think the demand for that will be too little right as there are too many exploitable xbox360's now right? Too bad, i receive tons of xenons for reball/reflow. It would have been alot of fun opening these xboxes for homebrew in the process of repair. the feeling of having repaired an old xbox360 is so so, but the feeling of giving people the ability to run emulators, media centers, and other cool homebrew software is so much more rewarding. Ah well, i can comfort myself with the thought that at least i can hack all other hardware revisions then. At least i can make those people happy.

## 2011-08-30 05:43:58, posted by: jsheradin

I wonder if freeboot works along with freestyle dash and such?

## 2011-08-30 06:10:02, posted by: Juggahaxor

[quote="jsheradin"]  
 I wonder if freeboot works along with freestyle dash and such?  
 [/quote]  
   
 Not the place for freeboot talk...legal homebrew only here.   
   
 Make sure you read the forum rules before posting again...Thank You!

## 2011-08-31 04:57:12, posted by: superspeed

I just wanted to say thank you to everyone involved in finding this method. Will we be able to launch a devmenu?

## 2011-08-31 10:07:31, posted by: webpad

It's a great job!

## 2011-09-03 13:09:51, posted by: beegee7730

Man, I can't wait for Falcon support. I have one that I got used for £10 with a dodgy disk drive that I'd love to be able to back up my games on.  
 So, is Linux on 360 reliable? I know on PS3 it's pretty poor.

## 2011-09-03 13:34:42, posted by: Cancerous1

[quote="chriss179"]  
 [quote="Juggahaxor"]  
   
 ...Xenon will not be supported because of the different hardware....  
 [/quote]  
   
 I hope this hack does not end the efforts on opening the xenons for homebrew then... But i think the demand for that will be too little right as there are too many exploitable xbox360's now right? Too bad, i receive tons of xenons for reball/reflow. It would have been alot of fun opening these xboxes for homebrew in the process of repair. the feeling of having repaired an old xbox360 is so so, but the feeling of giving people the ability to run emulators, media centers, and other cool homebrew software is so much more rewarding. Ah well, i can comfort myself with the thought that at least i can hack all other hardware revisions then. At least i can make those people happy.  
 [/quote]  
   
 Yes it is, writing homebrew does have a very rewarding feeling.

## 2011-09-04 20:27:07, posted by: olivagyok360

Hi All!  
   
 Yes This Great,but I can't make my image\_00000000.ecc file for JASPER because the command promt any time give faliure with my dump.Can You See The pictures. Anybody Help? :o  
   
 http://kepfeltoltes.hu/view/110904/1142911214\_j\_k\_p\_www.kepfeltoltes.hu\_.jpg  
 http://kepfeltoltes.hu/110904/1142911214\_j\_k\_p\_www.kepfeltoltes.hu\_.jpg  
   
 THX

## 2011-09-04 20:39:17, posted by: boflc

try:   
 http://www.xboxhacker.net/http://libxenon.org//viewtopic.php?t=5  
   
 if xbh's proxy fail hits you:  
 1) google "secret\_1BL"  
 2) scroll down to the link titled "Problem with imgbuild: assert allzero(CB[0x270:0x390])"  
 3) there's the key; enter that line secret\_1BL into build.py near the top of the script.  
   
 can't guarantee that'd work, but ir0nman@irc mentioned this was the fix to generate a working image for jaspers due to 1bl encryption.

## 2011-09-05 02:27:56, posted by: ddxcb

[quote="olivagyok360"]  
 Hi All!  
   
 Yes This Great,but I can't make my image\_00000000.ecc file for JASPER because the command promt any time give faliure with my dump.Can You See The pictures. Anybody Help? :o  
   
 http://kepfeltoltes.hu/view/110904/1142911214\_j\_k\_p\_www.kepfeltoltes.hu\_.jpg  
 http://kepfeltoltes.hu/110904/1142911214\_j\_k\_p\_www.kepfeltoltes.hu\_.jpg  
   
 THX  
 [/quote]  
   
 Try "CDJasper" instead of "CD"

## 2011-09-05 03:11:32, posted by: Mux

I've never worked with cpld's before. But I do have a xilinx FPGA, will it operate and run the VHDL code in similar fashion as the CPLD? Or will I have to modify something?

## 2011-09-05 20:25:37, posted by: olivagyok360

[quote="ddxcb"]  
 [quote="olivagyok360"]  
 Hi All!  
   
 Yes This Great,but I can't make my image\_00000000.ecc file for JASPER because the command promt any time give faliure with my dump.Can You See The pictures. Anybody Help? :o  
   
 http://kepfeltoltes.hu/view/110904/1142911214\_j\_k\_p\_www.kepfeltoltes.hu\_.jpg  
 http://kepfeltoltes.hu/110904/1142911214\_j\_k\_p\_www.kepfeltoltes.hu\_.jpg  
   
 THX  
 [/quote]  
   
 Try "CDJasper" instead of "CD"  
 [/quote]  
   
 Not good...THX :'(

## 2011-09-05 20:26:33, posted by: olivagyok360

[quote="boflc"]  
 try:   
 http://www.xboxhacker.net/http://libxenon.org//viewtopic.php?t=5  
   
 if xbh's proxy fail hits you:  
 1) google "secret\_1BL"  
 2) scroll down to the link titled "Problem with imgbuild: assert allzero(CB[0x270:0x390])"  
 3) there's the key; enter that line secret\_1BL into build.py near the top of the script.  
   
 can't guarantee that'd work, but ir0nman@irc mentioned this was the fix to generate a working image for jaspers due to 1bl encryption.  
 [/quote]  
   
 Same problem.....THX :'(

## 2011-09-05 21:25:01, posted by: olivagyok360

Hi All! :)  
   
 So,my Friend told me today,we have the new Bestpig prog. for ECC Glitch. I downloaded this,and I testing this.So,the Jasper 12625,and 13146 fine,and the Slim 12625 also,but the 13599 NOT GOOD,same problem have cannot make the image because the CB..... :o  
   
 Any Idea???  
   
 ![](http://kepfeltoltes.hu/110905/EEC_www.kepfeltoltes.hu_.jpg)[img]http://kepfeltoltes.hu/110905/EEC\_www.kepfeltoltes.hu\_.jpg[/img]  
   
 And here found the command prompt pictures:  
   
 http://kepfeltoltes.hu/110905/rrr\_www.kepfeltoltes.hu\_.jpg  
   
 THX!

## 2011-09-06 18:38:22, posted by: ar1424

Is anybody succesfully programed the CMOD from Digilent the same CMOD that they use in the tutorial? My problem is detecting the CMOD using the parallel JTAG cable provided from the tutorial. I followed the schematic from the tutorial how to build the cable. I'm not sure if the cable is working or my LPT card is compatible. My LPT port is not built in the motherboard, I bought a LPT PCI card would that work?

## 2011-09-07 08:08:45, posted by: Gypo

First of all I have to say thank you very much for all the hard work put into this by GliGli, Tiros and everybody else behind the scenes who developed this hack.  
   
 I've been lurking here for a little while now and had no reason to post until today.  
   
 I'm requesting the jed files included with the zip to be recompiled into jam format please, I need them in this format so this hack will be compatible with my jtag device (I'm unsure whether I'm allowed to name the device here so I'll keep quiet about it for now).   
   
 I really hope you guys can make this happen for me and plenty of other people out there.  
   
 Cheers.

## 2011-09-09 22:21:32, posted by: sizzler27

this is truly incredible, I owe you for this !

## 2011-10-17 20:11:54, posted by: chester1997

I don't want to sound like a noob or a leech but is there a big chance that this is coming to Xenon? congratz for the find, I'm sure Microsoft is pissed :P

## 2011-10-27 07:43:51, posted by: superspeed

Can someone help me build the image for a falcon I have went through all the steps and its telling me that python is not a recognized command.

## 2011-10-27 08:01:43, posted by: Juggahaxor

You have to also add python into your windows path after you install Python and Pycrypto.

## 2011-10-27 17:34:10, posted by: superspeed

[quote="Juggahaxor"]  
 You have to also add python into your windows path after you install Python and Pycrypto.  
 [/quote]  
 I have done that but it is still not letting me.

## 2011-12-09 23:10:19, posted by: mrdrifta

[quote="superspeed"]  
 [quote="Juggahaxor"]  
 You have to also add python into your windows path after you install Python and Pycrypto.  
 [/quote]  
 I have done that but it is still not letting me.  
 [/quote]  
   
 If your having trouble, try extracting the ggbuild folder into your python directory.   
 Worked for me when nothing else did.

## 2011-12-10 07:13:40, posted by: barnhilltrckn

I had the exact same thing happen to me and all i did was cd into the folder you need to then drag the python script onto the command window, then i wrote out the command needed. Worked everytime.  
   
 There are other ways for doing things though. Roger's multibuilder is pretty good and will make the .ecc image you if you dont put in the cpu key.