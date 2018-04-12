class HashListNode:
    def __init__(self, key, val = None):
        """
        DO NOT EDIT
        :param val of node
        :return None

        Constructor for Linked List Node, initialize next to None object
        """
        self.value = val
        self.key = key
        self.next = None

    def __str__(self):
        '''
        DO NOT EDIT
        String representation of a linked list node

        :return: String representation
        '''
        return str(self.key) + ":" + str(self.value)

    def __eq__(self, other):
        '''
        DO NOT EDIT
        Equality operator
        :return: True if equal, false if not
        '''

        if self and other:
            return self.value == other.value and self.next == other.next \
                   and self.key == other.key
        elif not self and not other:
            return True

        return False

class LinkedList:
    def __init__(self):
        """
        DO NOT EDIT
        :param None
        :return None

        Constructor for Singly Linked List, initialize head to None object
        """
        self.head = None
        self.tail = None

    def __eq__(self, other):
        """
        DO NOT EDIT
        Defines "==" (equality) for two linked lists
        :param other: Linked list to compare to
        :return: True if equal, False otherwise
        """

        if self.head != other.head or self.tail != other.tail:
            return False

        # Traverse through linked list and make sure all nodes are equal
        temp_self = self.head
        temp_other = other.head
        while temp_self is not None:
            if temp_self == temp_other:
                temp_self = temp_self.next
                temp_other = temp_other.next
            else:
                return False
        # Make sure other is not longer than self
        if temp_self is None and temp_other is None:
            return True


    # -------------------------------
    # ----- DO NOT MODIFY ABOVE -----
    # ----- MODIFY BELOW ------------
    # -------------------------------


    def __repr__(self):
        """
        String representation of Linked List
        :return: string of Linked List
        """
        output = ''
        temp_self = self.head
        while temp_self is not None:
            output = output + " -> " + str(temp_self)
            temp_self = temp_self.next
        return output[4:]


    __str__ = __repr__


    def append(self, key, value):
        """
        Push node to the end of the Linked List
        :param key: Key of element
        :param value: Value of element
        :return: None
        """
        new = HashListNode(key, value)
        if self.head is None:
            self.head = self.tail = new  # Make new node the head if Linked List empty
        else:
            self.tail.next = new  # add new node as tail of Linked List
            self.tail = new

    def remove(self, key):
        """
        Removes node in the Linked List
        :param key: Specified Key to be removed
        :return: None
        """
        if self.head is None:  # return if Linked List is empty
            return
        prev = self.head
        target = self.head.next  # create prev pointer and target poitner
        if prev.key == key:  # condition if head is wanted
            self.head = target
            return
        while target is not None:  # iterate through Linked List to remove node
            if target.key == key:
                prev.next = target.next
            prev = prev.next
            target = target.next

    def find(self, key):
        """
        Find node with a specified key in the Linked list
        :param key: Specified Key to be found
        :return: Found node or False
        """
        temp_self = self.head
        while temp_self is not None:
            if temp_self.key == key:  # found target node
                return temp_self
            temp_self = temp_self.next
        return False  # return if target node does not exist
