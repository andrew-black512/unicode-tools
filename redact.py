#!/usr/bin/python2
import clipboard
import re

# Regular expression to match any vowel (case-insensitive)
vowel_pattern = r"[aeiouAEIOU]"

def substitute_vowels_regex(text, p_pattern):
  """Substitutes vowels in a string with "*" using regular expression.

  Args:
    text: The string to be processed.

  Returns:
    The string with vowels replaced by "*".
  """
  return re.sub(p_pattern, "*", text)

# Get the clipboard contents
text = clipboard.paste()
new_text = substitute_vowels_regex(text,vowel_pattern)
clipboard.copy( new_text) 
print( new_text )

