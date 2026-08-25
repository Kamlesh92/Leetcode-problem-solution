class Solution:
    def generateString(self, str1, str2):
        n, m = len(str1), len(str2)
        word = ['?'] * (n + m - 1)
        fixed = [False] * (n + m - 1)

        for i in range(n):
            if str1[i] == 'T':
                for j in range(m):
                    if word[i + j] == '?' or word[i + j] == str2[j]:
                        word[i + j] = str2[j]
                        fixed[i + j] = True
                    else:
                        return ""

        for i in range(len(word)):
            if word[i] == '?':
                word[i] = 'a'

        for i in range(n):
            if str1[i] == 'F':
                if word[i:i+m] == list(str2):
                    changed = False
                    for j in range(m - 1, -1, -1):  
                        pos = i + j
                        if not fixed[pos]:
                            word[pos] = 'b' if word[pos] == 'a' else 'a'
                            changed = True
                            break
                    if not changed:
                        return ""

        return "".join(word)