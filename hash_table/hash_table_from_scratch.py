# hash_table = {}
# hash_table['rahul'] = 1
# how does it happends in background. 
# hash('rahul') = 1245%size (suppose 10) = 1245%10 = 5.
# put rahul to index 5.

# we will use list to implement our hash table.
values = [ ("foo",1), ("rahul",2)]
# NOTE: Instead of accessing the elements using index, how can we make sure, we access it using keys.
# OR, how can we figure out which index to store a value using it's key?

ARR_LEN = 4
values = [None] * ARR_LEN

def get_index(key):
    return hash(key) % ARR_LEN

# 1. NOTE: Handle collisions as well.
# We are using Chaining to handle collisions.
# if len(list)=2, there is a 50% chance that 2 strings will want to use same index. So
# instead of storing a (key,val) pair at each index instead store a list of key,val pairs.
values = [
    [("foo",1), ("rahul",2)],
    [("sachin",3), ("verma",4)]
]

# 2. NOTE: Load Factor.
# 1. if there are n keys, and b is the size of hash table. Then Load Factor = n/b
# 2. Load Factor (0.75 usually) is kept low so that there are less number of entries at one index, and lookup time is almost constant.
# 3. A high load factor means less space overhead but more lookup time and viceversa.

# 3. We will soon get to 100% collisions as all our indexes are populated, and now we will be doing linear
# lookups instead of constant ones. So why dont we just start with 1024 size. We can but it will take lot of memory even for a small smallest hash table.

# SOLUTION: keep the size flexible.
# Expand whenever hash table becomes too populated.
# start with len of 4 and double it to 8,16, 32..  as and when required.

class HashTable(object):
    def __init__(self, **kwargs):
        self.array = [None] * kwargs.get("initial_size")
    
    def hash(self, key):
        """
        Returns the position where a particular key will be hashed.
        """
        return hash(key) % len(self.array)
    
    def is_full(self):
        cnt = 0
        for i in self.array:
            if i:
                cnt+=1
        # return a bool.
        return cnt>len(self.array)/2
    
    def double(self):
        ht2 = HashTable(initial_size = 2*len(self.array))
        # NOTE: you can't just add values.
        # you need to REHASH them.
        for i in self.array:
            if not i:
                # check if not None
                for x in i:
                    ht2.add(x[0],x[1])

        self.array = ht2.array

    def add(self, key,val):
        if self.is_full():
            self.double()
        
        index = self.hash(key)
        if not self.array[index]:
            # index is empty, directly insert.
            self.array[index] = [(key,val)]
        else:
            #NOTE: handle the edge condition. 
            # might be an update or a new addition.
            # you need to check if the key already exists
            for i in self.array[index]:
                if i[0] == key:
                    i[1] = val
                    break
            else:
                # if break is not hit, that means that key doesn't exist already. 
                # simply add it to the end.
                self.array[index].append( (key,val))
    
    def get(self, key):
        index = self.hash(key)
        temp_list = self.array[index]
        # NOTE: Interesting case. If the load factor increases, lookup will be linear instead of 
        # O(1)

        if self.array[index] is None:
            raise KeyError()
        else:
            for i in temp_list:
                if i[0] == key:
                    return i[1]

            # key doesn't exists
            return KeyError()

hash_table = HashTable(initial_size=4)
hash_table.add("rahul",1)
hash_table.add("sachin",2)
hash_table.add("ruby",3)
hash_table.add("python",4)

print("HASH Table ", hash_table.array)
print(hash_table.get("sachin"))
    
