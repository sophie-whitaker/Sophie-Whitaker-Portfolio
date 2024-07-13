# -*- coding: utf-8 -*-
"""Sophie Whitaker Python Challenge.ipynb

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

# label months with a number, january to decemeber = 1 to 12
# label days with a number, sunday to saturday = 1 to 7

def day_year_starts_on(end):
    day_year_starts_on_val = 2
    day_count = 2

    for year in range(1900, end):
        is_leap_year = False
        if year % 4 == 0:
          if year % 100 != 0 or year % 400 == 0:
            is_leap_year = True

        for month in range(1, 12 + 1):
            days = 30
            if month in {1, 3, 5, 7, 8, 10, 12}:
                days = 31
            elif month == 2:
                days = 29 if is_leap_year else 28

            day_count += days
        print("day_count:", day_count)

    return day_count % 7

print("The day the year 1901 starts on:", day_year_starts_on(1901))

def sundays_on_first_of_month(start, end):
    day_month_starts_on = 3
    sundays_count = 0

    for year in range(start, end + 1):
        is_leap_year = False
        if year % 4 == 0:
          if year % 100 != 0 or year % 400 == 0:
            is_leap_year = True

        for month in range(1, 12 + 1):
            days = 30
            if month in {1, 3, 5, 7, 8, 10, 12}:
                days = 31
            elif month == 2:
                days = 29 if is_leap_year else 28

            day_month_starts_on = (day_month_starts_on + days) % 7

            if day_month_starts_on == 1:
                sundays_count += 1

    return sundays_count

start = 1901
end = 2000

answer = sundays_on_first_of_month(start, end)

print("How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?", answer)

"""Provide an updated or alternative script to calculate the number of Tuesdays that fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)."""

# label months with a number, january to decemeber = 1 to 12
# label days with a number, sunday to saturday = 1 to 7

def tuesdays_on_first_of_month(start, end):
    day_month_starts_on = 3
    tuesdays_count = 1

    for year in range(start, end + 1):
        is_leap_year = False
        if year % 4 == 0:
          if year % 100 != 0 or year % 400 == 0:
            is_leap_year = True

        for month in range(1, 12 + 1):
            days = 30
            if month in {1, 3, 5, 7, 8, 10, 12}:
                days = 31
            elif month == 2:
                days = 29 if is_leap_year else 28

            day_month_starts_on = (day_month_starts_on + days) % 7

            if day_month_starts_on == 3:
                tuesdays_count += 1

    return tuesdays_count

start = 1901
end = 2000

answer = tuesdays_on_first_of_month(start, end)

print("How many Tuesdays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?", answer)
