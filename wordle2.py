import random

fp = open("wordle_words", "r") # Creates wordbank
wordBank = "".join(fp.readlines())
wordBank = wordBank.split("\n")
fp.close()

def chooseWord(): # Chooses random word from wordbank
    for i in range(random.randint(0, 9111)):
        targetWord = wordBank[i]
    return targetWord

def guess(guessWord, targetWord): # Determines correct letters in guess
    if guessWord == "exit":
        print("Exited, the word was", targetWord)
        return True
    elif guessWord != targetWord:
        correct = ""
        for i, char in enumerate(guessWord):
            if char == targetWord[i]:
                correct += "\033[0;30;42m" + guessWord[i] + "\033[0;30;47m"
            elif char in targetWord:
                correct += "\033[0;30;43m" + guessWord[i] + "\033[0;30;47m"
            else:
                correct += "\033[0;30;47m" + guessWord[i]
        print(correct)
    elif guessWord == targetWord:
        print("\033[0;30;42m", guessWord, "\033[0;30;47m")
        print("\033[0;30;42m you won good job now piss off", "\033[0;30;47m")
        return True

def wordle(): # Plays wordle
    targetWord = chooseWord()
    guessCount = 0
    done = False
    while not done:
        guessWord = input("Enter guess: ")
        if guessWord not in wordBank:
            print("Not in dictionary")
            continue
        done = guess(guessWord, targetWord)
        if guessCount == 6:
            print("L, word was", targetWord)
            done = True
        guessCount += 1
    playAgain = input("Do you want to play again? (Y/n): ")
    if playAgain == "Y" or playAgain == "y":
        wordle()
