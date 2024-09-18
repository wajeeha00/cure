import os
import glob
import pandas as pd
from fpdf import FPDF
from pathlib import Path
 
def generate(invoices_path, pdfs_path, image_path, product_id, product_name, amount_purchased, price_per_unit, total_price):
    print("Starting generate function")
    print(f"Image path: {image_path}")
 
    # Use glob to find all Excel files in the provided invoices_path
    filepaths = glob.glob(os.path.join(invoices_path, '*.xlsx'))
    print(f"Found files: {filepaths}")
 
    for filepath in filepaths:
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()
        print(f"Processing file: {filepath}")
 
        filename = Path(filepath).stem
        try:
            invoice_nr, date = filename.split("-")
        except ValueError as e:
            print(f"Error splitting filename {filename}: {e}")
            continue
 
        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Invoice nr.{invoice_nr}", ln=1)
 
        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Date: {date}", ln=1)
 
        try:
            df = pd.read_excel(filepath, sheet_name="Sheet 1")
        except Exception as e:
            print(f"Error reading {filepath}: {e}")
            continue
 
        # Add a header
        columns = df.columns
        columns = [item.replace("_", " ").title() for item in columns]
        pdf.set_font(family="Times", size=10, style="B")
        pdf.set_text_color(80, 80, 80)
        pdf.cell(w=30, h=8, txt=columns[0], border=1)
        pdf.cell(w=70, h=8, txt=columns[1], border=1)
        pdf.cell(w=30, h=8, txt=columns[2], border=1)
        pdf.cell(w=30, h=8, txt=columns[3], border=1)
        pdf.cell(w=30, h=8, txt=columns[4], border=1, ln=1)
 
        # Add rows to the table
        for index, row in df.iterrows():
            pdf.set_font(family="Times", size=10)
            pdf.set_text_color(80, 80, 80)
            pdf.cell(w=30, h=8, txt=str(row[product_id]), border=1)
            pdf.cell(w=70, h=8, txt=str(row[product_name]), border=1)
            pdf.cell(w=30, h=8, txt=str(row[amount_purchased]), border=1)
            pdf.cell(w=30, h=8, txt=str(row[price_per_unit]), border=1)
            pdf.cell(w=30, h=8, txt=str(row[total_price]), border=1, ln=1)
 
        total_sum = df[total_price].sum()
        pdf.set_font(family="Times", size=10)
        pdf.set_text_color(80, 80, 80)
        pdf.cell(w=30, h=8, txt="", border=1)
        pdf.cell(w=70, h=8, txt="", border=1)
        pdf.cell(w=30, h=8, txt="", border=1)
        pdf.cell(w=30, h=8, txt="", border=1)
        pdf.cell(w=30, h=8, txt=str(total_sum), border=1, ln=1)
       
        # Add total sum sentence
        pdf.set_font(family="Times", size=10, style="B")
        pdf.cell(w=30, h=8, txt=f"The total price is {total_sum}", ln=1)
 
        # Add company name and logo
        pdf.set_font(family="Times", size=14, style="B")
        pdf.cell(w=25, h=8, txt=f"PythonHow")
        try:
            pdf.image(image_path, w=10)
        except Exception as e:
            print(f"Error adding image {image_path}: {e}")
 
        if not os.path.exists(pdfs_path):
            os.makedirs(pdfs_path)
 
        pdf_output_path = os.path.join(pdfs_path, f"{filename}.pdf")
        try:
            pdf.output(pdf_output_path)
            print(f"PDF saved as {pdf_output_path}")
        except Exception as e:
            print(f"Error saving PDF {pdf_output_path}: {e}")