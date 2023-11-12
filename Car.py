class Car:
    def __init__(self, brand, model, year, km):
        self.brand = brand
        self.model = model
        self.year = year
        self.km = km

    def set_brand(self, brand):
        self.brand = brand

    def set_model(self, model):
        self.model = model

    def set_year(self, year):
        self.year = year

    def set_km(self, km):
        self.km = km

    def get_brand(self):
        return self.brand

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_km(self):
        return self.km


c = Car('Cola', 'pepsi-3', 1993, 25)
print(f'Марка: {c.get_brand()}')
print(f'Модель: {c.get_model()}')
print(f'Год производства: {c.get_year()}')
print(f'Пробег: {c.get_km()}\n')

c.set_brand('Pepsi')
c.set_model('cola-21')
c.set_year(2000)
c.set_km(600)

print(f'Марка : {c.get_brand()}')
print(f'Модель: {c.get_model()}')
print(f'Год производства: {c.get_year()}')
print(f'Пробег: {c.get_km()}')