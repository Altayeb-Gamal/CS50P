import random


def main():
    while True:
        try:
            n = int(input("Level: "))
            if n >= 1:
                break
            else:
                while n < 1:
                    n = int(input("Level: "))
        except ValueError:
            pass
    rn = random.randint(1, n)
    while True:
        try:
            guess = int(input("Guess: "))
            if guess > 0:
                break
            else:
                continue
        except ValueError:
            pass
    while True:
        if guess == rn:
            print("Just right!")
            break
        elif guess < rn:
            print("Too small!")
            guess = int(input("Guess: "))
        elif guess > rn:
            print("Too large!")
            guess = int(input("Guess: "))


if __name__ == "__main__":
    main()
