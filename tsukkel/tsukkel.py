from random import *
from turtle import *
from math import *
##############1##############
#for#
#nimi = input("Palun sisesta oma nimi: ")
#kord = int(input("Mitu korda soovid tervitust saada? "))
#for i in range(1, kord+1):
#    print(f"Ole tervitatud, {nimi}, {i}. korda.")

#while#
#nimi = input("Palun sisestage oma nimi: ")
#kord = int(input("Mitu korda soovite tervitust saada? "))
#i = 1
#while i <= kord:
#    print(f"Ole tervitatud, {nimi}, {i}. korda.")
#    i+=1

#while True#
#nimi = input("Palun sisestage oma nimi: ")
#kord = int(input("Mitu korda soovite tervitust saada? "))
#i = 1
#while True:
#    if i == kord+1:
#        break
#    else:
#        print(f"Ole tervitatud, {nimi}, {i}. korda.")
#    i+=1



##############2##############
#for#
#summa = 0
#for i in range(10):
#    number="X"
#    while type(number) != int:
#        try:
#            number=int(input("Palun sisestage number: "))
#        except:
#            TypeError
#    summa += number
#print("Nende numbrite summa on:", summa)

#while#
#summa = 0
#count = 0
#while count < 10:
#    number = "X"
#    while type(number) != int:
#        try:
#            number = int(input("Palun sisestage number: "))
#        except TypeError:
#            pass
#    summa += number
#    count += 1
#print("Nende numbrite summa on:", summa)

#while True#
#summa = 0
#i = 0
#while True:
#    if i == 10:
#        break
#    number="X"
#    while type(number) != int:
#        try:
#            number=int(input("Palun sisestage number: "))
#        except:
#            TypeError
#    summa += number
#    i += 1
#print("Nende numbrite summa on:", summa)



##############3##############
#for#
#print("Tere tulemast liitmisharjutuste programmi!")
#limit = int(input("Sisestage suurim arv, mida soovite liitmiseks kasutada: "))
#count = int(input("Sisestage, kui palju liitmistehteid soovite teha: "))
#correct_answers = 0
#wrong_answers = 0
#for i in range(count):
#    num1 = randint(1, limit)
#    num2 = randint(1, limit)
#    answer = int(input(f"{num1} + {num2} = "))
#    if answer == num1 + num2:
#        print("Õige vastus!")
#        correct_answers += 1
#    else:
#        print("Vale vastus.")
#        print(f"Õige vastus on {num1 + num2}.")
#        wrong_answers += 1
#    if wrong_answers == 5:
#        print("Vale vastus viiel korral järjest. Programm lõpetab töö.")
#        break
#print(f"Te tegite {count} liitmist ning saite {correct_answers} õiget vastust.")

#while#
#num_of_transactions = int(input("Введите количество транзакций: "))
#min_num = int(input("Введите минимальное число для сложения: "))
#max_num = int(input("Введите максимальное число для сложения: "))
#correct_answers = 0
#incorrect_answers = 0
#transaction = 1
#while transaction <= num_of_transactions:
#    print(f"Транзакция {transaction}/{num_of_transactions}")
#    num1 = random.randint(min_num, max_num)
#    num2 = random.randint(min_num, max_num)
#    user_answer = int(input(f"Сколько будет {num1} + {num2}? "))
#    if user_answer == num1 + num2:
#        print("Правильно!")
#        correct_answers += 1
#    else:
#        print(f"Неправильно. Правильный ответ: {num1 + num2}")
#        incorrect_answers += 1
#    transaction += 1
#print(f"Вы ответили правильно на {correct_answers} из {num_of_transactions} вопросов.")

