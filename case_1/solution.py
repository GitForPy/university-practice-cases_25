def sum_negative_between_min_max(arr):
    """
    Находит сумму отрицательных элементов между минимальным и максимальным 
    элементами массива (границы не включаются).
    
    Args:
        arr: список чисел
    
    Returns:
        сумма отрицательных элементов между min и max
    """
    if len(arr) < 3:
        return 0
    
    # Находим минимальный элемент и его индекс
    min_val = arr[0]
    min_idx = 0
    for i in range(1, len(arr)):
        if arr[i] < min_val:
            min_val = arr[i]
            min_idx = i
    
    # Находим максимальный элемент и его индекс
    max_val = arr[0]
    max_idx = 0
    for i in range(1, len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
            max_idx = i
    
    # Определяем границы для суммирования
    start_idx = min_idx if min_idx < max_idx else max_idx
    end_idx = max_idx if min_idx < max_idx else min_idx
    
    # Суммируем отрицательные элементы между границами
    negative_sum = 0
    for i in range(start_idx + 1, end_idx):
        if arr[i] < 0:
            negative_sum += arr[i]
    
    return negative_sum


if __name__ == "__main__":
    # Тестовые случаи
    test_cases = [
        [3, -1, 4, -2, 5, -3, 1],  # min=-3, max=5, между ними: нет элементов
        [1, -2, 3, -4, 5, -1, 2],  # min=-4, max=5, между ними: нет элементов  
        [10, -5, 3, -2, 1, 8, -4], # min=-5, max=10, между ними: 3, -2, 1, 8, -4, сумма отриц.=-2-4=-6
        [-1, 5, -3, 2, -4, 8, 1],  # min=-4, max=8, между ними: нет элементов
        [2, -3, 5, -1, -2, 7, 1],  # min=-3, max=7, между ними: 5, -1, -2, сумма отриц.=-1-2=-3
    ]
    
    for i, test in enumerate(test_cases, 1):
        result = sum_negative_between_min_max(test)
        print(f"Тест {i}:")
        print(f"  Массив: {test}")
        print(f"  Сумма отрицательных между min и max: {result}")
        print()

