# Определение количества различных подстрок с использованием хэш-функции.
# Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
# Требуется найти количество различных подстрок в этой строке.

def str_hash(s):
    p = 32  # len(whitespace)+len(ascii_lowercase)
    hash = 0
    size = 10000
    for i in range(len(s)):
        hash += (ord(s[i]) - ord('a') + 1) * p ** i
    return hash % size


def get_substrings_count(s):
    lst = set()

    for i in range(len(s)-1):
        for j in range(i+1, len(s)+1):
            lst.add(str_hash(s[i:j]))
    return len(lst)-1  # Не учитываем саму строку


print(get_substrings_count("papa"))
