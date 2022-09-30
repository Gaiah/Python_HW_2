# 3. Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.

user_num = int(input("Input some number: "))
sum_total = 0
for i in range(1, user_num + 1):
    sum_total += sum([round((1 + 1/i)**i, )])
    print(round((1 + 1/i)**i, ), end = " ")
print(f'    ->  Sum = {sum_total}')