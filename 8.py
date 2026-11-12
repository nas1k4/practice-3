n = int(input())
count =0
a = 1 # будем ситать скольок раз нужно умножить 1 на 2 чтоб покрыть искомое число
while a < n:
    a *= 2
    count += 1
print(count)