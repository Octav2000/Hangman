import HangmanDrawings as HD
import random as r

mode = 0
mode = input('''mode = 1 => 1-player mode (the word will be chosen random from a list of words)
mode = 2 => 2-player mode (the word will be written by player 1 and player 2 has to guess it\nmode = ''')

wrong = 0  # how many times the second player guessed wrong
word = ""
listOfWords = ["masina", "casa", "catacombe", "bicicleta",
               "birou", "hangman", "strada", "pieton", "avion", "continent"]
player = 1
lettersGuessed = []
wordLetters = []
if(int(mode) == 2):
    word = input("Player 1\nWhat ward should the player 2 guess: ").upper()
    print(chr(27) + "[2J")
    player = 2
else:
    word = listOfWords[r.randint(0, len(listOfWords))].upper()

for i in range(len(word)):
    wordLetters.append("-")
# if the second player guessed wrong 6 times or there still are letters to be guessed


def checkWinner():
    if wrong == 6:
        return 0
    for i in wordLetters:
        if i == "-":
            return 1
    return 2


def letterGuessedorNot(letter):
    ok = 0
    for i in range(len(word)):
        if word[i] == letter:
            wordLetters[i] = letter
            lettersGuessed.append(letter)
            ok = 1
    if ok == 1:
        return 1  # if it was a guess
    else:
        global wrong
        wrong += 1
        lettersGuessed.append(letter)
        return 0  # if it wasn't a guess


def whatToDraw():
    if wrong == 0:
        HD.initialize()
    elif wrong == 1:
        HD.head()
    elif wrong == 2:
        HD.body()
    elif wrong == 3:
        HD.leftArm()
    elif wrong == 4:
        HD.rightArm()
    elif wrong == 5:
        HD.leftLeg()
    else:
        HD.rightLeg()


def letters():
    global lettersGuessed
    lettersGuessed = list(dict.fromkeys(lettersGuessed))
    print("Letters guessed: ", end="")
    print(lettersGuessed)
    print("The remaining letters: ", end="")
    print(wordLetters)


while True:
    if checkWinner() == 0:
        print("Player 2 lost")
        break
    elif checkWinner() == 2:
        print("Player 2 won")
        break
    else:
        guess = input("Player 2\nThe letter you want to guess: ").upper()
        letterGuessedorNot(guess)
        whatToDraw()
        letters()
