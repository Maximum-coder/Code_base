from multiprocessing.util import MAXFD

age = 15                 # int
temperature = 36.6       # float
message = 'Привет, мир!' # str
is_raining = False       # bool
passed_exam = True       # bool

n_1 = 1+1 # Сложение
n_2 = 1-1 # Вычитания
n_3 = 5*2 # Умножения
n_4 = 4.5/2 # Деление
n_5 = 10//3 # Целочисленное деление
n_6 = 15%4 # остаточное деление
n_7 = 5**3 # Возведение в степень

abs(-1)  # Число в модуле
min(10,1) # Поиск наименьшего числа
max(10,1) # Поиск наибольшего числа
round(5/3) # округление при деление в большую сторону
pow(5, 3) # Возведение в степень

string_1 = 'Hi ' + 'Maxim' #Конкатенация
string_2 = 'Hellow world!' * 3 #Умножение

type(age)
str(temperature)
float(age)
print(bool('1'))
print(bool(''))

password = input('Назовите пароль: ') # Тип данных str
password = int(input('Назовите пароль: '))# Тип данных int

name = input('Как вас зовут?')

print(f'Привет {name}')
print('Привет', name)

