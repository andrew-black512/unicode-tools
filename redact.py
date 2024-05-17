# Regular expression to match any vowel (case-insensitive)
vowel_pattern = r"[aeiouAEIOU]"

def substitute_vowels_regex(text):
  """Substitutes vowels in a string with "*" using regular expression.

  Args:
    text: The string to be processed.

  Returns:
    The string with vowels replaced by "*".
  """
  return re.sub(vowel_pattern, "*", text)

# Get the clipboard contents
text = clipboard.paste()
