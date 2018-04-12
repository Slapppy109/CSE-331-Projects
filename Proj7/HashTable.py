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
        """
        String output for Hash table
        :return: Hash table in string format
        """
        output = ''
        for i in range(self.tableSize):
            output = output + "[{}]: ".format(i) + str(self.table[i]) + "\n"
        return output

    def insert(self, key, value):
        """
        Inserts elements into hash table
        :param key: key of element to add in hash table
        :param value: value of the element to add in hash table
        :return: None
        """
        index = self.hash_function(key)
        if index == -1:  # condition if string is empty or None
            return
        target = self.table[index].find(key)  # check to see if key exist in Hash table
        if target:
            target.value = value  # update value in Hash table
        else:
            self.table[index].append(key, value)  # push new node onto Linked List in Hash table
            self.numItems += 1  # increment amount of items
        if self.numItems/self.tableSize > 0.75:  # check for loading factor
            self.double()  # double the Hash table size

    def find(self, key):
        """
        Find element in Hash table
        :param key: key of specified element to find
        :return: node element with specified key or False
        """
        target_index = self.hash_function(key)  # find index of key
        return self.table[target_index].find(key)  # return found node in Hash Table

    def lookup(self, key):
        """
        Find element in Hash Table
        :param key: key of specified element to find
        :return: value of node with specified key or False
        """
        target_index = self.hash_function(key)
        temp_target = self.table[target_index]
        target = temp_target.find(key)
        if not target:  # condition to return a bool
            return target
        return target.value  # return value of specified node

    def delete(self, key):
        """
        Remove element in the Hash Table
        :param key: key of specified element to remove
        :return: None
        """
        target_index = self.hash_function(key)
        temp_target = self.table[target_index]
        if temp_target.find(key):  # decrement amount of items if key exist in Hash Table
            self.numItems -= 1
        temp_target.remove(key)  # remove specified node in Hash Table

    def double(self):
        """
        Double the size of the table and rehash
        :return: None
        """
        self.tableSize *= 2  # double the size of the Hash Table
        self.rehash()  # rehash

    def rehash(self):
        """
        Rehash given table
        :return: None
        """
        new_table = [LinkedList() for i in range(self.tableSize)]  #make new table
        for i in range(self.tableSize//2):  # iterate through old table
            temp = self.table[i].head
            while temp is not None:
                n_index = self.hash_function(temp.key)
                new_table[n_index].append(temp.key, temp.value)  # transfer elements into new Hash Table
                temp = temp.next
        self.table = new_table  # set new Hash table as self.table


def FindWords(phrase, k):
    """
    Finds the occurrence of substrings in a phrase
    :param phrase: input string
    :param k: occurrence of substrings
    :return: set of substrings with k occurrences
    """
    Word_Table = HashTable()
    size = 2
    words = set()
    while size != len(phrase):
        for i in range(len(phrase) - size + 1):
            chunk = phrase[i:i+size]  # find chunks of words
            chunk = chunk.lower()
            occur = Word_Table.lookup(chunk)  # find occurrences of chunk in Hash Table
            if occur:  # if chunk existed before
                occur += 1  # increment occurrence
                Word_Table.insert(chunk, occur)  # update Hash table with incremented occurrence
            else:
                Word_Table.insert(chunk, 1)  # if substring has not existed before
        size += 1
    for i in range(Word_Table.tableSize):  # iterate through Hash Table to find substrings of k occurrences
        temp = Word_Table.table[i].head
        while temp is not None:
            if temp.value == k:
                words.add(temp.key)  # add substring to set
            temp = temp.next
    return words  # return set of interested substrings
