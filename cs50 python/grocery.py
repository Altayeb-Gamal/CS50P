grocery = {}


def main():
    while True:
        try:
            item = input().lower()
            grocery = add(item)
        except EOFError:
            break
        except KeyError:
            pass
    print_list()


def print_list():
    my_list = list(grocery.keys())
    my_list.sort()
    for i in my_list:
        print(grocery[i], i.upper())


def add(item):
    if not (item in grocery):
        grocery[item] = 0
    grocery[item] += 1
    return grocery


main()
