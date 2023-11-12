class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transaction = []

    def replenishment(self, sum):
        if sum > 0:
            self.balance += sum
            self.transaction.append(f'Пополнение счёта на сумму: {sum}')

    def withdrawal(self, sum):
        if 0 < sum <= self.balance:
            self.balance -= sum
            self.transaction.append(f'Снятие счёта на сумму: {sum}')

    def get_balance(self):
        return self.balance

    def get_transaction(self):
        return self.transaction


b = Bank('Тестов Тест', 100)
print('Клиент:', b.name)
print('Стартовый баланс:', b.get_balance())
b.replenishment(500)
b.withdrawal(100)
b.withdrawal(300)
print()
print('Транзакции по счету:')

for transaction in b.get_transaction():
    print(transaction)

print('Окончательный баланс:', b.get_balance())