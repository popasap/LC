class Solution:
    def climbStairs(self, n: int) -> int:
        #dp[i] = dp[i-1] + dp[i-2]
        
    
        memo={}
        return self.clim(n, memo)
    
    def clim(self, n, memo):
        if n in memo:
            return memo[n]
        elif n == 1:
            memo[1] = 1
            return memo[1]
        elif n == 2:
            memo[2] = 2
            return memo[2]
        memo[n] = clim(n-1, memo) + clim(n-2, memo) 
        return memo[n]
        
