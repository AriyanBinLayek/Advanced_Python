#!/usr/bin/python
"""
A siplified API for the datetime module
laura_hampton_session_4.py
"""
import datetime
import re 


re_patterns = [r'^\d+\/\d+\/\d+$', r'\d+\-\w\w\w\-\d\d',r'\d\d\d\d\-\d+\-\d+']


def get_date(str_date=None):
    if not str_date:
        return datetime.date.today() 
    elif re.search(r'^\d+\/\d+\/\d+$', str_date):
        day, month, year = str_date.split("/")
        try:
            return datetime.date(int(year), int(month), int(day))
        except ValueError as e:
            raise ValueError("Date must be in format DD/MM/YY",e)
    elif re.search(r'\d+\-\w\w\w\-\d\d',str_date):
        try:
            return datetime.datetime.strptime(str_date,"%d-%b-%y").date()
        except ValueError as e:
            raise ValueError("Date must be in format DD-Mon-YY",e)
    elif re.search(r'\d\d\d\d\-\d+\-\d+', str_date):
        try:
            year, month, day = str_date.split("-")
            return datetime.date(int(year), int(month), int(day))
        except ValueError as e:
            raise ValueError("Date must be in format YYYY-MM-DD")
    else:
        raise ValueError("Date format incorrect or not supported.")

def add_day(date, interval=0):  
    if interval == 0:
        return date + datetime.timedelta(1)
    try:
        return date + datetime.timedelta(int(interval))
    except TypeError as e:
        raise TypeError("Date interval must be an integer", e)

def add_week(date, week=0):
    if week == 0:
        weeks = 1
    else:
        try:
            weeks = int(week)
        except TypeError as e:
            raise TypeError("Date interval must be an integer", e)   
    return add_day(date, weeks*7)


def format_date(date_str, format="YYYY-MM-DD"):
    formats = ["%Y-%m-%d","%m/%d/%y","%d-%b-%y"]
    for el in formats:
        try:
            return datetime.datetime.strptime(date_str, el).date()
        except ValueError:
            pass
    raise ValueError("Date format not recognized.")

def main():
    d = format_date("2022-03-05")
    print d, type(d) 
    n = format_date("03/12/22", 'MM/DD/YY')
    print n, type(n)
    m = format_date("4-Apr-20", 'DD-Mon-YY')
    print m, type(m)


    # add_weeks() 
    # get_date()

if __name__ =='__main__':
    main() 