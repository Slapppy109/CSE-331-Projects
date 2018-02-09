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
        if self._size = 0:
            return True
        return false

    def top(self):
        if self._size != 0:
            return self._data[-1]
        return None

    # ---------------------------Mutator Functions------------------------------

    def push(self, addition):
        self._data.append(addition)

    def pop(self):
        return self._data.pop()

    def grow(self):
        if self._size == self._capacity:
            self._capacity *= 2

    def shrink(self):
        if self._capacity//2 >= self._size:
            if self._capacity >2:
                self._capacity /= 2


'''
Add doc strings here too!
'''
def Palindrome(phrase):
    pass