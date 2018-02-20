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


        if self.size == 0:
            return "Queue is empty"

        content = ""
        for ind in range(self.read, self.write)
            content = content + str(self.list[ind])




        return f"Contents: {content}"


    # DO NOT MODIFY or DELETE this line
    __repr__ = __str__

    def enqueue(self, number):
        if self.size == self.capacity:
			self.resize()
		self.list[(self.write + 1)% self.capacity]
		self.write = (self.write + 1)% self.capacity
		self.sum += number
		self.size += 1

    def dequeue(self):
        if self.size == 0:
			pass
		else:
			self.sum -= self.list[self.read]
			self.list[self.read] = None
			self.read = (self.read + 1)% self.capacity
			self.size -= 1
			
    def resize(self):
        bigger = [None] * (self.capacity * 2)
		b_ind = 0
		for ind in range(self.read,self.write):
			bigger[b_ind] = self.list[ind]
			b_ind += 1
		self.read = 0
		self.write = b_ind
		self.list = bigger

    def get_average(self):
        return self.sum/self.size
