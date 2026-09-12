class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows_m = len(matrix)
        columns_n = len(matrix[0])

        low = 0 
        high = (rows_m * columns_n) - 1

        while low <= high:
            mid = (low+high) // 2
            row = mid // columns_n
            col = mid % columns_n

            mid_element = matrix[row][col]

            if mid_element == target:
                return True 
            elif target > mid_element:
                low = mid + 1
            else:
                high = mid - 1
        
        return False
        
        