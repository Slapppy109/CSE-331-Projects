class Node:
    """Lightweight, nonpublic class for storing a singly linked node.
    should only be called within the LinkedQueue class definition """

    __slots__ = 'val', 'next'         # streamline memory usage

    def __init__(self, val, next):
        self.val = val
        self.next = next

    def __lt__(self, other):
        ''' assumes other is of same type, invoked with "<" '''
        return self.val <= other.val

    def __le__(self, other):
        ''' assumes other is of same type, invoked with "<=" '''
        return self.val <= other.val



class LinkedQueue:
    """FIFO queue implementation using a singly linked list for storage."""

    def __init__(self):
        """Create an empty queue."""
        self.head = None
        self.tail = None
        self.size = 0


    def __str__(self):
        ''' string implementation of current elements in queue '''
        head = self.head
        values = list()
        while head:
            values.append(str(head.val))
            head = head.next

        return ", ".join(values)

    __repr__ = __str__


################## start modifying below this line ######################
    def __len__(self):
        '''
        :return: size of queue
        '''
        return self.size

    def is_empty(self):
        '''
        :return: boolean of queue based on if empty
        '''
        if self.size == 0:
            return True
        return False

    def dequeue(self):
        '''
        :return: node that is "removed" from the queue
        '''
        return_node = self.head
        self.head = return_node.next  # move head pointer to next
        self.size -= 1  # decrement size
        return return_node.val


    def enqueue(self, element):
        '''
        :param element: desired data
        :return: None
        '''
        new_node = Node(element, None)  # create new node based off of element
        if self.size == 0:  # if queue is empty
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node  # add new node to the end of the queue
            self.tail = self.tail.next
        self.size += 1  # increment size


    def get_middle(self):
        '''
        :return: middle node
        '''
        mid = self.size // 2  #mid point
        temp_node = self.head
        for i in range(mid):  # iterate to find mid node
            temp_node = temp_node.next
        return temp_node.val  # return mid node
