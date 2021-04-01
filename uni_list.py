#!/usr/bin/python3
import argparse
import sys
import unicodedata

#----------------------------------------------------------
def print_unicode ( unicode_char ) :

    # print ( "%x %s" % (unicode_int,chr(unicode_int) ) , end=" ")
    print  (
       unicode_char,
       unicodedata.name(unicode_char)
    )

#----------------------------------------------------------
# arguments
filename = sys.argv[1]

with open(filename) as fh :
  for line in fh:
    for (i,c) in enumerate(line.rstrip() ) :
        print_unicode (c)
