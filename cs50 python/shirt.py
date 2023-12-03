import sys
from os.path import splitext
from PIL import Image, ImageOps


def main():
    if test_cla():
        try:
            image_file = Image.open(sys.argv[1])
        except FileNotFoundError:
            sys.exit("input does not exist")
        else:
            shirt = image.open("shirt.png")
            size = shirt.size
            muppet = ImageOps.fit(image_file, size)
            muppet.paste(shirt, shirt)
            muppet.save(sys.argv[2])


def test_cla():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    file1 = splitext(sys.argv[1])
    file2 = splitext(sys.argv[2])
    if not file1[1] in [".jpeg", ".png", ".jpg"]:
        sys.exit("Invalid input")
    if not file2[1] in [".jpeg", ".png", ".jpg"]:
        sys.exit("Invalid output")
    if file1[1] != file2[1]:
        sys.exit("Input and output have different extensions")
    else:
        return True

if __name__ == "__main__":
    main()