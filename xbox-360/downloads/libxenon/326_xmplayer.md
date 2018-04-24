# XMPlayer

## 2012-06-18 14:53:39, posted by: tuxuser

CHANGELOG [quote] Version 0.0.4:  
 - Fixed: Sometimes when mounting more than 1 USB device, it can crash, now it loads what it can  
 - Fixed: Overload buffer and memory leak leading to random crashes  
 - Fixed: Elf files not loading after a video has been played  
 - Fixed: Audio- and subdelay shows -0 ms  
 - Fixed: First time you enter osd menu when paused, it removes it again  
 - Fixed: Volume not changing in audio settings when paused  
 - Fixed: Mplayer crashes if .rar archive is not supported  
 - Fixed: Mplayer crashes if .rar archive is valid, but doesn't not contain video  
 - Changed: Disabled balance in osd menu, it doesn't work  
 - Changed: Libass disabled as default, beware libass makes xmplayer unstable  
 - Changed: Subfont from Arial to Dejavu Sans  
 - Changed: Removed Music and Photos menu for now, not supported  
 - Changed: "Restart" now restarts XMPlayer  
 - Added: Support for .rmvb files  
 - Added: New subtitle shader with selectable color and selectable outline color. Increased stability because libass is not needed  
 - Added: New Harddrive and DVD icons  
 - Added: XMplayer stops showing loading screen and shows underlying error message, if it indeed crashed  
 - Added: Restart to NXE in Global Setting in "Shutdown" option  
   
 Version 0.0.3:  
 - Fixed: Updated mount code to work with more usb devices (same as XeLL v0.993)  
 - Fixed: OSD bug  
 - Added: First binary release with Corona support!!  
   
 Version 0.0.2:  
 - Fixed: .avi files not playing after a .mkv, .mov or .mp4 file has been played  
 - Fixed: When entering a new folder "Item number/All item number" will not update until moving down on d-pad  
 - Fixed: When paused, the osd buttons (y, xbox, x) unpauses video, only (a) pauses/unpauses now  
 - Fixed: Osd\_show\_progression (x) only shows if osd-button (y) hasn't been pressed before  
 - Fixed: Lb and Rb doesn't seek -600/+600  
 - Fixed:The D-pad being buggy after a video has been played  
 - Fixed: Some bugs with osd displaying delay as -0 because of it being close to zero  
 - Fixed: Removed the 1 pixel-width line artifact in videos  
 - Changed: Osd-button (y) now switches from directly on/off, this means it only needs 1 press to full osd and not 3 presses  
 - Changed: When pressing the pause-button (a) progression will also show  
 - Changed: The page down icon now only shows, if there are at least more items than a page  
 - Changed: The (b) button doesn't exit to homescreen any more, it goes one level up, until root then goes to homescreen  
 - Changed: [extension.mp4] demuxer=mov to demuxer=lavf in mplayer.conf, lavf handles .mp4 files better than mov  
 - Changed: Updated libass to 0.10.0  
 - Changed: Ass/ssa is now subtitle default which means outline, color, scale etc. works   
 - Changed: The audio delay option in osd is more logical, a audio\_delay of 100 ms doesn't mean audio is 100 ms before video (mplayer standard), but 100 ms after  
 - Changed: Replaced mxml with tinyxml, because of loading problems and it seems lighter  
 - Changed: Updated GUI with button indicators, changed page size from 10 to 15  
 - Added: "Restart" and "Shutdown" buttons  
 - Added: A "smart menu" that saves your last selection and path when exiting a menu or playing a video (resets between devices)  
 - Added: Resume-playback function: if you stop a video in the middle of playing, it will save last position and resume from there if desired (more than a minute of video has to be played)  
 - Added: All libmenu's working functions available in the main osd, so libmenu will no longer be needed  
 - Added: Patch from mplayerdev's mailing list which adds support for playing videos inside multivolume uncompressed rar files  
 - Added: If a .rar file loads, it now gets the extension of the archived file, so the true extension profile is loaded  
 - Added: The (back) button goes directly back to homepage  
 - Added: Sort files. By pressing (x) in the file browser, you can order by Name or Date (day/month/year)  
 - Added: ASS settings can be accessed from the subtitle osd menu  
 - Added: Set ass=yes and vf=ass in mplayer config. This means it can be disabled and subfont can be used if desired  
   
 Version 0.0.1:  
 -Intial Release [/quote] README [quote] XMPlayer Version 0.0.4 - September 15, 2013  
 ================================================================================  
 Libxenon: d3b3270a3798c1f0b4faeb26e9dfaf24e8d41631  
   
 Known Issues  
 ================================================================================  
 Mounting:  
 - Endless loading screen: Restart. Not working try formatting using Gui Format32. If this doesn't work place xenon.elf   
 on root of internal hdd, and place the "mplayer" folder on the root of a usb (ntfs, fat) then launch  
 - Sometimes when mounting more than 1 USB, it will not find all of them. Just restart XMPlayer until it does  
   
 Playing video:  
 - Can crash while using play'n'charge kit  
 - Cannot seek in files over 2 gigabytes (split the files for now)  
 - Playing .rar can be unstable, sometimes freezing XMPlayer  
 - Prolonged pausing causes audio to go out of sync, "fix" this by seeking once in the file  
   
 Subtitles:  
 - ASS Subtitle handling can cause freezes and lag. If random crashes in video occurs, set ass=no and change   
 vf=ass to #vf=ass in config (ass is disabled by default)  
 - If your subs doesn't show all the characters, try a different font by replacing subfont.ttf in "mplayer" folder  
 - If you exit a video with subtitle-text on the screen, the text will still be there if you play a video wihout subtitles, you   
 can "fix" this by going into a video with subs and exiting when there is no sutitle-text  
   
 Other(s):  
 - Loading .elf files from the filebrowser on the internal harddrive will crash, this also means using "Restart" will crash if  
 xenon.elf is only placed on internal harddrive  
   
 Not implemented:  
 - Audio balance, surround sound and optical out are not supported  
 - Pictures and Music are not supported  
 - DVD not working (crash)  
 - No networking!  
   
 Install  
 ================================================================================  
 - Copy all files to the root of an usb stick, launch it by xell or latest dashlaunch  
   
 Debug  
 ================================================================================  
 - Do you get a red screen? Does xmplayer freeze or get stuck at endless loading? and nothing helps?  
 Read DEBUG so we can fix the problem together  
   
 Button Binds  
 ================================================================================  
 - In File Browser  
 A: enter  
 B: up one level  
 X: sort by  
 Back: back to homescreen  
 D-pad: direction  
   
 - In Video  
 A: pause/play  
 B: exit player  
 X: show progression  
 Y: OSD/Menu  
 Rb: seek 10 min forward  
 Lb: seek 10 min back  
 Rt: seek 10 sec forward  
 Lt: seek 10 sec back  
 Up: seek 1 min forward  
 Down: seek 1 min back  
 Right: seek 10 sek forward  
 Left: seek 10 sek back  
   
 Settings  
 ================================================================================  
 - Global  
 Exit action: Shutdown Button bind  
 Language: Menu language (English/French)  
   
 - Audio  
 Language: Set default audio track of video (i.e mkv with multiple languages)  
 Volume: Start volume  
 Soft Volume: Software volume boost  
   
 - Video  
 Frame Dropping: Set default frame dropping option  
 Vsync: Set default vertical sync option (can cause slow downs if on)  
   
 - Subtitles  
 Color: Color of the subtitle  
 Border Color: Color of the subtitle border  
 Code Page: the encoding of the subtitles (latin, baltic, arabic etc.)  
 Language: Default subtitle language  
   
 Thanks to  
 ================================================================================  
 Ced2911  
 Aioros  
 cancerous  
 GliGli  
 IceKiller  
 Juvenal  
 Natelx  
 Razkar  
 sk1080  
 tuxuser  
 [c0z]  
 siz-  
 Swizzy  
   
 Remember to support the xbox 360 legal homebrew community!  
 www.libxenon.org and #libxenon @ EFNet [/quote] Download: [url=http://file.libxenon.org/libxenon/binary/xmplayer-0.0.4.tar.gz]Click[/url]

