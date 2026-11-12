a = float(input()) #первое значение темпиратуры
count = 0
while a != 0:
    b = float(input()) #следующее значение
    if b == 0:
        break
    elif a > b:
        count += 1
    a = b
print(count)
