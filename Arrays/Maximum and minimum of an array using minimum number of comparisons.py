
class Solution:
    def solve(self,arr):
        mini , maxi = float('inf'), -float('inf')
        for i in arr:
            mini = min(mini,i)
            maxi = max(maxi,i)
        return [mini,maxi]

sol = Solution()
print(sol.solve([1,2,3,4,5,6]))