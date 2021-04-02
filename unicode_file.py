#!/usr/bin/python3
import argparse
import sys
import unicodedata

#----------------------------------------------------------
def print_unicode ( unicode_char ) :
     min_char = 0x80   # poss config
     n = ord(unicode_char )
     if n >= min_char :
         print  (
           "%4X" % n ,
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
