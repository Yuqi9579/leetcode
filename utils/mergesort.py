'''
归并排序

一个分解，重构的过程
时间复杂度O(nlogn)
'''


class MergeSort():
    '''
    排序一个list
    '''
    def __call__(self, *args):
        return self.mergesort(*args)
    
    def mergesort(self, l):
        '''
        递归
        '''
        if len(l) <= 1:
            return l
        mid = len(l) // 2   # len(s) = 9, mid = 5
        left = self.mergesort(l[:mid])
        right = self.mergesort(l[mid:])
        return self.merge(left, right) 


    def merge(self, left, right):
        '''
        合并两个已经排序好的列表，产生一个排序新列表
        '''
        res = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        res += (left[i:] + right[j:])
        return res



class MergeSortSortedList():
    '''
    排序几个排序过的lists，比如[[1,2,3],[3,6,9],[2,3,5]]
    返回排序后的list，不是array
    '''
    def __call__(self, *args):
        return self.mergesort(*args)[0]
    
    def mergesort(self, l):
        '''
        递归
        '''
        if len(l) <= 1:
            return l
        mid = len(l) // 2   # len(s) = 9, mid = 5
        left = self.mergesort(l[:mid])
        right = self.mergesort(l[mid:])
        return self.merge(left, right) 


    def merge(self, left_l, right_l):
        '''
        合并两个已经排序好的列表，产生一个排序新列表
        '''
        left = left_l[0]
        right = right_l[0]
        res = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        res += (left[i:] + right[j:])
        return [res]




if __name__ == '__main__':
    seq = [2,3,4,6,4,5,8,2,3,6,5,8,9,6]
    sort = MergeSort()
    print(sort(seq))