"""
12.	Write a  Python program to sum all the items in a list. Using both loop and sum function.
"""


list_1 = [2,3,4]

a = []
for i in range(0, len(list_1)) : #loop
    a.append(list_1[i])
print(sum(a)) # sum function