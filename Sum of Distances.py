from collections import defaultdict

class Solution:
    def distance(self, nums):
        n = len(nums)
        res = [0] * n
        
        pos = defaultdict(list)
        
        # Step 1: group indices
        for i, num in enumerate(nums):
            pos[num].append(i)
        
        # Step 2: process each group
        for indices in pos.values():
            k = len(indices)
            
            prefix = [0] * (k + 1)
            for i in range(k):
                prefix[i+1] = prefix[i] + indices[i]
            
            for i in range(k):
                left = indices[i] * i - prefix[i]
                right = (prefix[k] - prefix[i+1]) - indices[i] * (k - i - 1)
                res[indices[i]] = left + right
        
        return res