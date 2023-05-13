secret_word = input("Введите слово:")
print("\033[2J")
counter = 1
points = [0, 0, 0]
boolean = False
all_letters = list()
true_letters = list()
while boolean == False:
    if counter == 1:
        letter = input("Игрок 1 введите букву:")
    if counter == 2:
        letter = input("Игрок 2 введите букву:")
    if counter == 3:
        letter = input("Игрок 3 введите букву:")
    if letter in secret_word:
        print("ты угадал!!!")
        true_letters.append(letter)
        if counter == 1:
            points[0] += 1
            print("Ваши очки:",points[0])
        if counter == 2:
            points[1] += 1
            print("Ваши очки:",points[1])
        if counter == 3:
            points[2] += 1
            print("Ваши очки:",points[2])
    if letter in all_letters:
        print("Буква уже была!!!" )
    for symbol in secret_word:
        if symbol in true_letters:
            print(symbol, end="")
        else:
            print("*", end="")
    all_letters.append(letter)
    print("\nСписок: ",all_letters, "\n")
    counter+=1
    if counter == 4:
        counter = 1
    if set(true_letters) == set(secret_word):
        boolean = True
print("Игрок 1! Ваши очки: ",points[0])
print("Игрок 2! Ваши очки: ",points[1])
print("Игрок 3! Ваши очки: ",points[2])