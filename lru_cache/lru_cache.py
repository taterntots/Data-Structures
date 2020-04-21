import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit # Limit Keeps track of the maximum number of nodes available to hold
        self.size = 0 # Size keeps track of the number of nodes
        self.storage = DoublyLinkedList() # DLL to store order
        self.hash_storage = {} # Dictionary to store key:value pairs

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        # If the key is not in our hash table, do nothing (nothing to retrieve)
        if key not in self.hash_storage:
            return None
        # If the key is in our hash table, return that keys value and moves it to the front (head)
        else:
            self.storage.move_to_front(self.hash_storage[key])
            return self.hash_storage[key].value

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        # If the key-value pair is already in our cache
        if key in self.hash_storage:
            # Replace the old key's value with the new one
            self.hash_storage[key].value = value
        # Else if the cache is at maximum capacity
        elif self.limit > 10:
            # Remove the oldest entry to make room (tail)
            self.storage.remove_from_tail()
            # Add the new entry to the front (head)
            self.storage.add_to_head(key)
        # Else add the key-value pair to the cache to the front (head)
        else:
            self.storage.add_to_head(key)

list = {
    'derp': 4, 
    'flerp': 3
    }

LRUCache(3)

print(DoublyLinkedList(list))