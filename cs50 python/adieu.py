import inflect
p = inflect.engine()

def main():
    names = []
    while True:
        try:
            names.append(input("Name: "))
        except EOFError:
            break
    joined_names = p.join(names)
    print("Adieu, adieu, to", joined_names)



if __name__ == "__main__":
    main()