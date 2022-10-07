import requests
#from bs4 import BeautifulSoup
#import PyPDF2
from camelot.io import read_pdf
import openpyxl

# Geting the PDF returning an error if can not
try:
    URL = "https://vasvari.org/wp-content/uploads/2022-okt_-6.pdf"
    response = requests.get(URL)
    open("files/file.pdf", "wb").write(response.content)
except:
    print("An error has accourd when downloading and convertin the PDF file.")

# Convert PDF tabel to .xlsx file
file = "files/file.pdf"
tables = read_pdf(file)
print("Total tables extracted:", tables.n)
print(tables[0].df)
tables[0].to_xlsx("files/output.xlsx")

# Opening the .xlsx file an deletin unnesesary row and culomns
path = "files/output.xlsx"
wb = openpyxl.load_workbook(path)
sheet = wb.active

row = sheet.max_row
column = sheet.max_column

sheet.move_range("B4:L" + str(row + 3), rows=-3, cols=-1)

if (sheet['C3'].value == None):
    print("Deleting unnessesary rows...")
    sheet.delete_rows(3)

wb.save("files/format.csv")

# CREATE TABLE all_date (
#	type varchar(4),
#    lesson varchar(3),
#    class varchar(10),
#    inTheTimetabel varchar(10),
#    actualLesson varchar(10),
#    substituteTeacher varchar(20),
#    lessonDate varchar(10),
#    lessonNumber varchar(5),
#    fromWhere varchar(6),
#    toWhere varchar(6)
# )
