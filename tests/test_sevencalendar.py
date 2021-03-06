# -*- coding: UTF-8 -*-

import datetime

import pytest

import sevencal.sevencalendar as sevencalendar

def test_seven_date():
    d = sevencalendar.SevenDate.from_date(datetime.date(2017, 7, 3), datetime.date(1988, 6, 23))
    assert str(d) == '29.1.1.1'
    assert repr(d) == '1988-06-23 -> 29-1-1-1'
    assert d.to_date() == datetime.date(2017, 7, 3)
    d = sevencalendar.SevenDate.from_datetime(datetime.datetime(2017, 7, 4, 2, 33), datetime.date(1988, 6, 23), datetime.timedelta(hours=2, minutes=34))
    assert str(d) == '29.1.1.1'
    d = sevencalendar.SevenDate.from_datetime(datetime.datetime(2017, 7, 4, 2, 35), datetime.date(1988, 6, 23), datetime.timedelta(hours=2, minutes=34))
    assert str(d) == '29.1.1.2'
    d = sevencalendar.SevenDate.from_date(datetime.date(1988, 6, 23), datetime.date(1988, 6, 23))
    assert str(d) == '0.0.0'
    # Test that any day in a year can be converted to seven date and back.
    some_date = datetime.date(2016, 6, 23)
    for i in range(365):
        seven_date = sevencalendar.SevenDate.from_date(some_date)
        assert some_date == seven_date.to_date()
        some_date += datetime.timedelta(days=1)
