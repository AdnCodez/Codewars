def sort_array(source_array):
    odd_array = []
    final_array = []
    if not sort_array:
        return final_array
    for i in source_array:
        if i % 2 != 0:
            odd_array.append(i)
            odd_array = sorted(odd_array)
    final_array.extend(odd_array)
    for i in source_array:
        if i % 2 == 0:
            index = source_array.index(i)
            final_array.insert(index, i)

    return final_array


print(sort_array([5, 3, 2, 8, 1, 4]))
