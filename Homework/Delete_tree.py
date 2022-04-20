class Node:

    global arr
    arr = []
    
    def __init__(self, data, bypass = False) :
        self.left = None
        self.right = None
        self.data = data
        if (not bypass) :
            arr.append(self.data)

    def insert(self,data, bypass = False):
# Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data, bypass)
                else:
                    self.left.insert(data, bypass)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data, bypass)
                else:
                    self.right.insert(data, bypass)
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

    def delete(self , key) :

        print(f"Before Delete {key} in ", arr)
        for index in range(len(arr)) : 
            if arr[index] == key : 
                arr.pop(index)
                break
        print(f"After Delete {key} in ", arr)

        self.left = None
        self.right = None
        self.data = None

        for i in range(len(arr)): 
            self.insert(arr[i], True)


root = Node(100)
root.insert(50)
root.insert(150)
root.insert(20)
root.insert(60)
root.insert(120)

root.delete(60)
root.delete(50)
root.delete(100)

# print(root.inorderTravelsal(root))
# print(root.PreorderTraversal(root))
# print(root.PostorderTravelsal(root))


root.PrintTree()