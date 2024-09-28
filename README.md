# FSB Remaker
Shadps4 FSB remaker for Bloodborne.

Trying to create a program that generates deciphered FSB files from the audio in Bloodborne, which you need to convert by using foobar2000. I'm happy to get help (I'm too lazy to do it all myself). 

It's possible to do this manually, but it's a huge pain in ass to handle 500 files. 

First, you need to use foobar2000 along with the "VGStream" and "Encoder Pack" modules to convert all the audio files from the "sound" folder in Bloodborne. Simply select all the FSB files in the folder and load them into foobar2000. 
Next, go to the "Edit" menu and click "Delete All Dead Items." After that, click "Edit" again, select "Select All," right-click on the files, and choose "Convert."
A new window with conversion settings will open. Click on "Output Format" and choose "OGG" or another desired format. Then go back, select the "Destination" option, and choose the folder where you want to save the converted files. 
Finally, click "Convert." The process will take some time.

After this, use `folder_sort.py` to sort and rename the files as needed. The script will organize the files into newly created folders, making it easier to generate the FSB files.
At this point, you'll need to apply special settings to create an FSB file for each folder. However, progress is currently stuck at this step.
