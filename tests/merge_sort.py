def merge_sort(a_list):
    if len(a_list) > 1:
        # sorting part
        mid = len(a_list) // 2
        left_half = a_list[:mid]
        right_half = a_list[mid:]
        merge_sort(left_half)
        merge_sort(right_half)

        # merging of sorted halfs part 
        left_ind = 0
        right_ind = 0
        alist_ind = 0

        while left_ind < len(left_half) and right_ind < len(right_half):
            if left_half[left_ind] <= right_half[right_ind]:
                a_list[alist_ind] = left_half[left_ind]
                left_ind += 1
            else:
                a_list[alist_ind] = right_half[right_ind]
                right_ind += 1
            alist_ind += 1

        while left_ind < len(left_half):
            a_list[alist_ind] = left_half[left_ind]
            left_ind += 1
            alist_ind += 1

        while right_ind < len(right_half):
            a_list[alist_ind] = right_half[right_ind]
            right_ind += 1
            alist_ind += 1



arr = [6, 3, 9, 2]
merge_sort(arr)
print(arr)
