def move(my_list, direction):
    index_of_one = my_list.index(1)

    if direction == "right":
        step = 1
    elif direction == "left":
        step = -1
    else:
        return my_list

    new_index = index_of_one + step

    if 0 <= new_index < len(my_list):
        my_list[index_of_one], my_list[new_index] = 0, 1

    return my_list

