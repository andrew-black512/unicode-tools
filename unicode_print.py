#!/usr/bin/python3
import re
import sys
import unicodedata

# TODO ....
# REVIEW: it is wider than 80 cols so looks a though there is an extra line.
# allow decimal as well as Hex...

#----------------------------------------------------------
def print_unicode ( unicode_int ) :
    char = chr(unicode_int)
    # print ( "%x %s" % (unicode_int,chr(unicode_int) ) , end=" ")
    print  ( unicodedata.category(char), end="    ")
    if 1 :     #FEATURE munge SMALL / CAPITAL
      name = unicodedata.name(char)
      if re.search("CAPITAL", name ) :
        char_lower = char.lower()
        if char_lower == char :
            print(name, "same")
        else :
            print( ' see', char_lower, end='  ' )


      else :
        name = name.lower()
      print ( name )
    else:
      print  ( unicodedata.name(char) )
#-----------------------------
def print_column( text ) :
    print (text, end=' ')
#-----------------------------
# Prints out range of characters one per line
def print_table (char_int, num, repeat_ct) :
    char_int = char_int - (char_int % repeat_ct)

    # column headings if 2 or more
    print_column ('         ') # "%6X
    for i in range(0, 0 + repeat_ct  ):
        print_column ( '%x' %  i)
    print ('')
    #TODO print 8.9....F

    for i in range(char_int, char_int + num, repeat_ct ) :
        print_column ( "%6X : " % i)
        #print_column ( "%4x" % i ) ##if i % 4==0
        for j in range( i, i+repeat_ct ) :
            print_column(chr(j))
        print ('')
#-----------------------------
# Prints out range of characters one per line
def print_list ( from_int, num, repeat_ct_down=4 ) :

    for i in range(char_int, char_int + num ) :
        if i % repeat_ct_down == 0:
            print ('')
        if i % repeat_ct == 0:
            print_column ( "%6X : " % i)
        print_column(chr(i))
        print ('  ',end='')
        print_unicode( i )
    print ('')

#-----------------------------
# process args and set up "semi config variables"
try:
  assert len(sys.argv) - 1 == 3
  char_int = int(sys.argv[1], 16)
  num      = int(sys.argv[2] ) # TODO default to 1

  # only sensible/supported/tested values are 1,4,8
  repeat_ct = int(sys.argv[3] ) # TODO def = 8?
  repeat_ct_down = 8 # maybe repeat_ct unless that ==1

# Catch exceptions for bad arguments
except:
    # TODO: send to stderr
  print ("Usage: unicode_print.py U1 [num] [cols]")
  sys.exit()

if repeat_ct == 1 :
    print_list (char_int, num )
else :
    print_table (char_int, num, repeat_ct )
