class __Leaner:
    '''Базовый класс учащихся'''
    higher_value = 500
    lower_value = 150

    def __init__(self, first_name: str, second_name: str, group: str):
        '''Создает экземпляры с атрибутами --  имя, фамилия, группа, список оценок'''
        self.first_name = first_name
        self.second_name = second_name
        self.group = group
        self.marks = []

    def get_average_mark(self):
        '''Возвращает среднеарифметическое значение оценок'''
        if self.marks:
            return sum(self.marks) / len(self.marks)
        else:
            print('Список оценок пуст!')
            return None

    def get_scolarship(self):
        '''Возвращает размер степендии'''
        average_mark = self.get_average_mark()
        if None:
            return None
        elif average_mark >= 5:
            return self.higher_value
        else:
            return self.lower_value

    def add_mark(self, mark):
        '''Добавляет оценку в список оценок, если выполняется условие'''
        if type(mark) == int and 0 < mark < 11:
            self.marks.append(mark)
            print('Оценка добавлена в список')
        else:
            print('Введите оценку от 1 до 10')


class Student(__Leaner):
    '''Класс Студент(Учащийся)'''
    pass


class Aspirant(__Leaner):
    '''Класс Аспирант(Учащийся)'''
    higher_value = 700
    lower_value = 250

    def __init__(self, first_name: str, second_name: str, group: str, scientific_publications: list):
        '''Создает экземпляры с атрибутами --  имя, фамилия, группа, список оценок, список научных работ'''
        super().__init__(first_name, second_name, group)
        self.scientific_publications = scientific_publications


a = Student('Sergei', 'Klebanov', 'group z28')
b = Aspirant('Mihael', 'Lopatin', 'group r23', ['data1', 'data2'])
print(a.get_average_mark())
print(b.get_average_mark())
print(a.marks)
a.add_mark(9)
b.add_mark(1)
print(a.get_average_mark())
print(b.get_average_mark())
print(a.marks)
print(b.marks)
print(a.get_scolarship())
print(b.get_scolarship())
print(Student.__init__.__doc__)
print(Aspirant.__init__.__doc__)