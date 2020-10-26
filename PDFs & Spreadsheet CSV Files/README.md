# PDFs-and-Spreadsheet-CSV-Files-with-Python
## Working with CSV files
### Reading CSV files
```python
import csv
data = open('example.csv',encoding="utf-8")
csv_data = csv.reader(data)
data_lines = list(csv_data)
```
### Writing to CSV Files
#### New File, will overwrite any exisiting file with the same name
```python
# newline controls how universal newlines works (it only applies to text
# mode). It can be None, '', '\n', '\r', and '\r\n'. 
file_to_output = open('to_save_file.csv','w',newline='')
csv_writer = csv.writer(file_to_output,delimiter=',')
csv_writer.writerow(['a','b','c'])
# returns 7
csv_writer.writerows([['1','2','3'],['4','5','6']])
file_to_output.close()
```
#### Existing File
```python
f = open('to_save_file.csv','a',newline='')
csv_writer = csv.writer(f)
csv_writer.writerow(['new','new','new'])
# returns 13
f.close()
```
## Working with PDF files
### Reading PDF files
```python
import PyPDF2
# rb - read binary
f = open('Working_Business_Proposal.pdf','rb')
pdf_reader = PyPDF2.PdfFileReader(f)
pdf_reader.numPages
# returns 5

for num in range(pdf_reader.numPages):
    page = pdf_reader.getPage(num)
    pdf_text.append(page.extractText())

f.close()
```
### Adding to PDF files
```python
f = open('Working_Business_Proposal.pdf','rb')
pdf_reader = PyPDF2.PdfFileReader(f)
first_page = pdf_reader.getPage(0)
pdf_writer = PyPDF2.PdfFileWriter()
pdf_writer.addPage(first_page)
pdf_output = open("Some_New_Doc.pdf","wb")
pdf_writer.write(pdf_output)
f.close()
```