import numpy as np

number = np.random.randint(1, 100+1)  # Загадали число
print("Загадано число от 1 до 100")
print(number) # Проверка загаданного числа
my_list = [i for i in range(1, 100+1)] # Записали диапазон чисел
start = 1 # Начало диапазона чисел
stop = 100 # Конец диапазона чисел


def midian(my_list, number, start, stop):
    mid = (start + stop) // 2 # Нахождение половины интервала

    if number == my_list[mid]:
        return mid
    elif number < my_list[mid]:
        return midian(my_list, number, start, mid - 1)
    else:
        return midian(my_list, number, mid + 1, stop)


x = midian(my_list, number, start, stop)


print(f"Вы угадали число {my_list[x]}")