def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(plate):
    if not (2 <= len(plate) <= 6):
        return False
    if plate[0] == "0" :
        return False
    for p in plate:
        if p in [" ", ".", "," ]:
            return False
    if  plate[0].isnumeric() or plate[1].isnumeric():
            return False
    half = int(len(plate) / 2)
    if len(plate) > 2 and plate[half].isnumeric():
        if int(plate[half]) == 0:
            return False
    for i, p in enumerate(plate):
        if p.isnumeric():
            if not plate[i:].isnumeric():
                return False
    return True

if __name__ == "__main__":
    main()