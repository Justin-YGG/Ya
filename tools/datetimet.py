# coding: utf-8
import calendar

from datetime import datetime, date


def get_first_and_last_of_month_by_date(date_):
    assert isinstance(date_, date)

    _, last_day = calendar.monthrange(today.year, today.month)
    first_day = datetime.date(day=1, month=today.month, year=today.year)

    return first_day, last_day

