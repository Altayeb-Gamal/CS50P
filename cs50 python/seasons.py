import datetime
import inflect
import re


def main():
    date = input("Date of Birth: ")
    if isvalid_date(date):
        year, month, day = date.split("-")
        date = datetime.date(int(year), int(month), int(day))
        age_mins = calcualte_mins(date)
        age_min_words = num_to_words(age_mins)
        print(age_min_words)


def calcualte_mins(date):
    today = datetime.date.today()
    age_years = today.year - date.year
    age_months = today.month - date.month
    age_days = today.day - date.day
    age_days += age_months * 30 + (age_years * 365)
    age_mins = age_days * 24 * 60
    return age_mins


def isvalid_date(date):
    try:
        if re.match(r"^\d{4}-\d{2}-\d{2}$", date):
            return True
        else:
            raise ValueError
    except (ValueError):
        print("ValueError: Invalid date")
        return False
    except TypeError:
        print("TypeError: Invalid date")
        return False

def num_to_words(num):
    i = inflect.engine()
    return i.number_to_words(num)


if __name__ == "__main__":
    main()
