#!python
from linkedlist import LinkedList

class Set(object):

    def __init__(self, init_size=8):
        self.buckets = [LinkedList() for i in range(init_size)]
        self.length = 0

    def __repr__(self):
        """Return a string representation of this hash table"""
        return 'Set({})'.format(self.length)

    def _bucket_index(self, item):
        return hash(item) % len(self.buckets)

    def contains(self, item):
        """Return True if this hash table contains the given key, or False"""
        index = self._bucket_index(item)
        currentNode = self.buckets[index].head

        while currentNode != None:
            if currentNode.data == item:
                return True

            currentNode = currentNode.next

        return False

    def set(self, item):
        """Insert or update the given key with its associated value"""
        index = self._bucket_index(item)
        currentNode = self.buckets[index].head

        while currentNode != None:
            if currentNode.data == item:
                print(str(item) + " is already exists in the set")
                return

            currentNode = currentNode.next


        self.buckets[index].append(item)
        self.length += 1
        self.checkLoadFactor()

    def delete(self, item):
        """Delete the given key from this hash table, or raise KeyError"""
        index = self._bucket_index(item)
        currentNode = self.buckets[index].head

        while currentNode != None:
            if currentNode.data == item:
                self.buckets[index].delete(currentNode.data)
                self.length -= 1
                return

            currentNode = currentNode.next

        raise KeyError("Item does not exist in set")

    def getItems(self):
        """Return a list of all items in this hash table"""
        listOfItems = []

        for index in range(len(self.buckets)):
            currentNode = self.buckets[index].head

            while currentNode != None:
                listOfItems.append(currentNode.data)
                currentNode = currentNode.next

        return listOfItems

    def checkLoadFactor(self):
        # print("load factor " + str(float(self.length) / len(self.buckets)))
        if (float(self.length) / len(self.buckets)) > 0.75:
            self.resize()

    def resize(self):
        print("Resizing set")
        itemsToAdd = self.getItems()
        self.buckets = [LinkedList() for i in range(len(self.buckets) * 2)]
        self.length = 0

        for item in itemsToAdd:
            self.set(item)

if __name__ == '__main__':

    test = Set()
    test.set("A")
    print(test.getItems())
    test.set("B")
    print(test.getItems())
    test.set("C")
    print(test.getItems())
    test.set("D")
    print(test.getItems())
    test.set("E")
    print(test.getItems())
    test.set("F")
    print(test.getItems())
    test.set("G")
    print(test.getItems())
    test.set("H")
    print(test.getItems())
    test.set("I")
    print(test.getItems())
