# pb_10.py
class ClassE:
    def __call__(self, *args):
        print("This is __call__ function, args:", args)

e = ClassE()
print(callable(e))
e("arg1", "arg2")
