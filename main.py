# Запрашиваем у пользователя ввод списка чисел
list_numbers = list(map(int, input("Введите список чисел через запятую: ").split(','))) 
 # Создаем новый список, содержащий квадраты всех чисел из первоначального списка, используя генератор списков.
list_numbers_square = [x**2 for x in list_numbers]
# Выводим новый список с квадратами чисел.
print("Список квадратов:", list_numbers_square) 