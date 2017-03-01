class Node(object):

    def __init__(self):
        """Initialize this node with the given data"""
        # self.data = data
        self.children = {} # key:value as character:Node(character)

class Trie(object):
    def __init__(self):
        # Initialize empty node that will hold all first characters
        self.root = Node()

    # Theta(n)
    def insert(self, item):
        route = item[:-5]
        cost = item[-4:]
        currentNode = self.root

        for character in route:
            if character in currentNode.children:
                currentNode = currentNode.children[character]
            else:
                currentNode.children[character] = Node()
                currentNode = currentNode.children[character]

        currentNode.children["$"] = cost

    # O(n) Omega(1)
    def prefixSearch(self, item):
        # item = item + "$"
        currentNode = self.root

        for character in item:
            if character in currentNode.children:
                currentNode = currentNode.children[character]
            else:
                return None

        if "$" in currentNode.children:
            return currentNode.children["$"]
        else:
            return None

if __name__ == "__main__":
    trie = Trie()
    trie.insert("+86153,0.84")
    print(trie.prefixSearch("+86153"))

    # str1 = "example!!!!"
    # print(str1[:-4])
    # print(str1[-4:])
