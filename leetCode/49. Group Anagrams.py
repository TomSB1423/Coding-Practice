class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        store = {}
        for i in strs:
            temp = "".join(sorted(i))
            if temp not in store:
                store[temp] = [i]
            else:
                store[temp].append(i)
        store = [y for x, y in store.items()]
        return store
