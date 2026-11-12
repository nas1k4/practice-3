while True:
    s = input("Введите число: ")

    if s.isdigit():
        print("Введено целое число:", s)
        break
    else:
        print("Ошибка. Попробуйте еще раз.", end=" ")