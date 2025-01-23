def swap_char(word, i, j):
    swap_index = list(word)
    swap_index[i], swap_index[j] = swap_index[j], swap_index[i]

    return ''.join(swap_index)

def permute_string_rec(word, current_index, result):
    if current_index == len(word) - 1:
        result.append(word)
        return
    
    for i in range(current_index, len(word)):
        swapped_str = swap_char(word, current_index, i)
        permute_string_rec(swapped_str, current_index + 1, result)


def permute_word(word):
    result = []
    permute_string_rec(word, 0, result)
    return result




word = "abcd"
print(permute_word(word))
