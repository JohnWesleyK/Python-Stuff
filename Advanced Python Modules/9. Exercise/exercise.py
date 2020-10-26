# Unzipping
import zipfile
zip_obj = zipfile.ZipFile('unzip_me_for_instructions.zip','r')
zip_obj.extractall('unzipped_content')

# Browsing through folders using OS
import os
# print(os.getcwd())
ext_content_dir = 'C:\\Users\\th3j9\\PycharmProjects\\Advanced-Python-Modules\\9. Exercise\\unzipped_content\\extracted_content'
# print(os.listdir(ext_content_dir))
import re
phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
results = []
for folder, sub_folders, files in os.walk(ext_content_dir):
    # print("Currently looking at folder: " + folder)
    # print("THE FILES ARE: ")

    for f in files:
        if not('Instructions.txt' in f):
            # print("\t File: " + f)
            dir_add = os.path.join(ext_content_dir,folder)
            # print(dir_add) # to check if the path address is working
            os.chdir(dir_add) # changing current working directory
            file1 = open(f,"r") # opening txt file
            # print(file1.read()) # checking if it returns a string
            match = re.search(phone_pattern, file1.read())
            if not (match == None):
                results.append(match.group())
print(results)


