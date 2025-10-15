def binary_search(arr, target):
    """
    Binary Search Algorithm
    --------------------------------
    Input: Sorted list `arr` and value `target`
    Output: Index of `target` in `arr` if found, else -1
    --------------------------------
    Example:
        arr = [1, 3, 5, 7, 9]
        binary_search(arr, 7)  --> 3
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# Example usage
if __name__ == "__main__":
    numbers = [2, 4, 6, 8, 10]
    target = 8
    result = binary_search(numbers, target)
    print(f"Target {target} found at index {result}" if result != -1 else "Not found")
