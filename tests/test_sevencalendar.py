import datetime

import pytest

import sevencal.sevencalendar as sevencalendar

def test_seven_date():
    d = sevencalendar.SevenDate.from_date(datetime.date(2017, 7, 3), datetime.date(1988, 6, 23))
    assert str(d) == '29.1.1.1'
    assert repr(d) == '1988-06-23 -> 29-1-1-1'
    assert d.to_date() == datetime.date(2017, 7, 3)
