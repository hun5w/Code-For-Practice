y=iter([1,2,3,4,5])
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
# StopIteration

class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration  # 没有更多元素时抛出 StopIteration 异常

# 使用这个迭代器
my_iter = MyIterator([1, 2, 3, 4])
for item in my_iter:
    print(item)
