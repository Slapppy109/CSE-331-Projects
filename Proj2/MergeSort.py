
class LinkedListNode:
    def __init__(self, val = None):
        """
        :param val of node
        :return None

        Constructor for Linked List Node, initialize next to None object
        """
        self.val = val
        self.next = None

    def __le__(self, other):
        '''
        :param other: Linked list node
        :return: boolean value of less than equal to other
        '''
        if isinstance(other, LinkedListNode):
            return self.val <= other.val





class LinkedList:
    def __init__(self):
        """
        :param None
        :return None

        Constructor for Singly Linked List, initialize head to None object
        """
        self.head = None

    def __repr__(self):
        '''
        :param: none
        :return: string representation of linked list
        '''
        result = []
        current = self.head

        while current:
            result.append(str(current.val))
            current = current.next

        return " -> ".join(result)

    __str__ = __repr__


    def push_back(self, data):
        '''
        :param data:  val for new node to be added to Linked list
        :return: None
        '''
        node = LinkedListNode(data)
        if self.head:
            last = self.head
            while last.next:
                last = last.next
            last.next = node

        else:
            self.head = node




'''
ANYTHING BEFORE THIS COMMENT SHOULDN'T BE MODIFIED IN ANYWAY!
'''
# --------- START MODIFYING HERE ---------
def MergeSort(head):
    '''
    :param head: beginning node of the linked list
    :return: None
    '''
    #break condition
    if head.next is None:
        return head

    else:
        #sets initial pointers
        temp_node = head
        second_node = head.next
        #travel linked list with 2 pointers
        while second_node is not None:
            if second_node.next is None:
                #Once second node reaches the end break linked list into 2
                s2_head = temp_node.next
                temp_node.next = None
                break
            if temp_node.next.next is not None:
                temp_node = temp_node.next
            second_node = second_node.next
            if second_node.next is not None:
                second_node = second_node.next

        head = MergeSort(head)
        s2_head = MergeSort(s2_head)
        s = merge(head, s2_head)
        return s
def merge(s1, s2):
    '''
    :param s1: head of s1 linked list 
    :param s2: head of s2 linked list
    :return: s
    '''
    s = None
    s1_temp = s1
    s2_temp = s2
    #create initial value for the sorted linked list
    if s1.val < s2.val:
        s = s1_temp
        s1_temp = s1_temp.next
    else:
        s = s2_temp
        s2_temp = s2_temp.next
    #pointer for s linked list
    s_temp = s
    #Iterate through both linked list and sort it out into linked list s
    while(s1_temp is not None) and (s2_temp is not None):
        #Comparing conditions to determine what element between s1 and s2 goes into s
        if s1_temp.val < s2_temp.val:
            s_temp.next = s1_temp
            s_temp = s_temp.next
            s1_temp = s1_temp.next
        else:
            s_temp.next = s2_temp
            s_temp = s_temp.next
            s2_temp = s2_temp.next
    # Condition if s1 linked list is empty
    if s1_temp is None:
        s_temp.next = s2_temp
    # Condition if s2 linked list is empty
    elif s2_temp is None:
        s_temp.next = s1_temp
    return s