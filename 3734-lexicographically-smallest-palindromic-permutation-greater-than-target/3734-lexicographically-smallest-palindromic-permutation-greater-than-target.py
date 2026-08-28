class Solution(object):
    def lexPalindromicPermutation(self, s, target):
        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - ord('a')] += 1

       
        odd = 0
        mid = -1
        for i in range(26):
            if freq[i] % 2:
                odd += 1
                mid = i

        if odd > 1:
            return ""

        for i in range(26):
            freq[i] //= 2

        n = len(s)
        half = n // 2
        ans = [""] * n

        def make():
            if mid != -1:
                ans[half] = chr(mid + ord('a'))
            for i in range(half):
                ans[n - 1 - i] = ans[i]

        pos = 0

       
        while pos < half:
            c = ord(target[pos]) - ord('a')
            if freq[c] == 0:
                break
            ans[pos] = target[pos]
            freq[c] -= 1
            pos += 1

        
        if pos == half:
            make()
            res = "".join(ans)
            if res > target:
                return res

        # Backtrack
        while True:
            if pos < half:
                start = ord(target[pos]) - ord('a') + 1

                for c in range(start, 26):
                    if freq[c]:
                        ans[pos] = chr(c + ord('a'))
                        freq[c] -= 1

                        idx = pos + 1
                        for x in range(26):
                            while freq[x]:
                                ans[idx] = chr(x + ord('a'))
                                idx += 1
                                freq[x] -= 1

                        make()
                        return "".join(ans)

            if pos == 0:
                return ""

            pos -= 1
            freq[ord(target[pos]) - ord('a')] += 1


        """
        :type s: str
        :type target: str
        :rtype: str
        """
        