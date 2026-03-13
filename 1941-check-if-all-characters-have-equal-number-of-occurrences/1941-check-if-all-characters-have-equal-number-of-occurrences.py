from collections import Counter

class Solution(object):
    def areOccurrencesEqual(self, s):
        freq = Counter(s).values()
        return len(set(freq)) == 1
        
        