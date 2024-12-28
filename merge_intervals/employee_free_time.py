from utils.interval import Interval
import heapq

def employee_free_time(schedule):  
    if not schedule:
        return []
    
    heap = []
    result = []

    for i in range(len(schedule)):
        # store the value, index of the schedule and the index of the start time (val, i, j)
        heap.append((schedule[i][0].start, i, 0))

    heapq.heapify(heap)
    first_person_index = heap[0][1]
    first_start_schedule = heap[0][2]

     # Set 'previous' to the start time of first interval in heap.
    previous = schedule[first_person_index][first_start_schedule].start

    while heap:
        _, i, j = heapq.heappop(heap)
        interval = schedule[i][j]

        # If selected interval's start value is greater than the
        # previous value, it means that this interval is free.
        # So, add this interval (previous, interval's end value) into result.
        if interval.start > previous:
            result.append(Interval(previous, interval.start))
        
        previous = max(previous, interval.end)

        # If there is another interval in current employees' schedule,
        # push that into heap.
        if j + 1 < len(schedule[i]):
            next_schedule = schedule[i][j + 1]
            heapq.heappush(heap, (next_schedule.start, i, j + 1))
    
    return result
    
list = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
schedule = []

for i in range(len(list)):
    curr_schedule = list[i]
    person = []
    for j in range(len(curr_schedule)):
        [start, end] = curr_schedule[j]
        person_interval = Interval(start, end)
        person.append(person_interval)

    schedule.append(person)
        

output = employee_free_time(schedule)
for i in range(len(output)):
    print(str(output[i]))