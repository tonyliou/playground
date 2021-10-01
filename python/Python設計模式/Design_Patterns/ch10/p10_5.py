# p10_5.py
from p10_3 import fibonacci

def testNextItem():
    print("將Iterable物件轉成Iterator物件：")
    l = [1, 2, 3]
    itrL = iter(l)
    print(next(itrL))
    print(next(itrL))
    print(next(itrL))
    print("next()函數遍歷反覆運算器元素：")
    fib = fibonacci(4)
    print(next(fib))
    print(next(fib))
    print(next(fib))
    print(next(fib))
    print(next(fib))

testNextItem()
