import math
# 1 Массив чисел, найти сумму чисел, через циклы и рекурсию
# a_list = [1,2,3,4,5,6,7,8,9]
#sum = 0
#========================================================for
# for i in a_list:
#     sum += i
# print(sum)
#========================================================while
# while a_list:
#     sum = sum + a_list.pop()
# print(sum)
#========================================================recursion
# def recursion(work_list,sum = 0):
#     if work_list:
#         sum += work_list.pop()
#         return recursion(work_list, sum)
#     else:
#         print(sum)
#         return sum
# recursion(work_list=a_list)
#========================================================
# 2. [1,2,3] + [11,22,33] = [1,11,2,22,3,33]
# a_list = [1,2,3]
# b_list = [11,22,33]
# c_list = []
# for i in range(len(a_list)):
#     c_list.append(a_list[i])
#     c_list.append(b_list[i])
# print(c_list)
#========================================================
#3.Существует ли треугольник с заданными сторонами
# a_l = int(input("Введите сторону А:"))
# b_l = int(input("Введите сторону В:"))
# c_l = int(input("Введите сторону С:"))
# if (a_l+b_l) > c_l:
#     print("Существует")
# elif (c_l+a_l) > b_l:
#     print("существует")
# else:
#     print("No")
#========================================================
# x = float(input('Введите координаты широты точки А: '))
# y = float(input('Введите координаты долготы точки А: '))
# x1 = float(input('Введите координаты широты точки В: '))
# y1 = float(input('Введите координаты долготы точки В: '))
# R = 6371
# a_tuple = (x, x1)
# b_tuple = (y, y1)
#
# d = math.sin(x) * math.sin(x1) + math.cos(x) * math.cos(x1) * math.cos(y - y1)
# d = math.acos(math.cos(d))
# L = d * R
# L = L/10
# print(math.cos(d))
# print(d)
# print('Расстояние между точками А и В = ' + str(L) + ' км.')
#########################################################################

#Проверка, может ли быть решён такой пример

#
# a = int(input('Введите начало диапазона "a" : '))
# a1 = int(input('Введите конец диапазона "a" : '))
# b = int(input('Введите начало диапазона "b" : '))
# b1 = int(input('Введите конец диапазона "b" : '))
# c = int(input('Введите начало диапазона "с" : '))
# c1 = int(input('Введите конец диапазона "с" : '))
# #D = b * b - 4 * a * c
# a_list = []
# b_list = []
# c_list = []
#
# for i in range(a, a1 + 1):
#     for dis in range(b, b1+1):
#         for dis2 in range(c, c1+1):
#             D = dis ** 2 - 4 * i * dis2
#             if D > 0:
#                 a_list.append(D)
#                 print('Дискриминант равен -' , [D] , 'Cуществуют вещественные корни, график квадратичной функции пересекает ось Х в двух местах.')
#             elif D < 0:
#                 b_list.append(D)
#                 print('Дискриминант равен -' , [D] ,'Не существует вещественных корней, а только комплексные корни. График функции не пересекает ось Х.')
#             else:
#                 c_list.append(D)
#                 print('Дискриминант равен -' , [D] ,'Cуществует один вещественный корень, график функции пересекает ось Х в одном месте.')
# print(a_list)
# print(b_list)
# print(c_list)

#########################################################################

# Заменить "?" на "*"

# m = int(input("Введите кол-во строк: "))
# a_list = []
# for i in range(m):
#    a_str = input("Введите строку: ")
#    a_list.append(a_str.replace('?','*'))
# print(a_list)


#########################################################################


# 2009-06-15 ---> 15/06/2009


#a = "2009-06-15"
#b = "{}/{}/{}"
#a_list = a.split('-')
#a_list.reverse()
#b.format(a_list[0], a_list[1], a_list[2])
#print(b.format(a_list[0], a_list[1], a_list[2]))


#########################################################################

#Определить вес в тоннах и килограммах


#a = int(input("Введите вес: "))
#a_copy = a
#b = a / 1000
#c = a_copy / 10000
#print("Ваш вес в тоннах - ",c)
#print("Ваш вес в килограммах - ",b)


#########################################################################

# Пройдёт ли коробка в дверь

# a = int(input("Введите высоту коробки: "))
# b = int(input("Введите ширину коробки: "))
# c = int(input("Введите длинну коробки: "))
# a_d = 90
# b_d = 50
# if a < a_d and b < b_d:
#     print("Коробка пройдёт.")
# elif c < a_d and b < b_d:
#     print("Коробка пройдёт.")
# else:
#     print("Нет")

#########################################################################

#Высверлить квадрат в бруске

# a = int(input("Введите ширину бруса: "))
# d = float(input("Введите диаметр бревна: "))
# c = math.sqrt(a*a*2)
# if c<=d:
#     print("Можем")
# else:
#     print("Нет")


#########################################################################
# вагон(четные - верхние места, нечетные - нижние)

# print('Стандартный вагон имеет 54 места.')
# a = int(input('Введите номер в плацкартном вагоне для определения места: '))
# if a > 36 and a %2 == 0:
#     print('Ваше место верхнее и боковое!')
# elif a <= 36 and a %2 == 0:
#     print('Ваше место верхнее и в купе!')
# elif a <= 36 and a %2 != 0:
#     print('Ваше место нижнее и в купе!')
# elif a > 36 and a %2 != 0:
#     print('Ваше место нижнее и боковое!')
# else:
#     print('Вы ввели неверное место в вагоне.')


#########################################################################

# Размен купюрами 500,100,10,2
# m500 = 0
# m100 = 0
# m10 = 0
# m2 = 0
#
# money_input = int(input('Введите данные для размена купюрами 500,100,10 и 2: '))
# if money_input > 0:
#     money_output = money_input
#     m500 = money_output / 500
#     money_output = money_output % 500
#     m100 = money_output / 100
#     money_output = money_output % 100
#     m10 = money_output / 10
#     money_output = money_output % 10
#     m2 = money_output / 2
#     money_output = money_output % 2
#     m500 = math.floor(m500)
#     m100 = math.floor(m100)
#     m10 = math.floor(m10)
#     m2 = math.floor(m2)
#     # print(m500)
#     # print(m100)
#     # print(m10)
#     # print(m2)
#     # print(money_input)
#     print('Полученные купюры при обмене', money_input, ':''\n', m500, 'купюр - по 500грн''\n', m100, 'купюр - по 100грн''\n', m10, 'купюр - по 10грн'
#           '\n', m2, 'монет - по 2грн')
#     if money_output > 0:
#         print("Разменный пункт не смог разменять эти деньги -->", money_output, 'грн')
#     else:
#         print('Работа разменного пункта завершена.')
# else:
#     print('Введены неверные данные!')

#########################################################################

# n - простое или нет?

########################################################################

# Таблица умножения от а до b

# num_1 = int(input('input start: '))
# num_2 = int(input('input end: '))
# num_mnoj = int(input('input num "*": '))
# for i in range(num_1, num_2+1):
#     print('{} * {} = {}'.format(num_mnoj, i, num_mnoj*i))

########################################################################

# A[1] ↔ A[2]; A[3] ↔ A[4]

n = [input('Введите кол-во элементов: ')]
for i in n:
    print(i)



