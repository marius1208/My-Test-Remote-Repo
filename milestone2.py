import random

word_list = ["apple", "pineapple","pear","orange","strawberry"]
print(word_list)

word = random.choice(word_list)

print (word)

guess = input("Enter a letter:\n ")

if (len(guess) == 1 and guess.isalpha()== True ):
    print("good guess")
else:
    print("Oops! That is not a valid input.")
