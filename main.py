# TACK №1

name = input("Введіть своє ім'я: ")
age = int(input("Введвть свій вік: "))
if age < 0 and age > 130:
    print(f"Привіт, {name}! Твій вік — {age}.")
else:
    print("Помилка!")

# TACK №2.1

def hellow(name, age):
    print(f"Привіт, {name}! Твій вік — {age}.")

name = input("Введіть своє ім'я: ")
age = int(input("Введвть свій вік: "))

if age < 0 and age > 130:
    hellow(name, age)
else:
    print("Помилка!")

# TACK №2.2

def hellow(name, age):
    if age < 0 and age > 130:
        print(f"Привіт, {name}! Твій вік — {age}.")
    else:
        print("Помилка!")

name = input("Введіть своє ім'я: ")
age = int(input("Введвть свій вік: "))
hellow(name, age)

# TACK №3

try:
    my_list = []
    while True:
        num = int(input("Введіть додатнє число (або будь-яке від'ємне число для завершення): "))
        if num < 0:
            raise ValueError("Введено від'ємне число")
        my_list.append(num)
except ValueError as ve:
    print("Помилка:", ve)
finally:
    sum_of_numbers = sum(my_list)
    print("Сума всіх додатніх чисел:", sum_of_numbers)

# TACK №4.1

def removed(list):
    return sum(list)

try:
    my_list = []
    while True:
        num = int(input("Введіть додатнє число (або будь-яке від'ємне число для завершення): "))
        if num < 0:
            raise ValueError("Введено від'ємне число")
        my_list.append(num)
except ValueError as ve:
    print("Помилка:", ve)
finally:
    print("Сума всіх додатніх чисел:", removed(my_list))

# TACK №4.2

def main():
    numbers = []
    try:
        while True:
            num = float(input("Введіть додатнє число (або будь-що інше для завершення вводу): "))
            if num <= 0:
                raise ValueError("Введіть тільки додатні числа.")
            numbers.append(num)
    except ValueError as ve:
        print(f"Помилка: {ve}")
    
    if numbers:
        try:
            total_sum = sum(numbers)
            print(f"Сума всіх чисел: {total_sum}")
        except Exception as e:
            print(f"Помилка при розрахунку суми: {e}")

main() 