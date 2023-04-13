import random
win = 0
for number in range(1,11):
    if win < 3:
        player = int(input("Сделай ход: 1-камень 2-ножницы 3-бумага "))
        if player == 1:
            print("Ваш ход - камень")
        if player == 2:
            print("Ваш ход - ножницы")
        if player == 3:
            print("Ваш ход - бумага")
        comp = random.randint(1,3)
        if comp == 1:
            print("Ход компьютера - камень")
        if comp == 2:
            print("Ход компьютера - ножницы")
        if comp == 3:
            print("Ход компьютера - бумага")
        if comp == player:
            print("Ничья")
            win = win+0.5
        if comp == 1 and player == 2 or comp == 2 and player == 3 or comp == 3 and player == 1:
            print("Компухтер выграл")
        if comp == 2 and player == 1 or comp == 3 and player == 2 or comp == 1 and player == 3:
            print("Ты выграл")
            win = win+1