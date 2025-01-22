"""
21.	Write a Python program to get the frequency of elements in a list.
"""


numbers = ['A','B','E','A','C',1,1,6,1,5,'B']


dictionary = {}

for i in numbers:
    if i in dictionary:
        dictionary[i] += 1
    else:
        dictionary[i] = 1

print(dictionary)


