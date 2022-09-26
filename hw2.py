# Задача 43: Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# Пример:
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

import random as r

some_line = [ r.randint(0, i) for i in range(int(input('Введите количество числе последовательности = ')))]

rez = []
for i in range(len(some_line)-1):
    k = some_line[i]
    for j in range(i+1 , len(some_line)):
        if k== some_line[j]:
            rez.append(some_line[j])
print(f'{some_line} => {list(set(some_line).difference(set(rez)))}')
