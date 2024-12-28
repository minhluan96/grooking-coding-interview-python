def insert_interval(existing_intervals, new_interval):

    output = []
    i = 0
    [new_interval_start, new_interval_end] = new_interval

    while i < len(existing_intervals):
        if existing_intervals[i][0] < new_interval_start:
            output.append(existing_intervals[i])
            i += 1
        else:
            break

    # If the new interval starts after the end of the last interval appended to the output list,
    # just append the new interval to the output list.

    if not output or output[-1][1] < new_interval_start:
        output.append(new_interval)
    else:
        output[-1][1] = max(new_interval_end, output[-1][1])


    while i < len(existing_intervals):
        [curr_start, curr_end] = existing_intervals[i]
        if output[-1][1] < curr_start:
            output.append(existing_intervals[i])
        else:
            output[-1][1] = max(output[-1][1], curr_end)
        
        i+= 1

    return output


existing_intervals = [[1,6],[8,9],[10,15],[16,18]]
new_interval = [9,10]

print(insert_interval(existing_intervals, new_interval))