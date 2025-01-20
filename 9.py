"""
9.	Write a  Python program to find numbers 
between 100 and 400 (both included) where each digit of a number is an even number. 
Example: 122 is not the number but 222 is the number because all the digits are even

"""


start = 100
end = 400

All_even = []


for num in range(start, end+1):
    for digit in str(num):
        if (int(digit) % 2 != 0 ):
            break
    else:
        All_even.append(num)

print(All_even)





"""

# Manually testing taking user input

while True:
    input_a = int(input("Please enter a number between 200 and 400: "))
    if 100 <= input_a <= 400:
        break
    else:
        print("Invalid input! Please enter a number between 200 and 400.")

digit = []

for i in str(input_a):
    digit.append(int(i))

for i in range(0, len(digit)):
    if (digit[i] % 2 != 0 ):
        print("NOT ALL EVEN")
        break
    
else:
    print("ALL_EVEN")

"""