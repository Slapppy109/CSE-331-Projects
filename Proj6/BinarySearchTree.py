########################################
# PROJECT 6 - BinarySearchTree
# Author: Kevin Le
# PID:A51888220
########################################


class Node:
    # DO NOT MODIFY THIS CLASS #
    __slots__ = 'value', 'parent', 'left', 'right'

    def __init__(self, value, parent=None, left=None, right=None):
        """
        Initialization of a node
        :param value: value stored at the node
        :param parent: the parent node
        :param left: the left child node
        :param right: the right child node
        """
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

    def __eq__(self, other):
        """
        Describes equality comparison for nodes ('==')
        :param other: node being compare to
        :return: True if equal, False if not equal
        """
        return type(other) is type(self) and self.value == other.value

    def __repr__(self):
        """
        Defines string representation of a node (str())
        :return: string representing node
        """
        return str(self.value)


class BinarySearchTree:

    def __init__(self):
        # DO NOT MODIFY THIS FUNCTION #
        """
        Initializes an empty Binary Search Tree
        :return nothing
        """
        self.root = None
        self.size = 0

    def __eq__(self, other):
        # DO NOT MODIFY THIS FUNCTION #
        """
        Describe equality comparison for BSTs ('==')
        :param other: BST being compared to
        :return: True if equal, False if not equal
        """
        if self.size != other.size:
            return False
        if self.root != other.root:
            return False
        if self.root is None or other.root is None:
            return True  # Both must be None

        if self.root.left is not None and other.root.left is not None:
            r1 = self._compare(self.root.left, other.root.left)
        else:
            r1 = (self.root.left == other.root.left)
        if self.root.right is not None and other.root.right is not None:
            r2 = self._compare(self.root.right, other.root.right)
        else:
            r2 = (self.root.right == other.root.right)

        result = r1 and r2
        return result

    def _compare(self, t1, t2):
        # DO NOT MODIFY THIS FUNCTION #
        """
        Recursively compares two trees, used in __eq__.
        :param t1: root node of first tree
        :param t2: root node of second tree
        :return: True if equal, False if nott
        """
        if t1 is None or t2 is None:
            return t1 == t2
        if t1 != t2:
            return False
        result = self._compare(t1.left, t2.left) and self._compare(t1.right, t2.right)
        return result


    ### Implement/Modify the functions below ###

    def insert(self, value):
        '''
        Inserts a non-existent value into the Binary Tree
        :param value: value to insert
        :return: None
        '''
        new_node = Node(value)
        cur = self.root
        if self.root is None:
            self.root = Node(value)
            self.size += 1
        while cur is not None:  # condition walk the tree
            if value > cur.value:
                if cur.right is None:  # if right child is empty, populate the space with the new node
                    new_node.parent = cur
                    cur.right = new_node
                    self.size += 1
                    break
                cur = cur.right  # move to the right child
            elif value < cur.value:
                if cur.left is None:  # if left child is empty, populate the space with the new node
                    new_node.parent = cur
                    cur.left = new_node
                    self.size += 1
                    break
                cur = cur.left  # move to the left child
            else:  # if neither less than or greater than current value, then it is equal
                break

    def remove(self, value):
        '''
        Remove existing value from the binary search tree
        :param value: value to remove
        :return: None
        '''
        cur = self.root
        while cur is not None:
            if value > cur.value:
                cur = cur.right  # move to the right child
            elif value < cur.value:
                cur = cur.left  # move to the left child
            elif value == cur.value:  # found value
                parent = cur.parent
                if cur.left is None and cur.right is None:  # remove leaf node
                    if parent.right == cur:
                        parent.right = None
                    else:
                        parent.left = None
                    cur.parent = None
                    self.size -= 1
                elif cur.left is not None and cur.right is not None:  # remove node with 2 children
                    replacement = self.min(cur.right)  # find replacement value
                    self.remove(replacement)  # remove the replacement value from the tree
                    cur.value = replacement  # set cur value as the replacement value
                else:  # remove node with 1 child and promote
                    target_branch = cur.left  # initialize target_branch to promote
                    if target_branch is None:  # set target_branch to the right branch if target is empty
                        target_branch = cur.right
                    if parent.right == cur:  # if right child
                        parent.right = target_branch  # promote
                        target_branch.parent = parent
                    elif parent.left == cur:  # if left child
                        parent.left = target_branch  # promote
                        target_branch.parent = parent
                    cur.parent = None  # remove cur link to parent
                    self.size -= 1
                break

    def search(self, value, node):
        '''
        Search for value in node
        :param value: value to find
        :param node: starting node
        :return: node where value is found or parent of the value if in the tree
        '''
        if node is None:  # base case
            return None
        if value > node.value and node.right is not None:
            node = self.search(value, node.right)  # move right and set node of interest (node cascades down call stack)
        elif value < node.value and node.left is not None:
            node = self.search(value, node.left)  # move left and set node of interest (node cascades down call stack)
        return node  # return node of interest

    def inorder(self, node, inorder_list=list()):
        '''
        Traverse inorder
        :param node: starting node
        :param inorder_list: list holding values while traveling thru tree
        :return: list of elements inorder
        '''
        if node is None:  # base case to break recursion
            return
        self.inorder(node.left, inorder_list)  # travel left
        inorder_list.append(node.value)  # append element
        self.inorder(node.right, inorder_list)  # travel right
        return inorder_list

    def preorder(self, node, preorder_list=list()):
        '''
        Traverse preoder
        :param node: starting node
        :param preorder_list: list holding values while traveling thru tree
        :return: list of elements preorder
        '''
        if node is None:  # base case to break recursion
            return
        preorder_list.append(node.value)  # append element
        self.preorder(node.left, preorder_list)  # travel left
        self.preorder(node.right, preorder_list)  # travel right
        return preorder_list

    def postorder(self, node, postorder_list=list()):
        '''
        Traverse postorder
        :param node: starting node
        :param postorder_list: list holding values while traveling thru tree
        :return: list of elements postorder
        '''
        if node is None:  # base case to break recursion
            return
        self.postorder(node.left, postorder_list)  # travel left
        self.postorder(node.right, postorder_list)  # travel right
        postorder_list.append(node.value)  # append element
        return postorder_list

    def depth(self, value):
        '''
        Find depth of a value in tree
        :param value: target value to find depth
        :return: depth of value
        '''
        depth = 0  # initialize depth
        cur = self.root  # initialize cur pointer
        while cur is not None:  # travel tree
            if value < cur.value:
                cur = cur.left  # travel left
            elif value > cur.value:
                cur = cur.right  # travel right
            elif value == cur.value:
                return depth  # return depth
            depth += 1  # increment at each node
        return -1

    def height(self, node):
        '''
        Height of the tree
        :param node: starting node
        :return: height of the tree
        '''
        if node is None:  # condition set for node with only 1 child and causes a recursion on a none node
            return 0
        elif node.left is None and node.right is None:  # condition for leaf node
            return 0
        else:
            return 1 + max(self.height(node.left), self.height(node.right))  # return the height of biggest branch

    def min(self, node):
        '''
        Find min value of tree
        :param node: starting node
        :return: minimum value
        '''
        if node is None:
            return None
        target = self.min(node.left)  # recursive call to walk left and set min val (target cascades down call stack)
        if node.left is None:  # if no left node exist, you have the min
            return node.value
        return target

    def max(self, node):
        '''
        Find max value of tree
        :param node:  starting node
        :return: maximum value
        '''
        if node is None:
            return None
        target = self.max(node.right)  # recursive call to walk right and set max val (target cascades down call stack)
        if node.right is None:  # if no left node exist, you have the min
            return node.value
        return target

    def get_size(self):
        '''
        Amount of nodes
        :return: number of nodes
        '''
        return self.size