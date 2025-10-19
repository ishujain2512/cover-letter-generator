import os
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


def save_as_pdf(content, filename="cover_letter.pdf"):
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4
    y_position = height - 72  # start 1 inch from the top

    # Use a simple word wrap for long lines
    for line in content.split("\n"):
        wrapped_lines = wrap(line, width=90)  # wrap text for A4 width
        for wrapped_line in wrapped_lines:
            c.drawString(72, y_position, wrapped_line)
            y_position -= 15
            if y_position < 72:  # move to next page if space ends
                c.showPage()
                y_position = height - 72

    c.save()
    print(f"\n Cover letter saved as {filename}")