## 2012-06-18 19:03:43, posted by: ploggy

My USB HDD isn't working with Xell, it see's the Xenon.elf but doesn't load the file. :( Otherwise thank you or the release. :)  
 I should say it picks up and loads the Xenon.elf on my SD card (with SD adapter) but even when the Player loads it still doesn't pick up my External HDD?  
   
 Again thanks for the release :)

## 2012-06-19 00:02:57, posted by: ravendrow

thank you for the release i was getting tired of checking your github every hour on the hour lmao  
   
 all avi and mp4 files i have played work great however every time i try to play an MKV even a 480p one all i get is rainbow picture the audio sounds perfect pretty sure the encoding is x264 if that helps narrow down the prob for a future release.  
   
 otherwise F$#king Awesome work!!!!  
   
 oh yeah just wondering since this was released does that mean there is now an update for libxenon???

## 2012-06-19 03:01:31, posted by: Doerek

Do you Guys need help for translation?  
 If so...please let us know.  
   
 ![](http://evo-x.de/wbb3/wcf/icon/mobile_icon.png)[img]http://evo-x.de/wbb3/wcf/icon/mobile\_icon.png[/img]

## 2012-06-19 03:41:50, posted by: Juggahaxor

Nice work ... I've been looking forward to this since I saw the announcement , deep down I've really been looking forward to it since you could run homebrew, I'm also very happy to see it is being built with the legal toolchain...  
   
 Later  
   
 Edit: Forgot to say Thanks ... Thank You Ced2911 and all those involved ;)

## 2012-06-19 13:37:02, posted by: naxil

hello! firts THANKS for this Homebrew..  
 I have a little request: can u add the wired pad for control XMplayer? i have wired pad buyed on game#T#p the id is ID 0e6f:0301  
   
 thanks!

## 2012-06-19 17:24:31, posted by: doolcan

This is what a lot of people are waiting for. Great job and thanks for the hard work!

## 2012-06-19 21:54:32, posted by: c01eman.360

thanks ced. problem is h.264 mkv and mp4 videos are getting detected wrongly and are showing up garbled   
   
 gui is awsome though

## 2012-07-02 00:46:35, posted by: skaT777

the player dont work on many consoles (fat and slim)  
 give it a fix?   
 ( i come only to the Mplayer logo and the loading wheel)

## 2012-07-02 15:45:53, posted by: c01eman.360

try using a usbdrive smaller than 4gb thats the only way i can get it to work on mine :)

## 2012-07-03 14:01:10, posted by: skaT777

dont work i have a 3.6 gb usb stick in the xbox and open it whit Xell  
 i become the loading screen  
 then a red picture (like a flash) and then again loading  
 so it dont work T.T

## 2012-07-07 17:44:16, posted by: c01eman.360

have you tried a 2gb usb stick?

## 2012-07-17 15:14:28, posted by: siz

[quote="skaT777"]  
 dont work i have a 3.6 gb usb stick in the xbox and open it whit Xell  
 i become the loading screen  
 then a red picture (like a flash) and then again loading  
 so it dont work T.T  
 [/quote]  
   
 If you are on windows try formatting with Fat32 Format, google it, had some problems my self.

## 2012-08-02 22:35:22, posted by: Farid

