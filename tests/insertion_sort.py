def insertion_sort(a_list):
    for i in range(1, len(a_list)):             # grabs the whole list(indexes)
        value = a_list[i]
        while i > 0 and a_list[i-1] > value:    # while not at the start of the list and the previous value is bigger than current
            a_list[i] = a_list[i-1]             # searches for the right place for current value
            i -= 1
        a_list[i] = value                       # places it when out of loop(meaning the correct place was found)
    return a_list


print(insertion_sort([5, 4, 3, 2, 1]))
