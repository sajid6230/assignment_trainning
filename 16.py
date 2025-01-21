"""
16.	Write a program to check whether a given number is a palindrome. Eg: 101 is a palindrome
"""
a = int(input("Enter a number: "))

b = list(str(a))

c = []

for i in range(len(b)-1,-1,-1):
    c.append(b[i])

if c == b:
    print("YES! This is a Palindrome Number")
else:
    print("NO! Not a Palindrome Number ")

  