[quote="ravendrow"]  
 every time i try to play an MKV even a 480p one all i get is rainbow picture[/quote]  
   
 [quote="c01eman.360"]  
 thanks ced. problem is h.264 mkv and mp4 videos are getting detected wrongly and are showing up garbled   
 [/quote]  
   
 Same problem here, 720 MKV with rainbow/garbage :  
   
 ![](http://krauser.persiangig.com/image/xmPlayer.JPG)[img]http://krauser.persiangig.com/image/xmPlayer.JPG[/img]  
   
 Thanks for the awesome work

## 2012-10-19 14:02:09, posted by: siz

**[b]Readme[/b]** [code]================================================================================ XMPlayer 0.0.2 - October 19, 2012 ================================================================================ With a lot of help from especially Ced2911 and the Libxenon community, I can proudly present the new version of XMPlayer with added features, fixes and changes. Enjoy. /siz github: https://github.com/siz-/xmplayer ================================================================================ Changelog ================================================================================ Version 0.0.2: - Fixed: .avi files not playing after a .mkv, .mov or .mp4 file has been played - Fixed: When entering a new folder "Item number/All item number" will not update until moving down on d-pad - Fixed: When paused, the osd buttons (y, xbox, x) unpauses video, only (a) pauses/unpauses now - Fixed: Osd\_show\_progression (x) only shows if osd-button (y) hasn't been pressed before - Fixed: Lb and Rb doesn't seek -600/+600 - Fixed:The D-pad being buggy after a video has been played - Fixed: Some bugs with osd displaying delay as -0 because of it being close to zero - Fixed: Removed the 1 pixel-width line artifact in videos - Changed: Osd-button (y) now switches from directly on/off, this means it only needs 1 press to full osd and not 3 presses - Changed: When pressing the pause-button (a) progression will also show - Changed: The page down icon now only shows, if there are at least more items than a page - Changed: The (b) button doesn't exit to homescreen any more, it goes one level up, until root then goes to homescreen - Changed: [extension.mp4] demuxer=mov to demuxer=lavf in mplayer.conf, lavf handles .mp4 files better than mov - Changed: Updated libass to 0.10.0 - Changed: Ass/ssa is now subtitle default which means outline, color, scale etc. works - Changed: The audio delay option in osd is more logical, a audio\_delay of 100 ms doesn't mean audio is 100 ms before video (mplayer standard), but 100 ms after - Changed: Replaced mxml with tinyxml, because of loading problems and it seems lighter - Changed: Updated GUI with button indicators, changed page size from 10 to 15 - Added: "Restart" and "Shutdown" buttons - Added: A "smart menu" that saves your last selection and path when exiting a menu or playing a video (resets between devices) - Added: Resume-playback function: if you stop a video in the middle of playing, it will save last position and resume from there if desired (more than a minute of video has to be played) - Added: All libmenu's working functions available in the main osd, so libmenu will no longer be needed - Added: Patch from mplayerdev's mailing list which adds support for playing videos inside multivolume uncompressed rar files - Added: If a .rar file loads, it now gets the extension of the archived file, so the true extension profile is loaded - Added: The (back) button goes directly back to homepage - Added: Sort files. By pressing (x) in the file browser, you can order by Name or Date (day/month/year) - Added: ASS settings can be accessed from the subtitle osd menu - Added: Set ass=yes and vf=ass in mplayer config. This means it can be disabled and subfont can be used if desired Version 0.0.1: -Intial Release ================================================================================ Known Issues ================================================================================ - Cannot seek in files over 2 gigabytes (split the files for now) - Prolonged pausing causes audio to go out of sync, "fix" this by seeking once in the file - ASS Subtitle handling can cause freezes and lag. If rand om crashes in video occurs, set ass=no and change vf=ass to #vf=ass in config - Playing .rar can be unstable, sometimes freezing XMPlayer - If your subs doesn't show all the characters, try a different font by replacing subfont.ttf in <mplayer> folder - XMPlayer does not always mount usb (uda) even though it loads, reload XMPlayer and try again - Endless loading screen: Try formatting using Gui Format32, or try placing xenon.elf and symbols.elf on root of xbox's internal hdd. Place the <mplayer> folder on the root of a usb (ntfs, fat), and then run xenon.elf from the internal harddrive via Dashlaunch. - Can crash while using play'n'charge kit - Audio balance not working - Pictures and Music are not supported - No networking! ================================================================================ Install ================================================================================ - Copy all files to the root of an usb stick, launch it by xell or latest dashlaunch ================================================================================ Button Binds ================================================================================ #In File Browser -A: enter -B: up one level -X: sort by -Back: back to homescreen -D-pad: direction #In video -A: pause/play -B: exit player -X: show progression -Y: OSD/Menu -Rb: seek 10 min forward -Lb: seek 10 min back -Rt: seek 10 sec forward -Lt: seek 10 sec back -Up: seek 1 min forward -Down: seek 1 min back -Right: seek 10 sek forward -Left: seek 10 sek back ================================================================================ Settings ================================================================================ #Global Exit action: Shutdown Button bind Language: Menu language (English/French) #Audio Language: Set default audio track of video (i.e mkv with multiple languages) Volume: Start volume Soft Volume: Software volume boost #Video Frame Dropping: Set default frame dropping option Vsync: Set default vertical sync option #Subtitles Color: Color of the subtitle (only when ass=yes, which is default) Border Color: Color of the subtitle border (only when ass=yes, which is default) Code Page: the encoding of the subtitles (latin, baltic, arabic etc.) Language: Default subtitle language ================================================================================ Thanks to ================================================================================ Ced2911 Aioros cancerous GliGli IceKiller Juvenal Natelx Razkar sk1080 tuxuser [c0z] Remember to support the xbox 360 legal homebrew community! www.libxenon.org and #libxenon @ EFNet[/code] **[b]Screenshots[/b]**  
 http://imageshack.us/g/1/9820533/  
   
 **[b]Download[/b]**  
 [url=http://peecee.dk/upload/download/388067]Mirror[/url]   
   
 I thought I'd release a compiled version now that I do not have the opportunity to work on it for a couple of months.

## 2013-05-09 22:53:33, posted by: naxil

hello people. Thanku very much for this fantastic and **[b]LEGAL[/b]** homebrew!  
   
 Please continue this project! work very well now!  
   
 ps= if i run debian or ubuntu? i can use better mediacenter like xbmc? or vlc?

## 2013-08-29 15:37:12, posted by: medaved

Hello! Pls need help a recompilling mplayer for CORONA. new xell show pic, mplayer show only black screen ... 

## 2013-08-31 12:14:04, posted by: medaved

[code]build player cd mplayer; /usr/bin/make -f Makefile lib -j4; cd ../.. make[1]: ???? ? ??????? `/home/medaved/xmplayer/mplayer' xenon-ar rc libmplayer.a command.o m\_property.o mixer.o mp\_fifo.o mplayer.o parser-mpcmd.o pnm\_loader.o input/input.o libao2/ao\_mpegpes.o libao2/ao\_null.o libao2/ao\_pcm.o libao2/audio\_out.o libvo/aspect.o libvo/geometry.o libvo/video\_out.o libvo/vo\_mpegpes.o libvo/vo\_null.o sub/spuenc.o libvo/vo\_png.o libmenu/menu.o libmenu/menu\_chapsel.o libmenu/menu\_cmdlist.o libmenu/menu\_console.o libmenu/menu\_filesel.o libmenu/menu\_list.o libmenu/menu\_param.o libmenu/menu\_pt.o libmenu/menu\_txt.o libmenu/vf\_menu.o libvo/vo\_md5sum.o libvo/vo\_pnm.o libvo/vo\_tga.o libvo/vo\_yuv4mpeg.o asxparser.o bstr.o codec-cfg.o cpudetect.o edl.o fmt-conversion.o m\_config.o m\_option.o m\_struct.o mp\_msg.o mp\_strings.o mpcommon.o parser-cfg.o path.o playtree.o playtreeparser.o subopt-helper.o libaf/af.o libaf/af\_center.o libaf/af\_channels.o libaf/af\_comp.o libaf/af\_delay.o libaf/af\_dummy.o libaf/af\_equalizer.o libaf/af\_extrastereo.o libaf/af\_format.o libaf/af\_gate.o libaf/af\_hrtf.o libaf/af\_karaoke.o libaf/af\_pan.o libaf/af\_resample.o libaf/af\_scaletempo.o libaf/af\_sinesuppress.o libaf/af\_stats.o libaf/af\_sub.o libaf/af\_surround.o libaf/af\_sweep.o libaf/af\_tools.o libaf/af\_volnorm.o libaf/af\_volume.o libaf/filter.o libaf/format.o libaf/reorder\_ch.o libaf/window.o libmpcodecs/ad.o libmpcodecs/ad\_alaw.o libmpcodecs/ad\_dk3adpcm.o libmpcodecs/ad\_dvdpcm.o libmpcodecs/ad\_hwac3.o libmpcodecs/ad\_hwmpa.o libmpcodecs/ad\_imaadpcm.o libmpcodecs/ad\_msadpcm.o libmpcodecs/ad\_pcm.o libmpcodecs/dec\_audio.o libmpcodecs/dec\_teletext.o libmpcodecs/dec\_video.o libmpcodecs/img\_format.o libmpcodecs/mp\_image.o libmpcodecs/pullup.o libmpcodecs/vd.o libmpcodecs/vd\_hmblck.o libmpcodecs/vd\_lzo.o libmpcodecs/vd\_mpegpes.o libmpcodecs/vd\_mtga.o libmpcodecs/vd\_null.o libmpcodecs/vd\_raw.o libmpcodecs/vd\_sgi.o libmpcodecs/vf.o libmpcodecs/vf\_1bpp.o libmpcodecs/vf\_2xsai.o libmpcodecs/vf\_blackframe.o libmpcodecs/vf\_boxblur.o libmpcodecs/vf\_crop.o libmpcodecs/vf\_cropdetect.o libmpcodecs/vf\_decimate.o libmpcodecs/vf\_delogo.o libmpcodecs/vf\_denoise3d.o libmpcodecs/vf\_detc.o libmpcodecs/vf\_dint.o libmpcodecs/vf\_divtc.o libmpcodecs/vf\_down3dright.o libmpcodecs/vf\_dsize.o libmpcodecs/vf\_dvbscale.o libmpcodecs/vf\_eq.o libmpcodecs/vf\_eq2.o libmpcodecs/vf\_expand.o libmpcodecs/vf\_field.o libmpcodecs/vf\_fil.o libmpcodecs/vf\_filmdint.o libmpcodecs/vf\_fixpts.o libmpcodecs/vf\_flip.o libmpcodecs/vf\_format.o libmpcodecs/vf\_framestep.o libmpcodecs/vf\_gradfun.o libmpcodecs/vf\_halfpack.o libmpcodecs/vf\_harddup.o libmpcodecs/vf\_hqdn3d.o libmpcodecs/vf\_hue.o libmpcodecs/vf\_il.o libmpcodecs/vf\_ilpack.o libmpcodecs/vf\_ivtc.o libmpcodecs/vf\_kerndeint.o libmpcodecs/vf\_mirror.o libmpcodecs/vf\_noformat.o libmpcodecs/vf\_noise.o libmpcodecs/vf\_ow.o libmpcodecs/vf\_palette.o libmpcodecs/vf\_perspective.o libmpcodecs/vf\_phase.o libmpcodecs/vf\_pp7.o libmpcodecs/vf\_pullup.o libmpcodecs/vf\_rectangle.o libmpcodecs/vf\_remove\_logo.o libmpcodecs/vf\_rgbtest.o libmpcodecs/vf\_rotate.o libmpcodecs/vf\_sab.o libmpcodecs/vf\_scale.o libmpcodecs/vf\_smartblur.o libmpcodecs/vf\_softpulldown.o libmpcodecs/vf\_stereo3d.o libmpcodecs/vf\_softskip.o libmpcodecs/vf\_swapuv.o libmpcodecs/vf\_telecine.o libmpcodecs/vf\_test.o libmpcodecs/vf\_tfields.o libmpcodecs/vf\_tile.o libmpcodecs/vf\_tinterlace.o libmpcodecs/vf\_unsharp.o libmpcodecs/vf\_vo.o libmpcodecs/vf\_yadif.o libmpcodecs/vf\_yuvcsp.o libmpcodecs/vf\_yvu9.o libmpdemux/aac\_hdr.o libmpdemux/asfheader.o libmpdemux/aviheader.o libmpdemux/aviprint.o libmpdemux/demuxer.o libmpdemux/demux\_aac.o libmpdemux/demux\_asf.o libmpdemux/demux\_audio.o libmpdemux/demux\_avi.o libmpdemux/demux\_demuxers.o libmpdemux/demux\_film.o libmpdemux/demux\_fli.o libmpdemux/demux\_lmlm4.o libmpdemux/demux\_mf.o libmpdemux/demux\_mkv.o libmpdemux/demux\_mov.o libmpdemux/demux\_mpg.o libmpdemux/demux\_nsv.o libmpdemux/demux\_pva.o libmpdemux/demux\_rawaudio.o libmpdemux/demux\_rawvideo.o libmpdemux/demux\_realaud.o libmpdemux/demux\_real.o libmpdemux/demux\_roq.o libmpdemux/demux\_smjpeg.o libmpdemux/demux\_ts.o libmpdemux/demux\_ty.o libmpdemux/demux\_ty\_osd.o libmpdemux/demux\_viv.o libmpdemux/demux\_vqf.o libmpdemux/demux\_y4m.o libmpdemux/ebml.o libmpdemux/extension.o libmpdemux/mf.o libmpdemux/mp3\_hdr.o libmpdemux/mp\_taglists.o libmpdemux/mpeg\_hdr.o libmpdemux/mpeg\_packetizer.o libmpdemux/parse\_es.o libmpdemux/parse\_mp4.o libmpdemux/video.o libmpdemux/yuv4mpeg.o libmpdemux/yuv4mpeg\_ratio.o osdep/getch2-xenon.o osdep/timer-xenon.o stream/open.o stream/stream.o stream/stream\_bd.o stream/stream\_cue.o stream/stream\_file.o stream/stream\_mf.o stream/stream\_null.o stream/stream\_rar.o stream/unrar.o stream/url.o sub/eosd.o sub/find\_sub.o sub/osd.o sub/spudec.o sub/sub.o sub/sub\_cc.o sub/subreader.o sub/vobsub.o osdep/osdep\_xenon.o libvo/vo\_xenon.o libao2/ao\_xenon.o osdep/glob-xenon.o libxenon\_miss/xenon\_pthread.o libxenon\_miss/basename.o sub/font\_load.o libvo/aclib.o av\_helpers.o av\_opts.o libaf/af\_lavcac3enc.o libaf/af\_lavcresample.o libmpcodecs/ad\_ffmpeg.o libmpcodecs/ad\_spdif.o libmpcodecs/vd\_ffmpeg.o libmpcodecs/vf\_geq.o libmpcodecs/vf\_lavc.o libmpcodecs/vf\_lavcdeint.o libmpcodecs/vf\_screenshot.o libmpdemux/demux\_lavf.o stream/stream\_ffmpeg.o sub/av\_sub.o libmpcodecs/vf\_fspp.o libmpcodecs/vf\_mcdeint.o libmpcodecs/vf\_qp.o libmpcodecs/vf\_spp.o libmpcodecs/vf\_uspp.o sub/font\_load\_ft.o libmpcodecs/vf\_ass.o sub/ass\_mp.o sub/subassconvert.o libass/ass.o libass/ass\_bitmap.o libass/ass\_cache.o libass/ass\_drawing.o libass/ass\_font.o libass/ass\_fontconfig.o libass/ass\_library.o libass/ass\_parse.o libass/ass\_render.o libass/ass\_render\_api.o libass/ass\_shaper.o libass/ass\_strtod.o libass/ass\_utils.o libmpcodecs/ad\_mp3lib.o mp3lib/sr1.o libmpcodecs/vf\_pp.o stream/cache2.o tremor/bitwise.o tremor/block.o tremor/codebook.o tremor/floor0.o tremor/floor1.o tremor/framing.o tremor/info.o tremor/mapping0.o tremor/mdct.o tremor/registry.o tremor/res012.o tremor/sharedbook.o tremor/synthesis.o tremor/window.o stream/stream\_tv.o stream/tv.o stream/frequencies.o stream/tvi\_dummy.o libmpcodecs/ad\_libvorbis.o libmpdemux/demux\_ogg.o osdep/shmem.o true libmplayer.a make[1]: ????? ?? ???????? `/home/medaved/xmplayer/mplayer' [filebrowser.cpp] [input.cpp] [menu.cpp] [menu\_osd.cpp] /home/medaved/xmplayer/source/filebrowser.cpp:173:1: warning: deprecated conversion from string constant to 'char*' [-Wwrite-strings] /home/medaved/xmplayer/source/filebrowser.cpp:173:1: warning: deprecated conversion from string constant to 'char*' [-Wwrite-strings] /home/medaved/xmplayer/source/filebrowser.cpp:173:1: warning: deprecated conversion from string constant to 'char*' [-Wwrite-strings] /home/medaved/xmplayer/source/filebrowser.cpp:173:1: warning: deprecated conversion from string constant to 'char*' [-Wwrite-strings] /home/medaved/xmplayer/source/filebrowser.cpp:173:1: warning: deprecated conversion from string constant to 'char*' [-Wwrite-strings] /home/medaved/xmplayer/source/filebrowser.cpp:173:1: warning: deprecated conversion from string constant to 'char*' [-Wwrite-strings] /home/medaved/xmplayer/source/filebrowser.cpp:173:1: warning: deprecated conversion from string constant to 'char*' [-Wwrite-strings] /home/medaved/xmplayer/source/filebrowser.cpp:173:1: warning: deprecated conversion from string constant to 'char*' [-Wwrite-strings] /home/medaved/xmplayer/source/filebrowser.cpp:173:1: warning: deprecated conversion from string constant to 'char*' [-Wwrite-strings] /home/medaved/xmplayer/source/filebrowser.cpp:173:1: warning: deprecated conversion from string constant to 'char*' [-Wwrite-strings] /home/medaved/xmplayer/source/filebrowser.cpp:173:1: warning: deprecated conversion from string constant to 'char*' [-Wwrite-strings] /home/medaved/xmplayer/source/filebrowser.cpp:173:1: warning: deprecated conversion from string constant to 'char*' [-Wwrite-strings] /home/medaved/xmplayer/source/filebrowser.cpp:173:1: warning: deprecated conversion from string constant to 'char*' [-Wwrite-strings] /home/medaved/xmplayer/source/filebrowser.cpp:173:1: warning: deprecated conversion from string constant to 'char*' [-Wwrite-strings] /home/medaved/xmplayer/source/filebrowser.cpp:173:1: warning: deprecated conversion from string constant to 'char*' [-Wwrite-strings] /home/medaved/xmplayer/source/filebrowser.cpp:173:1: warning: deprecated conversion from string constant to 'char*' [-Wwrite-strings] /home/medaved/xmplayer/source/filebrowser.cpp:173:1: warning: deprecated conversion from string constant to 'char*' [-Wwrite-strings] /home/medaved/xmplayer/source/filebrowser.cpp:173:1: warning: deprecated conversion from string constant to 'char*' [-Wwrite-strings] /home/medaved/xmplayer/source/filebrowser.cpp:173:1: warning: deprecated conversion from string constant to 'char*' [-Wwrite-strings] /home/medaved/xmplayer/source/filebrowser.cpp:173:1: warning: deprecated conversion from string constant to 'char*' [-Wwrite-strings] /home/medaved/xmplayer/source/filebrowser.cpp:173:1: warning: deprecated conversion from string constant to 'char*' [-Wwrite-strings] /home/medaved/xmplayer/source/filebrowser.cpp:173:1: warning: deprecated conversion from string constant to 'char*' [-Wwrite-strings] /home/medaved/xmplayer/source/filebrowser.cpp:173:1: warning: deprecated conversion from string constant to 'char*' [-Wwrite-strings] /home/medaved/xmplayer/source/filebrowser.cpp:173:1: warning: deprecated conversion from string constant to 'char*' [-Wwrite-strings] /home/medaved/xmplayer/source/filebrowser.cpp:173:1: warning: deprecated conversion from string constant to 'char*' [-Wwrite-strings] /home/medaved/xmplayer/source/filebrowser.cpp:173:1: warning: deprecated conversion from string constant to 'char*' [-Wwrite-strings] /home/medaved/xmplayer/source/filebrowser.cpp:173:1: warning: deprecated conversion from string constant to 'char*' [-Wwrite-strings] /home/medaved/xmplayer/source/filebrowser.cpp:177:1: warning: deprecated conversion from string constant to 'char*' [-Wwrite-strings] /home/medaved/xmplayer/source/filebrowser.cpp:177:1: warning: deprecated conversion from string constant to 'char*' [-Wwrite-strings] /home/medaved/xmplayer/source/filebrowser.cpp:177:1: warning: deprecated conversion from string constant to 'char*' [-Wwrite-strings] /home/medaved/xmplayer/source/filebrowser.cpp:177:1: warning: deprecated conversion from string constant to 'char*' [-Wwrite-strings] /home/medaved/xmplayer/source/filebrowser.cpp:177:1: warning: deprecated conversion from string constant to 'char*' [-Wwrite-strings] /home/medaved/xmplayer/source/filebrowser.cpp:181:1: warning: deprecated conversion from string constant to 'char*' [-Wwrite-strings] /home/medaved/xmplayer/source/filebrowser.cpp:181:1: warning: deprecated conversion from string constant to 'char*' [-Wwrite-strings] /home/medaved/xmplayer/source/filebrowser.cpp:181:1: warning: deprecated conversion from string constant to 'char*' [-Wwrite-strings] /home/medaved/xmplayer/source/filebrowser.cpp:181:1: warning: deprecated conversion from string constant to 'char*' [-Wwrite-strings] /home/medaved/xmplayer/source/filebrowser.cpp: In function 'int ParseDirectory()': /home/medaved/xmplayer/source/filebrowser.cpp:326:18: error: 'struct dirent' has no member named 'd\_mtime' /home/medaved/xmplayer/source/filebrowser.cpp:327:39: error: 'struct dirent' has no member named 'd\_mtime' make[1]: *** [filebrowser.o] ?????? 1 make[1]: *** ???????? ?????????? ???????... /home/medaved/xmplayer/mplayer/stream/stream.h: In function 'int stream\_seek(stream\_t*, off\_t)': In file included from /home/medaved/xmplayer/source/../mplayer/libmpdemux/demuxer.h:27:0, from /home/medaved/xmplayer/source/../mplayer/mpcommon.h:25, from /home/medaved/xmplayer/source/menu.h:10, from /home/medaved/xmplayer/source/menu\_osd.cpp:33: /home/medaved/xmplayer/mplayer/stream/stream.h:322:3: warning: format '%llX' expects argument of type 'long long unsigned int', but argument 4 has type 'off\_t {aka long int}' [-Wformat] /home/medaved/xmplayer/mplayer/stream/stream.h:326:65: warning: format '%llx' expects argument of type 'long long unsigned int', but argument 4 has type 'off\_t {aka long int}' [-Wformat] /home/medaved/xmplayer/source/menu\_osd.cpp: In function 'void OsdSubtitlesOptions()': /home/medaved/xmplayer/source/menu\_osd.cpp:614:23: warning: deprecated conversion from string constant to 'char*' [-Wwrite-strings] /home/medaved/xmplayer/source/menu\_osd.cpp: In function 'void OsdAudioOptions()': /home/medaved/xmplayer/source/menu\_osd.cpp:750:19: warning: deprecated conversion from string constant to 'char*' [-Wwrite-strings] /home/medaved/xmplayer/source/menu\_osd.cpp:751:22: warning: deprecated conversion from string constant to 'char*' [-Wwrite-strings] /home/medaved/xmplayer/source/menu\_osd.cpp:752:21: warning: deprecated conversion from string constant to 'char*' [-Wwrite-strings] /home/medaved/xmplayer/mplayer/stream/stream.h: In function 'int stream\_seek(stream\_t*, off\_t)': In file included from /home/medaved/xmplayer/source/../mplayer/libmpdemux/demuxer.h:27:0, from /home/medaved/xmplayer/source/../mplayer/mpcommon.h:25, from /home/medaved/xmplayer/source/menu.h:10, from /home/medaved/xmplayer/source/menu.cpp:43: /home/medaved/xmplayer/mplayer/stream/stream.h:322:3: warning: format '%llX' expects argument of type 'long long unsigned int', but argument 4 has type 'off\_t {aka long int}' [-Wformat] /home/medaved/xmplayer/mplayer/stream/stream.h:326:65: warning: format '%llx' expects argument of type 'long long unsigned int', but argument 4 has type 'off\_t {aka long int}' [-Wformat] /home/medaved/xmplayer/source/menu.cpp: In function 'void OnScreenKeyboard(char*, u32)': /home/medaved/xmplayer/source/menu.cpp:584:2: warning: missing braces around initializer for 'XeColor::<anonymous struct>' [-Wmissing-braces] /home/medaved/xmplayer/source/menu.cpp:601:2: warning: missing braces around initializer for 'XeColor::<anonymous struct>' [-Wmissing-braces] /home/medaved/xmplayer/source/menu.cpp: In function 'void Browser(const char*, const char*)': /home/medaved/xmplayer/source/menu.cpp:766:6: warning: unused variable 'browser\_exit' [-Wunused-variable] /home/medaved/xmplayer/source/menu.cpp: In function 'void MenuMplayer()': /home/medaved/xmplayer/source/menu.cpp:1801:3: warning: deprecated conversion from string constant to 'char*' [-Wwrite-strings] /home/medaved/xmplayer/source/menu.cpp:1801:3: warning: deprecated conversion from string constant to 'char*' [-Wwrite-strings] /home/medaved/xmplayer/source/menu.cpp:1801:3: warning: deprecated conversion from string constant to 'char*' [-Wwrite-strings] /home/medaved/xmplayer/source/menu.cpp: In function 'void LoadingThread()': /home/medaved/xmplayer/source/menu.cpp:1879:8: warning: unused variable 'rot' [-Wunused-variable] /home/medaved/xmplayer/source/input.cpp:30:12: warning: 'rumbleCount' defined but not used [-Wunused-variable] /home/medaved/xmplayer/source/menu\_osd.cpp: At global scope: /home/medaved/xmplayer/source/menu\_osd.cpp:78:19: warning: 'osd\_options\_background' defined but not used [-Wunused-variable] /home/medaved/xmplayer/source/menu\_osd.cpp:175:13: warning: 'void osd\_options\_vsync\_callback(void*)' defined but not used [-Wunused-function] /home/medaved/xmplayer/source/menu.cpp: At global scope: /home/medaved/xmplayer/source/menu.cpp:114:18: warning: 'btn\_y\_text' defined but not used [-Wunused-variable] /home/medaved/xmplayer/source/menu.cpp:120:19: warning: 'btn\_y' defined but not used [-Wunused-variable] make: *** [build] ?????? 2[/code] wtf?

## 2013-09-01 11:32:02, posted by: siz

it's because xmplayer 0.02 uses Ced2911 libxenon repo. Libxenon master doesn't contain date in the dirent struct, maybe soon, but get Swizzy's branch and build libxenon again.

## 2013-09-01 19:30:06, posted by: medaved

how to help or get involved? Knowledge in programming a little while, but in practice there are more

## 2013-09-05 21:53:07, posted by: Swizzy

[quote="medaved"]  
 how to help or get involved? Knowledge in programming a little while, but in practice there are more  
 [/quote]  
   
 The easy way is to just fork the project and modify the code, if what you changed is good we'll put it in the master branch ;)

## 2013-09-06 00:06:24, posted by: siz

Maybe not the project from libxenon's git, as it's 0.01. Version 0.02 is here: https://github.com/siz-/xmplayer

## 2013-09-06 19:51:29, posted by: Swizzy

[quote="siz"]  
 Maybe not the project from libxenon's git, as it's 0.01. Version 0.02 is here: https://github.com/siz-/xmplayer  
 [/quote]  
   
 Not for long... i'll be updating it as soon as my computer is done fetching everything xD  
   
 ** edit: **  
   
 I've now updated the official repository to v0.0.2 followed by adding your latest changes with a fix of my own to your mount code update ;)

## 2013-09-07 03:23:43, posted by: medaved

Strangely enough, for some reason I can not compile the new code too, the error in the file filebrowser.h in mdate.I'll write more later

## 2013-09-07 21:10:03, posted by: Swizzy

[quote="medaved"]  
 Strangely enough, for some reason I can not compile the new code too, the error in the file filebrowser.h in mdate.I'll write more later  
 [/quote]  
   
 Are you using my branch for libxenon? if not, make sure to switch to it! (run "git checkout Swizzy" then go to toolchain and run "./build-xenon-toolchain libxenon")

## 2013-09-08 15:00:29, posted by: Jhuang4998

I am only able to launch the xmplayer app through USB drive, the external hard drive(1.5tb) and internal hard drive(250gb) always give error message(ex: files not found, or loading forever). It seems that I can only put those videos files to either USB drive or internal xbox hard drive, and It will not be able to launch the xmplayer if I have USB and external hard drive connect at the same time.  
   
 My question is all my videos collection are in external hard drive, is that a possible to play those videos through the external hard drive instead?

## 2013-09-08 16:29:08, posted by: Swizzy

Try putting the folder "mplayer" in the external hdd aswell and you'll probably have it working again ;)

## 2013-09-09 19:49:40, posted by: Stakhanov

thanks, I'm new to Xell as my corona were not able to show video until recently but even if this scene is small it's quite productive and cool.  
   
 I mean there's no proper video player for the NT part of the xbox, FFPlay freezes a lot and the native player is too restrictive, but this seems to be great and developpement is alive :D

## 2013-09-09 23:15:24, posted by: ratselhaft

Awesome! :D  
   
 Is there some way to enable optical audio?  
   
 Thank you!

## 2013-09-10 07:10:42, posted by: Swizzy

[quote="ratselhaft"]  
 Awesome! :D  
   
 Is there some way to enable optical audio?  
   
 Thank you!  
 [/quote]  
   
 That'd probably require some more reversing of the audio system, i don't have a way to test it and thus have no way of figuring out how to do so...

## 2013-09-15 20:51:08, posted by: tuxuser

Updated startpost with version v0.0.4

## 2013-09-16 08:02:48, posted by: medaved

add language file of Russian 8), based in French file.

### Attachments

[ru.lang](ru.lang)

## 2013-09-16 12:27:10, posted by: Swizzy

[quote="medaved"]  
 add language file of Russian 8), based in French file.  
 [/quote]  
   
 Tested it? if not; there might be an encoding problem as russian uses Unicode and not UTF-8

