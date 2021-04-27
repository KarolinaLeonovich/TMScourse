# У нас есть кафе. Нам нужно написать программу для работы баристы.
# Перед тем как писать программу, надо создать тестовые данные.

# 1. Каждый день в кафе заходит от 5 до 20 покупателей. Каждый покупатель берёт от 1 до 3 чашек кофе.
# Нужно написать функцию, которая будет генерировать тестовые данные при каждом вызове.

import random


def order_function():
    customers_number = random.randrange(5, 21)
    coffee_list = [random.randrange(1, 4) for every_customer in range(customers_number)]
    return coffee_list



# 2. К каждой покупке нужно добавить дату и время до минуты (2 отдельные переменные).
# Время работы кафе - с 9 до 20 часов.
# может быть погрешность если вдруг сгенерировало одинаковое время

def time_function():
    coffee_list = order_function()
    times_list = []
    for every_custom in coffee_list:
        hours = random.randrange(9, 21)
        minutes = random.randrange(0, 60)
        times_list.append((hours, minutes))
        times_list.sort()
    return dict(zip(times_list, coffee_list))

print(time_function())

# 3. Кафе работает 5 дней в неделю. В конце недели надо составить отчёт по кол-ву клиентов и покупок.
def week_report_func():
    customers_number = 0
    cofee_cup_number = 0
    for i in range(5):
        coffee_time_dict = time_function()
        ashats = list(coffee_time_dict.values())
        customers_number += len(ashats)
        cofee_cup_number += sum(ashats)
    print(f"За неделю было {customers_number} покупателей. Куплено {cofee_cup_number} кофе.")

week_report_func()

# """Дополнительные задачи"""

# 4. Нужно посмотреть, в какое время дня у баристы были перерывы в работе.
# Для этого, нужно взять все покупки за каждый день, сравнить время между ними и отобразить промежутки больше часа.
#добавить с учетом начала и конца работы

def check_barista_function():
    coffee_time_dict = time_function()
    time_list = list(coffee_time_dict.keys())
    time_list.append((20, 0))
    time_list.insert(0, (9, 0))
    for each_ashat_number in range(len(time_list)-1):
        min1 = time_list[each_ashat_number+1][0] * 60 + time_list[each_ashat_number+1][1]
        min2 = time_list[each_ashat_number][0] * 60 + time_list[each_ashat_number][1]
        break_time = min1 - min2
        if break_time > 60:
            print(f"Обратите внимание! Промежуток между {time_list[each_ashat_number][0]}:{time_list[each_ashat_number][1]} и {time_list[each_ashat_number+1][0]}:{time_list[each_ashat_number+1][1]} - {break_time//60} часов {break_time%60} минут!")



# 5. После перерасчёта оказалось, что для окупаемости, каждый день в кафе должно продаваться не меньше 20 чашек кофе.
# Надо написать декоратор, который будет проверять кол-во чашек кофе на каждый день. И если их было меньше 20,
# возвращать сообщение с ошибкой (подсказка: try/except).


