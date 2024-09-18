import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    filename = Path(filepath).stem.split("-")[0]
    date = Path(filepath).stem.split("-")[1]
    pdf.add_page()
    pdf.set_font(family="Times", size = 16, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice nr. {filename}", ln=1)
    pdf.cell(w=50, h=8, txt=f"Date {date}", ln=1)

    columns = df.columns
    columns = [item.replace("_"," ").title() for item in columns]
    pdf.set_font(family="Times", size=10, style = "B")
    pdf.set_text_color(80,80,80)
    pdf.cell(w=30, h=8, txt=columns[0], border=1)
    pdf.cell(w=68, h=8, txt=columns[1], border=1)
    pdf.cell(w=32, h=8, txt=columns[2], border=1)
    pdf.cell(w=30, h=8, txt=columns[3], border=1)
    pdf.cell(w=30, h=8, txt=columns[4], border=1, ln=1)

    for index, row in df.iterrows():
        pdf.set_font(family="Times", size=10)
        pdf.set_text_color(80,80,80)
        pdf.cell(w=30, h=8, txt=str(row["product_id"]), border=1)
        pdf.cell(w=68, h=8, txt=row["product_name"], border=1)
        pdf.cell(w=32, h=8, txt=str(row["amount_purchased"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["price_per_unit"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["total_price"]),border=1, ln=1)

    total_price = df["total_price"].sum()
    pdf.set_font(family="Times", size=10)
    pdf.set_text_color(80,80,80)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=68, h=8, txt="", border=1)
    pdf.cell(w=32, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt=str(total_price),border=1, ln=1)

    pdf.ln(15)
    pdf.set_font(family="Times", size=14, style="B")
    pdf.cell(w=50, h=8, txt= f"The total due amount is {total_price} Euros")


    pdf.output(f"{Path(filepath).stem}.pdf")
