# Вывести числа от 1 до 5
for i in range(1, 6):  # range(старт, стоп+1)
    print(i)

# Перебрать все буквы в слове
word = "Привет"
for letter in word:
    print(letter)

count = 0
while count < 5:
    print(count)
    count += 1  # увеличиваем count на 1

password = ""
while password != "12345":
    password = input("Введите пароль: ")
print("Добро пожаловать!")

for num in range(10):
    if num == 5:
        break  # выход при num=5
    print(num)  # выведет 0 1 2 3 4
