# Посчитать четные и нечетные цифры введенного натурального числа. Например,
# если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

number = int(input("Введите натуральное число: "))
sepo = ","
print("четные цифры в числе: ", end="")
for num in str(number):
    if int(num) % 2 == 0:
        print(num, end=" ")

print()

print("нечетные цифры в числе: ", end="")
for num in str(number):
    if int(num) % 2 != 0:
        print(num, end=" ")
