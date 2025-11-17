print('"Как тебя зовут?"')
name=input()
print('"Отлично', name, 'Хочешь ли ты сыграть в', 'игру?"', sep='...')
print('Ответить:')
print('1- "Какая на# игра?"')
print('2- "Пошел ты"')
print('3- "Я тут привязан, у меня выбор есть?"')
fingers=10
answer=int(input())
if answer==1 or answer==2:
    fingers -= 1
    print('*Тебе отрезали 1 палец.*')
    print('"Ой, прости... Случайно нож уронил."')
elif answer==3:
    print('"Тоже верно."')
print('"Мы, а точнее ты будешь играть в самую обычную рулетку, только ставка- твои пальцы"')
print('"Что-ж, начнем..."')
flag=True
import random
while fingers>0:
    bet=int(input('"Делай ставку" '))
    if bet<=0 or bet>fingers:
        print('"Ты как это реализовать собрался?"')
        while bet<=0 or bet>fingers:
            bet=int(input('"Ставка:" '))
    num=int(input('"На какое число от 0 до 36 ставишь?" '))
    if num<0 or num>36:
        print('"Я сказал от 0 до 36"')
        while num<0 or num>36:
            num=int(input('Число: '))
    print('"Вращайте барабан."')
    roll=random.randint(0, 37)
    if num==0:
        num_col='зеленый'
    elif (1<=num<=10 or 19<=num<=28) and num%2==0 or (11<=num<=18 or 29<=num<=36) and not num%2==0:
            num_col='черный'
    else:
        num_col='красный'
    if roll==0:
        roll_col='зеленый'
    elif (1<=roll<=10 or 19<=roll<=28) and roll%2==0 or (11<=roll<=18 or 29<=roll<=36) and not roll%2==0:
        roll_col='черный'
    else:
        roll_col='красный'
    if num_col==roll_col:
        print('*Тебе не отрезали ниодного пальца*')
        print('"Повезло тебе"')
    else:
        fingers -= bet
        if bet==1:
            print('*Тебе отрезали 1 палец*')
        elif 2<=bet<=4:
            print('*Тебе отрезали', bet, 'пальца*')
        else:
            print('*Тебе отрезали', bet, 'пальцев*')
    if fingers<=0:
        flag=False
        break
print('"Повезло тебе, живой остался. А теперь беги, с#ка Форест, беги"')
print('*Ты все еще привязан к стулу*')
