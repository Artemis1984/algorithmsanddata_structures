# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

X = int(input("Введите номер буквы: "))
if 64 < X < 123:
    print("Под этим номером в алфавите стоит буква:", chr(X))
else:
    print("Введите другое число, под этим номером нет буквы!")

