import homework

if __name__ == '__main__':
    test_cash_remained_positive = homework.CashCalculator(100)
    test_cash_remained_positive.add_record(homework.Record(36.24, 'test1'))
    test_cash_remained_positive.add_record(homework.Record(13.19, 'test2'))
    print(test_cash_remained_positive.get_today_cash_remained('rub'))
    print(test_cash_remained_positive.get_today_cash_remained('usd'))
    print(test_cash_remained_positive.get_today_cash_remained('eur'))
    print(test_cash_remained_positive.get_today_cash_remained('gbp'))

    test_cash_remained_zero = homework.CashCalculator(100)
    test_cash_remained_zero.add_record(homework.Record(60, 'test1'))
    test_cash_remained_zero.add_record(homework.Record(40, 'test2'))
    print(test_cash_remained_zero.get_today_cash_remained('rub'))
    print(test_cash_remained_zero.get_today_cash_remained('usd'))
    print(test_cash_remained_zero.get_today_cash_remained('eur'))

    test_cash_remained_negative = homework.CashCalculator(100)
    test_cash_remained_negative.add_record(homework.Record(36.29, 'test1'))
    test_cash_remained_negative.add_record(homework.Record(93.24, 'test2'))
    print(test_cash_remained_negative.get_today_cash_remained('rub'))
    print(test_cash_remained_negative.get_today_cash_remained('usd'))
    print(test_cash_remained_negative.get_today_cash_remained('eur'))

    test_calories_remained_positive = homework.CaloriesCalculator(1000)
    test_calories_remained_positive.add_record(homework.Record(20, 'test1'))
    test_calories_remained_positive.add_record(homework.Record(30, 'test2'))
    print(test_calories_remained_positive.get_calories_remained())
