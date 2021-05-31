#Program in Python to implement
#Single level
class Parent:
    parentname=""
    childname=""
    def show_parent(self):
        print(self.parentname)

class Child(Parent):
    def show_child(self):
        print(self.childname)

ch1=Child()
ch1.parentname = "TOKPE"
ch1.childname="Kossi"
ch1.show_parent()
ch1.show_child()
