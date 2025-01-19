"""

5.	Write a Python program to count the number of even and odd numbers in a series of numbers
Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
Expected Output :
Number of even numbers : 5
Number of odd numbers : 4
"""


numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 

odd_counter = 0
even_counter = 0

for i in numbers:
    if (i % 2 == 0 ) :
        even_counter += 1
    
    else:
        odd_counter += 1


print("Number of ODD numbers: ", odd_counter)
print("Number of EVEN numbers: ", even_counter)

## numbers = list(map(int, user_input.split()))