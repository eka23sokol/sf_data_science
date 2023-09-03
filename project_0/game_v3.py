"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np

""" Функция, которая угадывает загаданное число меньше, чем за 20 попыток!
"""

def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Ваш код начинается здесь
    count = 0
    # Создадим список в интервале от 1 до 100
    a = list(range(1,101))
    
    # Находим средний элемент последовательности
    left = 0
    right = len(a)
    center = (left + right) // 2
    
    # Значение среднего элемента сравнивается с искомым значением. 
    # Если значение среднего элемента оказывается равным искомому, поиск завершается.
     
    while number != a[center]:
      count += 1
      if number > a[center]:
        left = center + 1
      else:
        right = center - 1
      center = (left + right) // 2
      if left >= right:
        break
    # Ваш код заканчивается здесь

    return count

def score_game(game_core_v3) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        game_core_v3 ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(game_core_v3(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score

print('Run benchmarking for game_core_v3: ', end='')
score_game(game_core_v3)