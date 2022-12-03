'''
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
'''
class Two_Sums:

    def sol1(self, arr: list[int], target: int):
        for i,val in enumerate(arr):
            for j in range(i+1,len(arr)):
                check = val +arr[j]
                if check == target:
                    print([i,j])
       


    def sol2(self, arr: list[int], target: int):
        hashMap = {}
        for i, val in enumerate(arr):
            dif = target - val 
            if dif in hashMap:
                print([hashMap[dif],i])
                
            hashMap[val]= i



if __name__=='__main__':
    inp = [2,7,11,15]
    target = 22
    problems = Two_Sums()
    problems.sol2(inp,target)
    problems.sol1(inp,target)