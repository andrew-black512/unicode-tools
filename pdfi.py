#!/usr/bin/python3
import sys
import PyPDF2
import os
from datetime import datetime

#TODO poss library
def modtime ( p_filename ) :
    mtime = os.path.getmtime( p_filename )
    mtime_dt = datetime.fromtimestamp(mtime) 
    return mtime_dt
def format_time ( p_dt) :
    return p_dt.strftime('%d-%b-%Y %H:%M')
def modtime_str ( p_filename) :
    return format_time( modtime(p_filename))

def  print_info(input_pdf ):
      """
      prints info on pdf
      Args:
          input_pdf (str): Path to the input PDF file.
      """
      with open(input_pdf, 'rb') as input_file:
        reader = PyPDF2.PdfReader(input_file)
        pagect = len(reader.pages)
        time_str = modtime_str( input_pdf)
        print(f"{input_pdf[:40]:<40} {pagect:4d}    {time_str}")


filenames = sys.argv[1:]

print()
for f in filenames :
    print_info( f  )
print()            
