def find_longest_substring(input_str):

    character_map = {}
    res_len = -1

    left = 0

    for right in range(len(input_str)):
        c = input_str[right]

        if c not in character_map:
            character_map[c] = 0
        character_map[c] += 1
        
        while (right - left + 1) > len(character_map):
            c_left = input_str[left]
            character_map[c_left] -= 1
            if character_map[c_left] == 0:
                del character_map[c_left]
            
            left += 1
        
        res_len = max(right - left + 1, res_len)

    return res_len


def solution(input_str):
    if len(input_str) == 0:
        return 0
    
    window_start, longest, window_length = 0, 0, 0
    last_seen_at = {}

    for index, val in enumerate(input_str):
        # If the current element is not present in the hash map,
        # then store it in the hash map with the current index as the value.
        if val not in last_seen_at:
            last_seen_at[val] = index
        else:
            # If the current element is present in the hash map,
            # it means that this element may have appeared before.
            # Check if the current element occurs before or after `window_start`.
            if last_seen_at[val] >= window_start:
                window_length = index - window_start
                longest = max(longest, window_length)

                window_start = last_seen_at[val] + 1
            
            # Update the last occurrence of
            # the element in the hash map
            last_seen_at[val] = index

    index += 1
    # Update the longest substring's
    # length and starting index.
    longest = max(longest, index - window_start)

    return longest


string = "aaaabaaa"
print(find_longest_substring(string))
print(solution(string))