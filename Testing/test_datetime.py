import datetime
import pytest
import datetime_for_tests as dtt


def test_get_date():
    assert dtt.get_date() == datetime.date.today()
    assert dtt.get_date("5/5/2016") == datetime.date(2016, 05, 05)
    assert dtt.get_date("5-May-17") == datetime.date(2017, 05, 05) 
    assert dtt.get_date("2020-01-20") == datetime.date(2020, 01, 20) 
    with pytest.raises(ValueError):
        dtt.get_date("5-May-2017")
    with pytest.raises(ValueError):
        dtt.get_date("2015/Mar/03")
    with pytest.raises(ValueError):
        dtt.get_date("astring")

def test_add_day():
    assert dtt.add_day(datetime.date(2020,1,20), 5) == datetime.date(2020, 01, 25)
    assert dtt.add_day(datetime.date(2020,2,20)) == datetime.date(2020, 2, 21)
    assert dtt.add_day(datetime.date(2034, 9, 20), -2) == datetime.date(2034, 9, 18)
    with pytest.raises (TypeError):
        dtt.add_day("astring")
    with pytest.raises (ValueError):
        dtt.add_day("2017-12-02", "adj")
    with pytest.raises(TypeError):
        dtt.add_day("4/19", 9)

def test_add_week():
    assert dtt.add_week(datetime.date(2020, 1, 20), 5) == datetime.date(2020, 02, 24)
    assert dtt.add_week(datetime.date(2020, 1, 20)) == datetime.date(2020, 1, 27)
    with pytest.raises (TypeError):
        dtt.add_week("astring")

def test_format_date():
    assert dtt.format_date("2022-03-05") == datetime.date(2022, 03, 05)
    assert dtt.format_date("03/12/22", 'MM/DD/YY') == datetime.date(2022, 03, 12)
    assert dtt.format_date("4-Apr-20", 'DD-Mon-YY') == datetime.date(2020, 04, 04)
    with pytest.raises(ValueError):
        dtt.format_date("Wednesday, March 19th, 2048")
    with pytest.raises(ValueError):
        dtt.format_date("3.17.12")
    with pytest.raises(ValueError):
        dtt.format_date("4/12")
    with pytest.raises(ValueError):
        dtt.format_date("astring")