class Solution:
    def shortestBeautifulSubstring(self, s, k):
        smallStr = ""
        oneCnt = 0
        left = 0

        for right in range(len(s)):
            if s[right] == '1':
                oneCnt += 1

            while oneCnt == k:
                smallStr = self.lexico(
                    smallStr,
                    s[left:right + 1]
                )

                if s[left] == '1':
                    oneCnt -= 1

                left += 1

        return smallStr

    def lexico(self, str1, str2):
        if not str1:
            return str2

        if len(str1) > len(str2):
            return str2

        if len(str2) > len(str1):
            return str1

        return min(str1, str2)