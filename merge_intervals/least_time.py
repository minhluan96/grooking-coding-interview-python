def least_time(tasks, n):
    frequencies = {}

    for i in range(len(tasks)):
        task = tasks[i]
        if task not in frequencies:
            frequencies[task] = 0
        frequencies[task] += 1

    
    # sort the frequencies
    frequencies = dict(sorted(frequencies.items(), key=lambda x:x[1]))
    
    #store the max frequencies
    max_freq = frequencies.popitem()[1]

    #compute the maximum idle time
    idle_time = (max_freq - 1) * n

    #iterate over the frequencies array and update the idle time
    while frequencies and idle_time > 0:
        idle_time = idle_time - min(max_freq - 1, frequencies.popitem()[1])

    idle_time = max(0, idle_time)

    return len(tasks) + idle_time 


tasks = ["A","A","B","B"]
n = 2
print(least_time(tasks, n))