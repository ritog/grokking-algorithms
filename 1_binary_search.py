def binary_search(ls, item):
    """Takes a sorted list and an item, and returns the index of the item"""
    #indices for accessing elements in the array
    low = 0
    high = len(ls) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = ls[mid]
        if guess == item:
            return mid
        elif guess < item:
            low = mid + 1
        else:
            high = mid - 1

    return