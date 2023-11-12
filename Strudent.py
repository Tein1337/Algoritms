class Student:

    def __init__(self, name, age, average_mark, last_mark):
        self.name = name
        self.age = age
        self.average_mark = average_mark
        self.last_mark = last_mark

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def get_average_mark(self):
        return self.average_mark

    def set_average_mark(self, average_mark):
        self.average_mark = average_mark

    def get_last_mark(self):
        return self.last_mark

    def set_last_mark(self, last_mark):
        self.last_mark = last_mark


s = Student('Антон', 19, 4.5, 5)
print(f'Имя: {s.get_name()}')
print(f'Возраст: {s.get_age()}')
print(f'Средний балл: {s.get_average_mark()}')
print(f'Последняя оценка: {s.get_last_mark()}\n')

s.set_name('Александр')
s.set_age(22)
s.set_average_mark(4.1)
s.set_last_mark(3)

print(f'Имя: {s.get_name()}')
print(f'Возраст: {s.get_age()}')
print(f'Средний балл: {s.get_average_mark()}')
print(f'Последняя оценка: {s.get_last_mark()}')