#while True#
#num_tasks = 10 
#max_num = 50  
#correct_answers = 0  
#print(f"Добро пожаловать в программу для тренировки сложения!\nВыполните {num_tasks} заданий:")
#for i in range(num_tasks):
#    a = randint(1, max_num)
#    b = randint(1, max_num)
#    answer = int(input(f"{i + 1}) Сколько будет {a} + {b}? "))
#    if answer == a + b:
#        print("Правильно!")
#        correct_answers += 1
#    else:
#        print(f"Неправильно. Правильный ответ: {a + b}")
#print(f"Вы ответили правильно на {correct_answers} из {num_tasks} заданий.") 



##############4##############
#for#
#for i in range(1, 11):
#    print(i)
#print("Korrutustabel:")
#for i in range(1, 11):
#    for j in range(1, 11):
#        print(i * j, end='\t')
#    print()

#while#
#i = 1
#while i <= 10:
#    print(i)
#    i += 1
#print("Korrutustabel:")
#i = 1
#while i <= 10:
#    j = 1
#    while j <= 10:
#        print(i*j, end="\t")
#        j += 1
#    print()
#    i += 1

#while True#
#i = 1
#while True:
#    if i <= 10:
#        print(i)
#        i += 1
#    else:
#        break

#print("\nKorrutustabel:")
#for j in range(1, 11):
#    for k in range(1, 11):
#        print(j*k, end="\t")
#    print()



##############5##############
#for#
#n = int(input("Введите размер квадрата: "))
#for i in range(n):
#    for j in range(n):
#        if i == j or i + j == n - 1:
#            print("X", end="")
#        else:
#            print("0", end="")
#    print()

#while#
#n = int(input("Введите размер квадрата: "))
#i = 0
#while i < n:
#    j = 0
#    while j < n:
#        if i == j or i + j == n - 1:
#            print("X", end="")
#        else:
#            print("0", end="")
#        j += 1
#    print()
#    i += 1

#while True#
#while True:
#    n = int(input("Введите размер квадрата (целое нечетное число): "))
#    if n % 2 == 1:
#        break
#    else:
#        print("Размер квадрата должен быть нечетным числом!")
#i = 0
#while i < n:
#    j = 0
#    while j < n:
#        if i == j or i + j == n - 1:
#            print("X", end="")
#        else:
#            print("0", end="")
#        j += 1
#    print()
#    i += 1



##############6##############
###1###
#for#
#for i in range(5):
#    for j in range(5):
#        print("*", end="")
#    print()

#while#
#i = 0
#while i < 5:
#    j = 0
#    while j < 5:
#        print("*", end="")
#        j += 1
#    print()
#    i += 1

#while True#
#while True:
#    i = 0
#    while i < 5:
#        j = 0
#        while j < 5:
#            print("*", end="")
#            j += 1
#        print()
#        i += 1
#    break

###2###
#for#
#for i in range(1, 6):
#    for j in range(i):
#        print("*", end="")
#    print()

#while#
#i = 1
#while i <= 5:
#    j = 1
#    while j <= i:
#        print(chr(64 + j), end="")
#        j += 1
#    print()
#    i += 1

#while True#
#while True:
#    i = 1
#    while i <= 5:
#        j = 1
#        while j <= i:
#            print(chr(64 + j), end="")
#            j += 1
#        print()
#        i += 1
#    break

###3###
#for#
#for i in range(5, 0, -1):
#    for j in range(i):
#        print("*", end="")
#    print()

#while#
#i = 5
#while i >= 1:
#    j = 1
#    while j <= i:
#        print(chr(64 + j), end="")
#        j += 1
#    print()
#    i -= 1

#while True#
#while True:
#    i = 5
#    while i >= 1:
#        j = 1
#        while j <= i:
#            print(chr(64 + j), end="")
#            j += 1
#        print()
#        i -= 1
#    break



##############7##############
#for#
#for i in range(5):
#    print(random.randint(0, 9), end="")

#while#
#count = 0
#while count < 5:
#    number = random.randint(0, 9)
#    print(number, end="")
#    count += 1

#while True#
#while True:
#    count = 0
#    number_string = ""
#    while count < 5:
#        number = random.randint(0, 9)
#        number_string += str(number)
#        count += 1
#    print(number_string)
#    choice = input("Kas soovid jätkata? (jah/ei): ")
#    if choice.lower() != "jah":
#        break



