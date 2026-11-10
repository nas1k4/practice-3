x = int(input('Введите натуральное число '))
cnt = 0
if x <= 0:
    print('Вы ввели не натуральное число')
else:
    for a in range(1, x + 1):
        for b in range(1, x + 1):
            if a**2 + b**2 == x and a <= b:
                cnt += 1
    print(cnt)