n = int(input())
for i in range(2, n + 1):
    for j in range(2, i):
        #если число делится на что-то без остатка от прерываем проверку
        if i % j == 0:
            break
    else:
        print(i)