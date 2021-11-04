import time

def ordena(lista):
    tiempo_sort, lista_sort = selection_sort(lista)
    tiempo_bubble, lista_bubble = bubble_sort(lista)
    return tiempo_bubble, tiempo_sort, lista_sort, lista_bubble


def selection_sort(vector):
    arr = vector.split(',')
    arr = [int(i) for i in arr]
    start_time = time.time()
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    elapsed_time = time.time() - start_time
    return elapsed_time, arr

def bubble_sort(vector):
    arr = vector.split(',')
    arr = [int(i) for i in arr]
    start_time = time.time()
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    elapsed_time = time.time() - start_time
    return elapsed_time, arr
