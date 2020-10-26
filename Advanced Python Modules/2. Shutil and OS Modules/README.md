# Shutil and OS Modules
## Opening and Reading Files
### File Paths
Type pwd in Python Console
```python
pwd
```
```text
'C:\\Users\\th3j9\\PycharmProjects\\Advanced-Python-Modules'
```
### Create File
```python
f = open('practice.txt','w+')
f.write('wryyy')
f.close
```
### Getting Directories
Python has a built-in [os module](https://docs.python.org/3/library/os.html) that allows us to use operating system dependent functionality.
To get the current directory:
```python
import os
os.getcwd()
```
```text
'C:\\Users\\th3j9\\PycharmProjects\\Advanced-Python-Modules'
```
### Listing Files in a Directory
```python
# In your current directory
os.listdir()
```
```text
['.git',
 '.gitignore',
 '.idea',
 '1. Collections Module',
 '2. Shutil and OS Modules',
 '3. Datetime Module',
 '4. Math and Random Modules',
 '5. Python Debugger',
 'README.md']
```
```python
# In any directory you pass
os.listdir("C:\\\Users")
```
```text
['All Users',
 'Default',
 'Default User',
 'defaultuser0',
 'desktop.ini',
 'Public',
 'th3j9']
```
### Moving Files
**shutil** is a buit-in module used to move files to different locations. But, there are permission restrictions, for example if you are logged in a User A, you won't be able to make changes to the top level Users folder without the proper permissions, [more info](https://stackoverflow.com/questions/23253439/shutil-movescr-dst-gets-me-ioerror-errno-13-permission-denied-and-3-more-e)
```python
import shutil
shutil.move('practice.txt','C:\\Users\\th3j9')
```
```text
'C:\\Users\\th3j9\\practice.txt'
```
```python
os.listdir()
```
```text
['.git',
 '.gitignore',
 '.idea',
 '1. Collections Module',
 '2. Shutil and OS Modules',
 '3. Datetime Module',
 '4. Math and Random Modules',
 '5. Python Debugger',
 'README.md']
```
```python
shutil.move('C:\\Users\\th3j9\\PycharmProjects\\Advanced-Python-Modules\\2.Shutil-and-OS-Modules\practice.txt',os.getcwd())
```
```text
'C:\\Users\\th3j9\\PycharmProjects\\Advanced-Python-Modules\\practice.txt'
```
```python
os.listdir()
```
```text
['.git',
 '.gitignore',
 '.idea',
 '1. Collections Module',
 '2. Shutil and OS Modules',
 '3. Datetime Module',
 '4. Math and Random Modules',
 '5. Python Debugger',
 'practice.txt',
 'README.md']
```
### Deleting Files
**os module has 3 methods for deleting files:**
* os.unlink(path) which deletes a file at the path your provide
* os.rmdir(path) which deletes a folder (folder must be empty) at the path your provide
* shutil.rmtree(path) this is the most dangerous, as it will remove all files and folders contained in the path.
**All of these methods can not be reversed! Which means if you make a mistake you won't be able to recover the file. Instead we can use the send2trash module, A safer alternative that sends deleted files to the trash bin instead of permanent removal.**

Installing send2trash module using pip:
```bash
pip install send2trash
```
```python
import send2trash
os.listdir()
```
```text
['.git',
 '.gitignore',
 '.idea',
 '1. Collections Module',
 '2. Shutil and OS Modules',
 '3. Datetime Module',
 '4. Math and Random Modules',
 '5. Python Debugger',
 'practice.txt',
 'README.md']
```
```python
send2trash.send2trash('practice.txt')
os.listdir()
```
```text
['.git',
 '.gitignore',
 '.idea',
 '1. Collections Module',
 '2. Shutil and OS Modules',
 '3. Datetime Module',
 '4. Math and Random Modules',
 '5. Python Debugger',
 'README.md']
```
### Walking through a directory
os module has a direct method call for this called os.walk()
```python
os.getcwd()
```
```text
'C:\\Users\\th3j9\\PycharmProjects\\Advanced-Python-Modules'
```
```python
os.listdir()
```
```text
['.git',
 '.gitignore',
 '.idea',
 '1. Collections Module',
 '2. Shutil and OS Modules',
 '3. Datetime Module',
 '4. Math and Random Modules',
 '5. Python Debugger',
 'README.md']
```
```python
for folder, sub_folders, files in os.walk("Example_Top_Level"):
    
    print("Currently looking at folder: " + folder)
    print("THE SUBFOLDERS ARE: ")
    
    for sub_fold in sub_folders:
        print("\t Subfolder: " + sub_fold)
    
    print("THE FILES ARE: ")
    
    for f in files:
        print("\t File: " + f)
```
```text
Currently looking at folder: Example_Top_Level
THE SUBFOLDERS ARE: 
	 Subfolder: Mid-Example-One
THE FILES ARE: 
	 File: Mid-Example.txt
Currently looking at folder: Example_Top_Level\Mid-Example-One
THE SUBFOLDERS ARE: 
	 Subfolder: Bottom-Level-One
	 Subfolder: Bottom-Level-Two
THE FILES ARE: 
	 File: Mid-Level-Doc.txt
Currently looking at folder: Example_Top_Level\Mid-Example-One\Bottom-Level-One
THE SUBFOLDERS ARE: 
THE FILES ARE: 
	 File: One_Text.txt
Currently looking at folder: Example_Top_Level\Mid-Example-One\Bottom-Level-Two
THE SUBFOLDERS ARE: 
THE FILES ARE: 
	 File: Bottom-Text-Two.txt
```