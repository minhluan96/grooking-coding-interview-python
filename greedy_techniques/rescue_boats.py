def rescue_boats(people, limit):
    total_boats = 0
    weighted_people = sorted(people)

    left, right = 0, len(weighted_people) - 1

    while left <= right:
        if weighted_people[left] + weighted_people[right] <= limit:
            left += 1
            right -= 1
        else:
            right -= 1

        total_boats += 1

    return total_boats

people = [5,5,5,5] 
limit = 5
result = rescue_boats(people, limit)

print(result)