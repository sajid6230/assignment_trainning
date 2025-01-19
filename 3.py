"""""
3.	Write a  Python program to construct the following pattern, using a nested for loop. Bonuse: Make it dynamic by asking the user number of rows.
Pattern:
*
* *
* * *
* * * *

""""


number = input("Enter number: ")
num = int(number)

for i in range(1,num+1):
    for j in range(1,i+1):
        print("*", end =" " )

    print()
