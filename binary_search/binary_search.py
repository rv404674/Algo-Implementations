class BinarySearch:

    def __init__(self, arr, target):
        self.arr = arr
        self.target = target

    def binary_search(self):
        lo, hi = 0, len(self.arr)

        while lo<hi:
            mid = lo + (hi-lo)//2
            # dont use (lo+hi)//2. Integer overflow.
            # https://en.wikipedia.org/wiki/Binary_search_algorithm#Implementation_issues
            if self.arr[mid] == self.target:
                return mid

            if self.arr[mid] > self.target:
                hi = mid-1
            else:
                lo = mid+1

        return -1


# input in python3 returns a string
n = int(input('Enter the size of array'))

# example of using map
# a = ['1', '2'] conver it into int
# a = list(map(int, a)) in python2 this will work a=map(int,a)

# in python3 map returns a map object which is a generator where as in py2 map returns a list
# n is used so that even if we enter n+1 numbers list will only contain n number
arr = list(map(int, input("Enter the number").strip().split()))[:n]

target = int(input("Enter the number to be searched"))


print(BinarySearch(arr, target).binary_search())

