# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
n = int(input("Введите целое число (>3)"))
l = []
m = 0
for i in range(-n, n):
    l.append(i)
m = l[2] * l[5] #не нашел ФАЙЛ file.txt
print("Ваш список ", l)
print("Произведение элементов списка ", m)