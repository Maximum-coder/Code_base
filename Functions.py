def greeting(name):
    print(f"Привет, {name}!")

greeting("Саша")  # Выведет: Привет, Саша!

def plus(a, b):
    return a + b

result = plus(3, 5)
print(result)  # Выведет: 8

def multiply_by_two(x):
    return x * 2

print(multiply_by_two(5))  # 10

multiply_by_two = lambda x: x * 2
print(multiply_by_two(5))  # 10

print((lambda x: x * 2)(5))  # 10

people = [("Анна", 25), ("Петя", 17), ("Мария", 30)]
# Сортируем по возрасту (второй элемент в кортеже)
sort = sorted(people, key=lambda people: people[1])
print(sort)
# Вывод: [('Петя', 17), ('Анна', 25), ('Мария', 30)]
