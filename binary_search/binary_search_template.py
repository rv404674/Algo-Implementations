# this template can be used to solve all binary search problems.
# NOTE: we can apply binary search on any search space not just an array
# minimize K such that condition(k) is True.

# FIXME: dont use this for simple binary search, as it doesnt have == condition.

def binary_search(arr):
    def condition(value):
        # returns bool
        pass

    left,right = min(search_space), max(seach_space)
    while left<right:
        # NOTE:
        # dont use (left + right)//2. This is an implementation issue, that can cause
        # integer overflow. Lets say in C++, you did left=INT_MAX, right=INT_MAX, adding both these will
        # cause the value of left+right to become negative.
        # read this for further info.
        mid = left + (right-left)//2
        if condition(mid):
            right = mid
        else:
            left = mid+1
        
    return left

# NOTE:
# 1. Correctly Initialize left, right. Can be (0,n) or (1,n)
# 2. Decide return value. Check whether it should be left or left-1.
# Remember this: after exiting the while loop, left is the minimal k​ satisfying the condition function.
# 3. Design the condition function. This is the most difficult and most beautiful part
