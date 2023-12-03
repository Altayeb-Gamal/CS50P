import csv
import random
import sys


def main():
    name = (input("What is you'r name: ")).title()
    print(f"Hello {name}, ", end="")
    lvl = input(
        "Which level would you like to play (Hard[5 qoutes, 1 try], Medium[5 qoutes, 3 tries], or Easy[5 qoutes, 5 tries]): "
    ).lower()

    qoutes = list_maker()
    counter = choose_dif(lvl)
    tryies = get_lvl(lvl)
    score = 0
    print(f"You have {counter} qoutes to guess from and {tryies} tries, Good Luck!")
    while counter > 0:
        print(f"You have {counter} qoutes left and {tryies} tries left")
        ques = generate_qoute(qoutes, counter)
        print("Qoute:", ques)
        #for demo purposes
        print(qoutes[ques])
        answer = input("movie: ")
        while not answer.lower() == qoutes[ques].lower():
            if tryies > 0:
                print("Try again")
                answer = input("movie: ")
                tryies -= 1
        if test_answer(answer, ques, qoutes):
            score += 1
            del qoutes[ques]
        counter -= 1
    print(f"Your score is {score}")
    check_score(score, lvl)


def check_score(score, lvl):
    if score == choose_dif(lvl):
        return("Well done, perfect score")


def get_lvl(lvl):
    if lvl == "hard":
        return 1
    elif lvl == "medium":
        return 3
    elif lvl == "easy":
        return 5
    else:
        sys.exit("Invalid level")

def generate_qoute(qoutes, counter):
    if counter > 0:
        ques = random.choice(list(qoutes.keys()))
        return ques
    else:
        sys.exit("Game Over")


def choose_dif(lvl):
    if lvl == "hard":
        return 5
    elif lvl == "medium":
        return 5
    elif lvl == "easy":
        return 5
    else:
        sys.exit("Invalid level")


def list_maker():
    with open("qoutes.csv") as file:
        reader = csv.DictReader(file)
        qoutes = {}
        for row in reader:
            qoutes[row["qoute"]] = row["movie"]
    return qoutes


def test_answer(answer, ques, qoutes):
    if answer.lower() == (qoutes[ques]).lower():
        print("Correct")
        return True
    else:
        print(f"Wrong, answer is {qoutes[ques]}")
        return False


if __name__ == "__main__":
    main()
