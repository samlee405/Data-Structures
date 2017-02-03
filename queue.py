#!python
from linkedlist import LinkedList

# class Queue(object):
#
#     def __init__(self, iterable=None):
#         """Initialize this queue and enqueue the given items, if any"""
#         self.queue = []
#         self.queueLength = 0
#         if iterable:
#             for item in iterable:
#                 self.enqueue(item)
#
#     def __repr__(self):
#         """Return a string representation of this queue"""
#         return 'Queue({})'.format(self.length())
#
#     def is_empty(self):
#         """Return True if this queue is empty, or False otherwise"""
#         if len(self.queue) == 0:
#             return True
#         else:
#             return False
#
#     def length(self):
#         """Return the number of items in this queue"""
#         return self.queueLength
#
#     # O(1)
#     def peek(self):
#         """Return the next item in this queue without removing it,
#         or None if this queue is empty"""
#         if self.queueLength != 0:
#             return self.queue[0]
#         else:
#             return None
#
#     # O(1)
#     def enqueue(self, item):
#         """Enqueue the given item into this queue"""
#         self.queue.append(item)
#         self.queueLength += 1
#
#     # O(n)
#     def dequeue(self):
#         """Return the next item and remove it from this queue,
#         or raise ValueError if this queue is empty"""
#
#         if self.queueLength == 0:
#             raise ValueError
#         else:
#             valueToReturn = self.queue[0]
#             del self.queue[0]
#             self.queueLength -= 1
#
#             return valueToReturn


class Queue(LinkedList):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any"""
        super(Queue, self).__init__()
        if iterable:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue"""
        # return 'Queue({})'.format(self)

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise"""
        if self.length == 0:
            return True
        else:
            return False

    # def length(self):
    #     """Return the number of items in this queue"""
    #     return self.length

    def peek(self):
        """Return the next item in this queue without removing it,
        or None if this queue is empty"""
        if self.length != 0:
            return self.head.data
        else:
            return None

    # O(1)
    def enqueue(self, item):
        """Enqueue the given item into this queue"""
        self.append(item)

    # O(1)
    def dequeue(self):
        """Return the next item and remove it from this queue,
        or raise ValueError if this queue is empty"""

        if self.length == 0:
            raise ValueError
        else:
            valueToReturn = self.head.data
            super(Queue, self).delete(valueToReturn)
            self.length -= 1

            return valueToReturn
