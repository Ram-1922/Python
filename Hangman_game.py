# hangman game

import random
from module.wordslist import words
# words = ("apple","banana","pineapple","guava","mango")

hangman ={
    0:(" ",
       " ",
       " "),
    1:(" O",
       "  ",
       "  "),
    2:(" O",
       " |",
       "  "),
    3:(" O",
       "/|",
       "  "),
    4:(" O",
       "/|\\",
       "  "),
    5:(" O",
       "/|\\",
       "/ "),
    6:(" O",
       "/|\\",
       "/ \\ "),
}

def display_man(wrong_guesses):
    for i in hangman[wrong_guesses]:
        print(i)
def display_hint(hint):
    print(" ".join(hint))
    print("\n")
def display_answer(answer):
    print(" ".join(answer))

def main():
    answer=random.choice(words)
    hint = ['_']*len(answer)
    wrong_guesses=0
    guessed_letter=set()
    is_running=True
    while is_running:
        display_man(wrong_guesses)
        print("----------------------------------")
        display_hint(hint)
        guess = input("Enter a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input")
            continue 
        if guess in guessed_letter:
            print(f"{guess} is already guessed")
        elif guess in answer:
            for i in range(len(answer)):
                if guess == answer[i]:
                    hint[i]=guess
        else:
            wrong_guesses+=1
        guessed_letter.add(guess)
        if '_' not in hint:
            display_man(wrong_guesses)
            print("----------------------------------")
            display_hint(hint)
            print("You Win 🥳🎊")
            is_running=False
        elif wrong_guesses==6:
            display_man(wrong_guesses)
            print("----------------------------------")
            display_answer(answer)
            print("You Lose 😔")
            is_running=False

if __name__ == "__main__":
    main()