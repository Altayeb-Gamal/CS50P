def main():
    word = input("Input: ")
    short_word = short(word)
    print(short_word)



def short(word):
    new_word = ""
    for w in word:
        if w.lower() != "a" and w.lower() != "o" and w.lower() != "u" and w.lower() != "i" and w.lower() != "e":
            new_word += w

    return new_word


if __name__ == "__main__":
    main()