class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data"""
        self.data = data
        self.right = None
        self.left = None

    def __repr__(self):
        """Return a string representation of this node"""
        return 'Node({})'.format(repr(self.data))

class BinaryTree(object):
    def __init__(self, iterable=None):
        self.root = None
        if iterable:
            for item in iterable:
                self.insert(item)

    def insert(self, item, node=None):
        newNode = Node(item)

        if self.root == None:
            self.root = newNode
            return

        if node == None:
            node = self.root

        if (item < self.root.data):
            if (node.left != None):
                self.insert(item, node.left)
            else:
                node.left = newNode
        else:
            if (node.right != None):
                self.insert(item, node.right)
            else:
                node.right = newNode

    def search(self, item):
        currentNode = self.root

        while currentNode != None:
            if currentNode.data == item:
                return True
            elif item < currentNode.data:
                currentNode = currentNode.left
            elif item > currentNode.data:
                currentNode = currentNode.right

        return False

    # in order traversal
    def traversal(self, node=None, returnList=[]):
        # if binary search tree is empty return empty list
        if self.root == None:
            return returnList

        # initialize node as root node for first traversal() call
        if node == None:
            node = self.root

        # traverse downwards towards the left
        if node.left != None:
            self.traversal(node.left)

        # print/append current data @ node
        # print(node.data)
        returnList.append(node.data)

        # traverse downwards towards the right
        if node.right != None:
            self.traversal(node.right)

        return returnList

if __name__ == "__main__":
    bst = BinaryTree()
    bst.insert(20)
    # print(bst.root.data)
    bst.insert(15)
    # print(bst.root.left.data)
    bst.insert(10)
    # print(bst.root.left.left.data)
    bst.insert(21)
    # print(bst.root.right.data)
    print(bst.traversal())
