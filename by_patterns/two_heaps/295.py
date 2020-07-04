'''
295. Find median from data stream
Hard

https://www.youtube.com/watch?v=60xnYZ21Ir0

median：一个list的中间值，如果list长度为偶数，则median为中间两数的平均值
设计一个数据结构，可以实现下面两个操作：
1.void addNum(int num) 添加
2.double findMedian()

思路：1.每进来一个元素，对数据进行排序，找出中位数，注意中位数只存在于ordered list中
     2.用两个堆来放数据，一半为less(大根堆)，一半为larger(小根堆)，(len(less) - len(larger)) in [0,1]，在总个数为奇数时，less比larger多一个
     我们不太关心每个部分的排序，只关心less的最大值和larger的最小值，总数为奇数时，median = less.top，总数为偶数时，median = (less.top+larger.top)/2   
     heappop，heappush时间复杂度为logn
'''

from heapq import *

class MedianFinder():

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        self.count = 0 #用来计数加入的数据量

    def addNum(self, num: int) -> None:

        #这种做法能始终保证len(larger)<=len(less)，并不需要分类讨论count为奇偶的情况
        #count为奇数的时候if条件肯定会执行的

        heappush(self.max_heap, -num)
        heappush(self.min_heap, -self.max_heap[0])
        heappop(self.max_heap)
        if len(self.min_heap) > len(self.max_heap):
            heappush(self.max_heap, -self.min_heap[0])
            heappop(self.min_heap)
        self.count += 1

    def findMedian(self) -> float:
        if self.count % 2 == 0:
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        else:
            return -self.max_heap[0]

if __name__ == '__main__':

    finder = MedianFinder()
    for i in [1,6,5,4,7,8,3,4,5,6,2,3,7,8,6]:
        finder.addNum(i)
    print(finder.max_heap)
    print(finder.min_heap)
    print(finder.findMedian())