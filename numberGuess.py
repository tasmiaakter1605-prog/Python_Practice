import random
answer=random.randint(1,200)
guesses=0
is_running=True

while is_running:
    guess=int(input("Guess the number :"))
    guesses+=1
    if guess==answer:
        print(f"Your guess {guess} is correct ! Guesses={guesses}")
        play=input("Do you wanna play again?(y/n) :").lower()
        if play=="n":
            is_running=False
        elif play=="y":
            guesses=0
            answer=random.randint(1,200)
        else:
            print("Invalid input")

    elif guess>answer:
        print(f"Too high!")
    else:
        print(f"Too Low!")