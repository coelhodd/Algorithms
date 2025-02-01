def linear_search(li, element):
    for i in li:
        if i == element:
            return True
    return False

print(linear_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 29))
