import PyPDF2
import requests
from bs4 import BeautifulSoup

import camelot

import xlsxwriter

URL = "https://vasvari.org/wp-content/uploads/2022-okt_-6.pdf"
response = requests.get(URL)
open("files/file.pdf", "wb").write(response.content)

file = "files/file.pdf"

tables = camelot.read_pdf(file)
print("Total tables extracted:", tables.n)
print(tables[0].df)
tables[0].to_txt("files/output.txt")

#workbook = xlsxwriter.Workbook('files/output.xlsx')
#worksheet = workbook.add_worksheet()

#worksheet.write('A1', worksheet.read('B4'))
