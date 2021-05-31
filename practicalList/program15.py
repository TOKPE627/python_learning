class Level1:
    def m(self):
        print("In level1") 
        
class Level2(Level1):
    def m(self):
        print("In level2")
  
class Level3(Level1):
    def m(self):
         print("In Level3")     
      
class Level4(Level2, Level3):
    def m(self):
        print("In Level4")   
  
obj = Level4()
obj.m()
  
Level2.m(obj)
Level3.m(obj)
Level1.m(obj)