def groupAnagrams(strs):
    import collections     
    ans = collections.defaultdict(list)
    
    for s in strs:
        ans[tuple(sorted(s))].append(s)
    
    return ans.values()

if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    res = groupAnagrams(strs)
    print(res)