"""
17.	Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.

"""

a = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

b = []

for i in range(0, len(a)):
    if i not in (0,3,4):
        b.append(a[i])

print(b)