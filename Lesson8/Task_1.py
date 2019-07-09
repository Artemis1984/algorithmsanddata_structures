# Определение количества различных подстрок с использованием хеш-функции.
# Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.
# Пример работы функции:
# func("papa")
# 6
# func("sova")
# 9

import hashlib


def hash_func(string):

    string = string.replace(" ", "")
    hash_list = set()
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            if hashlib.sha1(string[i:j].encode("utf-8")).hexdigest() \
                    == hashlib.sha1(string.encode("utf-8")).hexdigest():
                continue
            hash_list.add(hashlib.sha1(string[i:j].encode("utf-8")).hexdigest())

    return len(hash_list)


word = "papa"
print(f"В тексте \'papa\' {hash_func(word)} подстрок")
word = "sova"
print(f"В тексте \'sova\' {hash_func(word)} подстрок")
while True:
    word = input("Введите текст: ")
    print(f"В тексте \'{word}\' {hash_func(word)} подстрок")
