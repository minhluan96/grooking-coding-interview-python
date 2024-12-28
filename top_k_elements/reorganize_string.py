# importing libraries
from collections import Counter
from heapq import *

def reorganize_string(str):

    character_frequency = {}
    max_heap = []
    result = []

    for c in str:
        if c not in character_frequency:
            character_frequency[c] = 0
        character_frequency[c] += 1

    for k, val in character_frequency.items():
        heappush(max_heap, (-val, k))

    last_popped_char = None

    while max_heap:
        (frequencies, most_freq_char) = heappop(max_heap)
        repeat_times = -frequencies

        if last_popped_char:
            heappush(max_heap, last_popped_char)
            last_popped_char = None

        result.append(most_freq_char)
        updated_frequencies = repeat_times - 1
        if updated_frequencies > 0:
            last_popped_char = (-updated_frequencies, most_freq_char)

    
    return "".join(result) if len(str) == len(result) else "" 

str = "aaaaabbbbbbb"
print(reorganize_string(str))