def move(my_list, direction):
    i = my_list.index(1)
    if direction == "right" and i < len(my_list) - 1:
        my_list[i], my_list[i+1] = 0, 1
    elif direction == "left" and i > 0:
        my_list[i], my_list[i-1] = 0, 1
    return my_list

