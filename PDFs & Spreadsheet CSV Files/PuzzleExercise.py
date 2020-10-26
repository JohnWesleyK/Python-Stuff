# Use Python to extract the Google Drive link from the .csv file
import csv
data = open('find_the_link.csv',encoding='utf-8')
csv_data = csv.reader(data)
data_lines  = list(csv_data)

csv_2d_array = []
GDrive_link = ''
for line in data_lines:
    csv_2d_array.append(line)

# print(len(csv_2d_array))

for i in range(len(csv_2d_array)):
    GDrive_link += csv_2d_array[i][i]

# print(GDrive_link)

import PyPDF2
file = open('Find_the_Phone_Number.pdf','rb')
pdf_reader = PyPDF2.PdfFileReader(file)

import re
pattern = r'\d{3}.\d{3}.\d{4}'
for num in range(pdf_reader.numPages):
    page_text = pdf_reader.getPage(num).extractText()
    match = re.search(pattern, page_text)
    if match:
        print(match.group())