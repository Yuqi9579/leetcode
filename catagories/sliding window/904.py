'''
Fruit into Baskets
Medium

在一排树中，第 i 棵树产生 tree[i] 型的水果。
你可以从你选择的任何树开始，然后重复执行以下步骤：

1.把这棵树上的水果放进你的篮子里。如果你做不到，就停下来。
2.移动到当前树右侧的下一棵树。如果右边没有树，就停下来。
请注意，在选择一颗树后，你没有任何选择：你必须执行步骤 1，然后执行步骤 2，然后返回步骤 1，然后执行步骤 2，依此类推，直至停止。

你有两个篮子，每个篮子可以携带任何数量的水果，但你希望每个篮子只携带一种类型的水果。
用这个程序你能收集的水果总量是多少？

##问题抽象: 求一个串中最长连续子串，该子串中只包含两类元素
'''
import doctest

def totalFruit(tree):
    '''
    >>> [1,2,1]
    3
    >>> [0,1,2,2]
    3
    >>> [3,3,3,1,2,1,1,2,3,3,4]
    5
    '''
    max_len = MAX = -float('inf')
    exist = [] #记录子串中的元素，最多为2
    j = 0
    pos = {} #记录每种元素最后出现的位置
    for i in range(len(tree)):
        pos[tree[i]] = i #更新位置，不用删除，记录所有的元素都行
        if tree[i] in exist:
            max_len = max(max_len, i-j+1) # i-j+1，知道首尾求长度的公式
        elif len(exist) < 2:
            max_len = max(max_len, i-j+1)
            exist.append(tree[i])
        else: #出现已知两元素之外的元素
            item = exist.pop(1-exist.index(tree[i-1])) # 例如[1,2,2,3]pop掉1，并且得到1
            exist.append(tree[i]) # append 3
            j = pos[item] + 1 # 将指针移动到第一个2，因为子串最多两个元素，所以3前面只能出现1,2...2,3或者1,2,3的情况
    return max_len

if __name__ == '__main__':
    print(totalFruit([0,1,6,6,4,4,6]))
        
