fp = open("wordle_words", "r")
import random
words = " ".join(fp.readlines())
words = words.split("\n")
all_words = []
for word in words:
    word = word.strip()
    all_words.append(word)
for i in range(random.randint(0, 9111)):
    word = all_words[i]
fp.close()
count = 0
def wordle(guess):
    if count == 6:
        return "you lose suck it"
    if guess == "exit":
        print("penis, the word was", word)
    elif guess not in all_words:
        print("Not in dictionary")
        guess = input("Input word: ")
        return wordle(guess)
    elif guess != word:
        new_guess = ""
        for i, char in enumerate(guess):
            if char == word[i]:
                new_guess += "\033[0;30;42m" + guess[i] + "\033[0;30;47m"
            elif char in word:
                new_guess += "\033[0;30;43m" + guess[i] + "\033[0;30;47m"
            else:
                new_guess += "\033[0;30;47m" + guess[i]
        print(new_guess)
        count += 1
        guess = input("\033[0;30;47m Input word: ")
        return wordle(guess)
    elif guess == word:
        print("\033[0;30;42m", guess, "\033[0;30;47m")
        print("\033[0;30;42m you won good job now piss off", "\033[0;30;47m")
        play = input("Play again? y/n: ")
        if play == "y" or play == "yes":
            guess = input("Input word: ")
            for i in range(random.randint(0, 9111)):
                word = all_words[i]
                count = 0
        else:
            return "penis"
