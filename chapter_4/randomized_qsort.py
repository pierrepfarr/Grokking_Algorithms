import random as rand

def quicksort(arr:list,left:int,right:int):
    if left < right:
        p = rand_partition(arr,left,right)
        quicksort(arr,left,p-1)
        quicksort(arr,p+1,right)

def rand_partition(arr:list,left:int,right:int):
    r_pivot = rand.randint(left,right)
    arr[r_pivot], arr[right] = arr[right],arr[r_pivot]
    return partition(arr,left,right)

def partition(arr:list,left:int,right:int):
    pivot = right
    i = left 
    for j in range(left,right):
        if arr[j] <= arr[pivot]:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i],arr[pivot] = arr[pivot], arr[i]
    return i 


if __name__ == "__main__":
    array = [10, 7, 8, 9, 1, 5]
    quicksort(array, 0, len(array) - 1)
    print(array)