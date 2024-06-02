# linear searching algorithm in python 

array = [5,7,8,9,14,55,74,36]
length = len(array)

def linearSearch(array, length, key):

    for i in range(0, length):
        if(array[i] == key):
            return i

    return -1        

print(linearSearch(array,length, 74 ))
