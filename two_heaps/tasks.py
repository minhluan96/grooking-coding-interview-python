from heapq import *


def tasks(tasks_list):
    heapify(tasks_list)
    machine_available = []
    optimal_machine = 0

    while tasks_list:
        # remove from "tasks_list" the task i with earliest start time
        task = heappop(tasks_list)

        if machine_available and task[0] >= machine_available[0][0]:
            # top element is deleted from "machines_available"
            machine_in_use = heappop(machine_available)
            # schedule task on the current machine
            machine_in_use = (task[1], machine_in_use[1])
        else:
            # if there's a conflicting task, increment the
            # counter for machines and store this task's
            # end time on heap "machines_available"
            optimal_machine += 1
            machine_in_use = (task[1], optimal_machine)

        heappush(machine_available, machine_in_use) 

    
    return optimal_machine

tasks_list = [[1,1],[5,5],[8,8],[4,4],[6,6],[10,10],[7,7]]
print(tasks(tasks_list))