def min_window(str1, str2):

    size_str1 = len(str1)
    size_str2 = len(str2)

    min_sub_len = float('inf')

    index_s1, index_s2 = 0, 0
    min_subsequence = ""

    while index_s1 < size_str1:
        if str1[index_s1] == str2[index_s2]:
            index_s2 += 1

            # check if index_s2 has reached the end of str2
            if index_s2 == size_str2:
                # initialize start to the index where all characters of
                # str2 were present in str1
                start, end = index_s1, index_s1
                index_s2 -= 1

                # decrement pointer index_s2 and start a reverse loop
                while index_s2 >= 0:
                    # decrement pointer index_s2 until all characters of
                    #  str2 are found in str1
                    if str1[start] == str2[index_s2]:
                        index_s2 -= 1
                    
                    # decrement start pointer everytime to find the
                    # starting point of the required subsequence
                    start -= 1
                
                start += 1

                # check if min_sub_len of sub sequence pointed
                # by start and end pointers is less than current min min_sub_len
                if end - start < min_sub_len:
                    min_sub_len = end - start
                
                    # update minimum subsequence string
                    # to this new shorter string
                    min_subsequence = str1[start:end+1]
                
                index_s1 = start
                index_s2 = 0
            
        index_s1 += 1


    return min_subsequence

str1 = "abcdebdde"
str2 = "bde"

print(min_window(str1, str2))