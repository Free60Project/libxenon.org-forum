# Getting current working directory?

## 2011-09-19 03:00:00, posted by: supatx

Is it possible? If not, how should I go about opening files relative to where my executable is located?

## 2011-09-19 03:05:21, posted by: Cancerous1

can you give a better explanation what you're trying to do?

## 2011-09-19 05:03:55, posted by: supatx

Load a file.  
   
 For instance: [code]* *FILE* fp = NULL; fp = fopen("data/fontset.bin", "rb"); if (!fp) // fail [/code] This always fails, even though data/fontset.bin exists.

## 2011-09-19 05:48:27, posted by: Cancerous1

try uda:/data/fontset.bin

## 2011-09-19 05:51:31, posted by: sk1080

but he doesent want to use an absolute path.....  
   
 He wants to use a relative path so that it can load a file from where it was launched, which afaik is not possible atm

## 2011-09-19 06:00:37, posted by: Cancerous1

[quote="sk1080"]  
 but he doesent want to use an absolute path.....  
   
 He wants to use a relative path so that it can load a file from where it was launched, which afaik is not possible atm  
 [/quote]  
   
 [quote="supatx"]  
 Is it possible? If not, how should I go about opening files relative to where my executable is located?  
 [/quote]  
   
 why so he does... thanks for stepping in and helping ;)

## 2011-09-19 06:11:46, posted by: supatx

[quote="sk1080"]  
 He wants to use a relative path so that it can load a file from where it was launched, which afaik is not possible atm  
 [/quote]  
   
 :(