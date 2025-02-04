def eficient_bubble_sort(a_list):
    """ Sort a list in ascending order using eficient bubble sort """
    list_length = len(a_list) - 1    # working with indexes
    for i in range(list_length):
        no_swaps = True
        for j in range(list_length - i): # the ' - i' prevents comparisons with values already sorted
            if a_list[j] > a_list[j+1]:
                a_list[j], a_list[j+1] = a_list[j+1], a_list[j]   # exchanging values with each other
                no_swaps = False
        if no_swaps:    # if after the inner loop executed there were no swaps then the list is already sorted
            return a_list
    return a_list

def inefficient_bubble_sort(a_list):
    """ Sort a list in ascending order using inefficient bubble sort """
    list_length = len(a_list) - 1
    for i in range(list_length):
        for j in range(list_length):
            if a_list[j] > a_list[j+1]:
                a_list[j], a_list[j+1] = a_list[j+1], a_list[j]
    return a_list


print(eficient_bubble_sort([9, 3, 2, 10, 5, 8]))
print(inefficient_bubble_sort([9, 8, 7, 6, 5, 4, 3, 2, 1]))
