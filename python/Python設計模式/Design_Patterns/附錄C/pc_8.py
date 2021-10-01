# pc_8.py
class CustomMetaclass(type):
    def __init__(cls, what, bases=None, dict=None):
        print("CustomMetaclass.__init__ cls:", cls)
        super().__init__(what, bases, dict)
    def __call__(cls, *args, **kwargs):
        print("CustomMetaclass.__call__ args:", args, kwargs)
        self = super(CustomMetaclass, cls).__call__(*args, **kwargs)
        print("CustomMetaclass.__call__ self:", self)
        return self

class CustomClass(metaclass=CustomMetaclass):
    def __init__(self, *args, **kwargs):
        print("CustomClass.__init__ self:", self)
        super().__init__()
    def __new__(cls, *args, **kwargs):
        self = super().__new__(cls)
        print("CustomClass.__new__, self:", self)
        return self
    def __call__(self, *args, **kwargs):
        print("CustomClass.__call__ args:", args)

obj = CustomClass("Meta arg1", "Meta arg2", kwarg1=1, kwarg2=2)
print(type(CustomClass))
print(obj)
obj("arg1", "arg2")
