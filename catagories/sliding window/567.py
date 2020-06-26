'''
Permutation in String
'''

from collections import Counter, defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        简单的sliding window，因为要在s2中寻找s1的permutation子串，
        所以只需要比较子串和s1是否每个元素的个数相等，用hashtable比较就行
        '''
        if len(s1) + len(s2) == 0:
            return False
        count = Counter(s1)
        wiz = len(s1)
        i = 0 
        while i <= len(s2) - wiz:
            if s2[i] not in count:
                i += 1
                continue
            exist = Counter(s2[i:i+wiz])
            if exist == count:
                return True
            i += 1
        return False
                    
                
 
        
        

if __name__ == '__main__':
    s1 = "pqzhi"
    s2 = "ghrqpihzybre"

    print(Solution().checkInclusion(s1, s2))
   
    