import re

def main():
    s = input("Input: ")
    print(count(s))


def count(s):
    count = 0
    count += len(re.findall(r"(^| )(U|u)m+( |,?|\.+|\n|$)*", s))
    return count


if __name__ == "__main__":
    main()