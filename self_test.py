import homework

test_cash_remained_positive = homework.CashCalculator(100)
test_cash_remained_positive.add_record(homework.Record(36.242, 'test1'))
test_cash_remained_positive.add_record(homework.Record(13.197, 'test2'))
print(test_cash_remained_positive.get_today_cash_remained('rub'))
print(test_cash_remained_positive.get_today_cash_remained('usd'))
print(test_cash_remained_positive.get_today_cash_remained('eur'))

test_cash_remained_zero = homework.CashCalculator(100)
test_cash_remained_zero.add_record(homework.Record(60, 'test1'))
test_cash_remained_zero.add_record(homework.Record(40, 'test2'))
print(test_cash_remained_zero.get_today_cash_remained('rub'))
print(test_cash_remained_zero.get_today_cash_remained('usd'))
print(test_cash_remained_zero.get_today_cash_remained('eur'))

test_cash_remained_negative = homework.CashCalculator(100)
test_cash_remained_negative.add_record(homework.Record(36.291, 'test1'))
test_cash_remained_negative.add_record(homework.Record(93.24, 'test2'))
print(test_cash_remained_negative.get_today_cash_remained('rub'))
print(test_cash_remained_negative.get_today_cash_remained('usd'))
print(test_cash_remained_negative.get_today_cash_remained('eur'))
