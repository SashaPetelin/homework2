# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

import math

n = int(input("Введите число: "))
print()
for i in range(1, n+1):
    print(math.factorial(i), end=' ')

