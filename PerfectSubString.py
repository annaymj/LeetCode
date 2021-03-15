```
# find the perfect substring that has each characater appear exactly k times 
s = '1102021222'
k = 2
# return the number of perfect substring, expected return 6
# s[0:1] = 11
# s[0:5] = 110202
# s[2:5] = 0202
# s[1:6] = 102021
# s[7:8] = 22
# s[8:9] = 22
```

def isPerfect(substring, k):
    s_dict = {}
    for char in substring:
        if char not in s_dict.keys():
            s_dict[char]  = 1
        else:
            s_dict[char] += 1
             
    for val in s_dict.values():
        if val != k:
            return False
    return True

def perfectSubstring(s,k):
    if k > len(s):
        return 0
     
    res = 0 
     # loop through the list to get substring 
    for i in range(len(s)- k + 1):
        for j in range(i+k, len(s)+1):  
            substring = s[i:j]
            # check whether the substring is a perfect string, if yes, res += 1
            if isPerfect(substring, k):                   
                res += 1
    return res



