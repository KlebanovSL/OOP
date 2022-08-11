class Kg:
    def __init__(self, value: float, measure_of_weight: str):
        self.value = value
        self.measure_of_weight = measure_of_weight
    def make_kg(self):
        '''Печатает значение в килограммах 1 тонна = 1000 кг, 1 центнер = 100 кг, 1 фунт = 0,45359237 кг, 1 пуд = 16,38 кг'''
        if 'тонн' in self.measure_of_weight:
            print(f"{self.value*1000} 'килограмм'")
        elif 'центнер' in self.measure_of_weight:
            print(f"{self.value * 100} 'килограмм'")
        elif 'фунт' in self.measure_of_weight:
            print(f"{self.value * 0.45359237} 'килограмм'")
        elif 'пуд' in self.measure_of_weight:
            print(f"{self.value * 16.38} 'килограмм'")
        else:
            print('Неверно указан формат веса!')
a = Kg(2, "тонны")
b = Kg(36, "центнера")
c = Kg(16, "фунтов")
d = Kg(2, "пуда")
e = Kg(4, "милиграмма")
a.make_kg()
b.make_kg()
c.make_kg()
d.make_kg()
e.make_kg()