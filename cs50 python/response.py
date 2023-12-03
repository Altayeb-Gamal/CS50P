import validators


def main():
    email = input("What's your email: ")
    print(is_valid(email))


def is_valid(email):
    if validators.email(email):
        return"Valid"
    else:
        return"Invalid"

if __name__ == "__main__":
    main()