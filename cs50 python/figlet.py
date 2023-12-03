from pyfiglet import Figlet
import sys
import random


def main():
    figlet = Figlet()
    fonts = figlet.getFonts()
    if len(sys.argv) == 1:
        font = random.choice(fonts)
    elif len(sys.argv) == 3:
        if sys.argv[1] in ["-f", "--font"]:
            if sys.argv[2] in fonts:
                font = sys.argv[2]
            else:
                sys.exit("Invalid usage")
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")
    text = input()
    figlet.setFont(font=font)
    print(figlet.renderText(text))


if __name__ == "__main__":
    main()
