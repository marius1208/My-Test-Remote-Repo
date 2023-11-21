import random

word_list = ["apple", "pineapple","pear","orange","strawberry"]
word = random.choice(word_list)
print(word)


""" Function that validates the letter user inputs

Takes in: user input
Returns: 
User input if it is a 1 character long letter
"Invalid letter. Please, enter a single alphabetical character." otherwise untill it is a 1 character long letter
"""
def validate_input():
    while(True):
        guess = input ("Guess a letter:\n")
        guess.lower
        if (len(guess) == 1 and guess.isalpha()== True ):
           return guess
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")


""" Function that checks if the letter in in the randomly chose word

    Takes in guess
    Returns : 
    "Sorry, {guess} is not in the word. Try again." is the guess is incorrect untill the user gets a correct guess
    "Good guess! {guess} is in the word." if the guess is correct
"""
def check_guess(guess):
    while (True):

        if (guess in word):
            print ("Good guess! " + guess + " is in the word.")
            break
        else:
            print ("Sorry, " + guess + " is not in the word. Try again.")
            check_guess(validate_input())
            break



check_guess(validate_input())
