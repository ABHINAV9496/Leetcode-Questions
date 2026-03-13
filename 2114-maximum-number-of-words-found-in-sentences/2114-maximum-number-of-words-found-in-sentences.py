class Solution(object):
    def mostWordsFound(self, sentences):
        max_words = 0
        
        for s in sentences:
            words = len(s.split())
            if words > max_words:
                max_words = words
        
        return max_words