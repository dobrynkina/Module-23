# Задача 2. Возраст
#
# Дан файл ages.txt, в котором построчно хранятся десять возрастов для каждого человека.
#
# Напишите программу, которая считывает файл, даёт имя для каждого возраста (можно просто использовать буквы алфавита)
# и выводит результат в новый файл result.txt в формате «имя — возраст». Программа должна обрабатывать следующие ошибки
# и выводить сообщение на экран:
#
# Попытка создания файла, который уже существует.
# На чтение ожидался файл, но это оказалась директория.
# Неверный тип данных и некорректное значение (две ошибки обрабатываются одинаково).
# При желании воспользуйтесь подсказкой, чтобы найти подходящие имена ошибок.

import random

try:
    file_age = open('ages.txt', 'r', encoding='utf-8')
    file_result = open('result.txt', 'x', encoding='utf-8')

    try:
        for age in file_age:
            randomUpperLetter = chr(random.randint(ord('A'), ord('Z')))
            str_a = f'{randomUpperLetter} : {int(age)}'
            file_result.write(str_a + '\n')
    except (ValueError, TypeError):
        print('Неверный тип данных или некорректное значение')

    file_result.close()
    file_age.close()

except (IsADirectoryError, FileNotFoundError, PermissionError):
    print('Отсутствует файл ages.txt')
except FileExistsError:
    print('Файл уже существует')

