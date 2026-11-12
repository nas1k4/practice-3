n = int(input())
suma = 0
for a in range(0, n + 1): #перебирает первое число на костяшке и оно должно быть меньше второго
    for b in range(a, n + 1):
        suma += a + b
print(suma)