# Zlx screen boundaries

## 2011-09-24 10:47:17, posted by: dreamboy

Hey guys for the ones developing libxenon applications with zlx library i leave here the screen bounds  
   
 |=============|  
 | 1.0f |  
 | - |  
 | -1.0f - 0.0f + 1.0f |  
 | + |  
 | -1.0f |  
 |=============|  
 ||  
 / \  
   
 0.0f -> center screen  
 1.0f -> max x and y coordinates  
 -1.0f -> min x and y coordinates  
 2.0f -> full width and height of the screen  
 hope it helps ;)   
   
 Best regards

## 2011-09-24 10:57:19, posted by: Juvenal

that seems abit odd.  
   
 From the left/top of the screen to center is only 1.0f, and from center to right/bottom is 2.0f.  
   
 Is this actually correct?

## 2011-09-24 11:16:55, posted by: dreamboy

[quote="Juvenal"]  
 that seems abit odd.  
   
 From the left/top of the screen to center is only 1.0f, and from center to right/bottom is 2.0f.  
   
 Is this actually correct?  
 [/quote]  
   
 yeah i know , ced2911 told me the screen size its 2.0f. and if you look to the image full screen code it uses 2.0 width and height  
   
 Sample:  
 Draw::DrawColoredRect(-1.0f, -1.0f, 1.0f, 1.0f, 0xff000000);  
 this way the color wont fill the full screen.  
   
 [align=center]![](http://img38.imageshack.us/img38/7672/20110924101203.jpg)[img]http://img38.imageshack.us/img38/7672/20110924101203.jpg[/img][/align]  
   
   
   
 Correct Code:  
 Draw::DrawColoredRect(-1.0f, -1.0f, 2.0f, 2.0f, 0xff00ff00);  
   
 PS: Im using the black color to draw the rectangle in the code above

## 2011-09-24 11:28:54, posted by: Juvenal

well, seeing as i know little about the actual meaning of the function arguments you used, im going to assume that its similar to this  
   
 Draw::DrawColoredRect(X, Y, Width, Height, Color);  
   
 and, assuming that the screen size is 2.0f in either direction, plugging in the values in your first example would give you a square 1.0f x 1.0f, meaning the upper right corner would be at 0, 0  
   
 This does not however mean the upper right corner of the screen is coordinates 2, 2. it is 1, 1.  
   
 Because -1 + 2 = 1.  
   
 Again, if i am entirely wrong do correct me.  
   
 EDIT: redacted, error was corrected :)