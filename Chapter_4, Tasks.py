def avg(a, b, c):
    return (a + b + c) / 3

# Проверка работы функции
print(avg(2, 4, 9))  # Выведет: 5.0
print(avg(10, 20, 30))  # Выведет: 20.0
print(avg(5, 5, 5))  # Выведет: 5.0

def multiply_on_three(x):
    return x * 3

multiply_on_three = lambda x: x * 3
