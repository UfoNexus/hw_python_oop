import datetime as dt


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []
        self.date_today = dt.date.today()
        self.date_week_ago = self.date_today + dt.timedelta(days=-7)

    def add_record(self, amount, date, comment):
        record = Record(amount, date, comment)
        self.records.append(record)

    def get_today_stats(self):
        amount_recorded = 0
        for i in self.records:
            if i.date == str(self.date_today):
                amount_recorded += i.amount
        return amount_recorded

    def get_remained(self):
        remaining = self.limit - self.get_today_stats()
        return remaining

    def get_week_stats(self):
        amount_recorded = 0
        for i in self.records:
            if i.date >= str(self.date_week_ago):
                amount_recorded += i.amount
        return amount_recorded


class Record:
    def __init__(self, amount, date, comment):
        self.amount = amount
        self.date = date
        self.comment = comment


class CashCalculator(Calculator):
    def get_today_cash_remained(self, currency):
        today_currency = {
            'rub': 1,
            'usd': 0.014,
            'eur': 0.011
        }
        currency_normal_writing = {
            'rub': 'руб',
            'usd': 'USD',
            'eur': 'Euro'
        }
        present_currencies = ', '.join(today_currency.keys())
        if self.get_remained() > 0:
            if currency in today_currency.keys():
                return (f'На сегодня осталось '
                        f'{self.get_remained() * today_currency[currency]} '
                        f'{currency_normal_writing[currency]}')
            else:
                return (f'Простите, мне неизвестна валюта {currency}. '
                        f'Предлагаю посчитать в валютах {present_currencies}.')
        elif self.get_remained() == 0:
            return 'Денег нет, держись'
        else:
            if currency in today_currency.keys():
                return (f'Денег нет, держись: твой долг - '
                        f'{abs(self.get_remained() * today_currency[currency])}'
                        f' {currency_normal_writing[currency]}')
            else:
                return (f'Простите, мне неизвестна валюта {currency}. '
                        f'Предлагаю посчитать в валютах {present_currencies}.')


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        if self.get_remained() > 0:
            return (f'Сегодня можно съесть что-нибудь ещё, но с общей '
                    f'калорийностью не более {self.get_remained()} кКал')
        else:
            return 'Хватит есть!'
