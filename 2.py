import random



magic_number = random.randint(1,9)
while True:
    number = input("Guess a number between 1 to 9: ")
    num = int(number)
    if 1 <= num <= 9:
        if (num == magic_number):
            print("Well guessed!")
            break
        else:
            print("try again")
    else:
        print("Please! input valid number")


