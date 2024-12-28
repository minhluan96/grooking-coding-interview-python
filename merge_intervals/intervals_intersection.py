def intervals_intersection(interval_list_a, interval_list_b):
    
    i, j = 0, 0
    intersections = []
    
    while i < len(interval_list_a) and j < len(interval_list_b):
        [a_start, a_end] = interval_list_a[i]
        [b_start, b_end] = interval_list_b[j]

        latest_start = a_start if a_start > b_start else b_start
        earliest_end = a_end if a_end < b_end else b_end

        if latest_start <= earliest_end:
            intersections.append([latest_start, earliest_end])

        if a_end < b_end:
            i += 1
        else:
            j += 1

    return intersections


a = [[1,4],[5,6],[7,8],[9,15]]
b = [[2,4],[5,7],[9,15]]

print(intervals_intersection(a, b))