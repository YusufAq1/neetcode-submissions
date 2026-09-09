# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        if guess(n) == 0:
            return n

        my_pick = n // 2
        low = 1
        high = n
        found = False
        while not found:
            result = guess(my_pick)
            if result == 0:
                found = True
                break
            elif result == 1:
                low = my_pick + 1
                my_pick = (low + high) // 2
                continue
            else:
                high = my_pick - 1
                my_pick = (low + high) // 2
        
        return my_pick


