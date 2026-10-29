# Hangman

A simple command-line Hangman game in Python. Guess the fruit one letter at a time before the hangman is fully drawn.

## Features

- Random fruit word each round
- ASCII hangman drawing that builds with every wrong guess
- Input validation (single letters only, no repeats)
- Play again option

## Requirements

- Python 3.x (no extra libraries needed)

## How to Run

```bash
python hangman.py
```

## How to Play

1. The game picks a random fruit and shows it as blanks: `_ _ _ _ _`
2. Type one letter per turn
3. Right guess: the letter is revealed in the word
4. Wrong guess: a part of the hangman is drawn and your failed attempts go up
5. Win by revealing the whole word
6. Lose if the hangman is fully drawn (5 failed attempts)

## Customize

- Add more words: edit the `words` list at the top of the file
- Change difficulty: add or remove pictures in the `hangman` list (max attempts follows the list length automatically)

## Author

Aryan Samantaray