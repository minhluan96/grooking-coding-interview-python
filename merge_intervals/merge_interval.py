def merge_intervals(intervals):
    if len(intervals) == 0:
        return []

    DEFAULT_INDEX = 0
    output = []

    first_interval = intervals[DEFAULT_INDEX]
    output.append(first_interval)

    del intervals[DEFAULT_INDEX]

    for i in range(len(intervals)):
        [start_selected, end_selected] = intervals[i]
        [start_current, end_current] = output[-1]

        if end_current < start_selected:
            output.append(intervals[i])
        else:
            new_start = start_current if start_current < start_selected else start_selected
            new_end = end_current if end_current > end_selected else end_selected

            output.pop()
            output.append([new_start, new_end])
    

    return output

intervals = [[1,5],[3,7],[4,6]]
print(merge_intervals(intervals))