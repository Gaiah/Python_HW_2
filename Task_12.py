# Задача 12: Петя задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя
# делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите отгадать задуманные Петей числа.

product = int(input('Input the product of numbers A and B: '))
sum_a = int(input('Input the sum of numbers A and B: '))
a = 1
while a < product:
    if product / a + a == sum_a:
        print(f'Your A is: {a} and your B is: {product // a} .')
        break
    else:
        a += 1
else:
    print('Incorrect data')