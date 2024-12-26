calls = 0
# Cоздаем функцию count_calls подсчитывающую вызовы остальных функций.
# Эта функция также должна вызываться в остальных двух функциях.
def count_calls ():
    global calls            # использования глобальной переменной внутри функции
    calls += 1              # изменяем значение переменной calls

# Создаем функцию string_info
# принимает аргумент - строку и возвращает кортеж из: длины этой строки, строку в верхнем регистре, строку в нижнем регистре
def string_info (string):
    string1 = str (string)
    result = (len (string1), string1.upper(), string1.lower())
    count_calls()
    return result

# Создаем функцию is_contains, которая принимает два аргумента: строку и список
def is_contains (string, list_to_search):
    string = str (string).lower()                           # приводим строку в один регистр
    list_to_search = list (list_to_search)
    count_calls()
    for i in range (len (list_to_search)):
        if str (list_to_search[i]).lower() == string:
            result = True
            break
        else:
            result = False
            continue
    return result


print (string_info('Capybara'))
print (string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))

print (calls)

# # 2 вариант
# calls = 0
# def count_calls ():
#     global calls
#     calls += 1
# def string_info (string):
#     count_calls()
#     return len(str(string)), str(string).lower(), str(string).upper()
# def is_contains (string, list_to_search):
#     count_calls()
#     str_list = list (list_to_search)
#     for i in range (len(str_list)):
#         str_list[i] = str (str_list[i]).upper()
#     return str_list.count(str(string).upper()) > 0
#
# print(string_info('Capybara'))
# print(string_info('Armageddon'))
# print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
# print(is_contains('cycle', ['recycling', 'cyclic']))
#
# print(calls)