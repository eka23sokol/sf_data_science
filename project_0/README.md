# Проект 0. Угадай число

## Оглавление
[1. Описание проекта](https://github.com/eka23sokol/sf_data_science/tree/main/project_0/project_0/README.md#Описание-проекта)
[2. Какой кейс решаем?](https://github.com/eka23sokol/sf_data_science/tree/main/project_0/project_0/README.md#Какой-кейс-решаем)
[3. Краткая информация о данных](https://github.com/eka23sokol/sf_data_science/tree/main/project_0/project_0/README.md#Краткая-информация-о-данных)
[4. Этапы работы над проектом](https://github.com/eka23sokol/sf_data_science/tree/main/project_0/project_0/README.md#Этапы-работы-над-проектом)
[5. Результат](https://github.com/eka23sokol/sf_data_science/tree/main/project_0/project_0/README.md#Результат)
[6. Выводы](https://github.com/eka23sokol/sf_data_science/tree/main/project_0/project_0/README.md#Выводы)

### Описание проекта
Угадать загаданное компьютером число за минимальное число попыток.

:arrow_up: [к оглавлению](https://github.com/eka23sokol/sf_data_science/tree/main/project_0/project_0/README.md#Оглавление)

### Какой кейс решаем?
Нужно написать программу, которая угадывает число за минимальное число попыток.

**Условия соревнования:**
- Компьютер загадывает целое число от 0 до 100, и нам его нужно угадать. Под "угадать", подразумевается "написать программу, которая угадывает число".
- Алгоритм учитывает информацию о том, больше ли случайное число или меньше нужного нам.

**Метрика качества**
Результаты оцениваются по среднему количестуву попыток при 1000 повторений

**Что практикуем**
Учимся писать хороший код на Python

### Краткая информация о данных
Аргументом функции является рандомное число в интервале от 1 до 100.

:arrow_up: [к оглавлению](https://github.com/eka23sokol/sf_data_science/tree/main/project_0/project_0/README.md#Оглавление)

### Этапы работы над проектом  
Берём число из середины последовательности 50 и сравниваем с загаданным числом. Если не угадали, то у нас тогда останется ещё половина вариантов.

:arrow_up: [к оглавлению](https://github.com/eka23sokol/sf_data_science/tree/main/project_0/project_0/README.md#Оглавление)


### Результаты:  
В нашем алгоритме мы каждый раз делим оставшийся интервал на 2.

:arrow_up: [к оглавлению](https://github.com/eka23sokol/sf_data_science/tree/main/project_0/project_0/README.md#Оглавление)


### Выводы:  
Таким образом каждый раз отсекая половину интервала можно в разы сократить количество попыток нахождения загаданного числа.

:arrow_up: [к оглавлению](https://github.com/eka23sokol/sf_data_science/tree/main/project_0/project_0/README.md#Оглавление)


Если информация по этому проекту покажется вам интересной или полезной, то я буду очень вам благодарен, если отметите репозиторий и профиль ⭐️⭐️⭐️-дами