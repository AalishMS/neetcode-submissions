class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer=[]
        for i in range(0,len(nums),1):
            for j in range(0,len(nums),1):
                if nums[i]+nums[j]==target and i!=j:
                    answer.append(i)
                    answer.append(j)
        answer.sort()
        unique=set(answer)
        final=list(unique)
        return final