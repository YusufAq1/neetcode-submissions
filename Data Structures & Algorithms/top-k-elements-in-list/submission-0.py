class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        


        count = {}
        
        for num in nums: 
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1


        ans = []

        while k != 0:
            max_key = max(count, key=count.get)
            ans.append(max_key)
            count.pop(max_key)
            k -= 1

        return ans