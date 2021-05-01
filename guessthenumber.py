import random

easylevel = 10
hardlevel = 5

def check_ans(ans,guess,turns):
    if guess > ans:
        print("Too high! Guess a lower number.")
        return turns-1
    elif guess < ans:
        print("Too low! Guess a higher number!")
        return turns-1
    else:
        print("Shot! You got the correct guess..")

def difficulty():
    level = input("Choose the difficulty level (easy/hard) : ")
    if level == "easy":
        return easylevel
    elif level == "hard":
        return hardlevel
    else:
        print("type easy/hard")

def main():
    print("********************************")
    print("* Welcome to the guessing game *")
    print("********************************")
    print("help me to guess a number between 1 to 100 - ")
    ans = random.randint(1, 100)
    turns = difficulty()
    guess =0
    while guess != ans :
        print(f"{turns} left!")
        guess = int(input("Guess a number:"))

        turns =check_ans(ans, guess, turns)
        if turns == 0:
            print("Oops! You lose!")
        elif guess != ans:
            print("Guess Again!")
main()
