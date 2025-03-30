coordinates = (10, 20)
colors = "красный", "зелёный", "синий"  # Скобки можно не ставить
empty_tuple = ()

point = (3, 5)
print(point[0])  # 3 (индексация как в списках)

# point[0] = 7  # Ошибка! Кортеж нельзя изменить

x, y = point  # Распаковка кортежа
print(x, y)   # 3 5

numbers = (1, 2, 2, 3)
print(numbers.count(2))  # 2
print(numbers.index(3))  # 3

fruits = {"яблоко", "банан", "апельсин"}
empty_set = set()  # Пустое множество (не `{}` — это словарь!)

lst = [1, 2, 2, 3]
unique = set(lst)  # {1, 2, 3}

a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)  # {1, 2, 3, 4, 5} (объединение)
print(a & b)  # {3} (пересечение)
print(a - b)  # {1, 2} (разность)

nums = {1, 2, 3}
nums.add(4)      # {1, 2, 3, 4}
nums.discard(2)  # {1, 3, 4}

my_dict = {
    "яблоко": "apple",
    "собака": "dog",
    "книга": "book"
}

grades = {"Анна": 5, "Иван": 4, "Мария": 5}

phone_book = dict(Анна="123-456", Иван="789-012")

print(grades["Анна"])  # Выведет: 5

grades["Петр"] = 4  # Добавит нового ученика
grades["Иван"] = 3  # Изменит оценку Ивана

if "Мария" in grades:
    print("Мария есть в журнале!")

del grades["Иван"]  # Удалит Ивана из журнала

print(grades.keys())  # Выведет: ['Анна', 'Мария', 'Петр']

print(grades.values())  # Выведет: [5, 5, 4]

for name, grade in grades.items():
    print(f"{name}: {grade}")

