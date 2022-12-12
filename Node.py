class Node:
    """
    Class Node
    """

    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None


class Tree:



    def createNode(self, data):
        return Node(data)

    def insert(self, node, data):
        # if tree is empty , return a root node
        if node is None:
            return self.createNode(data)
        if data < node.data:
            node.left = self.insert(node.left, data)
        elif data > node.data:
            node.right = self.insert(node.right, data)

        return node

    def search(self, node, data):
        if node is None or node.data == data:
            return node

        if node.data < data:
            return self.search(node.right, data)
        else:
            return self.search(node.left, data)

    def deleteNode(self, node, data):
        # Check if tree is empty.
        if node is None:
            return None
        if data < node.data:
            node.left = self.deleteNode(node.left, data)
        elif data > node.data:
            node.right = self.deleteNode(node.right, data)
        else:  
            if node.left is None and node.right is None:
                del node
            if node.left == None:
                temp = node.right
                del node
                return temp
            elif node.right == None:
                temp = node.left
                del node
                return temp

        return node



    def traversePreorder(self, root):
        if root is not None:
            print(root.data)
            self.traversePreorder(root.left)
            self.traversePreorder(root.right)

