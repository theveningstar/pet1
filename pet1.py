import random
import time
import array

def intro(): #OK
    time.sleep(1)
    print('Вы попали в мистический лабиринт. Он кишит мертвецами, змеями и бездонными ямами')
    time.sleep(2)
    print('Сможете ли вы выйти...')
    time.sleep(3)
    print('ЖИВЫМИ') 

def horror():
    bla = ['Вас укусило чудовище', 'Вы упали в яму', 'С потолка свалилась ядовитая змея']
    boo = random.choice(bla)
    print(boo)

wanna = 'Д' #OK
while wanna == 'Д' or wanna == 'Y':
    intro()
    from random import randint
    N = 10
    A = [0] * N
    for i in range (N):
        A[i] = randint(1, 3)
    print("Вы в самом центе лабиринта: введите число от 1 до 3 чтобы выбрать коридор")
    
    for i in range (8):
        gamer = input()
        if gamer == A[i]:
            print ('Вы уверенно движетесь вперед')
        else:
            horror()         
        
    gamer = input()
    if gamer == A[9]:
        print('Ура! Свобода!')
    else:
        print('А свобода была так близка...')

    print('Хотите сыграть еще? (Д или Н)')
    wanna = input()
