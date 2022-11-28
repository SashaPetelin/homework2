
a = input("Введите число: ")

sum = 0
for i in str(a):
    if i != '.':
        sum += int(i)
print(sum)