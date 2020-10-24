a = [1,2,3,4,5]

for x in a:
    print(x)

it = a.__iter__()
print(it)

while True:
    try:
        val = it.__next__()
    except StopIteration:
        break
    print(val)


class MyListIterator():
    '''
    迭代器中要实现__next__
    '''
    def __init__(self, my_list, start_index=0):
        self.my_list = my_list
        self.index = start_index
    def __next__(self):
        if self.index < len(self.my_list.data):
            val = self.my_list.data[self.index]
            self.index += 1
            return val
        else:
            raise StopIteration()


class MyList(): # 自己定义了一个可迭代list类，里面必须有一个iterator方法
    '''
    可迭代对象中要实现__iter__,就是一个迭代器
    '''
    def __init__(self, data):
        self.data = list(data)

    def __iter__(self): # 只要一个object实现了迭代函数，就是一个可迭代的对象
        return MyListIterator(self)

a = MyList([1,2,3,4])
for x in a:
    print(x)