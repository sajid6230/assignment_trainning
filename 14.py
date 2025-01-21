"""
14.	Write a Python program to get the largest number from a list. 
Using both loop and max function.
"""


a = [2,3,99,4,5,87,111]

b = []

for i in range(1, len(a)):
    b.append(a[i])
print("Maximum number in the list is: ",max(b))