"""

13.	Write a  Python program to multiply all the items in a list

"""


a = [1,2,3,4,5]

b = 1

for i in range(0, len(a)):
    b = b * a[i]

print("Multiplication value of each list item: ",b)

