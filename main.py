###
# Завдання 1
#
# У списку цілих, заповненому випадковими числами обчислити:
#
# ■ Суму негативних чисел;
#
# ■ Суму парних чисел;
#
# ■ Суму непарних чисел;
#
# ■ Добуток елементів з кратними індексами 3;
#
# ■ Добуток елементів між мінімальним та максимальним елементом;
#
# ■ Суму елементів, що знаходяться між першим та останнім позитивними елементами.
###

# # 1-5
# import random
#
# digits_number = 20
# numbers = []
#
# for i in range(digits_number):
#   numbers.append(random.randint (-10,10))
#
# print(numbers)
#
# negative_numbers = 0
# even_numbers = 0
# odd_numbers = 0
# multiples_of3 = 0
#
#
# for number in numbers:
#      if number < 0:
#         negative_numbers += number
#      if number % 2 == 0:
#         even_numbers += number
#      else:
#         odd_numbers += number
#      if i %3 == 0:
#         multiples_of3 += number
#
# print("Sum of negative numbers = ", negative_numbers)
# print("Sum of even numbers = ", even_numbers)
# print("Sum of odd numbers = ", odd_numbers)
# print("Sum of numbers multiple of 3 = ", multiples_of3)

# # 6

# import random
#
# digits_number = 20
# numbers = []
#
# for i in range(digits_number):
#   numbers.append(random.randint (0,10))
#
# print(numbers)
#
# smallest_number = min(numbers)
# largest_number = max(numbers)
#
# index_smallest_number = numbers.index(smallest_number)
# index_largest_number = numbers.index(largest_number)
#
# first_index = min(index_smallest_number,index_largest_number)
# last_index = max(index_largest_number,index_smallest_number)
#
# mul = 1
#
# for i in range(first_index + 1, last_index):
#   mul *= numbers[i]
#
# print("Multiplication of smallest and largest numbers = ", mul)

# # 7

import random

digits_number = 15
numbers = []

for i in range(digits_number):
  numbers.append(random.randint (-5,10))

print(numbers)

first_positive_index = None

for index in range(len(numbers)):
  if numbers[index] > 0:
    first_positive_index = index
    break

last_positive_index = None

for index in range(len(numbers) - 1, -1, -1):
  if numbers[index] > 0:
    last_positive_index = index
    break

positive_numbers_sum = 0

if first_positive_index is not None and last_positive_index is not None:
  for index in range(first_positive_index + 1, last_positive_index):
    positive_numbers_sum += numbers[index]

if first_positive_index is not None and last_positive_index is not None:
  print("Sum of first an last positive numbers:", positive_numbers_sum)
else:
  print("First or last positive number wasn't found")
  
  
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
  
  