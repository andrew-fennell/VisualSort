from visualsort.sorting_algorithms import insertion_sort

def test_empty_array():
    assert insertion_sort([]) == []

def test_one_element_array():
    assert insertion_sort([5]) == [5]

def test_short_array():
    assert insertion_sort([2, 6, 1, 7, 9, 3]) == [1, 2, 3, 6, 7, 9]

def test_long_array():
    assert (insertion_sort([83, 123, 124, 82, 855, 178, 235, 213, 234, 971, 185,
                       295, 872, 1854, 203, 912, 497, 986, 407, 836])
                       ==
                       [82, 83, 123, 124, 178, 185, 203, 213, 234, 235, 295,
                       407, 497, 836, 855, 872, 912, 971, 986, 1854])

def test_duplicate_values():
    assert insertion_sort([4, 2, 3, 4, 9, 5, 8]) == [2, 3, 4, 4, 5, 8, 9]

def test_multiple_duplicate_values():
    assert insertion_sort([2, 5, 2, 9, 3, 2, 9, 5]) == [2, 2, 2, 3, 5, 5, 9, 9]

def test_all_negative_values():
    assert insertion_sort([-2, -5, -1, -10, -9, -4]) == [-10, -9, -5, -4, -2, -1]

def test_positive_negative_values():
    assert insertion_sort([-2, 6, 1, -7, 9, -3]) == [-7, -3, -2, 1, 6, 9]