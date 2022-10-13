from PyPDF2 import PdfReader
import re

parts = []


# Exclude footer for wolof pdf
def visitor_body_wol(text, cm, tm, fontDict, fontSize):
    y = tm[5]
    if 54 < y:
        parts.append(text)


# Exclude footer for french pdf
def visitor_body_fr(text, cm, tm, fontDict, fontSize):
    y = tm[5]
    if 39 < y:
        parts.append(text)


# Extraction
def extract_pdf_text(filepath, language):
    pdf_file = PdfReader(filepath)
    if language == 'fr':
        interval = range(3, pdf_file.numPages)
        selector = visitor_body_fr
    if language == 'wol':
        interval = range(1, pdf_file.numPages)
        selector = visitor_body_wol
    for index in interval:
        page = pdf_file.pages[index]
        page.extract_text(visitor_text=selector)
        text = "".join(parts)
    return text


# Txt file
def generate_file(path, text):
    with open(path, 'w') as file:
        file.write(text)
    file.close()


# generate_file('../text_scrapped/coran/coran_wol.txt',
#               extract_pdf_text('../text_scrapped/coran/coran_wol.pdf', 'wol')
#               )

generate_file('../text_scrapped/coran/coran_fr.txt',
              extract_pdf_text('../text_scrapped/coran/coran_fr.pdf', 'fr')
              )
