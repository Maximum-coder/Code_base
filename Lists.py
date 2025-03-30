fruits = ["яблоко", "банан", "апельсин"]  # Строки
numbers = [1, 2, 3, 4, 5]                 # Числа
mixed = [1, "текст", True, 3.14]          # Разные типы
empty = []                                # Пустой список

fruits = ["яблоко", "банан", "апельсин"]

print(fruits[0])   # "яблоко" (первый элемент)
print(fruits[-1])  # "апельсин" (последний элемент)

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numbers[2:5])    # [2, 3, 4] (элементы с 2 по 4)
print(numbers[:3])     # [0, 1, 2] (первые 3 элемента)
print(numbers[5:])     # [5, 6, 7, 8, 9] (с 5 до конца)
print(numbers[::2])    # [0, 2, 4, 6, 8] (каждый второй)
print(numbers[::-1])   # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] (разворот)

fruits = ["яблоко", "банан"]
fruits.append("киви")
print(fruits)  # ["яблоко", "банан", "киви"]

fruits = ["яблоко", "банан", "киви"]
fruits.remove("банан")
print(fruits)  # ["яблоко", "киви"]

numbers = [3, 1, 4, 2]
numbers.sort()
print(numbers)  # [1, 2, 3, 4] (по возрастанию)

fruits = ["яблоко", "банан", "Апельсин"]
fruits.sort()
print(fruits)  # ['Апельсин', 'банан', 'яблоко'] (по алфавиту, учитывая регистр)
