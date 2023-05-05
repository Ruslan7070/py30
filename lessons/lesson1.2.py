# OOP - обьеткно ориентированное програмирование

def a(a, b):
    m = a * b
    print(m)


a(4, 3)

t = 1
t2 = 'str'
t3 = 2.3
t4 = True
t5 = ()
t6 = []
t7 = {}

print(type(t5))


class Person:
    head = True  # свойства

    def __init__(self, name, age):  # конструктор
        self.name = name
        self.age = age

    def __str__(self):  # магические методы
        return f'name is:{self.name}\n' \
               f'age is:{self.age}\n'


    def age2(self):  # метод
        self.age *= 2

    # def nameis(self):
    #     self.name = 'Islam'

    def __len__(self):
        return len(f'{self.name}{self.age}')


person = Person('Ruslan', 19)
# person.age2()
# print(person)
person2 = Person('Azimbek',17)
person3 = Person('Beka',19)

# person3.a1()
print(person)
print(person2)
print(person3)


# person.nameis()
# print(person)



# print(len(person2.name))
print(len(person))
print(len(person2))
print(len(person3))