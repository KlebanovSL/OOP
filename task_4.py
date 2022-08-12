class Kg:
    """ Содержит методы перевода из заданных мер веса в килограммы"""

    @staticmethod
    def get_from_tonn(value: float):
        """ Печатает значение в килограммах 1 тонна = 1000 кг """
        print(f"{value*1000:.2f} килограмм")

    @staticmethod
    def get_from_centner(value: float):
        """ Печатает значение в килограммах 1 центнер = 100 кг """
        print(f"{value * 100:.2f} килограмм")

    @staticmethod
    def get_from_funt(value: float):
        """ Печатает значение в килограммах 1 фунт = 0,45359237 кг"""
        print(f"{value * 0.45359237:.2f} килограмм")

    @staticmethod
    def get_from_pud(value: float):
        """ Печатает значение в килограммах 1 пуд = 16,38 кг"""
        print(f"{value * 16.38:.2f} килограмм")


Kg.get_from_tonn(3)
Kg.get_from_centner(4)
Kg.get_from_funt(5)
Kg.get_from_pud(6)
