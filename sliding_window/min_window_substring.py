def min_window(s, t):
    if t == "":
        return ""
    
    req_count = {}
    window = {}

    for c in t:
        req_count[c] = 1 + req_count.get(c, 0)

    for c in t:
        window[c] = 0
    
    current, required = 0, len(req_count)
    res, res_len = [-1, -1], float('inf')

    left = 0
    for right in range(len(s)):
        c = s[right]

        if c in t:
            window[c] = window.get(c, 0) + 1
        
        if c in req_count and window[c] == req_count[c]:
            current += 1
        
        while current == required:
            if (right - left + 1) < res_len:
                res = [left, right]
                res_len = right - left + 1
            
            if s[left] in t:
                window[s[left]] -= 1
            
            if s[left] in req_count and window[s[left]] < req_count[s[left]]:
                current -= 1
            
            left += 1
    
    left, right = res
    return s[left:right + 1] if res_len != float('inf') else ""



s = "ABCD"
t = "ABC"

print(min_window(s, t))
