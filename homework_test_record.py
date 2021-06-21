records = []


class Record:
    def __init__(self, amount, date, comment):
        self.amount = amount
        self.date = date
        self.comment = comment

    def __str__(self):
        return self.amount, self.date, self.comment


def add_record(amount, date, comment):
    record = Record(amount, date, comment)
    records.append(record)


add_record(1, '01.01.1990', 'test1')
add_record(2, '02.02.2990', 'test2')
print(records)
