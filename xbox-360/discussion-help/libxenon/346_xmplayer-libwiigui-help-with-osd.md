# xmplayer/libwiigui help with osd

## 2012-08-07 16:18:17, posted by: siz

Hey,  
   
 I am trying to make the libmenu in xmplayer available in the osd with libwiigui. Right now I am starting with subtitles using GuiOptionBrowser, and I can get it to change focus, but it doesn't respond to clicking. In Settings (and by googling) there is a while loop, but with this while loop the xmplayer just freezes:  
 [code]* *static void osdSubtitlesOptions() { bool firstRun = true; bool loopa = true; if (osd\_display\_option\_subtitle) { osd\_options\_window->SetFocus(0); osd\_options\_headline->SetText("Subtitle Options"); osd\_options\_subtitle\_window->SetVisible(true); osd\_options\_subtitle\_window->SetFocus(1); osd\_options\_subtitle->SetFocus(1); while (loopa == true) { //Removing while makes stuff selectable, but when clicking nothing happens, with while it freezes Menu\_Frame(); UpdatePads(); for (int i = 0; i < 4; i++) { mainWindow->Update(&userInput[i]); } int ret = osd\_options\_subtitle->GetClickedOption(); switch (ret) { case 0: { playerSwitchSubtitle(); break; } case 1: { sub\_visibility = 0; sub\_visibility = (sub\_visibility == 1) ? 0 : 1; break; } case 2: { sub\_pos++; if (sub\_pos>100) { sub\_pos = 0; } break; } case 3: { sub\_delay = sub\_delay + 0.1; if (sub\_delay > 10) { sub\_delay = -10; } break; } case 4: { text\_font\_scale\_factor = text\_font\_scale\_factor + 0.1; if (text\_font\_scale\_factor > 100) { text\_font\_scale\_factor = 0; } break; } case 5: { //Back button osd\_display\_option\_subtitle = 0; loopa = false; break; } } if (ret >= 0 || firstRun) { firstRun = false; sprintf(subtitle\_option\_list.value[0], "Sub"); if (sub\_visibility == 1) { sprintf(subtitle\_option\_list.value[1], "Enabled"); } else { sprintf(subtitle\_option\_list.value[1], "Disabled"); } sprintf(subtitle\_option\_list.value[2], "%d", sub\_pos); sprintf(subtitle\_option\_list.value[3], "%.1f s", sub\_delay); sprintf(subtitle\_option\_list.value[4], "%.2f", text\_font\_scale\_factor); sprintf(subtitle\_option\_list.value[5], "Back"); osd\_options\_subtitle->TriggerUpdate(); } } } //When removing while, else is added here osd\_options\_headline->SetText(""); osd\_options\_subtitle\_window->SetVisible(false); osd\_options\_subtitle\_window->SetFocus(0); osd\_options\_subtitle->SetFocus(0); osd\_options\_window->SetFocus(1); osd\_options\_menu\_subtitle\_btn->SetFocus(1); }[/code] Here is the whole menu.cpp on pastebin: http://pastebin.com/3VJMXmrx (Above code is line 1175)  
 The rest of xmplayer is the same as on my github, but without 2 new png's.  
   
 Can't seem to figure out why it doesn't work with the while, hope you guys can give a hint :)  
   
 My usb to rs232 ttl converter hasn't arrived yet (damn u Ebay), so can't give you any details from uart.   
   
 UPDATE:  
   
 Nevermind :D It seems to work now, without the while. Op just delete this topic 8)