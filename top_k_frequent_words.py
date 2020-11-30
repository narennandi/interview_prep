import collections, heapq


def topKFrequent(words, k):
    count = collections.Counter(words)
    heap = [(-freq, word) for word, freq in count.items()]
    heapq.heapify(heap)
    return [heapq.heappop(heap)[1] for _ in range(k)]

words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 2

print(topKFrequent(words, k))