class Solution:
    def survivedRobotsHealths(self, positions, healths, directions):
        order = sorted(range(len(positions)), key=positions.__getitem__)
        stack = []
        
        for i in order:
            if directions[i] == 'R':
                stack.append(i)
            else:
                hi = healths[i]
                while stack and hi:
                    j = stack[-1]
                    hj = healths[j]
                    
                    if hj < hi:
                        hi -= 1
                        healths[j] = 0
                        stack.pop()
                    elif hj > hi:
                        healths[j] = hj - 1
                        hi = 0
                    else:
                        healths[j] = 0
                        hi = 0
                        stack.pop()
                
                healths[i] = hi
        
        return [h for h in healths if h]