def testList():
    list = [1, 2, 3];
    list1 = list;
    print("id(list):", id(list))
    print("id(list1):", id(list1))
    print("修改之前：")
    print("list:", list)
    print("list1:", list1)
    list1.append(4);
    print("修改之後：")
    print("list:", list)
    print("list1:", list1)

testList()


