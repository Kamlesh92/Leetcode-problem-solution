class Solution:
    def minimumPushes(self, word: str) -> int:
        mp = Counter(word)
        pq = [0] * 8
        heapq.heapify(pq)
        chars = sorted(mp.keys(), key=lambda c: -mp[c])
        ans = 0
        for c in chars:
            el = heapq.heappop(pq)
            el += 1
            ans += mp[c] * el
            heapq.heappush(pq, el)
        return ans