class Node():

    def __init__(self,id,data):
        self.id=id
        self.parent = None
        self.children = []
        self.data = data

    def add_child(self,child):
        self.children.append(child)
        child.parent = self
    
    def is_child(self):
        if self.parent is not None:
            return True
        else:
            return False
    
    def print_tree_up(self):
        if self.parent!=None:
            parent = self.parent
            while parent.parent != None:
                print(parent)
                parent = parent.parent


    def __repr__(self):
        return f"Tree node at id {self.id} with parent: {self.parent.id}... data contained is {self.data}"

    def __str__(self):
        return f"Tree node at id {self.id} with parent: {self.parent.id}... data contained is {self.data}"

root = Node(1,"randomdataforthesakeofhavingsomethingtolookat")
branch = Node(2,[3,4,3,2,4,5,7,8,2,4,5,7,54,34,675,4,345,345,34])
branch1 = Node(3,"unrelated data")
branch2 = Node(4,["a list", "of strings"])
branch3 = Node(5,456)
branch4 = Node(6,"interesting")
branch5 = Node(7,"some stuff")
root.add_child(branch)
branch.add_child(branch1)
branch1.add_child(branch2)
branch2.add_child(branch3)
branch3.add_child(branch4)
branch4.add_child(branch5)
