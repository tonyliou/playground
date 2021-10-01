# p0_2.py
list = ['Thomson', 78, 12.58, 'Sunny', 180.2]
tinylist = [123, 'Tony']
print("list:", list)  # 輸出完整列表
print("list[0]:", list[0])  # 輸出清單的第一個元素
print("list[1:3]:", list[1:3])  # 輸出第二個至第三個元素
print("list[2:]:", list[2:])  # 輸出從第三個開始至清單末尾的所有元素
print("tinylist * 2 :", tinylist * 2)  # 輸出列表兩次
print("list + tinylist :", list + tinylist)  # 列印組合的清單
list[1] = 100
print("設置list[1]:", list)  # 輸出完整列表
list.append("added data")
print("list添加元素:", list)  # 輸出增加後的列表
