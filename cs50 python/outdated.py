months = {
"January" : "01",
"February" : "02",
"March" : "03",
"April" : "04",
"May" : "05",
"June" : "06",
"July" : "07",
"August" : "08",
"September" : "09",
"October" : "10",
"November" : "11",
"December" : "12"
}


def main():
    year, month, day = get_sort_date("Date: ")
    print(year,month, day, sep = "-")

def get_sort_date(prompt):

    while True:
        date = (input(prompt)).strip()
        if "/"in date:
            if not date[0].isalpha():
                month, day, year = date.split("/")
                if (int(month) > 12 or int(day) > 31 or int(year) < 1000):
                    date = (input(prompt)).strip()
                    continue
                else:
                    if int(day) < 10:
                        day = "0" + day
                    if int(month) < 10:
                        month = "0" + month
                    return year.strip(), month.strip(), day.strip()
        elif "," in date:
            if not date[0].isnumeric():    
                month_day , year = date.split(",")
                month, day = month_day.split(" ")
                if (int(day) > 31) or not(month in months) or int(year) < 1000:
                    date = (input(prompt)).strip()
                    continue
                else:
                    month = months[month]
                    if int(day) < 10:
                        day = "0" + day
                    return year.strip(), month, day


main()



