import random
"""
    Class that simulates a simple Hangman game

    Takes in : 
    word_list - list of words to randomly choose from
    num_lives - max number of lives that the user has

"""
class Hangman:
    def __init__(self,word_list,num_lives):
        self.word_list = word_list                        #A list of words
        self.num_lives = num_lives                        #The number of lives the player has at the start of the game.
        self.word = random.choice(word_list)              #The word to be guessed, picked randomly from the word_list
        self.word_guessed = []                            #A list of the letters of the word, with _ for each letter not yet guessed. 
        for self.i in range(int(len(self.word))):         #For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']. 
            self.word_guessed = self.word_guessed + ["_"] #If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
        #print(self.word) 
        #print(self.word_guessed) 
        unique_letters = set(self.word)            
        self.num_letters = len(unique_letters)                            #The number of UNIQUE letters in the word that have not been guessed yet
        self.list_of_guesses = []                         #A list of the guesses that have already been tried


    
    """
    Function for checking if a guess is correct or not

    Takes in :  
    guess - guess made by the user

    Returns:
    1. If the guess made by the user is not in the chosen word:
    Prints {guess} not in the word 
    Reduces num_lives by 1

    2. If the guess made by the user is  in the chosen word:
    Updates the word_guessed list with the guessed letter
    Reduces num_letters by 1
    """

    def check_guess (self,guess):
        guess = guess.lower()
        if (guess in self.word ):
            print ("Good guess! " + guess + " is in the word.")
            count = 0
            for i in self.word:
               count = count+1
               if i == guess:                   
                   self.word_guessed[count-1] = i
                   #print(self.word_guessed)
            self.num_letters = self.num_letters - 1
            print(self.word_guessed)
            #print( "Unique letters left to guess : ",self.num_letters)
        else:
            print ("Sorry, " + guess + " is not in the word. Try again.")
            self.num_lives -= 1
            print(" You have " , self.num_lives , " lives left")


    """
    Function that asks for input from the user

    Takes in :
    Input from user 

    Returns:
    If the input is not a alpabetical character, prints:
    "Invalid letter. Please, enter a single alphabetical character." 
    If the letter has been allready tried, prints:
    "You already tried that letter!"
    Otherwise, calls the check_guess function 
    
    
    """
    def ask_for_input(self):       
        guess = input ("Guess a letter:\n")
        if (len(guess) != 1 or guess.isalpha()!= True ):
            print("Invalid letter. Please, enter a single alphabetical character.")
        elif guess in self.list_of_guesses:
            print("You already tried that letter!")
        else:
            self.check_guess(guess)
            self.list_of_guesses.append(guess)
    """
    Function to play the game

    Constists of a while loop which terminates if num_lives is 0 , meaning the user lost
    or if num_lettes is 0 and num_lives is >0 meaning the user won
    
    
    """
    def play_game(self):
        print(self.word_guessed)
        while (True) :
            if self.num_letters == 0 and num_lives >0:
                print("Congratulations. You won the game!")
                break
            if self.num_lives == 0:
                print("You lost!")
                break
            if self.num_letters>0:
                self.ask_for_input()





word_list = ["apple", "pineapple","pear","orange","strawberry"] 
num_lives = 5 

Hangman_1 = Hangman(word_list,num_lives)
Hangman_1.play_game()


            
