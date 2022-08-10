class __Leaner:
    '''Базовый класс учащихся'''
    higher_value = 500
    lower_value = 150

    def __init__(self, first_name: str, second_name: str, group: str, marks: list):
        '''Создает экземпляры с атрибутами --  имя, фамилия, группа, список оценок'''
        self.first_name = first_name
        self.second_name = second_name
        self.group = group
        self.marks = marks

    @staticmethod
    def __average_mark(x):
        return sum(x) / len(x)

    def get_average_mark(self):
        '''Возвращает среднеарифметическое значение оценок'''
        return self.__average_mark(self.marks)

    @classmethod
    def __scolarship(cls, x):
        return cls.higher_value if x >= 5 else cls.lower_value

    def get_scolarship(self):
        '''Возвращает размер степендии'''
        return self.__scolarship(self.__average_mark(self.marks))

    @staticmethod
    def __mark(x, y):
        if type(y) == int and 0 < y < 11:
            x.append(y)
            print('Оценка добавлена в список')
        else:
            print('Введите оценку от 1 до 10')

    def add_mark(self, mark):
        '''Добавляет оценку в список оценок, если выполняется условие'''
        self.__mark(self.marks, mark)


class Student(__Leaner):
    '''Класс Студент(Учащийся)'''
    pass


class Aspirant(__Leaner):
    '''Класс Аспирант(Учащийся)'''
    higher_value = 700
    lower_value = 250

    def __init__(self, first_name: str, second_name: str, group: str, marks: list, scientific_publications: list):
        '''Создает экземпляры с атрибутами --  имя, фамилия, группа, список оценок, список научных работ'''
        super().__init__(first_name, second_name, group, marks)
        self.scientific_publications = scientific_publications


a = Student('Sergei', 'Klebanov', 'group z28', [4, 5, 6])
b = Aspirant('Mihael', 'Lopatin', 'group r23', [4, 5, 6, 6], ['data1', 'data2'])
print(a.get_average_mark())
print(a.marks)
a.add_mark(9)
b.add_mark(0)
print(a.marks)
print(b.marks)
print(a.get_scolarship())
print(b.get_scolarship())
print(Student.__init__.__doc__)
print(Aspirant.__init__.__doc__)