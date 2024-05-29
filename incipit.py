#!/usr/bin/python3

def  extract_first_n_pages(input_pdf,  num_pages):
      """
      Extracts the first N pages from a PDF and saves them to a new PDF.

      Args:
          input_pdf (str): Path to the input PDF file.
          num_pages (int): Number of pages to extract.
      """
      with open(input_pdf, 'rb') as input_file:
        reader = PdfReader(input_file)
        page = reader.pages[0]
        print(page.extract_text())

filenames = sys.argv[1:]