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

# NOTE: Handle collisions as well.
# We are using Chaining to handle collisions.
# if len(list)=2, there is a 50% chance that 2 strings will want to use same index. So
# instead of storing a (key,val) pair at each index instead store a list of key,val pairs.
values = [
    [("foo",1), ("rahul",2)],
    [("sachin",3), ("verma",4)]
]

class HashTable(object):
    def __init__(self, **kwargs):
        self.array = [None] * kwargs.get("initial_size")
    
    def hash(self, key):
        """
        Returns the position where a particular key will be hashed.
        """
        return hash(key) % len(self.array)
    
    def add(self, key,val):
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
    
