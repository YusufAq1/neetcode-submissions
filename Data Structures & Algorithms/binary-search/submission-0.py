class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        front = 0 
        back = len(nums)-1   

        while front <= back:
            mid = (back + front) // 2
            if nums[mid] == target:
                return mid
            if target > nums[mid]:
                front = mid + 1
            else:
                back = mid - 1
        
        return -1
       