# Hangman Beginner Project
# Initial Ideas and Plan
# List/Tuple of pre-chosen words
# Difficulty selection
# Select a random word
# Get length of word len()
# 

# UI
# Ascii art

# Setup a tuple of pre chosen words
# Tuples are constant lists
wordsEasy = ("cat","dog","book","plane","space")
wordsMedium = ("nintendo","abrupt","python","length","subway","charity","military")
wordsHard = ("microwave","azure","banjo","transcript","bandwagon","oxygen","vapourise","joking","volunteer")

gameOn = True
# Lives are assigned as variables rather than individual numbers to improve code maintainability
# easier to change lives in one location than multiple
easyLives = 8
mediumLives = 10
hardLives = 15

import time
import random as r

# everyone loves ascii art
def art():
    time.sleep(0.2)
    print('''--------------------------------------------------------------
888                                                           
888                                                           
888                                                           ''')
    time.sleep(0.5)
    print('''88888b.  8888b. 88888b.  .d88b. 88888b.d88b.  8888b. 88888b.  
888 "88b    "88b888 "88bd88P"88b888 "888 "88b    "88b888 "88b ''')
    time.sleep(0.2)
    print('''888  888.d888888888  888888  888888  888  888.d888888888  888 
888  888888  888888  888Y88b 888888  888  888888  888888  888 ''')
    time.sleep(0.3)
    print('''888  888"Y888888888  888 "Y88888888  888  888"Y888888888  888 
                            888                              
                        Y8b d88P                              
                        "Y88P"  
-------------------------------------------------------------- 
        \n\n''')
art()

print("Difficulty Selection Panel")
def difficultySelect():
    # loop until valid answer recieved and returned
    while True:
        selectDif = input("Do you want to play with 1. Easy, 2. Medium or 3. Hard words? ")
        # Checks for both int and str input
        # Ignores extraneous data only using the first char to make comparisons
        # Returns a string stating the mode chosen
        if selectDif == '1' or selectDif[0].lower() == 'e':
            print("Easy mode selected")
            return "easy"
        elif selectDif == '2' or selectDif[0].lower() == 'm':
            print("Medium mode selected")
            return "medium"
        elif selectDif == '3' or selectDif[0].lower() == 'h':
            print("Hard mode selected")
            return "hard"
        else:
            print("Invalid answer")
            print("Reply 1 for Easy, 2 for Medium or 3 for Hard\n")
            
modeSelect = difficultySelect()
# print(modeSelect) # for testing

# compare the selected mode and assign words and lives appropriate to that catergory
if modeSelect == "easy":
    words = wordsEasy
    guessCount = easyLives
elif modeSelect == "medium":
    words = wordsMedium
    guessCount = mediumLives
elif modeSelect == "hard":
    words = wordsHard
    guessCount = hardLives
else:
    # somethings gone wrong here
    print("game is broken, fix it")
    raise Exception("Houston we have a problem")

# function that controls playAgain
# reassigns the lives
def playAgainFunc():
    playAgain = input("Do you want to play again? Y/N ")
    global gameOn
    global guessCount
    if playAgain[0].lower() == 'y':
        gameOn = True
        if modeSelect == "easy":
            guessCount = easyLives
        elif modeSelect == "medium":
            guessCount = mediumLives
        elif modeSelect == "hard":
            guessCount = hardLives
        else:
            # this shouldnt happen
            # hopefully
            print("catastrophic failure")
            raise Exception("warp core breach")
        
    else:
        print("\n\nGame over! Thanks for playing!")
        # more ascii art :)
        art()
        gameOn = False


