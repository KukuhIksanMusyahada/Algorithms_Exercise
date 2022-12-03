'''
Given an integer array nums, 
return true if any value appears at least twice in the array, 
and return false if every element is distinct.
Input: nums = [1,2,3,1]
Output: true
'''

class Solution(object):
    def containsDuplicate(self, nums: list[int]):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hash = set()
        for val in nums:
            if val in hash:
                return True
            hash.add(val)

if __name__=='__main__':
    arr = [1,2,3,1]
    sol = Solution()
    is_contain = sol.containsDuplicate(arr)
    print(is_contain)