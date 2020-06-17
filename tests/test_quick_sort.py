import pytest
from sort.quick_sort import quick_sort

class TestMergeSort:
    def test_merge_sort(self):
        arr = []
        quick_sort(arr, 0, 0)
        assert arr == [], 'Function did not return the same input arr'

        arr = [1]
        quick_sort(arr, 0, 0)
        assert arr == [1], 'Function altered single-membered array'

        arr = [3, 1]
        quick_sort(arr, 0, 1)
        assert arr == [1, 3], 'Improper sort'

        arr = [4, 2, 6, 8, 2, 5, 4]
        quick_sort(arr, 0 , 6)
        assert arr == [2, 2, 4, 4, 5, 6, 8], 'Cannot handle duplicates or slightly longer lists'