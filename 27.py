"""
27.	Write a  Python program to compute the element-wise sum of given tuples.
Original lists:
(1, 2, 3, 4)
(3, 5, 2, 1)
(2, 2, 3, 1)
Element-wise sum of the said tuples:
(6, 9, 8, 6)
"""
a = (1, 2, 3, 4)
b = (3, 5, 2, 1)
c = (2, 2, 3, 1)

d = []


for i in range(len(a)):
    sum = a[i] + b[i] + c[i]
    d.append(sum)

print("Element-wise Sum: ",tuple(d))
