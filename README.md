FSB Remaker
Shadps4 FSB Remaker for Bloodborne

I’m working on a program that generates deciphered FSB files from the audio in Bloodborne, which first needs to be converted using foobar2000. I'm open to help (because I’m too lazy to do it all by myself!).

While it’s possible to do this manually, it’s a huge pain to handle over 500 files.

Steps:
Use foobar2000 along with the "VGStream" and "Encoder Pack" modules to convert all the audio files from the "sound" folder in Bloodborne.
Select all the FSB files in the folder and load them into foobar2000.
Go to the Edit menu and click Delete All Dead Items.
Click Edit again, select Select All, right-click on the files, and choose Convert.
A conversion settings window will open. Select Output Format and choose OGG or another preferred format.
Go back and select Destination to choose where the converted files should be saved.
Click Convert and let the process run—it may take some time.
After conversion, run folder_sort.py to organize and rename the files. The script will sort the files into newly created folders, making it easier to generate the FSB files.

At this point, you’ll need to configure special settings to create an FSB file for each folder. Unfortunately, progress is currently stuck at this stage.
