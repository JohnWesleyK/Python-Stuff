# f = open('practice.txt','w+')
# f.write('wryyy')
# f.close
import os
import shutil

for folder, sub_folders, files in os.walk("Example_Top_Level"):

    print("Currently looking at folder: " + folder)
    print("THE SUBFOLDERS ARE: ")

    for sub_fold in sub_folders:
        print("\t Subfolder: " + sub_fold)

    print("THE FILES ARE: ")

    for f in files:
        print("\t File: " + f)
