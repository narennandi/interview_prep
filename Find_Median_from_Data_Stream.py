class MedianFinder:
    """
    Simple Sorting
    
    Store the numbers in a resize-able container. 
    Every time you need to output the median, sort the container and output the median.

    Time complexity: O(nlogn)+O(1)≃O(nlogn).
    Adding a number takes amortized O(1) time for a container with an efficient resizing scheme.
    Finding the median is primarily dependent on the sorting that takes place. This takes O(n\log n)O(nlogn) time for a standard comparative sort.
    Space complexity: O(n) linear space to hold input in a container. No extra space other than that needed (since sorting can usually be done in-place).
    """

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.res = []

    def addNum(self, num: int) -> None:
        self.res.append(num)

    def findMedian(self) -> float:
        self.res.sort()
        count = len(self.res)
        
        if count % 2 == 0:
            r = int(count / 2)
            l = r - 1
            ans = (self.res[l]+self.res[r]) / 2
            return ans
        else:
            ans = self.res[count // 2]
            return ans

from heapq import *
class MedianFinder:
    """
    Approach 3: Two Heaps
    Alltogether, the add operation is O(logn), The findMedian operation is O(1).

    Time complexity: O(5⋅logn)+O(1)≈O(logn).
    At worst, there are three heap insertions and two heap deletions from the top. Each of these takes about O(logn) time.
    Finding the median takes constant O(1) time since the tops of heaps are directly accessible.

    Space complexity: O(n) linear space to hold input in containers.
    """
    def __init__(self):
        self.small = []  # the smaller half of the list, max heap (invert min-heap)
        self.large = []  # the larger half of the list, min heap

    def addNum(self, num):
        if len(self.small) == len(self.large):
            heappush(self.large, -heappushpop(self.small, -num))
        else:
            heappush(self.small, -heappushpop(self.large, num))

    def findMedian(self):
        if len(self.small) == len(self.large):
            return float(self.large[0] + (-self.small[0]))  / 2.0
        return float(self.large[0])

