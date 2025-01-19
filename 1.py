# Program to find numbers divisible by 7 and multiples of 5 between 1500 and 2700




for i in range(1500,2701):
    if (i%5 == 0 and i%7 == 0):
        print("The number:" , i, "is divided by 7 and multiples of 5")
 

print("Done")

