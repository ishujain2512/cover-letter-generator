from docx import Document
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from textwrap import wrap


def save_as_txt(content, filename="cover_letter.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"\n Cover letter saved as {filename}")


def save_as_docx(content, filename="cover_letter.docx"):
    doc = Document()
    doc.add_paragraph(content)
    doc.save(filename)
    print(f"\n Cover letter saved as {filename}")
