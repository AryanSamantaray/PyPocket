import random

words=["apple","banana","mango","litchi","papaya","strawberry"]
# words=["mango",]
word=random.choice(words)

hangman = [
    """
     -----
     |   |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
    =========
    """
]
print("welcome to hangman")
print("HINT: The word is a fruit.")


guessed=[]
wrong_attempts=0
max_attempts=5

while True:

    while wrong_attempts < max_attempts:
        guess=input("Guess the letter:").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("enter a single letter")
            continue

        if guess in guessed:
            print("already guessed that")
            continue

        guessed.append(guess)

        if guess in word:
            print("correct")
        else :
            wrong_attempts+=1
            print("wrong")
            print(hangman[wrong_attempts])

        print("failed attempts:", wrong_attempts, "/", max_attempts)

        shown =""
        for letter in word:
            if letter in guessed:
                shown+=letter+""
            else:
                shown=shown+"_"
        print(shown)
        print("Letters guessed so far:", guessed)

        if "_" not in shown:
                print("you won!")
                break

    if wrong_attempts == max_attempts:
        print("you lost! the word was", word)

    again = input("play again? (y/n): ").lower()
    if again != "y":
        print("thanks for playing")
        break

