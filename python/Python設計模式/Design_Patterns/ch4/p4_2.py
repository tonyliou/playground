def func(num):
    """定義內建函式並返回"""
    def firstInnerFunc():
        return "這是第一個內建函式"
    def secondInnerFunc():
        return "這是第二個內建函式"
    if num == 1:
        return firstInnerFunc
    else:
        return secondInnerFunc

print(func(1))
print(func(2))
print(func(1)())
print(func(2)())
