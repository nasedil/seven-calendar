# -*- coding: UTF-8 -*-

import datetime

import sevencal.sevencalendar as sevencalendar

def main():
    # A reference birth date would be the 23rd of June 1988.
    birth_date = datetime.date(1988, 6, 23)
    # Let's print all dates in one year in both calendars.
    some_date = datetime.date(2016, 6, 23)
    print("All days for a year:")
    for i in range(365):
        seven_date = sevencalendar.SevenDate.from_date(some_date, birth_date)
        print('{} -> {} -> {}'.format(some_date, seven_date, seven_date.to_date()))
        some_date += datetime.timedelta(days=1)
    # Now let's print all first days of a meriod for all meriods in all years up to 34.
    print('All first days of meriods:')
    d = sevencalendar.SevenDate(birth_date, 0, 1, 1, 1)
    for year in range(35):
        for meriod in range(1, 8):
            d.year = year
            d.meriod = meriod
            print('{} -> {}'.format(d, d.to_date()))
    # And print number of days for each meriod of the year 30.
    for meriod in range(0, 9):
        print('{} -> {}'.format(meriod, sevencalendar.SevenDate.days_in_meriod(30, meriod)))

if __name__ == '__main__':
    main()
