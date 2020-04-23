import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return f'Value: {self.value} | Left: {self.left} | Right: {self.right}'

    # Insert the given value into the tree
    def insert(self, value):
        # If the given value is less than the root value
        if value < self.value:
            # Check if self.left is a valid node
            # print(f'{value} is less than {self.value}')
            if self.left:
                self.left.insert(value)
            # Else if the left side is empty
            else:
                # Assign the empty node to be our value
                self.left = BinarySearchTree(value)
        # Otherwise, if the given value is greater than or equal to the root value
       
        else: 
            # Check if self.right is a valid node
            # print(f'{value} is greater than or equal to {self.value}')
            if self.right:
                self.right.insert(value)
            # Else if the right side is empty
            else:
                # Assign the empty node to be our value
                self.right = BinarySearchTree(value)
                # print(self.right)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # If the target value is equal to the root value, return true
        if target == self.value:
            # print(f'True: {target} is equal to {self.value}')
            return True

        # If the target value is less than the root value
        if target < self.value:
            # And if there are no more left branches to go through, return false
            if self.left == None:
                # print(f'False: {target} not found in left half')
                return False
            # Otherwise, if a node is found
            else:
                # Recursively keep going left
                self.left.contains(target)

        # If the target value is greater than the root value
        else:
            # And if there are no more right branches to go through, return false
            # print(f'{target} is greater than {self.value}')
            if self.right == None:
                # print(f'False: {target} not found in right half')
                return False
            # Otherwise, if a node is found
            else:
                # Recursively keep going right
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # Create a current maximum variable and set it to the root
        curr_max = self.value
        # print(f'curr_max = {curr_max}')
        # If there is a node to the right, set current maximum to that node
        if self.right:
            curr_max == self.right
            return self.right.get_max()
        # Otherwise, if there are no more nodes to the right, return current maximum
        else:
            # print(f'new_curr_max = {curr_max}')
            return curr_max

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # Call the function 'cb' on the value of each node
        cb(self.value)
        # If a node exists to the right, call cb
        if self.right:
            self.right.for_each(cb)
        # If a node exists to the right, call cb
        if self.left:
            self.left.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # (Base case) If the node provided does not exist, simply stop and return
        if node == None:
            return
        
        # Recursively run through the left and right, printing values
        self.in_order_print(node.left) # Recursive left
        print(node.value) # Must be placed between to get order right!
        self.in_order_print(node.right) # Recursive right

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # Make and reference our Queue() class, giving us access to its methods
        q = Queue()
        # Add the root to our queue
        q.enqueue(node)

        # While the queue still has elements
        while q.len() > 0:
            # Remove the oldest item in the queue and assign it to current_node
            current_node = q.dequeue()
            # Print the value of the current node
            print(current_node.value)

            # If there's a value left of the current node, add it to the queue
            if current_node.left:
                q.enqueue(current_node.left)
            # If there's a value right of the current node, add it to the queue
            if current_node.right:
                q.enqueue(current_node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # Make and reference our Stack() class, giving us access to its methods
        stack = Stack()
        # Add the root of the tree to the stack 
        stack.push(node)

        # While the stack still has elements
        while stack.len() > 0:
            # Remove the newest item in the stack and assign it to current_node
            current_node = stack.pop()
            # Print the value of the current node
            print(current_node.value)
            # If there's a value left of the current node, add it to the stack
            if current_node.left:
                stack.push(current_node.left)
            # If there's a value right of the current node, add it to the stack
            if current_node.right:
                stack.push(current_node.right)


    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

bs = BinarySearchTree(10)

# print(bs)

bs.insert(12)
bs.insert(8)
bs.insert(22)

bs.contains(10)

bs.get_max()

# bs.in_order_print()