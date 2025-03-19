import openpyxl

import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import config

class_name = config.class_name

def clean_array(array):
  return [item if item is not None else "" for item in array]

def getting_data():
  path = "../files/output.xlsx"
  wb = openpyxl.load_workbook(path)
  sheet = wb.active

  column_data = [cell.value for cell in sheet["D"]]
  clean_column_data = clean_array(column_data) # Replace None with empty string

  row_indexes = [i for i, s in enumerate(clean_column_data) if class_name in s] # Find all rows with the class name

  rows_data = []

  for row_index in row_indexes:
    row_data = [cell.value for cell in sheet[row_index + 1]]
    rows_data.append(clean_array(row_data))

  return rows_data
