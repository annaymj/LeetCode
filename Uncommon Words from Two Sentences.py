```
We are given two sentences A and B.  (A sentence is a string of space separated words.  Each word consists only of lowercase letters.)

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Return a list of all uncommon words. 

You may return the list in any order.

 

Example 1:

Input: A = "this apple is sweet", B = "this apple is sour"
Output: ["sweet","sour"]
Example 2:

Input: A = "apple apple", B = "banana"
Output: ["banana"]
```

class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        dict_A = {}
        dict_B = {}
        res = []

        for s in A.split():
            if s not in dict_A:
                dict_A[s] = 1
            else:
                dict_A[s] += 1
        
        for s in B.split():
            if s not in dict_B:
                dict_B[s] = 1
            else:
                dict_B[s] += 1
                
        for k in dict_A.keys():
            if dict_A[k] == 1 and k not in dict_B:
                res.append(k)
            
        for k in dict_B.keys():
            if dict_B[k] == 1 and k not in dict_A:
                res.append(k)
        
        return res
        
