# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны
# каждому из чисел в диапазоне от 2 до 9.

numbers = [i for i in range(2, 100)]

for i in range(2, 10):
    count = 0
    for j in numbers:
        if j % i == 0:
            count += 1
    print(f"числа кратные {i}, всего {count}")
