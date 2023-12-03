import sys
import csv
from tabulate import tabulate


def main():
    table = []
    if test_cla():
        try:
            file = open(sys.argv[1], "r")
            reader = csv.reader(file)
            for row in reader:
                table.append(row)
        except FileNotFoundError:
            sys.exit("File does not exist")
        else:
            print(tabulate(table, headers="firstrow", tablefmt="grid"))


def test_cla():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")
    else:
        return True


if __name__ == "__main__":
    main()
