def selection_sort(arr: list) -> list:
    """
    ...
    """

    left_b: int = 0

    for _ in range(len(arr, ) - 1, ):
        min_val = arr[-1]
        min_val_idx = -1

        for j in range(left_b, len(arr)):
            if arr[j] < min_val:
                min_val = arr[j]
                min_val_idx = j

        arr[left_b], arr[min_val_idx] = min_val, arr[left_b]
        left_b += 1

    return arr
