""" Example of Selection Sort Algorithm in Python 

    input: takes in an unsorted list of integers
    output: returns a sorted list
"""

def find_small(arr):
    small = arr[0] 
    idx = 0

    for i in range(1,len(arr)):
        if arr[i] < small:
            small = arr[i]
            idx = i 
    return idx


def selection_sort(arr:list) -> list:
    
    new_arr = []

    for i in range(len(arr)):
        # find smallest idx
        smallest = find_small(arr)  
        # pop and add
        new_arr.append(arr.pop(smallest))
    return new_arr
