import numpy as np

       
def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)


def game_core(number):

    count = 1
    max_range=100
    min_range=0
    av_range=50
    while number != av_range:
        count+=1
        if number > av_range:
            min_range=av_range
        elif number < av_range: 
            max_range=av_range
        av_range=round((max_range+min_range)/2)
    return(count)

# Проверяем
score_game(game_core)
