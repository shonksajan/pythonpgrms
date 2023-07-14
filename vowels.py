def is_vowel(char):
  vowels = "aeiouAEIOU"
  return char in vowels

def print_vowels(stringx):
  for char in stringx:
    if is_vowel(char):
      print(char, end="")

str =(input("Enter the string:"))
print_vowels(str)