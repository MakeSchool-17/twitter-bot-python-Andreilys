# hash tables map keys with objects
def hash_function(x, buckets):
    return hash(x) % buckets


class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def get_tail(self):
        return self.tail

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList(object):
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def insert(self, data, freq):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        if current is None:
            return None
        return current

    def __str__(self):
        current = self.head
        return str(current.data)


class HashTable(object):
    def __init__(self, table=None, bucket=None):
        # init with 10 buckets to start
        self.bucket = 10
        self.table = [[] for x in range(self.bucket)]

    def set(self, input, value):
        number_of_inputs = 0
        for bucket in self.table:
            if bucket:
                number_of_inputs += 1
        length = len(self.table)
        # double the buckets if number of inputs is at 50% of length of table
        if(number_of_inputs > length/2):
            self.bucket = self.bucket * 2
        self.table[hash_function(input, self.bucket)].append((input, value))

    def get(self, key):
        # Loop through i's
        for i in self.table:
            if i:
                if i[0][0] == key:
                    return i[0][1]

    def update(self, key, value):
        for bucket in self.table:
            if bucket:
                if bucket[0][0] == key:
                    # replace bucket[0]
                    bucket[0] = (key, value)

    def keys(self):
        keyList = []
        for i in self.table:
            if i:
                keyList.append(i[0][0])
        return keyList

    def values(self):
        keyList = []
        for i in self.table:
            if i:
                keyList.append(i[0][1])
        return keyList

if __name__ == '__main__':
    hashtable = HashTable()
    hashtable.set("Dogs", 5)
    hashtable.set("Turtles", 5)
    hashtable.set("Cats", 9)
    hashtable.update("Turtles", 20)
    print(hashtable.keys())
    print(hashtable.values())
