#!/usr/bin/python3
import sys
import PyPDF2

def  extract_first_n_pages(input_pdf ):
      """
      Extracts the first N pages from a PDF and saves them to a new PDF.

      Args:
          input_pdf (str): Path to the input PDF file.
          num_pages (int): Number of pages to extract.
      """
      with open(input_pdf, 'rb') as input_file:
        reader = PyPDF2.PdfReader(input_file)
        #TODO iterate on num_pages
        pagect = len(reader.pages)
        #date=.strftime('%d-%b-%Y')
        print(f"{input_pdf[:40]:<40}{pagect:4d}")


filenames = sys.argv[1:]

for f in filenames :
    extract_first_n_pages( f  )
            
