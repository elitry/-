list_ = [8, 9, -5, -3, 1, -10, 8, -10, -5, 0, 5, -4, 0, 10, -8, 1, 6, -6, 6, -9]
# TODO найти сумму, количество и среднее арифметическое уникальных чисел
a = sum(set(list_))
print(a)
b = len(set(list_))
print(b)
d = (round(a/b, 5))
print(d)