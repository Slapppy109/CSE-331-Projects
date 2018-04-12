from LinkedList import LinkedList, HashListNode


class HashTable:
    """
    Hash table class, utilizes linked list for resolving collisions with separate chaining
    """
    def __init__(self, tableSize=4):
        """
        DO NOT EDIT
        Initializes hash table
        :param tableSize: size of the hash table
        """
        self.tableSize = tableSize
        self.numItems = 0
        self.table = [LinkedList() for i in range(self.tableSize)]

    def __eq__(self, other):
        """
        DO NOT EDIT
        Equality operator
        :param other: other hash table we are comparing with this one
        :return: bool if equal or not
        """
        if self.tableSize != other.tableSize:
            return False
        for i in range(self.tableSize):
            if self.table[i] != other.table[i]:
                return False
        return True

    def hash_function(self, x):
        """
        DO NOT EDIT
        Converts a string x into a bin number for our hash table
        :param x: key to be hashed
        :return: bin number to insert hash item at in our table, -1 if x is an empty string
        """
        if not x:
            return -1
        hashed_value = 0

        for char in x:
            hashed_value = 181 * hashed_value + ord(char)

        return hashed_value % self.tableSize


    # ------------------------------------------
    # ---------- DO NOT MODIFY ABOVE -----------
    # ------------------------------------------
    # -------------- MODIFY BELOW --------------


    def __repr__(self):
        output = ''
        for i in range(self.tableSize):
            output = output + " -> " + self.table[i]
        return output[4:]

    def insert(self, key, value):
        if self.numItems/self.tableSize > 0.75:
            self.double()
        index = self.hash_function(key)
        new = HashListNode(key, value)
        target = self.table[index].find(key)
        if target:
            target.value = value
        else:
            self.table[index].append(new)
            self.numItems += 1

    def find(self, key):
        target_index = self.hash_function(key)
        temp_target = self.table[target_index]
        return temp_target.find(key)

    def lookup(self, key):
        target_index = self.hash_function(key)
        temp_target = self.table[target_index]
        target = temp_target.find(key)
        if target.value:
            return target.value
        return False

    def delete(self, key):
        target_index = self.hash_function(key)
        temp_target = self.table[target_index]
        temp_target.remove(key)

    def double(self):
        self.tableSize *= 2
        self.rehash()

    def rehash(self):
        new_table = [LinkedList() for i in range(self.tableSize)]
        for i in range(self.tableSize//2):
            temp = self.table[i].head
            while temp is not None:
                n_index = self.hash_function(temp.key)
                new_table[n_index].append(temp)
        self.table = new_table


def FindWords(phrase, k):
    pass
