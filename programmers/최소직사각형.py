def solution(sizes):
    x_max = 0
    y_max = 0
    for size in sizes:
        if size[0] < size[1]:
            temp_x = size[1]
            temp_y = size[0]
        else:
            temp_x = size[0]
            temp_y = size[1]
        if temp_x > x_max:
            x_max = temp_x
        if temp_y > y_max:
            y_max = temp_y

    return y_max * x_max