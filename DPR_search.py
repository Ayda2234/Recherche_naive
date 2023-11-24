def count_occurrences(arr, target):
    # Base case: if the array is empty, return 0
    if not arr:
        return 0

    # Base case: if the array has only one element, check if it's equal to the target
    if len(arr) == 1:
        return 1 if arr[0] == target else 0

    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively count occurrences in the left and right halves
    occurrences = count_occurrences(left_half, target) + count_occurrences(right_half, target)

    return occurrences

# Example usage:
arr = [1, 2, 3, 4, 2, 5, 2]
target_element = 2
result = count_occurrences(arr, target_element)

print(f'The element {target_element} occurs {result} times in the array.')
