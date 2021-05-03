# 295. Find Median from Data Stream
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

# 252. Meeting Rooms
class Solution:
    """
    Given an array of meeting time intervals where intervals[i] = [starti, endi], 
    determine if a person could attend all meetings.
    Example 1:

    Input: intervals = [[0,30],[5,10],[15,20]]
    Output: false
    """
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        
        intervals.sort(key = lambda x:x[0])
        
        for i in range(len(intervals)-1):
            if intervals[i][1] > intervals[i+1][0]:
                return False
            
        return True

# 253. Meeting Rooms II

class Solution:
    """
    Given an array of meeting time intervals intervals 
    where intervals[i] = [starti, endi], 
    return the minimum number of conference rooms required.
    
    Example 1:
    Input: intervals = [[0,30],[5,10],[15,20]]
    Output: 2
    """
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        import heapq
        
        intervals.sort(key=lambda x:x[0])
        
        heap = []
        for i in intervals:
            
            if heap and i[0] >= heap[0]:
                heapq.heapreplace(heap, i[1])
                
            else:
                heapq.heappush(heap, i[1])
                
        return len(heap)


class Solution:
    """
    Given a non-empty list of words, return the k most frequent elements.
    Your answer should be sorted by frequency from highest to lowest. 
    If two words have the same frequency, then the word with the lower alphabetical order 
    comes first.
    """
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        from collections import Counter
        
        d = Counter(words)
        
        heap = []
        
        for words, frequency in d.items():
            heap.append((-frequency, words))
        
        # Transform list x into a heap, in-place, in linear time.
        heapq.heapify(heap)
        
        return [heapq.heappop(heap)[1] for i in range(k)]

