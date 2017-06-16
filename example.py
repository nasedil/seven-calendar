import datetime

import sevencalendar

def main():
    # A reference birth date would be the 23rd of June 1988.
    birth_date = datetime.date(1988, 6, 23)
    # Let's print all dates in one year in both calendars.
    some_date = datetime.date(2016, 6, 23)
    for i in range(365):
        print('{} -> {}'.format(some_date, sevencalendar.seven_date(some_date, birth_date)))
        some_date += datetime.timedelta(days=1)

if __name__ == '__main__':
    main()
