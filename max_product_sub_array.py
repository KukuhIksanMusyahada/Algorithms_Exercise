'''
Given an integer array nums, find a subarray that has the largest product, and return the product.
The test cases are generated so that the answer will fit in a 32-bit integer.
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
'''
class Solution(object):

    def sol1(self, nums: list[int]):
        """
        :type nums: List[int]
        :rtype: int
        """
        prods = []
        for i in range(len(nums)):
            prod = 1
            for j in range(i,len(nums)):
                
                prod *= nums[j]
                prods.append(prod)
        return max(prods)

    def sol2(self, nums: list[int]):
        """
        :type nums: List[int]
        :rtype: int
        """
        curMin,curMax = 1,1
        res = max(nums)

        for val in nums:
            if val == 0:
                curMax,curMin = 1,1
                continue
            tmp = curMax * val
            curMax = max(curMax*val, curMin*val, val)
            curMin = min(tmp, curMin*val, val)
            res = max(curMin,curMax,res)
        return res








if __name__=='__main__':
    arr = [2,-3,-2,4]
    sol = Solution()
    print(sol.sol1(arr))
    print(sol.sol2(arr))