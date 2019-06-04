# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и
# позицию в массиве. Примечание к задаче: пожалуйста не путайте «минимальный» и
# «максимальный отрицательный». Это два абсолютно разных значения.
import random

rand_list = [random.randint(-50, 50) for i in range(25)]
print(rand_list)
min_max = -100
min_max_index = None

for i in rand_list:
    if min_max < i < 0:
        min_max = i
        min_max_index = rand_list.index(i)

print(f"максимальный отрицательный элемент в масиве это {min_max}, под индексом {min_max_index}")




