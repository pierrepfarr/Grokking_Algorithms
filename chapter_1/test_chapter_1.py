import pytest
from binary_serach import binary_search


def test_binary_search():
    list_1 = [1,2,19,26,32,50,61,63,72,82]
    list_2 = [100,105,234,434,609,738,902,1000,1394,1500]
    
    assert binary_search(list_1,32) == 4
    assert binary_search(list_1,50) == 5
    assert binary_search(list_2,1500) == 9
    assert binary_search(list_2,100) == 0
    assert binary_search(list_1,1000) == None
    assert binary_search(list_2,0) == None

if __name__ == "__main__":
    test_binary_search()
