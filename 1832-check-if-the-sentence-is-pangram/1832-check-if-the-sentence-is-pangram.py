class Solution(object):
    def checkIfPangram(self, sentence):
        a = 'abcdefghijklmnopqrstuvwxyz'
        for ch in a:
            if ch not in sentence:
                return False
        return True
      
        