##############8##############
#for#
#for i in range(1, 101):
#    if i % 2 == 0:
#        print(f"{i} on paaris arv")
#    else:
#        print(f"{i} on paaritu arv")
#paaris_arvud = len(range(2, 101, 2))
#paaritud_arvud = len(range(1, 101, 2))
#print(f"Paaris arvude arv: {paaris_arvud}")
#print(f"Paaritute arvude arv: {paaritud_arvud}")

#while#
#i = 1
#paaris_arvud = 0
#paaritud_arvud = 0
#while i <= 100:
#    if i % 2 == 0:
#        print(f"{i} on paaris arv")
#        paaris_arvud += 1
#    else:
#        print(f"{i} on paaritu arv")
#        paaritud_arvud += 1
#    i += 1
#print(f"Paaris arvude arv: {paaris_arvud}")
#print(f"Paaritute arvude arv: {paaritud_arvud}")
#while True#
#i = 1
#paaris_arvud = 0
#paaritud_arvud = 0

#while True:
#    if i > 100:
#        break
#    if i % 2 == 0:
#        print(f"{i} on paaris arv")
#        paaris_arvud += 1
#    else:
#        print(f"{i} on paaritu arv")
#        paaritud_arvud += 1
#    i += 1
#print(f"Paaris arvude arv: {paaris_arvud}")
#print(f"Paaritute arvude arv: {paaritud_arvud}")



##############9##############
#for#
#for i in range(1, 11):
#    print(f"5 x {i} = {5 * i}")

#while#
#i = 1
#while i <= 10:
#    print(f"5 x {i} = {5 * i}")
#    i += 1

#while True#
#i = 1
#while True:
#    if i > 10:
#        break
#    print(f"5 x {i} = {5 * i}")
#    i += 1



##############10##############
#for#
#for i in range(1, 101):
#    if i % 5 == 0:
#        print(i)

#while#
#i = 1
#while i <= 100:
#    if i % 5 == 0:
#        print(i)
#    i += 1

#while True#
#i = 1
#while True:
#    if i > 100:
#        break
#    if i % 5 == 0:
#        print(i)
#    i += 1

##############11##############
#for#
#number = random.randint(1, 10)

#for i in range(3):
#    guess = int(input("Arvake ära arv (1-10): "))
#    if guess == number:
#        print("Õige! Arvasite ära arvu", number)
#        break
#    else:
#        print("Vale arv, proovige uuesti!")
#else:
#    print("Kahjuks ei arvanud te arvu ära. Õige vastus oli", number)

#while#
#number = random.randint(1, 10)
#guesses_left = 3

#while guesses_left > 0:
#    guess = int(input("Arva ära arv vahemikus 1-10: "))
#    if guess == number:
#        print("Õige! Õnnitleme!")
#        break
#    else:
#        guesses_left -= 1
#        if guesses_left == 0:
#            print("Kahjuks ei arvanud sa õigesti. Õige arv oli", number)
#        else:
#            print("Vale arv! Sul on alles", guesses_left, "katset.")
#            play_again = input("Kas soovid veel arvata? (jah/ei) ")
#            if play_again.lower() == "jah":
#                continue
#            else:
#                break

#while True#
#number = randint(1, 10)

#while True:
#    guesses_left = 3
#    while guesses_left > 0:
#        guess = int(input("Arva ära arv vahemikus 1-10: "))
#        if guess == number:
#            print("Õige! Õnnitleme!")
#            break
#        else:
#            guesses_left -= 1
#            if guesses_left == 0:
#                print("Kahjuks ei arvanud sa õigesti. Õige arv oli", number)
#            else:
#                print("Vale arv! Sul on alles", guesses_left, "katset.")
#                play_again = input("Kas soovid veel arvata? (jah/ei) ")
#                if play_again.lower() == "jah":
#                    continue
#                else:
#                    break
#    play_again = input("Kas soovid uuesti mängida? (jah/ei) ")
#    if play_again.lower() == "jah":
#        number = random.randint(1, 10)
#        continue
#    else:
#        print("Aitäh mängimast!")
#        break



