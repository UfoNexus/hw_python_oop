import datetime as dt


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []
        self.date_today = dt.date.today()
        self.date_week_ago = self.date_today + dt.timedelta(days=-7)

    def add_record(self, new_record):
        self.records.append(new_record)

    def get_today_stats(self):
        amount_recorded = 0
        for i in self.records:
            if i.date == self.date_today:
                amount_recorded += i.amount
        return amount_recorded

    def get_remained(self):
        remaining = self.limit - self.get_today_stats()
        return remaining

    def get_week_stats(self):
        amount_recorded = 0
        for i in self.records:
            if i.date > self.date_week_ago and i.date <= self.date_today:
                amount_recorded += i.amount
        return amount_recorded


class Record:
    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        if date is None:
            self.date = dt.date.today()
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()


class CashCalculator(Calculator):
    USD_RATE = 0.014
    EURO_RATE = 0.012

    def get_today_cash_remained(self, currency):
        today_currency = {
            'rub': ['руб', 1],
            'usd': ['USD', CashCalculator.USD_RATE],
            'eur': ['Euro', CashCalculator.EURO_RATE]
        }
        if self.get_remained() > 0:
            currency_name_rate = today_currency[currency]
            cash_remained = self.get_remained() * currency_name_rate[1]
            cash_remained = round(cash_remained, 2)
            return (f'На сегодня осталось {cash_remained} '
                    f'{currency_name_rate[0]}')
        elif self.get_remained() == 0:
            return 'Денег нет, держись'
        else:
            currency_name_rate = today_currency[currency]
            cash_remained = self.get_remained() * currency_name_rate[1]
            cash_remained = round(abs(cash_remained), 2)
            return (f'Денег нет, держись: твой долг - {cash_remained}'
                    f' {currency_name_rate[0]}')


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        if self.get_remained() > 0:
            return (f'Сегодня можно съесть что-нибудь ещё, но с общей '
                    f'калорийностью не более {self.get_remained()} кКал')
        else:
            return 'Хватит есть!'
