# Задача №11. Решение в группах
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6


number = int(input('Enter number A: '))
count = 2
temp1 = 1
temp2 = 0
result = 0

while nuber > result:
    count += 1
    result = temp1 + temp2
    temp2 = temp1
    temp1 = result
if nuber ==0:
    print(0)
elif nuber==1:
    print(1)
elif nuber == result:
    print(count)
else:
    print(-1)

# number = int(input("Введите число А: "))
#
# count = 2
# temp1, temp2 = 0, 1
#
#
# while temp1 + temp2 < number:
#     count += 1
#     temp1, temp2 = temp2, temp1 + temp2
#
# if number == 0:
#     print(f"Позиция 1")
# elif number == 1:
#     print(f"Позиция 2 или 3")
# elif number == temp1 + temp2:
#     print(f"Позиция {count}")
# else:
#     print("-1")



# number_a = int(input("Enter a number: "))
#
# fib_number, fib_number1 = 0, 1
# counter = 2
#
# while fib_number + fib_number1 < number_a:
#     fib_number, fib_number1 = fib_number1, fib_number + fib_number1
#     counter += 1
#
# if number_a == 0:
#     print(1)
# elif number_a == 1:
#     print("It can be either 2 or 3")
# elif fib_number + fib_number1 == number_a:
#     print(counter + 1)
# else:
#     print(-1)