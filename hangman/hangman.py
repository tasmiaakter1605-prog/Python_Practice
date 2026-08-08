import string
import random
import wordlist
hangman={1:   "     0       ",
         2:   "     0     \n"  
              "     |       ",
        3:    "     0     \n"
              "    /|       ",
        4:    "      0     \n"
             "     /|\\     ",
        5:   "      0     \n"
             "     /|\\   \n"
             "     /       ",
        6:   "      0     \n"
             "     /|\\   \n"
             "     / \\     "
          }

guesses=0
is_running=True
answer=random.choice(wordlist.words)

def Play():
     play=input("Do you wanna play again? (y/n) :").lower()
     global is_running,guesses,answer
     if play=="n":
        is_running=False
     elif play=="y":
        guesses=0
        answer=random.choice(wordlist.words)
     else:
        print("Invalid input")





while is_running:
    
    guess=['_','_','_','_','_','_']
    inpt=input("guess the word : ")
    guesses+=1
    for i in range(0,6):
        if(inpt[i]==answer[i]):
            guess[i]=inpt[i]
    if "".join(guess)==answer:
        print(f"You guessed the correct answer {answer}")
        Play()
    else:
        if guesses>=6:
            print(f"{hangman[6]}")
            print(f"You failed!Correct word {answer}")
            Play()
        else:
            print(f"Word : ",end="")
            for i in guess:
                print(f"{i}",end=" ")
            print()
            print(f"=============")
            print(f"{hangman[guesses]}")
            print(f"=============")
