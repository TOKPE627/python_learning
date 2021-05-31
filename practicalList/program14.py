#WAP in python to implement
#multi-level
#In this type of inheritance, a class can inherit from a child class or derived class.
class MyFamily:
    def show_my_family(self):
        print("My family:")
  
class Father(MyFamily):
    fathername=""
    def show_father(self):
        print(self.fathername)

class Mother(MyFamily):
    mothername=""
    def show_mother(self):
        print(self.mothername)

class Son(Father, Mother):
    def show_parent(self):
        print("My father is: ", self.fathername)
        print("My mother is: ", self.mothername)

s1=Son()
s1.fathername = "TOKPE Ahouanye Dodo"
s1.mothername ="SOTODJI Rose"
s1.show_my_family()
s1.show_parent()