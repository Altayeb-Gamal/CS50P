import random


def main():
    lvl = get_level()
    counter = 0
    score = 0
    for _ in range(10):
        x, y = generate_two_ints(lvl)
        print(f"{x} + {y} = ", end="")
        try:
            answer = int(input())
        except ValueError:
            print("EEE")
            counter += 1
            continue
        if answer == x + y:
            score += 1
            continue
        while answer != x + y:
            print("EEE")
            counter += 1
            try:
                print(f"{x} + {y} = ", end="")
                answer = int(input())
            except  ValueError:
                print("EEE")
                counter += 1
                pass
            if counter == 3:
                print(f"{x} + {y} = {x + y}")
                break
    print(score)


def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n in [1, 2, 3]:
                break
        except:
            pass
    return n


def generate_two_ints(lvl):
    x, y = 0, 0
    if lvl == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif lvl == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    elif lvl == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    
    return x, y
if __name__ == "__main__":
    main()
