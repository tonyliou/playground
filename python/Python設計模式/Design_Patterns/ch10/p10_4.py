# p10_4.py
from collections import Iterable, Iterator
from p10_3 import gen, fibonacci 
# 引入Iterable和Iterator

def testIsIterator():
    print("是否為Iterable物件：")
    print(isinstance([], Iterable))
    print(isinstance({}, Iterable))
    print(isinstance((1, 2, 3), Iterable))
    print(isinstance(set([1, 2, 3]), Iterable))
    print(isinstance("string", Iterable))
    print(isinstance(gen, Iterable))
    print(isinstance(fibonacci(10), Iterable))
    print("是否為Iterator物件：")
    print(isinstance([], Iterator))
    print(isinstance({}, Iterator))
    print(isinstance((1, 2, 3), Iterator))
    print(isinstance(set([1, 2, 3]), Iterator))
    print(isinstance("string", Iterator))
    print(isinstance(gen, Iterator))
    print(isinstance(fibonacci(10), Iterator))

testIsIterator()
