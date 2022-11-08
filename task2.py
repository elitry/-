main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
def get_count_char(main_str):
    dictionary = {}
    for letter in main_str:
       if letter.isalpha():
         letter = letter.lower()
         if dictionary.get(letter):
           dictionary[letter] += 1
         else:
          dictionary[letter] = 1 # TODO посчитать количество каждой буквы в строке в аргументе str_
    return dictionary

def second(dict2, main_str):
    dictionary = {}
    mainlen = sum(dict2.values())#len(main_str)
    for letter, counts in dict2.items():
        dictionary[letter] = counts / mainlen * 100
    return dictionary

letdict = get_count_char(main_str)
letdict2 = second(letdict, main_str)

print(letdict)