while gameOn == True:
    #print(words)
    #print(len(words))
    randNum = r.randint(0,len(words)-1)
    #print(randNum)
    #print(words[randNum])

    # selects a random word from list corresponding to difficulty
    selectedWord = words[randNum]
    # determines length of word
    # used in loops
    lengthWord = len(selectedWord)
    print("You have %s guesses." % (guessCount))
    print("When guessing type a single letter only")
    print("The word to guess is:\n")
    print("_ " * lengthWord)
    print("")

    correctLetters = ''
    wrongLetters = ''

    # main loop
    guessed = False
    while guessed == False:
            # asks for user inout
            userGuess = input("\nEnter your guess here: ")
            # compares user guess with target word
            if userGuess in selectedWord:
                # adds the users guess to a list of "in target word"
                correctLetters = correctLetters + userGuess
                print("\nGood guess! %s is in the hidden word!" % (userGuess))
            # this bit doesnt seem to work :/
            elif userGuess == "end":
                gameOn = False
                break
            # tbf i dont think i used wrongLetters again but its nice to have available?
            else:
                wrongLetters = wrongLetters + userGuess
            # checks if all the letters in the target word have been found
            foundAll = True
            for i in range(lengthWord):
                if selectedWord[i] not in correctLetters:
                    foundAll = False
                    guessCount-=1
                    break
            if foundAll == True:
                # breaks loop
                print("Well done you have guess the word %s!" % (selectedWord))
                guessed = True
            else:
                print("\nKeep guessing!")
                print("You have %s guesses left." % (guessCount))
            # prints the guessed letters, format could be nicer    
            for i in range(len(correctLetters)):
                print(correctLetters[i])
            # no more lives, breaks loop to try again
            if guessCount == 0:
                print("FAIL")
                print("The target word was %s." % (selectedWord))
                break
                
    playAgainFunc()

empty = input()



# couldve used more functions to decompose the problem                


# Here are a few ways you could improve the code:

# Instead of having three separate tuples for the words at different difficulty levels, you could create a single dictionary with the difficulty level as the key and the words as the values. This would make it easier to select the words for a particular difficulty level.

# Instead of using global variables to keep track of the game state and the number of lives remaining, you could define a Game class that maintains this information as instance variables. This would make the code easier to read and maintain, and would also make it easier to add new features to the game.

# The difficultySelect() function can be simplified by using a while loop instead of a for loop. You can also use the in keyword to check if the user's input is in the list of valid options, rather than checking for each option individually.

# The playAgainFunc() function is redundant, as the same functionality can be achieved with a simple while loop that continues the game as long as the user wants to play.

# The art() function could be improved by using a triple-quoted string to print the ASCII art, rather than printing each line individually with a delay in between. This would make the code more concise and easier to read.

# Instead of printing the ASCII art every time the game starts, you could define a constant string at the top of the script that contains the ASCII art, and print it only once, when the game first starts.

# Here is an example of how your code could be rewritten with these changes:

# Copy code
# import random

# class Game:
#     # Dictionary of words at different difficulty levels
#     WORDS = {
#         "easy": ["cat", "dog", "book", "plane", "space"],
#         "medium": ["nintendo", "abrupt", "python", "length", "subway", "charity", "military"],
#         "hard": ["microwave", "azure", "banjo", "transcript", "bandwagon", "oxygen", "vapourise", "joking", "volunteer"]
#     }

#     # ASCII art
#     ART = """
#     --------------------------------------------------------------
#     888                                                           
#     888                                                           
#     888                                                           
#     88888b.  8888b. 88888b.  .d88b. 88888b.d88b.  8888b. 88888b.  
#     888 "88b    "88b888 "88bd88P"88b888 "888 "88b    "88b888 "88b 
#     888  888.d888888888  888888  888888  888  888.d888888888  888 
#     888  888888  888888  888Y88b 888888  888  888888  888888  888 
#     888  888"Y888888888  888 "Y88888888  888  888"Y888888888  888 
#                                 888                              
#                             Y8b d88P                              
#                             "Y88P"  
#     --------------------------------------------------------------
#     """

#     # Number of lives at different difficulty levels
#     LIVES = {
#         "easy": 8,
#         "medium": 10,