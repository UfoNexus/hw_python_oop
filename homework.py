import datetime as dt


DATE_FORMAT = '%d.%m.%Y'


class Calculator:

    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, new_record):
        self.records.append(new_record)

    def get_today_stats(self):
        date_today = dt.date.today()
        today_records = [i.amount for i in self.records
                         if i.date == date_today]
        amount_recorded = sum(today_records)
        return amount_recorded

    def get_remained(self):
        remaining = self.limit - self.get_today_stats()
        return remaining

    def get_week_stats(self):
        date_today = dt.date.today()
        date_week_ago = date_today - dt.timedelta(days=7)
        week_records = [i.amount for i in self.records
                        if date_week_ago < i.date <= date_today]
        amount_recorded = sum(week_records)
        return amount_recorded


class Record:

    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        if date is None:
            self.date = dt.date.today()
        else:
            self.date = dt.datetime.strptime(date, DATE_FORMAT).date()


class CashCalculator(Calculator):

    RUB_RATE = 1
    USD_RATE = 72.1
    EURO_RATE = 86.1

    def get_today_cash_remained(self, currency):
        remained = self.get_remained()
        today_currency = {
            'rub': ('руб', self.RUB_RATE),
            'usd': ('USD', self.USD_RATE),
            'eur': ('Euro', self.EURO_RATE)
        }
        currency_name, currency_rate = today_currency[currency]
        cash_remained = remained / currency_rate
        cash_remained = round(cash_remained, 2)
        if remained == 0:
            return 'Денег нет, держись'
        elif remained > 0:
            return (f'На сегодня осталось {cash_remained} '
                    f'{currency_name}')
        return (f'Денег нет, держись: твой долг - {abs(cash_remained)}'
                f' {currency_name}')


class CaloriesCalculator(Calculator):

    def get_calories_remained(self):
        remained = self.get_remained()
        if remained > 0:
            return ('Сегодня можно съесть что-нибудь ещё, но с общей '
                    f'калорийностью не более {remained} кКал')
        return 'Хватит есть!'
