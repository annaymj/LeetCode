intervals = [[1,3],[2,6],[8,10],[15,18]]


class Solution:
    def merge(self, intervals):
      intervals = sorted(intervals)
      result = [intervals[0]]
      
      for i in range(1,len(intervals),1):
        for j in range(len(result)):
          cur_result = self.compare(result[j],intervals[i])
          result.remove(result[j])
          result.append(cur_result)
        
      return result
          
          
          
  
    # assuming the intervals are sorted   
    def compare(self,inter1, inter2):
      
      #case1: 2 within 1
      if inter1[0] <= inter2[0] and inter1[1] >= inter2[1]:
        return inter1
      
      #case2: 1 and 2 does not overlap
      elif inter1[1] < inter2[0]:
        return[inter1,inter2]
      
      #case3: 1 over with 2
      elif inter1[1] >= inter2[0] and inter1[0] <= inter2[0]:
        return[inter1[0],inter2[1]]
       

S = Solution()
S.compare([1,3],[2,6])
S.merge([[1,3],[2,6]])
S.merge([intervals])

S.merge([[1,9],[2,6],[3,7],[10,16]])