import trie

def main():
    # get routes and place them into trie
    routes = getRoutes()
    routeTrie = generateTrie(routes)

    # get phone numbers
    phoneNumbers = getPhoneNumbers()

    # get costs for each phone number
    costs = getCosts(phoneNumbers, routeTrie)
    print(costs)

def getRoutes():
    f = open("route-costs-1000000.txt", "r")
    routes = []

    for line in f:
        routes.append(line[:-1])

    return routes

# def getRoutesFromMultipleFiles():

def generateTrie(routes):
    routeTrie = trie.Trie()

    for route in routes:
        routeTrie.insert(route)

    print("Trie generated")
    return routeTrie

def getPhoneNumbers():
    f = open("phone-numbers-3.txt", "r")
    phoneNumbers = []

    for line in f:
        phoneNumbers.append(line[:-1])

    return phoneNumbers

def getCosts(phoneNumbers, routeTrie):
    costs = []

    for number in phoneNumbers:
        price = findPriceForNumber(number, routeTrie)
        costs.append((number, price))

    return costs

def findPriceForNumber(phoneNumber, routeTrie):
    length = len(phoneNumber)

    while length > 0:
        if routeTrie.prefixSearch(phoneNumber[:length]):
            return routeTrie.prefixSearch(phoneNumber[:length])

        length -= 1

    assert ValueError("Number inputted has no matching route")


if __name__ == "__main__":
    main()
