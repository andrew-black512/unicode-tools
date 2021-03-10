#!/usr/bin/python3
import argparse
import sys
import re

# arguments
filename = sys.argv[1]

with open(filename) as fh :
  for line in fh:
    for (i,c) in enumerate(line) :
        print (c)
