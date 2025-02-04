def insertion_sort(a_list):
    for i in range(1, len(a_list)): # 1 até o último índice, ou seja, pega todos os índices da lista
        value = a_list[i]           # define uma variável chamada value para guardar o valor no índice atual i
        j = i
        while j > 0 and a_list[j - 1] > value:      # enquanto j(i) for maior que zero e o valor anterior for maior que o atual
            a_list[j] = a_list[j - 1]               # então o valor atual será o valor anterior
            j -= 1                                  # decrementa j(i)
        a_list[j] = value                           
    return a_list



print(insertion_sort([9, 8, 7, 6]))
