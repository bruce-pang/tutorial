class MyType(type):
    def __init__(cls, name, bases, attrs):
        # 2.填充类
        print('Initializing class', name)
        super(MyType, cls).__init__(name, bases, attrs)
    def __new__(cls, name, bases, attrs):
        # 1.创建空值的类
        print('Creating class', name)
        return super(MyType, cls).__new__(cls, name, bases, attrs)
    def __call__(cls, *args, **kwargs): # __call__方法会在实例化类的对象的时候自动触发子类对象 __new__和__init__方法
        print("执行type的__call__方法")
        obj = cls.__new__(cls, *args, **kwargs)
        print("==========")
        cls.__init__(obj, *args, **kwargs)
        return obj

class Base(object, metaclass=MyType):
    def __init__(self):
        print("初始化")

    def __new__(cls, *args, **kwargs):
        print("实例化类的对象")
        return object.__new__(cls)

    def __call__(self, *args, **kwargs):
        print("执行Base的__call__方法")

obj = Base()
obj()

#1.类是由MyType创建的。 类其实是MyType类实例化的对象。
#2.Base是类，MyType类的对象； Base() <====> MyType()() -> 一个类实例化出来的对象， 对象()会执行__call__方法