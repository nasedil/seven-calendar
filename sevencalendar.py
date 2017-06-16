"""
Converts datetime to 777-calendar format.

The format is the following.  It depends on birth date.  In the following examples we use as example the following birth date: 1988-06-23.  Here are the rules:
 * Date consists of four or three parts:  year, meriod, week and day.  Sometimes week is missing.
 * Date is written as following:  year.meriod.week.day or year.meriod.day (like 25.6.6.4 or 29.0.9).
 * Year shows an age of a person.  So for a date which is slightly after birthday the year value would be the same as age.  For example, date 1995-07-09 would have year value 7 in 777-calendar.
 * Meriod is a kind of month that in general case contains 7 weeks of 7 days.  There are special cases for 21 or 28 days around the reference birthday (mostly 21 days, but once in a while 28).  So birthday and 7 days after birthday are of meriod 0, and also days till the rest of the week.  That means meriod 0 may contain 8 to 14 days.  Then, days before birthday are of meriod 8, which may have from 8 to 14 days.  The remaining 343 days between meriod 0 and meriod 8 in a year are regular meriods, each having 49 days, and named from 1 to 7.
 * Regular meriods have weeks, named from 1 to 7.  In special meriods there are no weeks.
 * Day in regular meriod is the same as days of the week in the traditional calendar:  Monday is day 1 and Sunday is day 7.  In meriod 8 days are counted from 1, in meriod 0 -- from 0.
"""

import datetime

class SevenDate(object):
    """777-calendar date object.
    """

    def __init__(self, birth_date, year, meriod, week, day):
        """Init with values."""
        self.birth_date = birth_date
        self.year = year
        self.meriod = meriod
        self.week = week
        self.day = day

    def __str__(self):
        """Convert to string."""
        if self.week is None:
            value = '{}.{}.{}'.format(self.year,
                                      self.meriod,
                                      self.day)
        else:
            value = '{}.{}.{}.{}'.format(self.year,
                                         self.meriod,
                                         self.week,
                                         self.day)
        return value

def seven_date(input_date, birth_date):
    """Return date in 777-calendar format for a given date and birthday.
    """
    # We calculate year.  If input date is after birthday in its year, then it's difference between input year and birth date year.  Otherwise it's the difference in years minus one.
    year = input_date.year - birth_date.year
    if ((input_date.month < birth_date.month) or
        (input_date.month == birth_date.month and input_date.day < birth_date.day)):
        year -= 1
    # Now we calculate meriod, week and day.  We create a reference date year.0.0 which is a last passed birthday.  And then we follow meriods from birthday until we find the one which includes input date.
    reference_date = datetime.date(birth_date.year+year, birth_date.month, birth_date.day)
    birthday_weekday = reference_date.isoweekday()
    zero_meriod_days = 1 + 7 + 7 - birthday_weekday
    meriod = 0
    week = None
    if (reference_date + datetime.timedelta(days=zero_meriod_days) > input_date):
        day = (input_date - reference_date).days
    else:
        reference_date += datetime.timedelta(days=zero_meriod_days)
        meriod = 1
        while reference_date + datetime.timedelta(days=49) <= input_date:
            reference_date += datetime.timedelta(days=49)
            meriod += 1
        if meriod < 8:
            week = (input_date - reference_date).days // 7 + 1
            day = input_date.isoweekday()
        else:
            day = (input_date - reference_date).days + 1
    # Now create 777-calendar object.
    seven_date = SevenDate(birth_date, year, meriod, week, day)
    return seven_date
