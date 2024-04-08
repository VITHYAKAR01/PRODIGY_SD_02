import random

def main():
    MIN = 1
    MAX = 100
    guess = 0
    guesses = 0
    answer = random.randint(MIN, MAX)

    while guess != answer:
        guess = int(input("Enter a Guess: "))
        if guess > answer:
            print("Guess is Too high!")
        elif guess < answer:
            print("Guess is Too low!")
        else:
            print("CORRECT YOU WON!")
        guesses += 1
    print("**********************")
    print("Correct Answer is:", answer)
    print("Number Of Guess You have Taken is:", guesses)
    print("**********************")

if __name__ == "__main__":
    main()

