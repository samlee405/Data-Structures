from set_custom import Set

def union(set1, set2):
    unionItems = set1.getItems() + set2.getItems()

    newSet = Set()
    for item in unionItems:
        newSet.set(item)

    return newSet

def intersection(set1, set2):
    intersectionItems = [x for x in set1.getItems() if x in set2.getItems()]

    newSet = Set()
    for item in intersectionItems:
        newSet.set(item)

    return newSet

def isSubset(set1, set2):
    for item in set1.getItems():
        if not set2.contains(item):
            return False

    return True

def difference(set1, set2):
    newSet = Set()

    for item in set1Items.getItems():
        if not set2.contains(item):
            newSet.set(item)

    return newSet

def setEquality(set1, set2):
    if isSubset(set1, set2) and isSubset(set2, set1):
        return True
    else:
        return False

if __name__ == '__main__':
    # set1 = Set()
    # set1.set("A")
    # set1.set("B")
    # set1.set("C")
    #
    # set2 = Set()
    # set2.set("C")
    # set2.set("D")
    # set2.set("E")

    # print(union(set1, set2).getItems())
    # print(intersection(set1, set2).getItems())

    set1 = Set()
    set1.set("C")

    set2 = Set()
    set2.set("C")
    set2.set("D")
    set2.set("E")

    assert isSubset(set1, set2) is True
    assert isSubset(set2, set1) is False
