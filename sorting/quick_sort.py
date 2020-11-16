# NOTE:
# for revision check this out
# https://www.youtube.com/watch?v=uXBnyYuwPe8&ab_channel=BackToBackSWE
# then this https://backtobackswe.com/platform/content/quicksort/code

import random

class Solution:
    def quicksort(self, arr):
        self.quick_sort_util(arr, 0, len(arr)-1)
        return arr
    
    def quick_sort_util(self, arr, left, right):
        if len(arr) == 1:
            return arr
        if left<right:
            partition_index = self.partition(arr, left, right)
            self.quick_sort_util(arr, left, partition_index-1)
            self.quick_sort_util(arr, partition_index+1, right)
    
    def partition(self, arr, left, right):
        # this will rearrange the array in such a way
        # elements_on_left <pivot<elements_on_right

        pivot_index = right
        # i is used to track the last placed element < pivot
        i = left-1
        # j is used to scan the array

        for j in range(left, right):
            if arr[j] <= arr[pivot_index]:
                i+=1
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[i+1], arr[pivot_index] = arr[pivot_index], arr[i+1]
        return i+1

#print(Solution().quicksort([1,3,2,4,5,7,9,6,10,8]))

