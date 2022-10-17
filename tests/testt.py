import openpyxl
from re import search

path = "../files/format.xlsx"
wb = openpyxl.load_workbook(path)

sheet = wb.active
row = sheet.max_row
classes = []
print(type(row))
print(row)
# Search class
for i in range(0, row):
    if search("11.c", sheet['C' + i].value):
        classes.append(i)

print(classes)
