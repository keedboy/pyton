artifact_one = False
artifact_two = False
artifact_three = False
score = 0
product = 0
x = 0

myname = input("Как тебя зовут дорогой друг: ")
print("Приятно познакомиться дорогой, "+myname+"!")

print("Самое время начать наше путешествие! Правила таковы мы с тобой, "+myname+" , сейчас начинаем свой путь с нулем(0) очков и по ходу игры и ответов на вопросы ты будешь получать баллы:")

print("")
print("    1 задание === 10 очков")
print("    2 задание === 20 очков")
print("    3 задание === 30 очков")
print("")

print("У 33 моряков было 561 консервных банок каждый час каждыйиз них ест по 1 банке.")

answer_one = input("Cколько часов они будут есть?")

if answer_one == "17":
    print("Молорчик все правильно держи артефакт и очки")
    artifact_one = True
    score = 10
    print("")
    print("Артефакт один добыт")
    print("")
    print("Прибавлено 10 очков")
else:
    print("Бро сорян неправильно")
    artifact_Two = False
    score = 0
    print("")
    print("Артефакт один не добыт")
    print("")
    print("Прибавлено 0 очков")

print("у саши было 10952 он сьел 1/4 этих яблок а 4/6 оставшихся он отдал коле")

answer_two = input("Cколько яблок осталось?")

if answer_two == "2738":
    print("Молорчик все правильно держи артефакт и очки")
    artifact_two = True
    score = score+20
    print("")
    print("Артефакт два добыт")
    print("")
    print("Прибавлено 20 очков")
else:
    print("Бро сорян неправильно")
    artifact_one = False
    score = score+0
    print("")
    print("Артефакт два не добыт")
    print("")
    print("Прибавлено 0 очков")
    
print("скорость самолета 1232 km/h он летел 1134 часа после посадки в Рио-дежанейро он полетел в Токио с скоростью 1365 km/h  979 часов и каждый километр из него падало 435 мандаринов")

answer_two = input("Cколько мандаринов вывалелось?")

if answer_two == "1090664190":
    print("Молорчик все правильно держи артефакт и очки")
    artifact_three = True
    score = score+30
    print("")
    print("Артефакт три добыт")
    print("")
    print("Прибавлено 30 очков")
else:
    print("Бро сорян неправильно")
    artifact_three = False
    score = score+0
    print("")
    print("Артефакт три не добыт")
    print("")
    print("Прибавлено 0 очков")
print("ты можешь что нибудь купить если хватает очков:")
print("1.Common FN FAL Acid Carbon 10 очков")
print("2.Epic UMP45 Cerberus 20 очков")
print("3.StatTrack-Legendary AWM Winter Sport 30 очков")
print("4.Arcane M4A1 Year of The Tiger и Buterfly Legacy 40 очков")
print("5.Arcane Dual Daggers Harmony и AWM Treasure Hunter 50 очков")
print("6.Пропустить")
print("У вас ",score," очков")
product = int(input("чего вы хотите?"))
if product == 1:
    if score >= 10:
        print("Поздравляю вы купили Common FN FAL Acid Carbon 10 очков")
        print("У вас отнято 10 очков")
        score = score-10
        print("У вас ",score," очков")
        if artifact_one == True:
            print("артефакт один есть")
            x = x+1
        else:
            print("артефакт один нет")
        if artifact_two == True:
            print("артефакт два есть")
            x = x+1
        else:
            print("артефакт два нет")
        if artifact_three == True:
            print("артефакт три есть")
            x = x+1
        else:
            print("артефакт три нет")
        if x == 3:
            print("ты выграл у тебя есть Common FN FAL Acid Carbon 10 очков")
        else:
            print("ты проиграл но у тебя есть Common FN FAL Acid Carbon 10 очков")
elif product == 2:
    if score >= 20:
        print("Поздравляю вы купили Epic UMP45 Cerberus 20 очков")
        print("У вас отнято 20 очков")
        score = score-20
        print("У вас ",score," очков")
        if artifact_one == True:
            print("артефакт один есть")
            x = x+1
        else:
            print("артефакт один нет")
        if artifact_two == True:
            print("артефакт два есть")
            x = x+1
        else:
            print("артефакт два нет")
        if artifact_three == True:
            print("артефакт три есть")
            x = x+1
        else:
            print("артефакт три нет")
        if x == 3:
           print("ты выграл у тебя есть Epic UMP45 Cerberus 20 очков")
        else:
            print("ты проиграл но у тебя есть Epic UMP45 Cerberus 20 очков")
elif product == 3:
    if score >= 30:
        print("Поздравляю вы купили StatTrack-Legendary AWM Winter Sport 30 очков")
        print("У вас отнято 30 очков")
        score = score-30
        print("У вас ",score," очков")
        if artifact_one == True:
            print("артефакт один есть")
            x = x+1
        else:
            print("артефакт один нет")
        if artifact_two == True:
            print("артефакт два есть")
            x = x+1
        else:
            print("артефакт два нет")
        if artifact_three == True:
            print("артефакт три есть")
            x = x+1
        else:
            print("артефакт три нет")
        if x == 3:
            print("ты выграл у тебя есть StatTrack-Legendary AWM Winter Sport 30 очков")
        else:
            print("ты проиграл но у тебя есть StatTrack-Legendary AWM Winter Sport 30 очков")
elif product == 4:
    if score >= 40:
        print("Поздравляю вы купили Arcane M4A1 Year of The Tiger и Buterfly Legacy 40 очков")
        print("У вас отнято 40 очков")
        score = score-40
        print("У вас ",score," очков")
        if artifact_one == True:
            print("артефакт один есть")
            x = x+1
        else:
            print("артефакт один нет")
        if artifact_two == True:
            print("артефакт два есть")
            x = x+1
        else:
            print("артефакт два нет")
        if artifact_three == True:
            print("артефакт три есть")
            x = x+1
        else:
            print("артефакт три нет")
        print("ты победил и у тебя Arcane M4A1 Year of The Tiger и Buterfly Legacy 40 очков")
elif product == 5:
    if score >= 50:
        print("Поздравляю вы купили Arcane Dual Daggers Harmony и AWM Treasure Hunter 50 очков")
        print("У вас отнято 50 очков")
        score = score-50
        print("У вас ", score ," очков")
        if artifact_one == True:
            print("артефакт один есть")
            x = x+1
        else:
            print("артефакт один нет")
        if artifact_two == True:
            print("артефакт два есть")
            x = x+1
        else:
            print("артефакт два нет")
        if artifact_three == True:
            print("артефакт три есть")
            x = x+1
        else:
            print("артефакт три нет")
        print("ты победил и у тебя Arcane Dual Daggers Harmony и AWM Treasure Hunter 50 очков")
elif product == 6:
    print("ОК вы просто пропустили")
    if artifact_one == True:
        print("артефакт один есть")
        x = x+1
    else:
        print("артефакт один нет")
    if artifact_two == True:
        print("артефакт два есть")
        x = x+1
    else:
        print("артефакт два нет")
    if artifact_three == True:
        print("артефакт три есть")
        x = x+1
    else:
        print("артефакт три нет")
    if x == 3:
        print("ты победил")
    else:
        print("ты проиграл")
        