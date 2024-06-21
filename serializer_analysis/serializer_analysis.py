class SerializerMetaclass(type):
    def __new__(cls, name, bases, attrs):
        # print(name, bases, attrs)
        data_dict = {}
        for k,v in list(attrs.items()): # 由于dict在遍历的时候删除元素会改变字典的大小，从而导致迭代器失效，所以需要先将attrs.items()转换为list
            # print(k, v)
            if isinstance(v, int):
                # del attrs[k]
                data_dict[k] = attrs.pop(k) # 删除attrs中的k-v键值对，并将其添加到data_dict中
        attrs['_declared_fields'] = data_dict
        return super().__new__(cls, name, bases, attrs)

class BaseSerializer(object): # 由type创建
    pass

class Serializer(BaseSerializer, metaclass=SerializerMetaclass):
    pass

class ModelSerializer(Serializer):
    pass

class UserSerializer(ModelSerializer):
    v1 = 123
    v2 = 456
    v3 = '八嘎'

print(UserSerializer._declared_fields) # 创建UserSerializer时，SerializerMetaclass的__new__方法被调用，UserSerializer的_declared_fields属性被设置为121212122
print(UserSerializer.v3) # '八嘎'
#print(UserSerializer.v2) # 报错
#print(UserSerializer.v1) # 报错
