import re
import sys


def main():
    time = convert(input("Hours: "))
    print(time)


def convert(t):
    is_correct = re.search(
        r"^([0-9][0-2]?):?([0-5][0-9])* (AM|PM)? to ([0-9][0-2]?):?([0-5][0-9])? (AM|PM)?$",
        t,
    )
    if is_correct:
        slices = is_correct.groups()
        if int(slices[0]) > 12 or int(slices[3]) > 12:
            raise ValueError
        start_time = f24(slices[0], slices[1], slices[2])
        end_time = f24(slices[3], slices[4], slices[5])
        return f"{start_time} to {end_time}"
    else:
        raise ValueError


def f24(h, m, am_pm):
    if am_pm == "PM":
        if int(h) == 12:
            h = 12
        else:
            h = int(h) + 12
    else:
        if int(h) == 12:
            h = 0
        else:
            h = int(h)
    if m == None:
        m = "00"
    else:
        m = m
    new_hour = f"{h:02}"
    new_minute = f"{m:02}"
    return f"{new_hour}:{new_minute}"


if __name__ == "__main__":
    main()
