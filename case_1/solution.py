def sum_negative_between_min_max(arr):
    """
    Находит сумму отрицательных элементов между минимальным и максимальным 
    элементами массива (границы не включаются).
    
    Args:
        arr: список чисел
    
    Returns:
        сумма отрицательных элементов между min и max
    """
    if len(arr) < 3: # Исключил бессмысленные случаи, когда между минимумом и максимумом не может физически существовать элементов.
        return 0
    
    # Поиск минимального элемента и его индекса
    min_val = arr[0]
    min_idx = 0
    for idx in range(1, len(arr)):
        if arr[idx] < min_val:
            min_val = arr[idx]
            min_idx = idx
    
    # Находим максимальный элемент и его индекс
    max_val = arr[0]
    max_idx = 0
    for idx in range(1, len(arr)):
        if arr[idx] > max_val:
            max_val = arr[idx]
            max_idx = idx
    
    # Определяем границы для суммирования на основне найденных индексов
    start_idx = min_idx if min_idx < max_idx else max_idx
    end_idx = max_idx if min_idx < max_idx else min_idx
    
    # Суммируем отрицательные элементы между границами
    negative_sum = 0
    for idx in range(start_idx + 1, end_idx):
        if arr[idx] < 0:
            negative_sum += arr[idx]
    
    return negative_sum


if __name__ == "__main__":

    # Тестирование
    test_cases = [
        [3, -1, 4, -2, 5, -3, 1],  # min=-3, max=5, между ними: нет элементов
        [-1, 5, -4, 2, -3, 8, 1],  # min=-4, max=8, между ними: -3
        [-100, -3, 5, -1, -2, 7, 100],  # min=-3, max=7, между ними: -3, -1, -2, сумма отриц.=-3-1-2=-6
    ]
    
    for i, test in enumerate(test_cases, 1):
        result = sum_negative_between_min_max(test)
        print(f"Тест {i}:")
        print(f"  Массив: {test}")
        print(f"  Сумма отрицательных между min и max: {result}")
        print()

