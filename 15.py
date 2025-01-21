
"""
15.	Write a program to check whether a given string is a palindrome or not. 
Palindrome words have the same spelling if you reverse the string. 
Eg: Dad is a palindrome because it is the same when you reverse it.

"""

a = input("input a word= ")

b = list(a)
c = []
for i in range(len(b)-1, -1, -1):
    c.append(b[i])
if c == b :
    print("This is a Palindrome word")
else:
    print("XX NOT a Palindrome word XX") 