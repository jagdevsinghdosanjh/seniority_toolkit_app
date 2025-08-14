from PyPDF2 import PdfReader, PdfWriter
from io import BytesIO

def split_pdf(pdf_file, pages_per_split):
    reader = PdfReader(pdf_file)
    total_pages = len(reader.pages)
    output_files = []

    for start in range(0, total_pages, pages_per_split):
        writer = PdfWriter()
        for i in range(start, min(start + pages_per_split, total_pages)):
            writer.add_page(reader.pages[i])

        output = BytesIO()
        writer.write(output)
        output.seek(0)
        output_files.append(output)

    return output_files
