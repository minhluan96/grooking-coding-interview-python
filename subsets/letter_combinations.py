def backtrack(index, path, digits, letters, combinations):
    # If the length of path and digits is same,
    # we have a complete combination
    if len(path) == len(digits):

        # Join the path list into a string and add it to combinations list
        combinations.append(''.join(path))
        return # Backtrack

    # Get the list of letters using the index and digits[index]
    possible_letters = letters[digits[index]]
    if possible_letters:
        for letter in possible_letters:
            # Add the current letter to the path
            path.append(letter)
            # Recursively explore the next digit
            backtrack(index + 1, path, digits, letters, combinations)
            # Remove the current letter from the path before backtracking to explore other combinations
            path.pop()
    

def letter_combinations(digits):
    combinations = []

    if not digits:
        return []
    
    digits_mapping = {
        '1': [''],
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }

    backtrack(0, [], digits, digits_mapping, combinations)

    return combinations

digits = '24'
result = letter_combinations(digits)
print(result)