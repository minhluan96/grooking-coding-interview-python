def search(arr, target):

    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == target:
            return True
        
        if arr[low] == arr[mid] and arr[mid] == arr[high]:
            low += 1
            high -= 1

        if low >= len(arr) and high < 0:
            return False

        if arr[low] <= arr[mid]:
            if arr[low] <= target and target < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
                    
        else:
            if arr[mid] < target and target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1

    return False

arr = [6989] , 
target = -6914
print(search(arr, target))