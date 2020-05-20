from number import game_core

# Ask user to select a random number between 1 and 99.
number = int(input('Загадайте число от 1 до 99:\n'))

# Run the algorithm.
attempts_count = game_core(number)
print(f'Алгоритм угадал число за {attempts_count} попыток.')