## 2013-09-16 14:41:28, posted by: medaved

I did not get to compile it ...

## 2013-12-02 15:56:52, posted by: yuvalm

I try to play a movie. :huh:  
 Tried avi and mp4, from a usb and HDD. Tried running xenon.elf from usb and HDD. Same result in all situations.  
   
 As soon as I select a file it comes up "start from 00:00" or "play from beginning". select either option and the video freezes on the xbox (rgh btw), fans still going but no response and I have to turn off the system to reboot.  
   
 Any help would be appreciated.  
   
 i did telnet and the main error was:  
   
 [iso9660] Error: fs\_iso9660: disc is not iso9660  
   
 how can i fix this?

## 2013-12-03 21:49:00, posted by: Swizzy

[quote="yuvalm"]  
 I try to play a movie. :huh:  
 Tried avi and mp4, from a usb and HDD. Tried running xenon.elf from usb and HDD. Same result in all situations.  
   
 As soon as I select a file it comes up "start from 00:00" or "play from beginning". select either option and the video freezes on the xbox (rgh btw), fans still going but no response and I have to turn off the system to reboot.  
   
 Any help would be appreciated.  
   
 i did telnet and the main error was:  
   
 [iso9660] Error: fs\_iso9660: disc is not iso9660  
   
 how can i fix this?  
 [/quote]  
   
 disable everything related to ISO9660/DVD and it may solve your problem...

