
"""
20.	Write a  Python program to find the second smallest number in a list.
"""


list1 = input("Insert a list of numbers (Coma-seperated) : ")

set_1 = set(map(int, list1.split(','))) # converted it to set to remove duplicates

list2 = list(set_1)
list2.sort()

print("The sorted list (asc): ",list2)

print("The second lowest number is : ", list2[1])




