class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        if len(s) == 2:
            if s[0] != s[1]:
                return 2 
            else:
                return 1 
        
        dups = set()

        left = 0 
        right = 1

        dups.add(s[left])
        max_substring = 1
        while left < right and right < len(s):
            substring = 0 
            if s[left] == s[right]:
                left += 1
                right += 1
                continue
            elif s[right] not in dups:
                dups.add(s[right])
                substring = (right - left) + 1
                right += 1
            else:
                dups.remove(s[left])
                left += 1
                
          
            max_substring = max(max_substring, substring)
        
        return max_substring
            