## 2013-12-12 14:08:43, posted by: Spider

Hello there, i recently download this program to watch movies on Xbox 360.   
 I didn't have any problem to launch Xmplayer on the HDD or USB  
   
 But i have the same issue that yuvalm, when i try to play a movie (it's a Blue-ray rip 1080) on format .mp4, and it freezes.  
   
 What should i do? How can i "disable everything related to ISO9660/DVD" like its says in the post before?  
   
 Thanks for the help, and sorry for my english im from Argentina

## 2013-12-14 20:42:03, posted by: Swizzy

[quote="Spider"]  
 Hello there, i recently download this program to watch movies on Xbox 360.   
 I didn't have any problem to launch Xmplayer on the HDD or USB  
   
 But i have the same issue that yuvalm, when i try to play a movie (it's a Blue-ray rip 1080) on format .mp4, and it freezes.  
   
 What should i do? How can i "disable everything related to ISO9660/DVD" like its says in the post before?  
   
 Thanks for the help, and sorry for my english im from Argentina  
 [/quote]  
   
 Do you have the same debug output? (using telnet...)

## 2014-06-02 08:23:48, posted by: LegendaryFire

Awesome work here, finally got to try it out a bit. Out of curiosity, is this project still in development? Always wanted a solid media player on my Xbox 360 and I've finally found one, I just hope that some customizability features will be incorporated if it's still in development.  
   
 Besides that, awesome work. Hope to see future releases soon.