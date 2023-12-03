import sys
import csv


def main():
    data = []
    processed_data = []
    if test_cla():
        try:
            with open(sys.argv[1], "r") as file1:
                reader = csv.reader(file1)
                data = list(reader)
        except FileNotFoundError:
            sys.exit("Could not read {}".format(sys.argv[1]))
        else:
            for i, row in enumerate(data):
                if i == 0:
                    continue
                else:
                    last, first = row[0].split(",")
                    processed_data.append({"first": first.lstrip(), "last": last, "house": row[1]})         
            with open(sys.argv[2], "w") as file2:
                writer = csv.DictWriter(file2, fieldnames=["first","last", "house"])
                writer.writeheader()
                for row in processed_data:
                    writer.writerow(row)


def test_cla():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Could not read {}".format(sys.argv[1]))
    elif not sys.argv[2].endswith(".csv"):
        sys.exit("Could not read {}".format(sys.argv[2]))
    else:
        return True


if __name__ == "__main__":
    main()
