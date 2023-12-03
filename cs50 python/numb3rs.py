import re


def main():
    ip = input("IPv4 Address: ")
    print(validate(ip))


def validate(ip):
    if re.search(r"^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$", ip):
        num_list = ip.split(".")
        for num in num_list:
            if int(num) >= 0 and int(num) <= 255:
                continue
            else:
                return "False"
        return "True"
    else:
        return "False"

if __name__ == "__main__":
    main()