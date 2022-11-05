class Charecter:
    name = ""
    damage = 1
    health = 100
    defence = 0
    die = 0


    def __init__(self, name, health, damage, defence):
        self.name = name
        self.health = health
        self.damage = damage
        self.defence = defence
    def __str__(self):
       return f'=={self.name}==\n' \
              f' Здоровье: {self.health}\n' \
              f' Урон: {self.damage}\n' \
              f' Защита: {self.defence}\n'
    def win(self):
        print("Выиграл")
        self.die = 1
    def stroke(self):
        print('-----------------')
    def take_damage(self,damage):
        self.health -= max(damage, 0)
    def attack(self, target):
        target.take_damage(self.damage)
    def is_alive(self, health, target):
        if health <= 0:
            print(f'{self.name} Умер')
            target.win(self)






