def partition(arr, start, end):
    """
    Helper that handles swapping of elements.

    Returns
    -------
    an integer representing the new partition index.
    """
    pi = start - 1       # partition index 
    pivot = arr[end]     # pivot to compare against
  
    for j in range(start, end): 
        
        if arr[j] <= pivot: 
    
            pi += 1 
            arr[pi], arr[j] = arr[j], arr[pi] 
  
    arr[pi + 1], arr[end] = arr[end], arr[pi + 1] 
    
    return pi + 1 
  
  

def quick_sort(arr, start, end):
    """
    Function that orchestrates the overall sort.
    
    Parameters
    ----------
    arr: [list] array to be sorted
    start, end: [int] indices of start and end of sort 
    """
    if start < end: 
  
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(arr,start,end) 
  
        # Sort elements before and after partition
        quick_sort(arr, start, pi - 1) 
        quick_sort(arr, pi + 1, end) 