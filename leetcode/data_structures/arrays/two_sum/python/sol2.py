class Solution:    
    def solve(self, d, nums: List[int], i: int, t: int):
        if(t-nums[i]) in d.keys(): return d[t-nums[i]], i
        else: 
            d[nums[i]] = i
            return self.solve(d=d, nums=nums, i=i+1, t=t)
            
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return self.solve(d=dict(), nums=nums, i=0, t=target)
