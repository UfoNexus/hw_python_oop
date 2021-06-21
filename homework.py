import datetime as dt


class Calculator:
    def __init__(self, limit):
        self.limit = limit

    records = []

    def add_record(amount, date, comment):
        i = len(records)
        records.append(Record(amount, date, comment))


class Record:
    def __init__(self, amount, date, comment):
        self.amount = amount
        self.date = date
        self.comment = comment


class CaloriesCalculator(Calculator):
    pass


class CashCalculator(Calculator):
    pass
