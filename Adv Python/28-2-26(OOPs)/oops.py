"""class person:
    x=5
    y=10
    def func():
        print('h')

obj=person()
obj.func()"""
#TypeError: person.func() takes 0 positional arguments but 1 was given
#because -- obj itself pass as a argument --> obj.func(obj)

class person:
    x=5
    y=10
    def func(self,name,age):
        self.name=name
        self.age=age
    

obj=person()
obj.func("dev",20)
print(obj.name)
print(obj.age)

print(obj.__dict__)

#an object is a entity that has attribute and behaviour . eg -- parot is a object having 
# attribute : name,age,colur .....Behaviour : dancing , singing 
# since all members in a py are private in nature while in java we have to use public,private,protected...

class person:
    x=5
    y=10
    def func(self,name,age):
        self.name=name
        self.age=age
    
    def func2(self,age):
        pass
    
obj=person()
obj.func("dev",20)
print(obj.name)
print(obj.age)