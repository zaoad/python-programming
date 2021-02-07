from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        arr=[]
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if(nums[i]+nums[j]+nums[k]==0):
                        arr.append([nums[i],nums[j],nums[k]])
        return arr;
if __name__=='__main__':
        arr=Solution.threeSum(Solution,[-1,0,1,2,-1,-4])
        print(arr)