# Игра: Угадай число

## Задача
Угадать загаданное компьютером число за минимальное число попыток.

## Условия
Компьютер загадывает целое число от 0 до 100, и нам его нужно угадать. Под «угадать», конечно, подразумевается «написать программу, которая угадывает число».
Алгоритм учитывает информацию о том, больше ли случайное число или меньше нужного нам.
## Решение
Решение использует двоичный (бинарный) поиск (также известен как метод деления пополам или дихотомия) — классический алгоритм поиска элемента в отсортированном массиве (векторе), использующий дробление массива на половины.

### Поиск элемента в отсортированном массиве
1. Определение значения элемента в середине структуры данных. Полученное значение сравнивается с ключом.
2. Если ключ меньше значения середины, то поиск осуществляется в первой половине элементов, иначе — во второй.
3. Поиск сводится к тому, что вновь определяется значение серединного элемента в выбранной половине и сравнивается с ключом.
4. Процесс продолжается до тех пор, пока не будет найден элемент со значением ключа или не станет пустым интервал для поиска.
