from set_custom import Set

# {"A", "B", "C"} U {"C", "D", "E"} = {"A", "B", "C", "D", "E"}
def union(set1, set2):
    # set1items = set1.getItems()
    # set2items = set2.getItems()
    # set1items = set1items + set2items
    # set1items += set2items
    # set1items.extend(set2items)
    # a = a + 1
    # a += 1
    #
    # newSet = Set()
    # for item in iter(set1):
    #     newSet.set(item)
    # for item in iter(set2):
    #     newSet.set(item)
    unionItems = set1.getItems() + set2.getItems()

    newSet = Set()
    for item in unionItems:
        newSet.set(item)

    return newSet

# {"A", "B", "C"} ∩ {"C", "D", "E"} = {"C"}
def intersection(set1, set2):
    intersectionItems = [x for x in set1.getItems() if set2.contains(x)]

    newSet = Set()
    for item in intersectionItems:
        newSet.set(item)

    return newSet

# {"A", "B"} c {"A", "B", "C"}
def isSubset(set1, set2):
    for item in set1.getItems():
        if not set2.contains(item):
            return False

    return True

# {"A", "B", "C"} - {"A", "B"} = {"C"}
def difference(set1, set2):
    newSet = Set()

    for item in set1.getItems():
        if not set2.contains(item):
            newSet.set(item)

    return newSet

def setEquality(set1, set2):
    if len(set1) != len(set2):
        return False

    return isSubset(set1, set2) and isSubset(set2, set1)

if __name__ == '__main__':
    set1 = Set()
    set1.set("A")
    set1.set("B")
    set1.set("C")

    set2 = Set()
    set2.set("C")
    set2.set("D")
    set2.set("E")

    # print(union(set1, set2).getItems())
    # print(intersection(set1, set2).getItems())
    print(difference(set1, set2).getItems())

    # set1 = Set()
    # set1.set("C")
    #
    # set2 = Set()
    # set2.set("C")
    # set2.set("D")
    # set2.set("E")
    #
    # assert isSubset(set1, set2) is True
    # assert isSubset(set2, set1) is False
