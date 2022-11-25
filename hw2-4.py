# Задайте список из N элементов, заполненных числами из промежутка 
# [-N, N].
# Найдите произведение элементов на указанных индексах. 
# Индексы вводятся одной строкой, через пробел.
# n = 3
# [-3, -2, -1, 0, 1, 2, 3]
# --> 0 2 3
# -3 * -1 * 0 = 0
# Вывод: 0

n = -1
while  n < 0:
    n = int(input('Введите положительное целое число членов последовательности '))

from random import randint
numbers = []
for i in range(n):
    numbers.append(randint (-n,n))
print(numbers)


mult = 1
y = input('введите позиции через пробел')
poz = y.split(" ")
for i in range(len(poz)):
    z = poz[i]
    mult = mult*numbers[int(z)]
print( mult)