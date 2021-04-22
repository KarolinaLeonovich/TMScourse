from random import choice, randrange
import copy

fruit = ('apple', 'pear', 'cherry', 'banana', 12)
vegetables = ['tomato', 'onion', 'carrot', 17]
berries = ('blueberry', 'cranberry', 'watermelon', 8)


'''
Обязательные задачи
'''
# 1. На склад поступил новый товар. Надо пересмотреть склад и исправить ошибки, сделать первую товара букву заглавной.
# Все типы товаров должны быть неизменяемыми, чтобы кто-то случайно не перепутал их снова.
def revise_func(array):
    temp_list = list(array)
    new_temp_list = []
    for i in temp_list:
        if type(i) is str:
            i = i.title()
            new_temp_list.append(i)
        else:
            new_temp_list.append(i)
    final_tuple = tuple(new_temp_list)
    return final_tuple

fruit = revise_func(fruit)
print(fruit)
vegetables = revise_func(vegetables)
print (vegetables)
berries = revise_func(berries)
print(berries)


# В овощи забыли добавить капусту. Цифра в категории - это цена товара этого типа.
def add_new_position_func(goods_tuple, position):
    temp_array = list(goods_tuple)
    temp_array.insert(-1, position.title())
    return(tuple(temp_array))

vegetables = add_new_position_func(vegetables, "cabbage")
print(vegetables)


# 2. Для удобства хранения, нужно объединить все товары в один объект, при этом сохранить структуру типов.

def tuple_to_dict_func(*arrays):
    return dict((name, eval(name)) for name in arrays)
#fruit vegetables berries

goods_dictionary = tuple_to_dict_func("fruit", "vegetables", "berries")
print(goods_dictionary)


# 3. На складе закончились морковка и арбузы. Надо перенести их в категорию "finished".
finished = ()
goods_dictionary.update(tuple_to_dict_func("finished"))
print(goods_dictionary)

def finished_goods_func(storage, goods):
    storage["finished"] = list(storage["finished"])
    print(storage["finished"])
    for k, v in storage.items():
        storage[k] = list(v)
    for k, v in storage.items():
        if goods in v:
            storage["finished"].append(v.pop(v.index(goods)))
        else:
            pass
# у меня не получилось в 1 цикл(((
finished_goods_func(goods_dictionary, "Carrot")
finished_goods_func(goods_dictionary, "Watermelon")
print(goods_dictionary)

# 4. Если название продукта длиннее 6 символов, нужно отображать только первые 6.
# Рассчитать и вывести на экран стоимость каждого отдельного продукта.
def print_recipe_func(storage):
    storage_temp = copy.copy(storage)
    del storage_temp["finished"]
    for v in storage_temp.values():
        price = v[-1]
        for i in range(len(v)-1):
            print(f"{v[i][:5]} - {price} dollars.")

print_recipe_func(goods_dictionary)

'''
Дополнительные задачи:
'''
# 5. На все товары, где есть буква "r", нужно сделать скидку в 20%.
# А если их 2, то 25,5%, и сумму округлить до 2 символов после запятой.
def discount_func(storage):
    storage_temp = copy.copy(storage)
    del storage_temp["finished"]
    for v in storage_temp.values():
        price = v[-1]
        for i in range(len(v)-1):
            if v[i].count("r") == 2:
                disc255_price = round((price*0.255), 2)
                print(f"{v[i][:5]} - {disc255_price} dollars. DISCOUNT 25,5%")
            elif v[i].count("r") == 1:
                disc20_price = round((price * 0.2), 2)
                print(f"{v[i][:5]} - {disc20_price} dollars.DISCOUNT 20%")
            else:
                print(f"{v[i][:5]} - {price} dollars.")

discount_func(goods_dictionary)


# 6. Когда кто-то покупает товар, на экране должен отобразиться чек с товаром, кол-вом и суммой.
# product_list = []   # В эту переменную нужно добавить все актуальные товары
# order = {choice(product_list): randrange(10)}     # Заказ на товар и кол-во

def order_func(storage):
    storage_temp = copy.copy(storage)
    del storage_temp["finished"]
    product_list = []
    for v in storage_temp.values():
        for i in range(len(v) - 1):
            product_list.append(v[i])
    order = {choice(product_list): randrange(1, 10)}
    print(order)
    good, quantity = order.popitem()
    for v in storage_temp.values():
        for i in range(len(v)):
            if v[i] == good:
                price = v[-1]
    total_price = price * quantity
    print(f"Чек: {good} - {quantity} штук. С вас {total_price} долларов.")


order_func(goods_dictionary)


