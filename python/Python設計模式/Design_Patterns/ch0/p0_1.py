# p0_1py
age = 18        # int
weight = 62.51  # float
name = "Tony"	# string
print("age:", age)
print("weight:", weight)
print("name:", name)
# 變數的類型可以直接改變
age = name
print("age:", age)

a = b = c = 5
# a、b、c三個變數指向相同的記憶體空間，具有相同的值
print("a:", a, "b:", b, "c:", c)
print("id(a):", id(a), "id(b):", id(b), "id(c):", id(c))
