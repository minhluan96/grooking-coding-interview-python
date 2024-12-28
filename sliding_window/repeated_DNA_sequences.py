def find_repeated_sequences(dna, k):

    map = dict()
    
    for i in range(len(dna)):
        left = i
        right = i + k if i + k <= len(dna) else len(dna)
        
        sub_dna = dna[left:right]
        if len(sub_dna) < k:
            continue   

        if sub_dna not in map:
            map[sub_dna] = 0
        
        map[sub_dna] += 1

    output = []
    for key, val in map.items():
        if val > 1:
            output.append(key)


    return set(output)


def find_repeated_sequences_alternative_answer(dna, k):
    string_length = len(dna)
    mapping = { 'A': 1, 'C': 2, 'G': 3, 'T': 4 }

    # base on the number of dna character
    base_value = 4

    # Numeric representation of the sequence
    numbers = [0] * string_length
    for i in range(string_length):
        numbers[i] = mapping.get(dna[i])

    hash_value = 0

    hash_set = set()
    output = set()

    for i in range(string_length - k + 1):

        # If the window is at its initial position, calculate the hash value from scratch
        if i == 0:
            for j in range(k):
                hash_value += numbers[j] * (base_value ** (k - j - 1))

        # Otherwise, utilize the previous hash value
        else:
            previous_hash_value = hash_value
            hash_value = ((previous_hash_value - numbers[i - 1] * (base_value ** (k - 1))) * base_value) + numbers[i + k - 1]


        # If the current hash value is present in the hash set, the current substring has been repeated, so we add it to the output
        if hash_value in hash_set:
            output.add(dna[i:i + k])

        hash_set.add(hash_value)

    return output



dna = 'AAAAACCCCCAAAAACCCCCC'
k = 8

# dna = 'CGG'
# k = 1

print(find_repeated_sequences(dna, k))
print(find_repeated_sequences_alternative_answer(dna, k))