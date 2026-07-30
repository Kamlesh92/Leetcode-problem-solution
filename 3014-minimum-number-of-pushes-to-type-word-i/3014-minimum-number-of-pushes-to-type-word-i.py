class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        
        q = n // 8
        r = n % 8
        
        return (q + 1) * (4 * q + r)