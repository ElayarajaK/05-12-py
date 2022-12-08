from unicodedata import name


class A:
    def __init__(self,name):
        self.name=name;
    def printval(self):
        print(self.name)
    def __str__(self) :       
       return  "value : {},marks :{}".format(self.name,10);
    

obj = A(10);

print(obj.name)
