def main():
    due = 50
    print("Amount Due:", due)
    while (due > 0):
        coins = int(input("Insert coins: "))
        if (coins == 25 or coins == 10 or coins == 5):
            due = calculate(coins, due)
            if due > 0:
                print("Amount Due:", due)
        else:
             print("Amount Due:", due)
             coins = int(input("Insert coins: "))
        if due <= 0:
            change(coins, due)




def calculate(coins, due):
    if coins == 25:
        due -= 25
    elif coins == 10:
        due -= 10
    elif coins == 5:
        due -= 5
    return due

def change(coins, due):
    print("Change Owed:", abs(due))




main()