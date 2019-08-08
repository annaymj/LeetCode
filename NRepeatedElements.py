import collections

A = [1,2,3,3]
class Solution:
    def repeatedNTimes(self, A):
        n = len(A)/2
        set_A = set(A)
        for num in set_A:
            if A.count(num) == n:
                return num
    
    def repeatedNTimes2(self,A):
        count = collections.Counter(A)
        for k in count:
          if count[k] > 1:
            return k
          
S = Solution()
S.repeatedNTimes2(A)