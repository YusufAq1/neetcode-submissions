class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) <= 1:
            return len(nums)
        
        nums.sort()

        max_sequence = 0 
        longest_sequence = 1 

        for i in range(0, len(nums)-1):
            
            if nums[i+1] == nums[i] + 1:
                longest_sequence += 1 
            elif nums[i+1] == nums[i]:
                i += 1
            else:
                max_sequence = max(longest_sequence, max_sequence)
                longest_sequence = 1 
                i += 1
            
            i += 1 
        
        return max(max_sequence, longest_sequence)
            

        