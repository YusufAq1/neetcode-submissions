class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0],nums[1])
        
        nums[2] += nums[0]
        max1 = nums[2]
        max2 = max(nums[0],nums[1])

        for i in range(3,len(nums)):
            if nums[i-1] != max2:
                nums[i] += max2
                max1 = max(max2, max1)
                max2 = nums[i]
            else:
                nums[i] += max1
                max2 = max(max2, max1)
                max1 = nums[i]
            
        
        return max(nums[len(nums)-1], nums[len(nums)-2])