f = open('fileone.txt','w+')
f.write('ONE DAY')
f.close()

f = open('filetwo.txt','w+')
f.write('DAY ONE')
f.close()

import zipfile

compressed_file = zipfile.ZipFile('compressed_file.zip','w')
compressed_file.write('fileone.txt',compress_type=zipfile.ZIP_DEFLATED)
compressed_file.write('filetwo.txt',compress_type=zipfile.ZIP_DEFLATED)
compressed_file.close()

zip_obj = zipfile.ZipFile('compressed_file.zip','r')
zip_obj.extractall('extracted_content')

import shutil
dir_to_zip = 'C:\\Users\\th3j9\\PycharmProjects\\Advanced-Python-Modules\\8. Zipping and Unzipping Files with Pyhton'
output_filename = 'example'
shutil.make_archive(output_filename,'zip',dir_to_zip)

shutil.unpack_archive('example.zip','final_unzip','zip')
