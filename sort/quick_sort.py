def swap(arr, i, j):
    """
    Swaps elements i and j of arr in place.

    Parameters
    ----------
    arr: [list] the array to swap values.

    i, j: [int] indices of two array elements to swap.
    """
    arr[i], arr[j] = arr[j], arr[i]


def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    # Track indices of seperator, number, and pivot
    sep = 0
    num = 0
    piv = len(arr) - 1

    while num < len(arr):
        print(sep, num, piv)
        print(arr)
        if arr[num] <= arr[piv]:
            if num > piv:
                swap(arr, num, piv)
            sep += 1

        num += 1
    
    # Address pivot
    if arr[piv] < arr[sep]:
        swap(arr, piv, sep)

    # Sort remaining chunks
    quick_sort(arr[:sep])
    quick_sort(arr[sep:])

    
