'''
18.	Write a program to check whether a number is prime or not. 
Hint: Prime numbers have no other factors except for 1 and the number itself.

'''

num = int(input("Insert a number : "))

for i in range(2,num):
    if (num %  i == 0):
        print("Not a Prime Number")
        break
else:
    print("Prime number")