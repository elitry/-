def get_random_password(n = 8):
    import random
    propisniye = list(map(chr, range(ord('a'), ord('z'))))
    zaglavniye = list(map(chr, range(ord('A'), ord('Z'))))
    chisla = list(map(chr, range(ord('0'), ord('9')+1)))
    parol = list(map(chr, range(ord('a'), ord('z')))) + list(map(chr, range(ord('A'), ord('Z'))))+list(map(chr, range(ord('0'), ord('9')+1)))
    return ''.join(random.sample(parol, n))# TODO написать функцию генерации случайных паролей


print(get_random_password())
