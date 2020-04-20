import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        # Add an item to the the back of the queue
        self.storage.add_to_tail(value)

    def dequeue(self):
        # If the list is not empty, remove the first item in the queue
        if len(self.storage) > 0:
            return self.storage.remove_from_head()
        # If none of the above conditions are met return none
        else:
            return None

    def len(self):
        # Returns the number of items in the queue
        return len(self.storage)

## ------------------------------------------------------------
## ------------------------Regular List-----------------------
## ------------------------------------------------------------

    # def __init__(self):
    #     self.size = 0
    #     # Why is our DLL a good choice to store our elements?
    #     self.storage = []

    # def enqueue(self, value):
    #     # Add an item to the the back of the queue
    #     self.storage.append(value)
    #     # Increases the size of the list by one
    #     self.size += 1

    # def dequeue(self):
    #     # If the list is not empty, delete the first item in the queue
    #     if len(self.storage) > 0:
    #         return self.storage.pop(0)
    #     # If the list is empty, return None
    #     # elif len(self.storage) == 0 :
    #     #     return None
    #     # # If none of the above conditions are met (less than zero), return the list
    #     # else:
    #     #     return self.storage

    # def len(self):
    #     # Returns the number of items in the queue
    #     return len(self.storage)