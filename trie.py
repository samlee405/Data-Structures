class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data"""
        self.data = data
        self.children = {}

    def __repr__(self):
        """Return a string representation of this node"""
        return 'Node({})'.format(repr(self.data))

class Trie(object):
    def __init__(self):
        self.root = Node(None)

    # θ(n)
    def insert(self, item):
        currentNode = self.root

        for character in item:
            if character in currentNode.children:
                print(character + " is in string")
                currentNode = currentNode.children[character]
            else:
                print(character + " is not in string")
                currentNode.children[character] = Node(character)
                currentNode = currentNode.children[character]

    # O(n) Ω(1)
    def prefixSearch(self, item):
        currentNode = self.root

        for character in item:
            if character in currentNode.children:
                currentNode = currentNode.children[character]
            else:
                return False

        return True

if __name__ == "__main__":
    trie = Trie()
    trie.insert("example")
    print("\n")
    trie.insert("extinct")
    print("\n")
    trie.insert("extinguish")
    print(trie.prefixSearch("extin"))
    print(trie.prefixSearch("exam"))
    print(trie.prefixSearch("exit"))
