class Nobody:
    '''Простой класс для решения первой задачи в теме ООП'''
    def __init__(self, name):
        '''Присваивает значение атрибуту экземпляра, если аргумент == заданному значению,
иначе присваивает другое заданное значение'''
        self.name = name if name == "Nobody" else f"I'm Nobody, not {name}"
a = Nobody("Allmighty")
print(a.name)
print(Nobody.__doc__)
print(Nobody.__init__.__doc__)
