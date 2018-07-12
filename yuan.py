# -*- coding: utf-8 -*-
#type()
class Hello(object):
    def hello(self,name='world'):
        print('Hello,%s' %name)

h=Hello()
h.hello()
#type()可以查看一个类型或变量的类型，Hello是一个class,类型就是type,h是一个实例，它的类型就是class, Hello
print (type(Hello))
print (type(h))


#利用type()动态创建出类
def fn(self,name='world'):
    print('Hello,%s' %name)
#创建一个class对象，type（）函数依次传入3个参数，class的名称，继承的父类集合，方法名称和函数绑定
Hello2=type('Hello2',(object,),dict(hello2=fn))
h2=Hello2()
h2.hello2()

class ListMetaclass(type):
    def __new__(cls,name,bases,attrs):
        attrs['add']=lambda self,value:self.append(value)
        return type.__new__(cls,name,bases,attrs)
class MyList(list,metaclass=ListMetaclass):
    pass
L=MyList()
L.add(1)

#定义Field类，保存数据库表的字段名和字段类型
class Field(object):
    def __init__(self,name,column_type):
        self.name = name
        self.column_type = column_type
    def __str__(self):
        return ('%s:%s' %(self.__class__.__name__,self.name))
#在Field的基础上，定义各种类型的field
class StringField(Field):
    def __init__(self,name):
        super(StringField, self).__init__(name,'varchar(100)')
class IntegerField(Field):
    def __init__(self,name):
        super(IntegerField, self).__init__(name,'bigint')

class ModelMetaclass(type):
    def __new__(cls, name,bases,attrs):
        if name=='Model':
            return type.__new__(cls,name,bases,attrs)
        print ('Found model:%s'%name)
        mappings =dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings  # 保存属性和列的映射关系
        attrs['__table__'] = name  # 假设表名和类名一致
        return type.__new__(cls, name, bases, attrs)

class Model(dict,metaclass=ModelMetaclass):
    def __init__(self,**kw):
        super(Model, self).__init__(**kw)
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attributes '%s'"% key)

    def __setattr__(self, key, value):
        self[key]=value
    def save(self):
        fields=[]
        params=[]
        args =[]
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))

class User(Model):
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')
u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
print (u.save())
