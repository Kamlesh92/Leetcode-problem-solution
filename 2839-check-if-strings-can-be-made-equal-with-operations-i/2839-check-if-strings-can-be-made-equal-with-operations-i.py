class Solution:
    def canBeEqual(self, s1, s2):
        even1, odd1 = [], []
        even2, odd2 = [], []
        
        for i in range(len(s1)):
            if i % 2 == 0:
                even1.append(s1[i])
                even2.append(s2[i])
            else:
                odd1.append(s1[i])
                odd2.append(s2[i])
        
        even1.sort()
        even2.sort()
        odd1.sort()
        odd2.sort()
        
        return even1 == even2 and odd1 == odd2