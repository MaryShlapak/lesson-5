# Завдання 2
#
# Є список цілих, заповнений випадковими числами.
#
# На підставі даних цього масиву потрібно:
#
# ■ Створити список цілих, що містить лише парні числа з першого списку;
#
# ■ Створити список цілих, що містить лише непарні числа з першого списку;
#
# ■ Створити список цілих, що містить лише негативні числа з першого списку;
#
# ■ Створити список цілих, що містить лише позитивні числа з першого списку.


import random

digits_number = 20
numbers = []

for i in range(digits_number):
    numbers.append(random.randint(-10,10))

print(numbers)

even_numbers = [number for number in numbers if number % 2 == 0]

odd_numbers = [number for number in numbers if number % 2 != 0]

negative_numbers = [number for number in numbers if number < 0]

positive_numbers = [number for number in numbers if number > 0] 

# друзі-айтішники підказали, що можна отак в рядок записувати. Не знаю чи це коректно але працює

print("List of even numbers:", even_numbers)
print("List of odd numbers:", odd_numbers)
print("List of negative numbers:", negative_numbers)
print("List of positive numbers:", positive_numbers)