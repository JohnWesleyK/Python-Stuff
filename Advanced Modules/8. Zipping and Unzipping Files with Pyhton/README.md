# Zipping and Unzipping Files with Python
## Zipping Files
### Creating files to compress
```python
f = open('fileone.txt','w+')
f.write('ONE DAY')
f.close()

f = open('filetwo.txt','w+')
f.write('DAY ONE')
f.close()
```
The [zipfile library](https://docs.python.org/3/library/zipfile.html) is built in to Python, we can use it to compress folders or files. To compress all files in a folder, just use the os.walk() method to iterate this process for all the files in a directory.
We're creating zip file first then writing to it.
```python
import zipfile

compressed_file = zipfile.ZipFile('compressed_file.zip','w')
compressed_file.write('fileone.txt',compress_type=zipfile.ZIP_DEFLATED)
compressed_file.write('filetwo.txt',compress_type=zipfile.ZIP_DEFLATED)
compressed_file.close()
```
## Extracting from Zip Files
We can do this with either the extractall() method to get all the files, or just using the extract() method to only grab individual files.
```python
zip_obj = zipfile.ZipFile('compressed_file.zip','r')
zip_obj.extractall('extracted_content')
```
## Using shutil library for zipping and unzipping
When you want to archive everything at once, The shutil library has easy to use commands for this.
```python
import shutil
dir_to_zip = 'C:\\Users\\th3j9\\PycharmProjects\\Advanced-Python-Modules\\8. Zipping and Unzipping Files with Pyhton'

# creating a zip archive
output_filename = 'example'
shutil.make_archive(output_filename,'zip',dir_to_zip)

# Extracting a zip archive
shutil.unpack_archive('example.zip','final_unzip','zip')
```