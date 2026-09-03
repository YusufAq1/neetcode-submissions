class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        front = 0
        back = len(s) - 1

        pattern = r"[a-zA-Z0-9]"

        while front < back:
            match1 = re.match(pattern, s[front])
            match2 = re.match(pattern, s[back])
            if not match1:
                front += 1
                continue
            if not match2:
                back -= 1
                continue
            if s[front].lower() != s[back].lower():
                return False
            else:
                front += 1
                back -= 1
                
        
        return True