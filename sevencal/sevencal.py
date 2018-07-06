#!/usr/bin/python
from argparse import ArgumentDefaultsHelpFormatter
from argparse import ArgumentParser
import datetime

import sevencal.sevencalendar as sevencalendar

def date_type(s):
    """Convert string to datetime.
    """
    return datetime.datetime.strptime(s, '%Y-%m-%d').date()

def main():
    """Helper command-line tool for sever-calendar.."""
    parser = ArgumentParser(description='777-calendar converter tool',
                            formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument('-d', '--date',
                        type=date_type,
                        default=datetime.datetime.now(),
                        help='The date to convert (in format yyyy-mm-dd)')
    parser.add_argument('-b', '--birth-date',
                        type=date_type,
                        default=datetime.date(1988, 6, 23),
                        help='The reference (birth) date of the calendar (in format yyyy-mm-dd)')
    args = parser.parse_args()
    print(sevencalendar.SevenDate.from_date(args.date, birth_date=args.birth_date))

if __name__ == '__main__':
    main()
