class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        if s == t:
            return True 

        map = {}

        for letter in s:
            if letter not in map:
                map[letter] = 1
            else:
                map[letter] += 1

        map2 = {}

        for letter in t:
            if letter not in map2:
                map2[letter] = 1
            else:
                map2[letter] += 1
        
        if map == map2:
            return True 
        else:
            return False
        
           
                
