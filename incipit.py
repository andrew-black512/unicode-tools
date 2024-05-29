#!/usr/bin/python3
import sys
import PyPDF2

def  extract_first_n_pages(input_pdf,  num_pages):
      """
      Extracts the first N pages from a PDF and saves them to a new PDF.

      Args:
          input_pdf (str): Path to the input PDF file.
          num_pages (int): Number of pages to extract.
      """
      with open(input_pdf, 'rb') as input_file:
        reader = PyPDF2.PdfReader(input_file)
        writer = PyPDF2.PdfWriter()
        page = reader.pages[0]
        print(page.extract_text())
        writer.add_page(page)
        writer.write("output.pdf")


filenames = sys.argv[1:]
for f in filenames :
    print (f)
    extract_first_n_pages( f, 1 )