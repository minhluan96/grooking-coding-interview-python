def back_track(n, left_count, right_count, output, results):
    # Base case where count of left and right braces is "n"
    if left_count >= n and right_count >= n:
        results.append(''.join(output))
    
    # Case where we can still append left braces
    if left_count < n:
        output.append('(')
        back_track(n, left_count + 1, right_count, output, results)
        output.pop()
        
    # Case where we append right braces if the current count
    # of right braces is less than the count of left braces
    if right_count < left_count:
        output.append(')')
        back_track(n, left_count, right_count + 1, output, results)
        output.pop()
        

def generate_combinations(n):
    result = []
    output = []

    if n == 0:
        return []
    
    back_track(n, 0, 0, output, result)

    return result

n = 3
result = generate_combinations(n)
print(result)
