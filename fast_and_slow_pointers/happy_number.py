def calculate_sum_of_squared_digit(n):
    m = n
    total = 0
    while m > 0:
        last_digit = m % 10
        total += pow(last_digit, 2)
        m  //= 10
    
    return total


def is_happy_number(n):

    # Replace this placeholder return statement with your code
    slow = n
    fast = calculate_sum_of_squared_digit(n)

    while fast != 1 and slow != fast:
        slow = calculate_sum_of_squared_digit(slow)
        fast = calculate_sum_of_squared_digit(calculate_sum_of_squared_digit(fast))

    if fast == 1:
        return True
    
    return False


print(is_happy_number(28))