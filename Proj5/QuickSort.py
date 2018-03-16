from Queue import LinkedQueue, Node


def insertion_sort(queue):
    '''
    :param queue: desired queue to be sorted
    :return: None
    '''
    if len(queue) == 0:
        return
    sorted = queue.head  # initial sorted linked list
    next_elm = queue.head.next
    sorted.next = None
    while next_elm != None:
        target = next_elm
        next_elm = next_elm.next
        if target.val < sorted.val:  # place node at front if smallest value
            target.next = sorted
            sorted = target
        else:
            scan = sorted
            while (scan.next != None) and (target.val > scan.next.val):  # find appropriate index for value
                scan = scan.next
            target.next = scan.next  # place node at the index
            scan.next = target
    queue.head = sorted  # set sorted to be the queue


def pick_pivot(queue, left, right):
    '''
    :param queue: desired queue
    :param left: left most value
    :param right: right most value
    :return: median value of left, right and mid
    '''
    cap = len(queue)
    if cap == 0:
        return None
    mid = queue.get_middle()  # get mid of queue
    if left < mid:  # comparisons
        if left >= right:
            return left
        elif mid < right:
            return mid
    else:
        if left < right:
            return right
        elif mid >= right:
            return mid
    return right


def quick_sort(queue):
    '''
    :param queue: desired queue to be sorted
    :return: None
    '''
    if len(queue) <= 10:
        insertion_sort(queue)
        return
    pivot = pick_pivot(queue, queue.head.val, queue.tail.val)  # pick pivot
    lesser = LinkedQueue()  # initialize lesser, greater, and equal queues
    greater = LinkedQueue()
    equal = LinkedQueue()
    while not queue.is_empty():  # divide Queue up based on pivot
        if queue.head.val > pivot:
            greater.enqueue(queue.dequeue())
        elif queue.head.val < pivot:
            lesser.enqueue(queue.dequeue())
        else:
            equal.enqueue(queue.dequeue())
    quick_sort(greater)  # partition greater queue
    quick_sort(lesser)  # partition lesser queue
    while not lesser.is_empty():  # concatenate the partitioned queues
        queue.enqueue(lesser.dequeue())
    while not equal.is_empty():
        queue.enqueue(equal.dequeue())
    while not greater.is_empty():
        queue.enqueue(greater.dequeue())