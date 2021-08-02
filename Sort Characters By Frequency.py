```
Given a string s, sort it in decreasing order based on the frequency of characters, and return the sorted string.

 

Example 1:

Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input: s = "Aabb"
Output: "bbAa"
Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
```

class Solution:
    def frequencySort(self, s: str) -> str:
        char_dict = {} 
        res = ''
        for char in s:
            if char not in char_dict.keys():
                char_dict[char] = 1
            else:
                char_dict[char] += 1
                
        # sort char_dict by values
        sorted_dict = dict(sorted(char_dict.items(), key=lambda item: item[1], reverse = True))
        
        for k in sorted_dict.keys():
            res += k * sorted_dict[k]
#            for v in range(sorted_dict[k]):
#                res += k   
        return res
        
