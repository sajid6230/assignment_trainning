"""
22.	Write a program to check whether a letter is a vowel or a consonant
"""



letter = input("Enter a letter: ")

if len(letter) == 1 and letter.isalpha():
   letter1 = letter.upper()
   
   if letter1 not in ("A","E", "I", "O", "U"):
     print("Consonant")
   else:
      print("Vowel")
else:
   print("Please enter a valid letter")