##############12##############
#for#
#algsumma = float(input("Sisestage algne summa: "))
#aastad = int(input("Sisestage aastate arv: "))

#print("Aasta\tAlgsumma\tIntress\t\tAasta lõpuks")
#kokku_intress = 0

#for i in range(1, aastad+1):
#    intress = round(algsumma * 0.05, 2)
#    lopusumma = round(algsumma + intress, 2)
#    kokku_intress += intress
#    print(f"{i}\t{algsumma:.2f}\t\t{intress:.2f}\t\t{lopusumma:.2f}")
#    algsumma = lopusumma

#kokku_summa = round(algsumma, 2)
#kokku_kasum = round(kokku_summa - algsumma, 2)

#print(f"Summa kokku: {kokku_summa:.2f}€")
#print(f"Kasum: {kokku_kasum:.2f}€")

#while#
#algsumma = float(input("Sisestage algne summa: "))
#aastad = int(input("Sisestage aastate arv: "))

#intress = 0.05
#aasta = 1
#summa = algsumma

#print("Aasta\tAlgsumma\tIntress\t\tAasta lõpuks")
#while aasta <= aastad:
#    intress_summa = summa * intress
#    summa += intress_summa
#    print(f"{aasta}\t{algsumma:.2f}\t\t{intress_summa:.2f}\t\t{summa:.2f}")
#    aasta += 1

#kokku_summa = summa
#kasum = kokku_summa - algsumma

#print(f"\nSumma kokku: {kokku_summa:.2f}€")
#print(f"Kasum: {kasum:.2f}€")

#while True#
#algsumma = float(input("Sisesta algne summa: "))
#aastad = int(input("Sisesta aastate arv: "))

#aasta = 1
#intress = algsumma * 0.05
#aastalõppsumma = algsumma + intress

#print("Aasta   Algsumma    Intress     Aasta lõpuks")
#print(f"{aasta:<8} {algsumma:<12.2f} {intress:<12.2f} {aastalõppsumma:<12.2f}")

#while True:
#    aasta += 1
#    algsumma = aastalõppsumma
#    intress = algsumma * 0.05
#    aastalõppsumma = algsumma + intress
#    print(f"{aasta:<8} {algsumma:<12.2f} {intress:<12.2f} {aastalõppsumma:<12.2f}")
    
#    if aasta == aastad:
#        break

#kokkusumma = round(aastalõppsumma, 2)
#kasum = round(aastalõppsumma - algsumma, 2)

#print(f"Summa kokku: {kokkusumma}€")
#print(f"Kasum: {kasum}€")



##############13##############
#for#
#print("Arv\tRuut\tKuup")
#for i in range(1, 11):
#    square = i ** 2
#    cube = i ** 3
#    print(f"{i}\t{square}\t{cube}")

#while#
#print("Arv\tRuut\tKuup")
#i = 1
#while i <= 10:
#    ruut = i**2
#    kuup = i**3
#    print(f"{i}\t{ruut}\t{kuup}")
#    i += 1

#while True#
#i = 1
#print("Arv\tRuut\tKuup")
#while True:
#    square = i**2
#    cube = i**3
#    print(f"{i}\t{square}\t{cube}")
#    i += 1
#    if i > 10:
#        break



##############14##############
#for#
#for i in range(1, 11):
#    for j in range(1, 11):
#        print("{:4}".format(i*j), end="")
#    print()

#while#i = 1
#while i <= 10:
#    j = 1
#    while j <= 10:
#        print("{:4d}".format(i*j), end="")
#        j += 1
#    i += 1
#    print()

#while True#
# defineerime muutujad
#row = 1
#col = 1

# loome tsükli, mis jookseb lõpmatuseni
#while True:

