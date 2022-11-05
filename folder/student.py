import datetime
class Student:
    name = ""
    bornYear = 0
    group = ""
    Ball = 0
    year = 0
    age = 0
    def __init__(self, name, bornYear, group, Ball):
        self.name = name
        self.bornYear = bornYear
        self.group = group
        self.Ball = Ball
    def __str__(self):
       return f'---{self.name}---\n' \
              f' Год рождения: {self.bornYear}\n' \
              f' Группа: {self.group}\n' \
              f' Средний бал: {self.Ball}\n'
    def get_age(self, bornYear):
        year = datetime.date.today().year
        age = year - bornYear
        print(f' Ему {age}')

