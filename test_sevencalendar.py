import datetime

import pytest

import sevencalendar

def test_seven_date():
    d = sevencalendar.seven_date(datetime.date(2017, 7, 3), datetime.date(1988, 6, 23))
    assert str(d) == '29.1.1.1'

def test_repr():
    d = sevencalendar.seven_date(datetime.date(2017, 7, 3), datetime.date(1988, 6, 23))
    assert repr(d) == '1988-06-23 -> 29-1-1-1'
