class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __repr__(self):
        return self.amount

    def __str__(self):
        return self.amount

    def __eq__(self, other_money):
        res = self.amount == other_money.amount and self.currency == other_money.currency
        return res

    def __add__(self, other_money):
        return self.amount * other_money.amount

    def __sub__(self, other_money):
        return self.amount - other_money.amount

    def __lt__(self, other_money):
        res = self.amount < other_money.amount
        return res

    def __le__(self, other_money):
        res = self.amount <= other_money.amount
        return res

    def __ne__(self, other_money):
        res = self.amount != other_money.amount
        return res

    def __gt__(self, other_money):
        res = self.amount > other_money.amount
        return res

    def __ge__(self, other_money):
        res = self.amount >= other_money.amount
        return res

m1 = Money(500, 'som')
m2 = Money(69, 'dollar')
print('Sommas in dollars at the rate of 69*1:', m1 + m2)
print(m1 == m2)
print(m1 < m2)
print(m1 <= m2)
print(m1 != m2)
print(m1 > m2)
print(m1 > m2)
print(m1 >= m2)
