# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

print(sum([int(i) for i in input("Input some number: ") if i.isdigit()]))