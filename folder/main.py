from charecter import Charecter
import time
a = input("your name> ")
b = input("player 2 name> ")
player1 = Charecter(name=a,defence=10,damage=3,health=100)
player2 = Charecter(name=b,defence=12,damage=2,health=100)
admin = Charecter(name="admin", damage=100, defence=100,health=200 )
while True:
    print(player1)
    print(player2)

    time.sleep(2)
    admin.stroke()
    player1.attack(player2)
    player2.attack(player1)
    player1.is_alive(health=player1.health, target=player2)
    player2.is_alive(health=player2.health, target= player1)


    print(player1)
    print(player2)

    if player1.die == 1 or player2.die == 1:
        break
    time.sleep(2)
    admin.stroke()

