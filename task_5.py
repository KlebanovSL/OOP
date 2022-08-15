class Person:
    def __init__(self, name, surname, age):
        self.verify_str(name)
        self.verify_str(surname)
        self.verify_int(age)

        self.__name = name
        self.__surname = surname
        self.__age = age

    @classmethod
    def verify_int(cls, value):
        """ Проверяет на целое число """
        if type(value) != int:
            raise TypeError('Значение должно быть целым числом!')

    @classmethod
    def verify_str(cls, value):
        """ Проверяет на строку """
        if type(value) != str:
            raise TypeError('Значение должно быть строкой!')

    @classmethod
    def verify_value(cls, value):
        """ Проверяет равно ли значение 1 или -1 и возвращает значение"""
        if value != 1 and value != -1:
            raise ValueError('Изменять значение можно только на +1 или -1!')
        else:
            return value

    def set_age(self, value):
        if self.verify_value(value):
            self.__age += value

    def full_name(self):
        """ Выводит на экран имя и фамилию через пробел """
        print(f"{self.__name} {self.__surname}")

a = Person('Сергей', 'Клебанов', 36)
a.full_name()
a.set_age(1)
print(a.__dict__)