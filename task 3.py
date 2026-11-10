while True:
    num = int(input("Введите число: "))
    root = int(num ** 0.5)

    if root * root == num:
        print(f"Число {num} является полным квадратом!")
        break
    else:
        print(f"Число {num} НЕ является полным квадратом. Попробуйте еще раз.")