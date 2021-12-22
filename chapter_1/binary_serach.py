""" Example of Binary Search Algorithm in Python 

    input: takes in a sorted list of integers
    output: returns the index of the target value
"""

def binary_search(sorted:list,target:int) -> int:
    
    left = 0
    right = len(sorted)-1

    while left <= right:
        mid = (left+right)//2
        guess = sorted[mid]

        if guess == target:
            return mid
        elif guess < target:
            left = mid+1      
        else:
            right = mid-1
    return None