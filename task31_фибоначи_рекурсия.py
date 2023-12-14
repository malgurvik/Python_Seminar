# Задача №31. Решение в группах
# Последовательностью Фибоначчи называется
# последовательность чисел a0, a1, ..., an, ..., где a0 = 0,
# a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21

def fib(num):
    if num == 0 or num == 1:  # if num in (0, 1):
        return num
    return Fib(num - 1) + Fib(num - 2)

print(Fib(7))
