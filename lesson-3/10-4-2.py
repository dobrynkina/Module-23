# Задача 2. Логирование
#
# Возможно, вы замечали, что некоторые программы не просто выдают ошибку и закрываются, но и записывают эту ошибку в файл.
# Таким образом проще сформировать отчёт об ошибках, а значит, программисту будет проще их исправить. Это называется логированием ошибок.
#
# Дан файл words.txt, в котором построчно записаны слова. Необходимо определить количество слов,
# из которых можно получить палиндром (привет предыдущим модулям).
# Если в строке встречается число, то программа выдаёт ошибку ValueError и записывает эту ошибку в файл errors.log

def pallindrome(string):
    dict_char = dict()
    count_n = 0
    check_p = False

    for sym in string:
        dict_char[sym] = dict_char.get(sym, 0) + 1

    for i in dict_char.values():
        if i % 2 != 0:
            count_n += 1

    if count_n <= 1:
        check_p = True

    return check_p


count_pallindrome = 0
file = open('words.txt', 'r', encoding='utf-8')

try:
    for i_str in file:
        i_str = i_str.rstrip()
        for i_sym in i_str:
            if i_sym.isdigit():
                raise ValueError
        if pallindrome(i_str):
            count_pallindrome += 1

except ValueError:
    error_log = open('error_log.txt', 'w', encoding='utf-8')
    error_log.write(str(ValueError) + "строка не полностью состоит из букв!")
else:
    print('Всего паллиндромов', count_pallindrome)
