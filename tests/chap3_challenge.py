from bisect import bisect_left

def binary_search(L, element):
    index = bisect_left(L, element) # this function returns the index of the element inside the list or where it would be
    try:
        if index <= len(L) and L[index] == element: # checks if the returned index is in range of the list and if it equals the value
            return True
    except:
        return False

print(binary_search(['apple', 'banana', 'cranberry', 'date', 'egg fruit'], 'cranberry'))
