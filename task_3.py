class MyString:
    def __init__(self, value: str):
        self.value = str(value)

    def __gt__(self, other):
        return len(self.value) > len(other.value)

    def __ge__(self, other):
        return len(self.value) >= len(other.value)

    def __eq__(self, other):
        return len(self.value) == len(other.value)

    def __ne__(self, other):
        return len(self.value) != len(other.value)

    def __lt__(self, other):
        return len(self.value) < len(other.value)

    def __le__(self, other):
        return len(self.value) <= len(other.value)

a = MyString('Akunamatata')
b = MyString('Heya!')
print(a > b)
print(a >= b)
print(a == b)
print(a != b)
print(a <= b)
print(a < b)