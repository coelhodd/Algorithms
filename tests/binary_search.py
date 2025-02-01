def binary_search(L, element):
    """ Defining a binary search algorithm """ 

    # Grabing the indexes of the first and last elements
    first = 0
    last = len(L) - 1

    while last >= first: # 'while there are elements in the list'
        mid = (first + last) // 2
        if L[mid] == element:
            return True
        else:
            if element < L[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return False


print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 30))
