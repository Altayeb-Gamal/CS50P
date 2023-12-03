import sys


def main():

    if validate_cla():
        try:
            file = open(sys.argv[1], "r")
            lines = file.readlines()
            line_count = count_lines(lines)
            print(line_count)
        except FileNotFoundError:
            sys.exit("File does not exist")


def count_lines(lines):
    line_count = 0
    for line in lines:
        if not line.lstrip().startswith("#") and not line.isspace():
            line_count += 1
    return line_count


def validate_cla():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line argument")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")
    else:
        return True


if __name__ == "__main__":
    main()
