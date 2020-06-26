# -*- coding: UTF-8 -*-

"""
Converts datetime to 777-calendar format.

The format is the following.  It depends on birth date.  In the following examples we use as example the following birth date: 1988-06-23.  Here are the rules:
 * Date consists of four or three parts:  year, meriod, week and day.  Sometimes week is missing.
 * Date is written as following:  year.meriod.week.day or year.meriod.day (like 25.6.6.4 or 29.0.9).
 * Year shows an age of a person.  So for a date which is slightly after birthday the year value would be the same as age.  For example, date 1995-07-09 would have year value 7 in 777-calendar.
 * Meriod is a kind of month that in general case contains 7 weeks of 7 days.  There are special cases for 21 or 28 days around the reference birthday (mostly 21 days, but once in a while 28).  So birthday and 7 days after birthday are of meriod 0, and also days till the rest of the week.  That means meriod 0 may contain 8 to 14 days.  Then, days before birthday are of meriod 8, which may have from 7 to 20 days.  The remaining 343 days between meriod 0 and meriod 8 in a year are regular meriods, each having 49 days, and named from 1 to 7.
 * Regular meriods have weeks, named from 1 to 7.  In special meriods there are no weeks.
 * Day in regular meriod is the same as days of the week in the traditional calendar:  Monday is day 1 and Sunday is day 7.  In meriod 8 days are counted from 1, in meriod 0 -- from 0.
 * Birthday is the first day of the year (1995-06-23 has date 7.0.0).
 * Dates before birth have negative years: 1985-07-20 is −3.1.3.5.
 * Not only a birth date can be used as a reference point, but any other date of some importance.  That way, we can represent some date in several ways, one relative to a birth day, and one relative to some other day (say, day of death, or some important life event).
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

    def __repr__(self):
        """Return string representation of the object."""
        return '{} -> {}-{}-{}-{}'.format(self.birth_date, self.year, self.meriod, self.week, self.day)

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

    @staticmethod
    def from_date(input_date, birth_date=datetime.date(1988, 6, 23)):
        """Return date in 777-calendar format for a given date and birthday.
        """
        # We calculate year.  If input date is after birthday in its year, then it's difference between input year and birth date year.  Otherwise it's the difference in years minus one.
        year = input_date.year - birth_date.year
        if ((input_date.month < birth_date.month) or
            (input_date.month == birth_date.month and input_date.day < birth_date.day)):
            year -= 1
        # Now we calculate meriod, week and day.  We create a reference date year.0.0 which is a last passed birthday.  And then we follow meriods from birthday until we find the one which includes input date.
        reference_date = datetime.date(birth_date.year+year, birth_date.month, birth_date.day)
        birthday_weekday = reference_date.isoweekday() # [1..7]
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

    @staticmethod
    def from_datetime(input_datetime, birth_date=datetime.date(1988, 6, 23), delta=datetime.timedelta(hours=3)):
        """Return date in 777-calendar format for a given datetime and birthday, using delta to decite how much 777-calendar is shifted forward from regalar calendar.

        The time part of the input datetime is used to shift previous 777-date a bit compared to a regular date forward.  That is done to account for late-night stay before sleep, which still means previous day in the person-centric 777-calendar.
        """
        adjusted_datetime = (input_datetime - delta).date()
        return SevenDate.from_date(adjusted_datetime, birth_date)

    def to_date(self):
        """Convert to traditional date."""
        # We add years to birth date.
        d = datetime.date(self.birth_date.year+self.year, self.birth_date.month, self.birth_date.day)
        # And then add meriods, weeks and days up to required date.
        if self.meriod == 0:
            d += datetime.timedelta(days=self.day)
        else:
            zero_meriod_days = 1 + 7 + 7 - d.isoweekday()
            d += datetime.timedelta(days=zero_meriod_days)
            d += datetime.timedelta(days=49*(self.meriod-1))
            if self.meriod < 8:
                d += datetime.timedelta(days=7*(self.week-1)+self.day-1)
            else:
                d += datetime.timedelta(days=self.day-1)
        return d

    @staticmethod
    def days_in_meriod(year, meriod, birth_date=datetime.date(1988, 6, 23)):
        """Return number of days in a specific meriod of a 777-year.
        """
        if meriod == 0:
            sd = SevenDate(birth_date, year, meriod, 0, 0)
        elif meriod <= 7:
            return 49
        elif meriod == 8:
            sd = SevenDate(birth_date, year, meriod, 0, 1)
        else:
            raise ValueError('Wrong value of meriod: {}; bust be from in range [0—8]'.format(meriod))
        count = 0
        while sd.meriod == meriod:
            count += 1
            rd = sd.to_date() + datetime.timedelta(days=1)
            sd = SevenDate.from_date(rd, birth_date)
        return count
