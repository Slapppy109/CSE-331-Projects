import string
###################################
# PROJECT 3 - STACK
# Author: Kevin Le
# PID: A51888220
###################################

class Stack:
    # DO NOT MODIFY THIS CLASS #
    def __init__(self, capacity=2):
        """
        Creates an empty Stack with a fixed capacity
        :param capacity: Initial size of the stack.
        """
        self._capacity = capacity
        self._data = [0] * self._capacity
        self._size = 0

    def __str__(self):
        """
        Prints the elements in the stack from bottom of the stack to top,
        followed by the capacity.
        :return: string
        """
        if self._size == 0:
            return "Empty Stack"

        output = []
        for i in range(self._size):
            output.append(str(self._data[i]))
        return "{} Capacity: {}".format(output, str(self._capacity))

    ###### COMPLETE THE FUNCTIONS BELOW ######

    # --------------------Accessor Functions---------------------------------
    def get_size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def top(self):
        if self._size != 0:
            return self._data[self._size - 1]
        return None

    # ---------------------------Mutator Functions------------------------------

    def push(self, addition):
        '''
        Adds elements on top of the stack
        :param addition:
        :return: None
        '''
        self.grow() #Grow the stack if needed
        self._data[self._size] = addition
        self._size += 1

    def pop(self):
        '''
        Removes the top element of the stack
        :return: the top element of the stack
        '''
        popped = self._data[self._size - 1]
        self._data[self._size - 1] = None
        self._size -= 1
        self.shrink() #Shrink the stack if needed
        return popped

    def grow(self):
        '''
        :return: None
        '''
        if (self._size + 1) >= self._capacity: #check if growth needed
            self._capacity *= 2 #change size of capacity
            new = [None] * self._capacity
            ind = 0
            for elm in self._data: #copy data over to new stack
                new[ind] = elm
                ind += 1
            self._data = new



    def shrink(self):
        '''
        :return: None
        '''
        if ((self._size) <= self._capacity//2) and (self._size > 2): #check if growth needed
            self._capacity = self._capacity // 2 #change size of capacity
            new = [None] * self._capacity
            ind = 0
            for elm in self._data: #copy data over to new stack
                if ind < self._size:
                    new[ind] = elm
                    ind += 1
            self._data = new

def Palindrome(phrase):
    if (len(phrase) == 1) or (len(phrase) == 0): #empty or length 1 strings return true for palindromes
        return True
    check = Stack()

    # Section of code to strip string of all spaces and punctuation
    n_phrase1 = phrase.replace(" ", "")
    n_phrase2 = ""
    for char in n_phrase1:
        if char.isalnum():
            n_phrase2 += char
    n_phrase3 = n_phrase2

    # Removing middle char in an odd palindrome
    if len(n_phrase2) % 2 == 1:
        mid = len(n_phrase2)//2
        n_phrase3 = n_phrase2[:mid] + n_phrase2[mid + 1:]
    n_phrase = n_phrase3.lower()

    for char in n_phrase: #checking if one half of the string is the same as the other
        if char == check.top():
            check.pop()
        else:
            check.push(char)
    return check.is_empty() #if stack is empty, then string is a palindrome
