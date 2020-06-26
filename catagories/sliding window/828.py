'''
828. Count Unique Characters of All Substrings of a Given String
Hard

求每个substring中unique char(只出现一次的char)的个数，再求和
思路：1.暴力解法遍历所有子串 
     2.原思路是找子串再找char，现在转换思路，遍历char，找该char在多少个substr中是unique的
        比如ABFCDEF，对于F来说，第一个F前的子串2，第一个到第二个之间子串3
        以第一个F为unique char的子串个数为2+3+2*3+1，最后的1是F自身
        i=pos(F1) j=(pos(F2)-pos(F1)-1) i+j+ij+1 (i+j可化简)
'''


class Solution():
    def uniqueLetterString(self, s: str) -> int:
        pos = {} # 存储每个char的位置，char的位置可能有多个，所以value是list
        for i in range(len(s)):
            char = s[i]
            if char not in pos:
                pos[char] = [i]
            else:
                pos[char].append(i)
        
        sum_uchar = 0 #sum of unique char
        for char_pos in pos.values():
            if len(char_pos) == 1:
                i = char_pos[0]
                j = len(s) - char_pos[0] - 1
                sum_uchar += (i+j+i*j+1)
            
            else:
                for n in range(len(char_pos)):
                    if n == 0:
                        i = char_pos[n]
                        j = char_pos[n+1] - char_pos[n] - 1
                    elif n == len(char_pos) - 1:
                        i = char_pos[n] - char_pos[n-1] - 1
                        j = len(s) - char_pos[n] - 1
                    else: 
                        i = char_pos[n] - char_pos[n-1] - 1 
                        j = char_pos[n+1] - char_pos[n] - 1
                    sum_uchar += (i+j+i*j+1)

        return sum_uchar 




if __name__ == '__main__':
    s = 'LEETCODE'
    print(Solution().uniqueLetterString(s))