secret_word = input("Введите слово:")
print("\033[2J")
counter = 1
points = [0, 0, 0]
boolean = False
all_letters = list()
true_letters = list()
while boolean == False:
    letter = input(f"Игрок {counter}  введите букву:") 
    if letter in secret_word:
        print("ты угадал!!!")
        true_letters.append(letter)
        points[counter-1] += 1
    print("Ваши очки:",points[counter-1])
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