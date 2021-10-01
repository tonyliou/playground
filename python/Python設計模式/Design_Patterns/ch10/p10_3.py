# p10_3.py
#  方法一：使用()定義生成器
gen = (x * x for x in range(10))

#  方法二：使用yield定義generator函數
def fibonacci(maxNum):
    """斐波那契數列的生成器"""
    a = b = 1
    for i in range(maxNum):
        yield a
        a, b = b, a + b
def testIterable():
    print("方法一，0-9的平方數：")
    for e in gen:
        print(e, end="\t")
    print()
    print("方法二，斐波那契數列：")
    fib = fibonacci(10)
    for n in fib:
        print(n, end="\t")
    print()
    print("內置容器的for迴圈：")
    arr = [x * x for x in range(10)]
    for e in arr:
        print(e, end="\t")
    print()
    print()
    print(type(gen))
    print(type(fib))
    print(type(arr))

testIterable()
