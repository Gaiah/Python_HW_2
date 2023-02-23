# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите
# минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

qnt = int(input('Input the quantity of coins: '))
count = 0
for i in range(qnt):
    num = int(input('Input 0 for side A and 1 for side B: '))
    if num == 0:
        count += 1

if count <= qnt - count:
    print(f'You should flip {count} coins. ')
else:
    print(f'You should flip {qnt - count} coins. ')