#!/usr/bin/python
import datetime

import sevencal.sevencalendar as sevencalendar

def main():
    """Helper tool for sever-calendar, prints date of today."""
    today = datetime.date.today()
    print(sevencalendar.SevenDate.from_date(today))

if __name__ == '__main__':
    main()