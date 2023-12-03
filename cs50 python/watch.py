import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    if groubs := re.search(r"https?://(?:www.)?youtube.com/embed/(\w+)", s):
        return "https://youtu.be/" + groubs.group(1)
    else:
        return None

if __name__ == "__main__":
    main()