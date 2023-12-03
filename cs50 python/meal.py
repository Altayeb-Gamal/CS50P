def main():
    time = input("What time is it? ")
    hours, minutes = time.split(":")

    if convert(time) >= 7.0 and convert(time) <= 8.0:
        print("breakfast time")
    elif convert(time) >= 12.0 and convert(time) <= 13.0:
        print("lunch time")
    elif convert(time) >= 18.0 and convert(time) <= 19.0:
        print("dinner time")


def convert(t):
    hours, minutes = t.split(":")
    converted_time = float(hours) + (float(minutes) / 60)
    return converted_time


if __name__ == "__main__":
    main()
