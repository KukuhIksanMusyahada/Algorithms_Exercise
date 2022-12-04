'''
Given an integer array nums, 
find the subarray which has the largest sum and return its sum.
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Constrain:
1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
'''

class Solution(object):
    def sol1(self, nums: list[int]):
        """
        :type nums: List[int]
        :rtype: int
        """
        sums = []
        for i in range(len(nums)):
            for j in range(i,len(nums)+1):
                sum = 0
                for k in range(i,j):
                    sum += nums[k]
                sums.append(sum)
        return max(sums)
                    

    def sol2(self, nums: list[int]):
        """
        :type nums: List[int]
        :rtype: int
        """
        sums = []
        for i in range(len(nums)):
            sum = 0
            for j in range(i,len(nums)):
                sum += nums[j]
                sums.append(sum)
        return max(sums)

    def sol3(self, nums: list[int]):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSum = nums[0]
        curSum = 0

        for val in nums:
            if curSum< 0:
                curSum = 0
            curSum += val
            maxSum = max(curSum,maxSum)
        return maxSum
        


if __name__=='__main__':
    arr = [5,4,-1,7,8]
    sol = Solution()
    print(sol.sol1(arr))
    print(sol.sol2(arr))
    print(sol.sol3(arr))