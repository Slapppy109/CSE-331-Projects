class CircularQueue(object):
    def __init__(self, capacity=2):
        """
        Initialize the queue to be empty with a fixed capacity
        :param capacity: Initial size of the queue
        """
        self.capacity = capacity
        self.size = 0
        self.list = [0] * self.capacity
        self.sum = 0
        self.read = 0
        self.write = 0

    def __eq__(self, other):
        return self.capacity == other.capacity \
               and self.size == other.size \
               and self.read == other.read \
               and self.write == other.write

    # ----------------------- MODIFY BELOW THIS LINE ---------------------------
    def __str__(self):
        """
        Converts contents of queue into a string
        :return: contents (string format of queue)
        """
        if self.size == 0:
            return "Queue is empty"

        content = ""
        read_ptr = self.read
        for i in range(self.size):
            if content:
                content += ' -> '
                content += str(self.list[read_ptr])
            else:
                content = str(self.list[read_ptr])
            read_ptr = (read_ptr + 1) % self.capacity  # increment pointer in queue
        return f"Contents: {content}"

    # DO NOT MODIFY or DELETE this line
    __repr__ = __str__

    def resize(self):
        """
        Grow queue when capacity is reached by 2
        :return: None
        """
        bigger = [None] * (self.capacity * 2)  # create bigger queue
        read_ptr = self.read
        for i in range(self.capacity):  # iterate through old queue to copy into new queue
            bigger[i] = self.list[read_ptr]
            read_ptr = (read_ptr + 1) % self.capacity
        self.capacity *= 2  # setting capacity
        self.list = bigger  # setting new list as queue
        self.read = 0  # normalize queue
        self.write = self.size

    def enqueue(self, number):
        """
        Add and element into the backend of the queue
        :param number:
        :return: None
        """
        if self.size == 0:  # if queue was originally empty
            self.list[self.read] = number
            self.write = (self.write + 1) % self.capacity
        else:
            if self.size == self.capacity:  # resize if queue's capacity has been reached
                self.resize()
            self.list[self.write] = number  # add onto end of queue
            self.write = (self.write + 1) % self.capacity  # set write pointer
        self.sum += number  # add to sum
        self.size += 1  # increment size

    def dequeue(self):
        """
        Remove front element from queue
        :return: None
        """
        if self.size == 0:
            pass
        else:
            read_ptr = self.read
            self.sum -= self.list[read_ptr]  # reduce sum when element is removed
            self.list[read_ptr] = None  # remove element
            self.read = (read_ptr + 1) % self.capacity  # increment read pointer
            self.size -= 1  # reduce size

    def get_average(self):
        """
        Calculate average of elements in queue
        :return: average of queue
        """
        if self.size == 0:
            return 0
        return self.sum / self.size  # average of elements in the queue
