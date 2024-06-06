#!/usr/bin/python3
import sys
import PyPDF2

def  extract_first_n_pages(input_pdf, w,  num_pages):
      """
      Extracts the first N pages from a PDF and saves them to a new PDF.

      Args:
          input_pdf (str): Path to the input PDF file.
          num_pages (int): Number of pages to extract.
      """
      with open(input_pdf, 'rb') as input_file:
        reader = PyPDF2.PdfReader(input_file)
        page = reader.pages[0]
        print(page.extract_text())
        w.add_page(page)


filenames = sys.argv[1:]
writer = PyPDF2.PdfWriter()

for f in filenames :
    print (f)
    extract_first_n_pages( f, writer, 1 )
            
writer.write("output.pdf")
