import sys

class Solution:
    def getSecondLargest(self, arr):
        first_largest = -sys.maxsize
        second_largest = -sys.maxsize

        for element in arr:
            if element > first_largest:
                second_largest = first_largest
                first_largest = element
            elif element != first_largest and element > second_largest:
                second_largest = element

        if second_largest != -sys.maxsize:
            return second_largest

        return -1