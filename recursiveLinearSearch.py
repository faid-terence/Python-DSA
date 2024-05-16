def recursive_linear_search(arr, target, index=0):
    """
    Perform a recursive linear search to find the target value in the array.

    Parameters:
    arr (list): The array to search.
    target: The value to search for.
    index (int): The starting index for search.

    Returns:
    int: The index of the target value if found, otherwise -1.
    """
    # Base case: If index exceeds the length of the array, return -1
    if index >= len(arr):
        return -1

    # If the element at the current index matches the target, return the index
    if arr[index] == target:
        return index

    # Recursive case: Search in the rest of the array
    return recursive_linear_search(arr, target, index + 1)

# Example usage:
arr = [1, 2, 3, 4, 5]
target = 5
result_index = recursive_linear_search(arr, target)
if result_index != -1:
    print(f"Target {target} found at index {result_index}.")
else:
    print(f"Target {target} not found in the array.")
