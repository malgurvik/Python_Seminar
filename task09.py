# Задача №9. Решение в группах
# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while
# Input: 5
# Output: 120


n = int(input('Enter number: '))
# i = 1
result = 1
while n > 0:
    result *= n
    n -= 1
# while i <= n:
#     result *= i
#     i += 1
print(result)
