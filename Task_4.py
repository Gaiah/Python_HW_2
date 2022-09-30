# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

from curses.ascii import isdigit


user_range_num = int(input("smth: "))
user_pos_1 = int(input("Input position 1 number: "))
user_pos_2 = int(input("Input position 2 number: "))

path = "file.txt"
data = open("file.txt", "w")
list = []
product = 1

for i in range(-user_range_num, user_range_num + 1):
        list.append(i)
print(list)

for i in range(1, user_range_num * 2 + 2):            # new range for file.txt
    i = str(i)
    data.write("\n")
    data.write(i)
data.close()


data = open("file.txt", "r")

for line in data:
    line = int(line)
    if line == user_pos_1:
        print(user_pos_1)
data.close()
## to be continued....