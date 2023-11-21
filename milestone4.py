import random

class Hangman:
    def __init__(self,word_list,num_lives):
        self.word_list = word_list                        #A list of words
        self.num_lives = num_lives                        #The number of lives the player has at the start of the game.
        self.word = random.choice(word_list)              #The word to be guessed, picked randomly from the word_list
        self.word_guessed = []                            #A list of the letters of the word, with _ for each letter not yet guessed. 
        for self.i in range(int(len(self.word))):         #For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']. 
            self.word_guessed = self.word_guessed + ["_"] #If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
        print(self.word) 
        print(self.word_guessed)              
        self.num_letters = 0                              #The number of UNIQUE letters in the word that have not been guessed yet
        self.list_of_guesses = []                         #A list of the guesses that have already been tried


    

    def check_guess (self,guess):
        guess = guess.lower()
        if (guess in self.word ):
            print ("Good guess! " + guess + " is in the word.")
            count = 0
            for i in self.word:
               count = count+1
               #print(type(i))
               #print(type(count))
               if i == guess:                   
                   self.word_guessed[count-1] = i
                   print(self.word_guessed)
            self.num_letters = self.num_letters - 1
            print(self.num_letters)
        else:
            print ("Sorry, " + guess + " is not in the word. Try again.")
            self.num_lives -= 1
            print(type(self.num_lives))
            print(" You have " , self.num_lives , " lives left")

    def ask_for_input(self):
        while (True):
            guess = input ("Guess a letter:\n")
            if (len(guess) != 1 or guess.isalpha()!= True ):
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)


num_lives = 5  
word_list = ["apple", "pineapple","pear","orange","strawberry"] 
Hangman_1 = Hangman(word_list,num_lives)
Hangman_1.ask_for_input()

    

    
                





