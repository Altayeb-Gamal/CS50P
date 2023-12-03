def main():
    greeting = input("Greeting: ").lower().strip()
    value = greet(greeting)
    print(value)


def greet(greeting):
    greeting = greeting.lower().strip()
    words = greeting.split(",")
    first = words[0]
    if first == "hello":
        value = "$0"
    elif greeting[0] == "h":
        value = "$20"
    else:
        value = "$100"
    return value


if __name__ == "__main__":
    main()
