```
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.
 

Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

Example 2:
Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
```




class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates = sorted(candidates)
        results = []
            
        if sum(candidates) < target:
            return []
        elif sum(candidates) == target:
            results.append(candidates)
            return results
        
        self.dfs(target, [], 0, results, candidates)
        
        results2=[] 
        for lst in results:
            if lst not in results2:
                results2.append(lst)
        
        return results2
    
    def dfs(self,remain, comb, start, results, candidates):
        if remain == 0:
            # make a deep copy of the current combination
            comb_list = list(comb)
            # if comb_list not in results:
            results.append(comb_list)
            return
        elif remain < 0:
            # exceed the scope, stop exploration.
            return

        for i in range(start, len(candidates)):
            # add the number into the combination
            comb.append(candidates[i])
            # give the current number another chance, rather than moving on
            self.dfs(remain - candidates[i], comb, i + 1, results, candidates)
            # backtrack, remove the number from the combination
            comb.pop()
