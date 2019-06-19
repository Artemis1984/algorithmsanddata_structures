# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал
# (т.е. 4 числа) для каждого предприятия. Программа должна определить среднюю прибыль
# (за год для всех предприятий) и отдельно вывести наименования предприятий,
# чья прибыль выше среднего и ниже среднего.

from collections import namedtuple

Company = namedtuple("Company", "name, first, second, third, fourth")

num_of_comp = int(input("Введите количество предприятий: "))

all_companies = []
for i in range(num_of_comp):
    name = input(f"Введите имя {i + 1} предприятия: ")
    info = []
    for j in range(len(Company._fields) - 1):
        info.append(input(f"Введите прибыль за {j + 1} квартал: "))

    all_companies.append(Company(name, info[0], info[1], info[2], info[3]))

sum_ = 0

for i in all_companies:
    for j in range(1, len(i._fields)):
        sum_ += int(i[j])

print(f"Средняя прибыль за год всех компаний составляет: {sum_/len(all_companies)}$")

for i in all_companies:
    each_sum = 0
    for j in range(1, len(i._fields)):
        each_sum += int(i[j])

    if each_sum < sum_/len(all_companies):
        print(f"У компании {i.name} прибыль меньше среднего: {each_sum}$")
    elif each_sum > sum_/len(all_companies):
        print(f"У компании {i.name} прибыль больше среднего: {each_sum}$")
    else:
        print(f"У компании {i.name} прибыль равна среднему: {each_sum}$")




