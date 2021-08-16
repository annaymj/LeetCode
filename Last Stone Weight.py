```
You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the smallest possible weight of the left stone. If there are no stones left, return 0.

 

Example 1:

Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.
Example 2:

Input: stones = [1]
Output: 1


```


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        sorted_stones = sorted(stones)
        
        while len(sorted_stones) > 1:
            stone1 = sorted_stones.pop()
            stone2 = sorted_stones.pop()
            
            # if stone1 == stone2, do nothing
            # if the two largest stones do not have equal weights, get the difference, update sorted_stones
            if stone1 != stone2:
                diff = stone1 - stone2
             
                # create new sorted_stones
                new_stones = []
                i = 0
                
                # append to new_stones list
                while i < len(sorted_stones) and sorted_stones[i] <= diff:
                    new_stones.append(sorted_stones[i])
                    i += 1 
                    
                new_stones.append(diff)
                
                # append the rest of the array
                while i < len(sorted_stones):
                    new_stones.append(sorted_stones[i])
                    i += 1 
                    
                # replace the array    
                sorted_stones = new_stones
    
                
        if len(sorted_stones) > 0 :
            return sorted_stones[0]
        return 0
        
