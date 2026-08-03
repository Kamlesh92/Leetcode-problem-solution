class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        def dfs(i):
            nonlocal memo, n

            
            if i >= n:
                return 0

            
            if i in memo:
                return memo[i]

            res = float('-inf')
            agg = 0              

            for j in range(i, i + 3):
                
                if j >= n:
                    break
                agg += stoneValue[j]

                
                temp = agg - dfs(j + 1)

                
                res = max(res, temp)

            
            memo[i] = res

            return memo[i]

        n = len(stoneValue)
        memo = dict()

        alice = dfs(0)

        return 'Alice' if alice > 0 else 'Tie' if alice == 0 else 'Bob'