from math import sqrt
# input - функция, которая получает строку с клавиатуры
# int - функция, преобразующая в целое число

width = int(input())
height = int(input())

# f'' - форматированный вывод
print(f'Площадь = {width * height}')
print(f'Периметр = {(width + height) * 2}')