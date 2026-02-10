def find(search_list, value):
    low_index = 0
    high_index = len(search_list) - 1
    while low_index <= high_index:
        middle_index = (low_index + high_index) //2
        if search_list[middle_index] == value:
            return middle_index
        elif search_list[middle_index] > value:
            high_index = middle_index - 1
        else:
            low_index = middle_index + 1
    raise ValueError("value not in array") 