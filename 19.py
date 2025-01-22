"""
19.	Write a Python program to append a list to the second list.
"""

numbers1 = input("Insert 1st lits(coma-seperated): ")

numbers2 = input("Insert 2nd lits(coma-seperated): ")

list1 = list(map(int, numbers1.split(',')))

list2 = list(map(int, numbers2.split(',')))


list3 = []

for i in list1:
    list3.append(i)

for j in list2:
        list3.append(j)

print(list3)

