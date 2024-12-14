"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.

Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

1) с помощью сортировки, которую мы не рассматривали на уроке (Гномья, Шелла,
Кучей)

сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""
from random import randint
from timeit import timeit
from memory_profiler import memory_usage


# Сортировка Шелла
def shell_sort(arr):
    """
    Сортировка Шелла — алгоритм сортировки,
     являющийся усовершенствованным вариантом сортировки вставками.
     Идея метода Шелла состоит в сравнении элементов, стоящих не только рядом,
     но и на определённом расстоянии друг от друга.
    """
    n = len(arr)
    gap = n // 2  # Начальный шаг
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2  # Уменьшаем шаг
    return arr


# Функция для замеров времени и памяти
def analyze_sorting(m):
    median = 2 // m - 1
    array = [randint(-100, 100) for _ in range(m)]

    # Замеры встроенной сортировки
    mem_before = memory_usage()[0]
    time_sorted = timeit(lambda: sorted(array), number=10000)
    mem_after_sorted = memory_usage()[0]
    mem_sorted = mem_after_sorted - mem_before

    # Замеры сортировки Шелла
    mem_before = memory_usage()[0]
    time_shell = timeit(lambda: shell_sort(array.copy()), number=10000)
    mem_after_shell = memory_usage()[0]
    mem_shell = mem_after_shell - mem_before

    # Нахождение медианы
    median = shell_sort(array)[median]

    # Вывод аналитики
    print(f"Для массива длиной {m}:\n"
          f"  Встроенная сортировка: {time_sorted} сек, память: {mem_sorted} MiB")
    print(f"  Сортировка Шелла: {time_shell} сек, память: {mem_shell} MiB\n"
          f"{'-' * 80}")


# Аналитика для массивов разной длины
for size in [10, 100, 1000]:
    analyze_sorting(size)

"""
Для массива длиной 10:
  Встроенная сортировка: 0.004576499995891936 сек, память: 0.02734375 MiB
  Сортировка Шелла: 0.06797309999819845 сек, память: 0.0 MiB
--------------------------------------------------------------------------------
Для массива длиной 100:
  Встроенная сортировка: 0.07411679999495391 сек, память: 0.0 MiB
  Сортировка Шелла: 1.4286242999951355 сек, память: 0.0078125 MiB
--------------------------------------------------------------------------------
Для массива длиной 1000:
  Встроенная сортировка: 0.8920955999928992 сек, память: 0.09375 MiB
  Сортировка Шелла: 27.31152830000792 сек, память: 0.046875 MiB
--------------------------------------------------------------------------------
"""
