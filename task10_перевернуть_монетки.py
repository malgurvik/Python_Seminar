# Задача 10: На столе лежит количество n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2


# import random

coins = [0, 1, 0, 1, 1, 0, 0]
# eagle = coins.count(0)
# tail_of_coin = coins.count(1)
# if eagle <= tailOfCoin:
#     print(eagle)
# else:
#     print(tailOfCoin)

eagle=0
tail_of_coin=0
for coin in coins:
    if coin==0:
        eagle+=1
    else:
        tail_of_coin+=1
if eagle <= tail_of_coin:
    print(eagle)
else:
    print(tail_of_coin)