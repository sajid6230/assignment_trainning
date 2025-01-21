"""
19.	Write a Python program to append a list to the second list.
"""

numbers1 = input("Insert 1st lits(coma-seperated): ")

numbers2 = input("Insert 2nd lits(coma-seperated): ")

list1 = list(map(int, numbers1.split(',')))

list2 = list(map(int, numbers2.split(',')))


list3 = []

for i in range(0, len(list1)):
    list3.append(list1[i])

for j in range(0,len(list2)):
        list3.append(list2[j])

print(list3)

