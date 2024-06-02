# binary searching algorithm in python

array = [10,11,12,13,14,15,16]
low = 0
high = len(array)-1
key = 16

def binarySearch(array, low, high, key):

    if high >= low:
        mid = (low + high) // 2

        if array[mid] == key:
            return mid
        elif array[mid] > key:
            return binarySearch(array, low, mid-1, key)
        
        else:
             return binarySearch(array, mid+1, high, key)

    else:
        return -1

print(binarySearch(array, low, high, key))
