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
    predict = 50
    
    while number != predict:
        count += 1
        if number > predict:
          predict += 25
          if number > predict:
            predict += 12
            if number > predict:
              predict += 6
              if number > predict:
                predict += 3
              elif number < predict:
                predict -= 3
            elif number < predict:
              predict -= 6
          elif number < predict:
            predict -= 12              
        elif number < predict:
          predict -= 25
    # Ваш код заканчивается здесь

    return count

def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score

print('Run benchmarking for game_core_v3: ', end='')
score_game(game_core_v3)