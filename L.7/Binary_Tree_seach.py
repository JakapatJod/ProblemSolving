class Node:
    
    def __init__(self,data) :
        
        self.left = None
        self.right = None
        self.data = data
    def insert(self,data):
# Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
            
    def findval(self,lkval):
        if lkval < self.data:
            if self.left is None:
                return str(lkval)+" Not Found"
            return self.left.findval(lkval)
        elif lkval > self.data:
            if self.right is None:
                return str(lkval)+" Not Found"
        else:
            print(str(self.data) + " is found ")
        
# Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()

    
    
root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
print(root.findval(7))
print(root.findval(14))
root.PrintTree()