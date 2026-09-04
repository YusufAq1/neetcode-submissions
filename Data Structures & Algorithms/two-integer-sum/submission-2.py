class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # sorted_nums = sorted(nums, key=lambda x:x[0])
        sorted_nums = sorted((value, index) for index,value in enumerate(nums))

        i = 0
        j = len(nums) - 1

        while i != j:
            sum = sorted_nums[i][0] + sorted_nums[j][0]
            if sum > target:
                j -= 1
            elif sum < target:
                i += 1
            else:
                return [min(sorted_nums[i][1],sorted_nums[j][1]), max(sorted_nums[i][1],sorted_nums[j][1])]
                