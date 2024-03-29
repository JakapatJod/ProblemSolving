class Node:
    
    def __init__(self,data) :
        
        self.left = None
        self.right = None
        self.data = data

    def insert(self,data):
# Compare the new data with the parent node
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


root = Node(100)
root.insert(50)
root.insert(150)
root.insert(30)
root.insert(60)
root.insert(120)

rt = root.delete(root, 100)
print("The data of the root is ", rt.data)



#print(root.inorderTravelsal(root))
print(root.PreorderTraversal(root))
#print(root.PostorderTravelsal(root))
root.PrintTree()