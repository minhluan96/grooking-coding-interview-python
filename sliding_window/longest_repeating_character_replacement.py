def longest_repeating_character_replacement(s, k):
    
    window_start = 0
    max_len_substr = 0
    character_map = {}
    most_frequent_char = 0

    for window_end in range(len(s)):
        right_char = s[window_end]

        if right_char not in character_map:
            character_map[right_char] = 0
        
        character_map[right_char] += 1

        most_frequent_char = max(most_frequent_char, character_map[right_char])

        while (window_end - window_start + 1) - most_frequent_char > k:
            left_char = s[window_start]
            character_map[left_char] -= 1

            if character_map[left_char] == 0:
                del character_map[left_char]
            
            window_start += 1
        
        max_len_substr = max(max_len_substr, window_end - window_start + 1)
        
    return max_len_substr


s = "aaacbbbaabab"
k = 2
print(longest_repeating_character_replacement(s, k))