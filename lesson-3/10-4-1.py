# Задача 1. Имена
#
# В базе данных одной компании есть баг (или, может быть, фича): если ввести туда имя сотрудника меньше чем из трёх букв,
# то база сломается и упадёт. Как компания принимает на работу людей, например, с китайскими именами, непонятно.
#
# Дан файл people.txt, в котором построчно хранится N имён пользователей.
#
# Напишите программу, которая берёт количество символов в каждой строке файла и в качестве ответа выводит общую сумму.
# Если в какой-либо строке меньше трёх символов (не считая литерала \n), то вызывается ошибка, и программа завершается.
#
# Файл people.txt создать можно вручную или кодом.

count_sym = 0

try:
    f_people = open('people.txt', 'r', encoding='utf-8')

    for i_man in f_people:
        i_man = i_man.rstrip()
        if len(i_man) < 3:
            raise BaseException('Длина строки меньше 3 символов')
        count_sym += len(i_man)

    print('Сумма символов', count_sym)

except FileExistsError:
    print('Такой файл не существует')
else:
    print('Успешное выполнение задачи')
    f_people.close()
finally:
    if not f_people.closed:
        f_people.close()
    print('Конец')
