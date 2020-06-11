import pytest
from sort.merge_sort import merge_sort

class TestMergeSort:
    def test_merge_sort(self):
        arr = []
        assert merge_sort(arr, 0, 0) == [], 'Function did not return the same input arr'

        arr = [1]
        assert merge_sort(arr, 0, 0) == [1], 'Function altered single-membered array'

        arr = [3, 1]
        assert merge_sort(arr, 0, 1) == [1, 3], 'Improper sort'

        arr = [4, 2, 6, 8, 2, 5, 4]
        assert merge_sort(arr, 0, 6) == [2, 2, 4, 4, 5, 6, 8], 'Cannot handle duplicates or slightly longer lists'