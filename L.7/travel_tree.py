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

# Inorder travelsal
# Left -> Right -> Root
    def inorderTravelsal(self,root):
        res = []
        if root :
            res = self.inorderTravelsal(root.left)
            res.append(root.data)
            res = res + self.inorderTravelsal(root.right)
        return res

# Preorder traversal
# Root -> Left -> Right 
    def PreorderTraversal(self,root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.PreorderTraversal(root.left)
            res = res + self.PreorderTraversal(root.right)
        return res
    
# Postorder travelsal
# left -> Right -> Root
    def PostorderTravelsal(self,root):
        res = []
        if root:
            res = self.PostorderTravelsal(root.left)
            res = res + self.PostorderTravelsal(root.right)
            res.append(root.data)
        return res

    def inorderTravelsal(self,root):
        res = []
        if root :
            res = self.inorderTravelsal(root.right)
            res.append(root.data)
            res = res + self.inorderTravelsal(root.left)
        return res

root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)

print(root.findval(7))
print(root.findval(14))
print(root.inorderTravelsal(root))
print(root.PreorderTraversal(root))
print(root.PostorderTravelsal(root))
root.PrintTree()