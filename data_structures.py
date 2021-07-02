"""
Name: Thy Nguyen
Project: Customized Posters Ordering System
"""


class HashMap:
    """
    For user management
    """

    def __init__(self, size):
        """ Initialize hash map """
        self.hash_map = [[] for i in range(size)]

    def size(self):
        """ How many cells inside hash table"""
        return len(self.hash_map)

    def put(self, key, value):
        """ Add new key-value pair, or update value of the old key
        Key is item unique id, Value is item (e.g. User) instance """
        hash_id = hash(key) % self.size()
        bucket = self.hash_map[hash_id]
        if (key, value) in bucket:
            for i in range(len(bucket)):
                if bucket[i][0] == key:
                    bucket[i] = (key, value)  # update
                    break
        else:
            bucket.append((key, value))  # add new key-value

    def get_value(self, key):
        """ Get item (e.g. User) instance whose id is the given key """
        hash_id = hash(key) % self.size()
        bucket = self.hash_map[hash_id]
        key_lst = [k[0] for k in bucket]
        if key in key_lst:
            for i in range(len(bucket)):
                if bucket[i][0] == key:
                    return bucket[i][1]
        else:
            return None

    def delete_value(self, key):
        """ Delete item (e.g. User) """
        hash_id = hash(key) % self.size()
        bucket = self.hash_map[hash_id]
        key_lst = [k[0] for k in bucket]
        if key in key_lst:
            for i in range(len(bucket)):
                if bucket[i][0] == key:
                    bucket.pop(i)
                    break


class Operations:
    """
    Common Operations between Stack and Queue
    """

    def __init__(self):
        """ Constructor """
        self.items = []
        self.counts = 0
        self.removed = 0

    def size(self):
        """ Get the number of items inside a collection """
        return self.counts

    def empty(self):
        """ Check if the collection is empty or not """
        return self.size() == 0

    def clear(self):
        """ Clear collection """
        self.items = []
        self.counts = 0
        self.removed = 0


class Stack(Operations):
    """
    Stack class
    """

    def push(self, item):
        """ Push item """
        if item is not None:
            self.items += [item]
            self.counts += 1

    def multi_push(self, new_items):
        """ Push multiple items """
        for item in range(len(new_items)):
            self.push(item)

    def pop(self):
        """ Pop top item """
        if not self.empty():
            self.counts -= 1
            self.removed += 1
            return self.items.pop()
        return None

    def multi_pop(self, nums):
        """ Pop multiple items """
        for i in range(nums):
            self.pop()

    def peek(self):
        """ Peek top item """
        if not self.empty():
            return self.items[-1]
        return None

    def __str__(self):
        """ String representation of stack """
        items = ''
        for i in self.items[::-1]:
            items += str(i) + '\n'
        return "top " + items + "bottom"

    def __repr__(self):
        """ Repr representation """
        return str(self.counts) + ' item(s) pushed; ' \
               + str(self.removed) + ' item(s) popped'


class Queue(Operations):
    """
    Queue class.
    """

    def enqueue(self, item):
        """ Add item """
        if item is not None:
            self.items += [item]
            self.counts += 1

    def multi_enqueue(self, new_items):
        """ Enqueue multiple items """
        for item in range(len(new_items)):
            self.enqueue(item)

    def dequeue(self):
        """ Dequeue front item """
        if not self.empty():
            self.counts -= 1
            self.removed += 1
            return self.items.pop(0)
        return None

    def multi_pop(self, nums):
        """ Dequeue multiple items """
        for i in range(nums):
            self.dequeue()

    def peek(self):
        """ Peek front item """
        if not self.empty():
            return self.items[0]
        return None

    def __str__(self):
        """ String representation of queue """
        items = ''
        for i in self.items:
            items += str(i) + ' '
        return "(front) " + items + "back"

    def __repr__(self):
        """ Repr representation """
        return str(self.counts) + ' item(s) enqueued; ' \
               + str(self.removed) + ' item(s) dequeued'
