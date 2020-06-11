def merge(arr, start, mid, end):
    """
    Takes two intervals - first from the start to mid and second from mid+1 to 
    the end. Merges them in a sorted order.
    """

    # create a temporary array
    temp = [0] * (end - start + 1)

    # crawlers for both intervals and for temp
    i, j, k = start, mid+1, 0

    # traverse both lists and in each iteration add smaller of both elements in temp 
    while (i <= mid) and (j <= end):
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            k += 1
            i += 1

        else:
            temp[k] = arr[j]
            k += 1
            j += 1

    # add elements left in the first interval 
    while i <= mid:
        temp[k] = arr[i]
        k += 1
        i += 1

    # add elements left in the second interval 
    while j <= end:
        temp[k] = arr[j]
        k += 1
        j += 1

    # copy temp to original interval
    for i in range(start, end + 1):
        arr[i] = temp[i - start]

def merge_sort(arr, start, end):
    """
    Returns
    -------
    A 1-D array sorted from least to greatest.

    Parameters
    ----------
    arr: [list, tuple] a potentially unsorted 1-D array.
    start: [int] starting index of current interval of arr
    end: [int] ending index of current interval of arr
    """
    if start < end:
        # Pick an integer midpoint index
        mid = (start + end) // 2

        # Sort left side
        merge_sort(arr, start, mid)

        # Sort right side
        merge_sort(arr, mid+1, end)

        # Merge two halves together
        merge(arr, start, mid, end)
    
    return arr