"""
43 multiply-strings
https://leetcode.com/problems/multiply-strings/ 
"""
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        #  if either one is 0 return 0
        if num1 == "0" or num2 == "0":
            return "0" 
        
        def count_zero(num):
            zero = 0
            for i in num[::-1]:
                if i == "0":
                    zero += 1
                else: break
            return zero 
        zero1 = count_zero(num1)
        zero2 = count_zero(num2) 
        
        def cut_zero(num, zero):
            num += "0"
            num = num[:-zero]
            return num 
        num1 = cut_zero(num1, zero1+1)
        num2 = cut_zero(num2, zero2+1) 
        
        total = 0
        for h0, i in enumerate(num1[::-1]):
            base = 10**h0
            curr = 0
            for h1, j in enumerate(num2[::-1]): 
                curr += (ord(j) - ord("0")) * (ord(i) - ord("0")) * 10**h1 
            total += curr * base 
        return str(total * 10**(zero1 + zero2))
                
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res1, res2 = 0, 0 
        for d in num1:
            res1 = res1 * 10 + (ord(d) - ord('0'))
        for d in num2:
            res2 = res2 * 10 + (ord(d) - ord('0'))
        return str(res1 * res2) 
"""

"""
304. Range Sum Query 2D - Immutable
https://leetcode.com/problems/range-sum-query-2d-immutable/ 
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not (matrix and matrix[0]):
            self.Mx = []
        else:
            n, m = len(matrix), len(matrix[0])
            print(n,m)
            self.Mx = [[0 for _ in range(m+1)] for __ in range(n+1)]
            for i in range(n):
                for j in range(m):
                    self.Mx[i+1][j+1] = self.Mx[i][j+1] + self.Mx[i+1][j] - self.Mx[i][j] + matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1+1, col1+1, row2+1, col2+1
        if not self.Mx:
            return 0
        return self.Mx[row2][col2] + self.Mx[row1-1][col1-1] - self.Mx[row2][col1-1] - self.Mx[row1-1][col2] 
        
"""
523. Continuous Subarray Sum
https://leetcode.com/problems/continuous-subarray-sum/
"""
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False
        if not k:
            prev = nums[0]
            c = 0
            for i in nums[1:]:
                if i == 0 and prev == 0:
                    return True
                elif i == 0:
                    c, prev = 1, 0
                else:
                    c, prev = 0, i
            return False
        sum_ = 0
        dict_ = {}
        for i, n in enumerate(nums):
            sum_ += n
            rem = sum_ % k 
            if rem != 0:
                if rem not in dict_:
                    dict_[rem] = i, sum_
                else:
                    if i - dict_[rem][0] > 1: 
                        return True
            elif i > 0:
                return True
        return False
    """
    pre_sum
    """
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mp = {0: -1}
        prefix_sum = 0
        for i, num in enumerate(nums):
            prefix_sum += num
            if k != 0:
                prefix_sum = prefix_sum % k
            if prefix_sum in mp:
                if i - mp[prefix_sum] > 1:
                    return True
            else:
                mp[prefix_sum] = i

        return False

