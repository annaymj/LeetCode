# Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array 
# such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_dict={}
        for i in range(len(nums)):
            if nums[i] in num_dict.keys():
                if i - num_dict[nums[i]] <= k:
                    return True
                else:
                    num_dict[nums[i]] = i
            else:
                num_dict[nums[i]] = i
        return False
    
    
    def containsNearbyDuplicate3(self, nums: List[int], k: int) -> bool:
        num_set = set()
        
        for i in range(len(nums)):
            if nums[i] in num_set:
                return True
            num_set.add(nums[i])
            
            if len(num_set) > k:
                num_set.remove(nums[i-k])
        return False
        
        
    def containsNearbyDuplicate2(self, nums: List[int], k: int) -> bool:
        num_dict = {}
        for i in range(len(nums)):
            if nums[i] not in num_dict.keys():
                num_dict[nums[i]] = [i]
            else:
                num_dict[nums[i]].append(i)
        
        for num in num_dict:
            index_list = num_dict[num]
            if len(index_list) >= 2:
                for i in range(1,len(index_list)):
                    if index_list[i] - index_list[i-1] <= k:
                        return True
        return False
                
        
