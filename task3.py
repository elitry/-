def get_unique_list_numbers():
    import random
    listik = []
    while len(listik) < 15:
     n = random.randint(-10,10)
     if n not in listik:
      listik.append(n)
    return listik# TODO написать функцию для получения списка уникальных целых чисел


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
