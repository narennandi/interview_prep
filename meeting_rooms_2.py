import heapq

def minMeetingRooms(intervals):
    #sort based on start time
    intervals.sort(key=lambda x:x[0])
    
    heap = []  # stores the end time of intervals
    for i in intervals:
        if heap and i[0] >= heap[0]: 
            # means two intervals can use the same room one after the other
            heapq.heapreplace(heap, i[1])
        else:
            # a new room is allocated
            heapq.heappush(heap, i[1])
    return len(heap)

intervals = [[0, 30],[5, 10],[15, 20]]
print(minMeetingRooms(intervals))