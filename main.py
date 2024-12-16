len = int(input("Введите длину массива: ")) #ввод числа для длинны массива
numbers=[0]*len 
for i in range (0,len): #создание списка прогрессии
    numbers[i] = int(input("Введите число: ")) #ввод числа
numbers_2=[0]*len 
for i in range(0,len): #создание списка прогрессии
    numbers_2[i] = pow(numbers[i],2) #возведение в квадрат чисел
print(numbers_2) #вывод на экран
