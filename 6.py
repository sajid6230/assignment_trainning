"""
6.	Write a  Python program to get the Fibonacci series between 0 and 50.
Note : The Fibonacci Sequence is the series of numbers :
0, 1, 1, 2, 3, 5, 8, 13, 21, ....
Every next number is found by adding up the two numbers before it.
Expected Output : 1 1 2 3 5 8 13 21 34

"""

n = int(input("Enter the number of terms for the Fibonacci sequence: "))
numbers = list(range(0,n))
fibonacci = []

for i in range(0, len(numbers)):
    if i == 0:
        fibonacci.append(0)
    elif i == 1:
        fibonacci.append(1)
    else:
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])

print("fibonacci sequence: ", fibonacci)



"""
#Another method

n = int(input("Enter the number of terms for the Fibonacci sequence: "))

# Start with the first two Fibonacci numbers
a, b = 0, 1
print(a, b, end=" ")  # Print the first two terms


for _ in range(2, n):  
    c = a + b  
    print(c, end=" ")  
    a, b = b, c 

"""