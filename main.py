import timeit
import random


# Реалізація сортування злиттям
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged


# Реалізація сортування вставками
def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key


# Використання вбудованого алгоритму сортування Python (Timsort)
def timsort(arr):
    arr.sort()


# Функція для генерації тестових масивів
def generate_test_arrays(sizes):
    return [random.sample(range(size * 10), size) for size in sizes]


# Функція для вимірювання часу виконання сортувань
def measure_sort_performance():
    sizes = [100, 1000, 5000]
    insertion_times = []
    merge_times = []
    timsort_times = []

    for size in sizes:
        arr = [random.randint(0, size) for _ in range(size)]
        insertion_stmt = f"insertion_sort({arr})"
        merge_stmt = f"merge_sort({arr})"
        timsort_stmt = f"sorted({arr})"

        insertion_time = timeit.timeit(insertion_stmt, globals=globals(), number=1)
        merge_time = timeit.timeit(merge_stmt, globals=globals(), number=1)
        timsort_time = timeit.timeit(timsort_stmt, globals=globals(), number=1)

        insertion_times.append(f"{insertion_time:.6f}")
        merge_times.append(f"{merge_time:.6f}")
        timsort_times.append(f"{timsort_time:.6f}")

    return insertion_times, merge_times, timsort_times


# Підготовка тестових даних
sizes = [100, 1000, 5000]
test_arrays = generate_test_arrays(sizes)

insertion_times, merge_times, timsort_times = measure_sort_performance()

# Вивід результатів
print("Час виконання сортування вставками:", insertion_times)
print("Час виконання сортування злиттям:", merge_times)
print("Час виконання Timsort:", timsort_times)
