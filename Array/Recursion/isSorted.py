def isSorted(arr):
    size = len(arr)
    
    if size==0 or size ==1:
        return True
    
    if(arr[-1] < arr[-2]):
        return False
    
    arr.pop()
    return isSorted(arr)


print(isSorted([1,2,6,4,5]))