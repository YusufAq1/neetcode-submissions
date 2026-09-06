class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        if len(nums) == 2:
            if nums[0] == nums[1] and abs(0-1) <= k:
                return True
            else:
                return False

        sorted_pairs = sorted(enumerate(nums), key=lambda x: x[1])

        l,r = 0,1 
        while r < len(sorted_pairs):
            if sorted_pairs[l][1] == sorted_pairs[r][1] and abs(sorted_pairs[l][0] - sorted_pairs[r][0]) <= k:
                return True
            else:
                l = r
                r += 1

            
        
        return False