#     väljastame rea numbrid
#    if col == 1:
#        for i in range(1, 11):
#            print("{:<5}".format(i), end="")
#        print("\n")

#     väljastame ridade korrutised
#    print("{:<5}".format(row * col), end="")

#     läheme järgmisele veerule
#    col += 1

#     kui oleme jõudnud 10ni, läheme järgmisele reale
#    if col == 11:
#        print("\n")
#        row += 1
#        col = 1

#     kui oleme jõudnud reani 11, lõpetame tsükli
#    if row == 11:
#        break



##############15##############
#for#
#katsete_arv = 0
#while True:
#    vastus = input("Osta elevant ära! ")
#    katsete_arv += 1
#    if vastus.lower() == "elevant":
#        print("Õige vastus! Sul kulus", katsete_arv, "katset.")
#        break

#while True#
#kordused = 0
#while True:
#    vastus = input("Osta elevant ära! ")
#    kordused += 1
#    if vastus.lower() == "elevant":
#        print("Õige vastus! Sa ostsid elevanti!")
#        break
#print(f"Küsimust esitati {kordused} korda.")



##############16##############
#for#
#while#
#while True#



##############17##############


#height = int(input("Sisesta ridade arv: "))
#width = int(input("Sisesta veergude arv: "))

#square_size = 50


#screen = Screen()


#t = Turtle()


#for i in range(height):
#    for j in range(width):
#        t.penup()
#        t.goto(j * square_size, -i * square_size)
#        t.pendown()
#        for k in range(4):
#            t.forward(square_size)
#            t.left(90)


#done()



##############18##############
## Genereeri juhuslikud arvud N ja M
#N = randint(1, 10)
#M = randint(1, 10)

## Väljasta ruudud ja kuubid
#for i in range(1, max(N, M)+1):
#    if i <= N:
#        print(i**2, end=' ')
#    else:
#        print('  ', end=' ')
#    if i <= M:
#        print(i**3)



##############19##############

#n = int(input("Mitu arvu soovite sisestada? "))
#numbers = []

#for i in range(n):
#    num = float(input("Sisestage arv: "))
#    numbers.append(num)

#summa = sum(numbers)
#keskmine = summa / n
#korrutis = prod(numbers)
#geo_keskmine = pow(korrutis, 1/n)

#print("Summa:", summa)
#print("Aritmeetiline keskmine:", keskmine)
#print("Geomeetriline keskmine:", geo_keskmine)
#print("Korrutis:", korrutis)




##############20##############
#a = int(input("Sisesta esimene neljakohaline arv: "))
#b = int(input("Sisesta teine neljakohaline arv: "))
#c = int(input("Sisesta kolmas neljakohaline arv: "))
#d = int(input("Sisesta neljas neljakohaline arv: "))

#suurim = max(a*1000+b, b*1000+a, c*1000+d, d*1000+c)
#vaikseim = min(a*1000+b, b*1000+a, c*1000+d, d*1000+c)

#print("Suurim arv on:", suurim)
#print("Kõige väiksem arv on:", vaikseim)



##############21##############
#n = int(input("Mitu nime soovid sisestada? "))

#pikim_nimi = ""
#lyhim_nimi = "x" * 100  # Algväärtustame väga pika sõnega, et iga sisestatud sõna saaks seda lühema puhul asendada

#for i in range(n):
#    nimi = input("Sisesta nimi: ")
#    if len(nimi) > len(pikim_nimi):
#        pikim_nimi = nimi
#    if len(nimi) < len(lyhim_nimi):
#        lyhim_nimi = nimi

#print("Pikim nimi:", pikim_nimi)
#print("Lühim nimi:", lyhim_nimi)



##############22##############
#count = 0
#while True:
#    text = input("Arvuti kirjutab: Tahan kommi! ")
#    if text.lower() == "komm":
#        count += 1
#        break
#    else:
#        count += 1

#print("Kasutaja palus kommi {} korda.".format(count))