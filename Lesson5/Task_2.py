# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как
# [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque


hex_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

while True:

    memo_number = 0
    result = deque()
    number2 = deque(str.upper(input("Введите первое шестнадцатеричное число: ")))
    number1 = deque(str.upper(input("Введите второе шестнадцатеричное число: ")))

    if len(number1) > len(number2):
        number2.extendleft('0' * (len(number1) - len(number2)))
    elif len(number2) > len(number1):
        number1.extendleft('0' * (len(number2) - len(number1)))

    for i in range(len(number1) - 1, -1, -1):

        if number1[i] in hex_numbers and number2[i] in hex_numbers:

            repo = hex_numbers.index(number1[i]) + hex_numbers.index(number2[i])

            if repo > len(hex_numbers) - 1:

                result.appendleft(hex_numbers[repo - len(hex_numbers) + memo_number])
                memo_number = 1

            else:
                if repo + memo_number > len(hex_numbers) - 1:
                    result.appendleft('0')
                else:
                    result.appendleft(hex_numbers[repo + memo_number])
                    memo_number = 0

    if memo_number == 1:
        result.appendleft(memo_number)

    print(*result)


