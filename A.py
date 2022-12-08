from abc import ABC, abstractmethod


class TATA(ABC):

    
    @abstractmethod
    def method1(self):
        print("from method1 ..")
    @abstractmethod
    def method2(self):
        print("from method2 ..")
    @abstractmethod
    def method3(self):
        print("from method3 ..")




class TCS(TATA):
    def method1(self):
        print("This TCS child comp 1")
    
    def method3(self):
         print("This TataSteal child comp 1")
class TataPoer(TCS):
    def method2(self):
         print("This TP child comp 1")
    

#class TataSteal(TataPoer):
          
   
       
        
#obj = TataSteal();

#obj.method1();
#obj.method2();
#obj.method3();
obj=TataPoer();
obj.method1();
obj.method2();
obj.method3();
