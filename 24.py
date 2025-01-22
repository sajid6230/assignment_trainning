"""
24.	Write a Python program to add an item to a tuple.
"""


tuple_1 = ("A", "B", "C")
list_1 = list(tuple_1)

input_1 = input("Insert anything: ")

list_1.append(input_1)

tuple_2 = tuple(list_1)

print(tuple_2)
