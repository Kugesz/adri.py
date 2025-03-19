import pdfplumber
import pandas as pd

def convert_pdf_to_excel() -> None:
    pdf_path = "../files/file.pdf"
    xlsx_path = "../files/output.xlsx"

    with pdfplumber.open(pdf_path) as pdf:
        first_page = pdf.pages[0]  # Assuming the table is on the first page
        table = first_page.extract_table()  # Extract table 
    # Convert to a DataFrame
    df = pd.DataFrame(table)    
    # Save to Excel
    df.to_excel(xlsx_path, index=False, header=False)
