#!python
from linkedlist import LinkedList

# class Stack(object): # dynamic array
#
#     def __init__(self, iterable=None):
#         """Initialize this stack and push the given items, if any"""
#         self.length = 0
#         self.stack = []
#         if iterable:
#             for item in iterable:
#                 self.push(item)
#
#     def __repr__(self):
#         """Return a string representation of this stack"""
#         return 'Stack({})'.format(self.stack)
#
#     def is_empty(self):
#         """Return True if this stack is empty, or False otherwise"""
#         if self.length == 0:
#             return True
#         else:
#             return False
#
#     def peek(self):
#         """Return the top item on this stack without removing it,
#         or None if this stack is empty"""
#         if self.length != 0:
#             return self.stack[self.length - 1]
#         else:
#             return None
#
#     def push(self, item):
#         """Push the given item onto this stack"""
#         self.stack.append(item)
#         self.length += 1
#
#     def pop(self):
#         """Return the top item and remove it from this stack,
#         or raise ValueError if this stack is empty"""
#         if self.length == 0:
#             raise ValueError
#         else:
#             valueToReturn = self.stack[self.length - 1]
#             del self.stack[self.length - 1]
#             self.length -= 1
#             return valueToReturn

class Stack(object): # linked list

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any"""
        self.stack = LinkedList()
        if iterable:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack"""
        return 'Stack({})'.format(self.stack)

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise"""
        if self.stack.length == 0:
            return True
        else:
            return False

    def length(self):
        """Return the number of items in this stack"""
        # print(self.stack.length)
        return self.stack.length

    def peek(self):
        """Return the top item on this stack without removing it,
        or None if this stack is empty"""
        if self.stack.length != 0:
            return self.stack.tail.data
        else:
            return None

    def push(self, item):
        """Push the given item onto this stack"""
        self.stack.append(item)

    def pop(self): # implement a doubly linked list to have constant speed
        """Return the top item and remove it from this stack,
        or raise ValueError if this stack is empty"""
        if self.stack.length == 0:
            raise ValueError
        else:
            valueToReturn = self.stack.tail.data

            current = self.stack.head
            previous = None
            while current.next != None:
                previous = current
                current = current.next

            if current is self.stack.head:
                self.stack.head = None
            if current is self.stack.tail:
                if previous is not None:
                    previous.next = None
                self.stack.tail = previous

            self.stack.length -= 1

            return valueToReturn
