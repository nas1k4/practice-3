n, k, r = map(int, input().split())
a = 1 # номер дня
l = n # длина нити
while l < r:
    l = l + (l * k / 100) # новая длина нити
    a += 1
print(a)