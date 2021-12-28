import pytest
from selection_sort import selection_sort


def test_selection_sort():
    list_1 = [100,5,32,95,96,58,11,26,38,75,49,52,34]
    list_2 = [10000,5000,48,90,633,548,4487,548]
    sorted_list_1 = sorted(list_1)
    sorted_list_2 = sorted(list_2)

    assert selection_sort(list_1) == sorted_list_1
    assert selection_sort(list_2) == sorted_list_2
    
