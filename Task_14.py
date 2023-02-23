# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = int(input('Input a number: '))
number = 1
while number * 2 <= n:
    number *= 2
    print(number, end=' ☆ ')