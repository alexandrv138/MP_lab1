"""Модуль с реализованными сортировками:
Сортировка простыми вставками, шейкер, слиянием"""


def insert_sort(arr):
    """метод простых вставок"""
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def shaker_sort(arr):
    """ shaker sort"""
    size = len(arr)
    k = size - 1
    lb = 1
    ub = size - 1

    while True:
        for j in range(ub, 0, -1):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
                k = j
        lb = k + 1

        for j in range(1, ub + 1):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
                k = j
        ub = k - 1

        if (lb >= ub):
            break


def merge(arr, low, mid, high):
    """ Функция для записи отсортированного подмассива в оригинальный массив"""
    buffer = [None] * (high + 1 - low)
    h, i, j = low, 0, mid + 1

    while h <= mid and j <= high:
        if arr[h] <= arr[j]:
            buffer[i] = arr[h]
            h += 1
        else:
            buffer[i] = arr[j]
            j += 1
        i += 1

    if h > mid:
        for k in range(j, high + 1):
            buffer[i] = arr[k]
            i += 1
    else:
        for k in range(h, mid + 1):
            buffer[i] = arr[k]
            i += 1

    for k in range(0, high - low + 1):
        arr[low + k] = buffer[k]


def merge_sort(arr, low, high):
    """ Сортирует массив сортировкой слиянием"""
    if low < high:
        mid = (low + high) // 2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid + 1, high)
        merge(arr, low, mid, high)
