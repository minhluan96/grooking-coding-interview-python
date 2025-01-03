# -- DO NOT CHANGE THIS SECTION -----------------
    
# import main as api_call

def is_bad_version(v): # is_bad_version() is the API function that returns true or false depending upon whether the provided version ID is bad or not
    pass
    # return api_call.is_bad(v)
# ----------------------------------------------- 

def first_bad_version(n):

    # Replace this placeholder return statement with your code
    first = 1
    last = n

    counter = 0
    while first <= last:
        mid = (first + last) // 2
        counter += 1
        if is_bad_version(mid):
            last = mid - 1
        else:
            first = mid + 1


    return [first, counter]