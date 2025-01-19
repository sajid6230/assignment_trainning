"""
4.	Write a  Python program that accepts a word from the user and reverses it.

"""
word_a = input("Enter a Word : ")
word = list(word_a)
a = (len(word))

r_word = ""

for i in range(a-1,-1,-1):
    r_word = r_word + word[i]
    
print("Reversed Word : ",r_word)