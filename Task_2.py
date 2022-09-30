# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Способ 1 (покороче). Не пойму, на что консоль ругается
# product = 1
# print((int(product * i) for i in range(1, int(input("Input some N: ") + 1))))

#Способ 2
user_num = int(input("Input some N: "))

product = 1

for i in range(1, user_num + 1):
    product *= i
    print(product, end = " ")
