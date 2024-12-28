from heapq import *

def most_booked(meetings, rooms):
    count = [0] * rooms

    available = [i for i in range(rooms)]
    used_rooms = []

    # sort the meetings by their start time
    meetings.sort()

    for start_time, end_time in meetings:

        # free any room that finished their meeting by the current starting time
        while used_rooms and used_rooms[0][0] <= start_time:
            ending, room = heappop(used_rooms)
            heappush(available, room)

        # if no room available, delay a meeting until a room becomes free
        if not available:
            end, room = heappop(used_rooms)
            # increase the end_time to calculate after
            end_time = end + (end_time - start_time)
            # push to available since this room was the room that will become free soon than other room, just need to wait
            heappush(available, room)

        room = heappop(available)
        # the new end time will be calculate from the start time or combination of the gap between previous end and current start time
        heappush(used_rooms, (end_time, room))
        count[room] += 1
    
    # room that held the most meetings
    return count.index(max(count))

        



    
    return -1